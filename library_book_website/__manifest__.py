{
    'name': 'Library Website',
    'version': '1.0',
    'category': 'Website',
    'description': 'Website interface for library management',
    'license': 'LGPL-3',
    'depends': ['website', 'library_management'],
    'data': [
        'views/library_website_views.xml',
    ],
    'installable': True,
    'application': False,
}
