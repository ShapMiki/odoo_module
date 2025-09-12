{
    "name": "My Library Management",
    "version": "1.0",
    "author": "Mikita",
    "category": "Library",
    "depends": ["base", "event", "mail"],

    "data": [
        'views/library_book_kanban.xml',
        'views/library_book_actions.xml',
        'views/library_book_views.xml',
        'views/library_views_inherit.xml',
        'views/library_book_menu.xml',

        'security/library_security.xml',
        'security/ir.model.access.csv',

        'report/book_report.xml',
        'data/library_cron.xml',
        'data/email_view_template.xml',
    ],

    "test": ['tests/test_tour.js'],
    "demo":[
        'demo/library_book_test.xml',
    ],
    "installable": True,
    "application": True,
}
