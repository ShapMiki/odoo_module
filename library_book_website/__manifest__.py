{
    'name': 'Library Website',
    'version': '1.0',
    'category': 'Website',
    'description': 'Website interface for library management',
    'license': 'LGPL-3',
    'depends': ['website', 'library_management'],
    'data': [
        'views/library_website_views.xml',
        'views/library_book_templates.xml',
        'views/library_book_home_inherit.xml',
        'views/library_website_manager_views.xml',
        'views/library_book_snippets.xml',
        'security/library_website_security.xml',
        'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_frontend': [
            '/library_book_website/static/src/css/library_book.scss',
            '/library_book_website/static/src/js/library_book.js',
            '/library_book_website/static/src/js/owl/library_book_owl.js',
            '/library_book_website/static/src/js/owl/library_book_mount.js',
            'library_book_website/static/src/xml/library_book_owl.xml',
        ],
    },
    'installable': True,
    'application': False,
}
