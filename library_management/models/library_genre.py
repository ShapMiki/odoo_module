from odoo import models, fields



class LibraryGenre(models.Model):
    _name = "library.genre"
    _description = "Library Genre"

    name = fields.Char("Name", required=True)
    description = fields.Text("Description")
