from odoo import http
from odoo.http import request
import json
import os

class LibraryWebsite(http.Controller):

    @http.route('/', type='http', auth='public', website=True)
    def list_books(self, **kw):
        books = request.env['library.book'].sudo().search([])
        return request.render('library_book_website.library_books_template', {
            'books': books,
        })

    @http.route('/manager', type='http', auth='user', website=True)
    def manager_page(self, **kwargs):
        is_manager = request.env.user.has_group('library_book_website.group_library_manager')
        print(f"\n\nis_manager: {is_manager}\n\n")
        return request.render('library_book_website.restricted_content', {
            'is_manager': is_manager,
        })

    @http.route('/library/contact/submit', type='http', auth='public', website=True, csrf=True)
    def contact_submit(self, **post):
        name = post.get('name')
        message = post.get('message')

        print(f"NOW {name} write: {message}")

        return request.redirect('/')

    @http.route(['/library/book/<model("library.book"):book>'], type='http', auth='public', website=True)
    def book_detail(self, book, **kwargs):
        """Дружелюбный URL для отдельной книги"""
        return request.render('library_book_website.book_detail_template', {
            'book': book,
        })


    @http.route('/robots.txt', type='http', auth='public')
    def robots_txt(self):
        """Возвращает robots.txt для SEO"""
        robots_path = os.path.join(os.path.dirname(__file__), '..', 'static', 'robots.txt')
        try:
            with open(robots_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return request.make_response(content, headers=[('Content-Type', 'text/plain')])
        except FileNotFoundError:
            return request.make_response('User-agent: *\nAllow: /', headers=[('Content-Type', 'text/plain')])

    @http.route('/sitemap.xml', type='http', auth='public')
    def sitemap_xml(self):
        """Генерирует sitemap.xml для SEO"""
        books = request.env['library.book'].sudo().search([])
        
        sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
        sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        
        # Главная страница
        sitemap += '  <url>\n'
        sitemap += '    <loc>/</loc>\n'
        sitemap += '    <changefreq>daily</changefreq>\n'
        sitemap += '    <priority>1.0</priority>\n'
        sitemap += '  </url>\n'
        
        # Страницы книг
        for book in books:
            sitemap += '  <url>\n'
            sitemap += f'    <loc>/library/book/{book.id}</loc>\n'
            sitemap += '    <changefreq>weekly</changefreq>\n'
            sitemap += '    <priority>0.8</priority>\n'
            sitemap += '  </url>\n'
        
        sitemap += '</urlset>'
        
        return request.make_response(sitemap, headers=[('Content-Type', 'application/xml')])

