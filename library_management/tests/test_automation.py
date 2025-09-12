from odoo.tests.common import TransactionCase
from odoo.tests import HttpCase



class TestDemoData(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super(TestDemoData, cls).setUpClass()
        cls.model = cls.env['library.book']
    
    def test_demo_books(self):
        books_count = self.model.search_count([])
        self.assertTrue(books_count >= 2)


class TestLibraryBookWebTour(HttpCase):

    def test_library_book_tour(self):
        self.start_tour("/", 'library_book_tour', login="admin")
