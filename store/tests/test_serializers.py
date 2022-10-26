from django.test import TestCase

from store.models import Book
from store.serializers import BooksSerializer


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(name='Test book1', price=33)
        book_2 = Book.objects.create(name='Test book2', price=36)
        data = BooksSerializer([book_1, book_2], many = True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'Test book1',
                'price': '33.00'
            },
            {
                'id': book_2.id,
                'name': 'Test book2',
                'price': '36.00'
            }
        ]
        self.assertEqual(data, expected_data)