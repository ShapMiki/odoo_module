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
    ],
    'assets': {
        'web.assets_frontend': [
            'static/src/css/library_book.scss',
            'static/src/js/library_book.js',
            'static/src/js/owl/library_book_owl.js',
            'static/src/js/owl/library_book_mount.js',
            'static/src/xml/library_book_templates.xml',
        ],
    },
    'installable': True,
    'application': False,
}
