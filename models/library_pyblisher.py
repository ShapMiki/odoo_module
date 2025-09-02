from odoo import models, fields



class LibraryPublisher(models.Model):
    _name = "library.publisher"
    _description = "Library publisher"

    name = fields.Char("Name", required=True)

    books_ids = fields.One2many(
        comodel_name='library.book',
        inverse_name='publisher_id',
        string='books'
    )

