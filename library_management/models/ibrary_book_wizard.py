from odoo import models, fields
from odoo.exceptions import UserError



class BookAvailabilityWizard(models.TransientModel):
    _name = 'library.book.availability.wizard'
    _description = 'Confirm book avaible'

    confirm_text = fields.Char(default="Are you sure you want to change book availability?")

    def action_confirm(self):
       
        active_id = self.env.context.get('active_id')
        book = self.env['library.book'].browse(active_id)
        if not book:
            raise UserError("Book not found")

        book.is_available = not book.is_available
        print("\nconfirm")
        return {'type': 'ir.actions.act_window_close'}
    