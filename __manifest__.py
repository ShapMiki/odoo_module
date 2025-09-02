{
    "name": "My Library Management",
    "version": "1.0",
    "author": "Mikita",
    "category": "Library",
    "depends": ["base", "event"],
    "data": [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_views.xml',
        'views/library_views_inherit.xml',
        'report/book_report.xml',
        'views/event_kanban.xml',
        'data/library_cron.xml',
    ],
    "installable": True,
    "application": True,
}

