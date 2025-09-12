from odoo import models, fields, api
from odoo.exceptions import UserError
import requests
import logging



_logger = logging.getLogger(__name__)


class LibraryBook(models.Model):
    _name = "library.book"
    _description = "Library Book"

    title = fields.Char("Title", required=True)
    author = fields.Char("Author")
    isbn = fields.Char("ISBN")
    description = fields.Text("Description")
    published_date = fields.Date("Published Date")
    is_available = fields.Boolean("Is Available", default=True)
    count_pages = fields.Integer("Pages", default=0)


    large_type = fields.Char("large_type", compute=('_compute_large_type'), store=True)
    full_title = fields.Char("full_title", compute=('_compute_full_title'), store=True)

    publisher_id = fields.Many2one(
        comodel_name='library.publisher',
        string='Publisher'
    )

    genre_ids = fields.Many2many(
        comodel_name='library.genre',
        relation='library_book_genre_rel',
        column1='book_id',
        column2='genre_id',
        string='Genres'
    )

    price = fields.Float("price", default=0)
    price_in_pln = fields.Float("Price in pln", default=0, store=False)

    image = fields.Image("image")

    _sql_constraints = [
        (
            'book_unique',
            'unique(isbn, full_title)',
            'book not unique'
        ),
        (
            'count_page_check',
            'CHECK(count_pages >= 0)',
            'Invalid page count'
        ),
    ]


    @api.depends('title', 'author')
    def _compute_full_title(self):
        for line in self:
            line.full_title = (line.author or "") + " " + (line.title or "")


    @api.depends('count_pages')
    def _compute_large_type(self):
        for line in self:
            large_type_str = None
            if 0 < line.count_pages <= 50:
                large_type_str = 'Mini'
            elif 50 < line.count_pages <= 300:
                large_type_str = "normal"
            elif 300 < line.count_pages <= 3000:
                large_type_str = "Large"
            elif line.count_pages > 3000:
                large_type_str = "Epic"

            line.large_type  = large_type_str

 
    def get_price_in_pln(self):
        
        key = self.env['ir.config_parameter'].sudo().get_param('currency_api_key')

        params = {
            'apikey': key,
            'base_currency': "USD",
        }

        try:
            request = requests.get('https://api.freecurrencyapi.com/v1/latest', params=params)
            request.raise_for_status()
            pln_currency = request.json()['data']['PLN']
        except requests.exceptions.RequestException as e:
            _logger.error("Error fetching geocode data: %s", e)
            raise UserError("Try leter")
        except KeyError as e:
            _logger.error("Unexpected JSON format: missing key %s", e)
            raise UserError("Try leter")

        self.ensure_one()
        value = self.price * pln_currency
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'library.book',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'current',
            'context': dict(self.env.context, default_price_in_pln=value),
        }
    
    def action_mark_as_featured(self):
        for record in self:
            if not record.is_available:
                record.is_available = True
        return True

    def update_price_cron(self):
        for record in self:
            record.price += 0.01

    def action_send_followup_email(self):
        template = self.env.ref('library_management.library_email_template')
        for record in self:
            template.send_mail(record.id, force_send=True)


class LibraryResPartner(models.Model):
    _inherit = 'library.book'

    size = fields.Integer("size", default=100)
    recomendate_screen_size = fields.Char("Recomendate screen size", default="1980x1080")
