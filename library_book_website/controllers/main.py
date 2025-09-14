from odoo import http
from odoo.http import request

class LibraryWebsite(http.Controller):

    @http.route('/library/book', type='http', auth='public', website=True)
    def list_books(self, **kw):
        books = request.env['library.book'].sudo().search([])
        return request.render('library_book_website.library_books_template', {
            'books': books,
        })
