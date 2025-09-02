from odoo import models, fields, api

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


    def action_mark_as_featured(self):
        for record in self:
            if not record.is_available:
                record.is_available = True
        return True

    def update_price_cron(self):
        for record in self:
            record.price += 0.01

