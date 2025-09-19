from odoo import models, fields


class website_contact(models.Model):
    _name = "librarywebsite.contact"
    _description = "linrary contact"

    name = fields.Char(required=True)
    message = fields.Text()
