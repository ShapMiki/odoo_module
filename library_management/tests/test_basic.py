from odoo.tests.common import TransactionCase



"""
SavepointCase - быстрые тесты без сохранения транзакции.
TransactionCase - полноценные тесты, каждая функция откатывается после выполнения.
HttpCase - для UI и web-тестирования (с Selenium).
"""

class TestLibraryIntegration(TransactionCase):

    def test_create_and_confirm_book(self):
        """"""
        
        book = self.env['library.book'].create({
            'title': 'Integration Test Book',
            'author': 'Test Author',
            'isbn': '1234567890',
            'count_pages': 100,
        })
        self.assertTrue(book, "Книга должна быть создана")


        if hasattr(book, "action_confirm"):
            book.action_confirm()
            self.assertEqual(book.state, 'confirmed', "Книга должна перейти в статус 'confirmed'")
