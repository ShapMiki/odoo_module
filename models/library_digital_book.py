from odoo import fields, models

class LibraryResPartner(models.Model):
    _inherit = 'library.book'

    size = fields.Integer("size", default=100)
    recomendate_screen_size = fields.Char("Recomendate screen size", default="1980x1080")


    