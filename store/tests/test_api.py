from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from store.models import Book
from store.serializers import BooksSerializer


class BooksApiTestCase(APITestCase):
    def setUp(self):
        self.book_1 = Book.objects.create(name='Test book 1', price=39, author_name='Author 1')
        self.book_2 = Book.objects.create(name='Test book 2', price=36, author_name='Author 2')
        self.book_3 = Book.objects.create(name='Test book Author 1', price=36, author_name='Author 2')
        self.book_4 = Book.objects.create(name='Test book 4', price=33, author_name='Author 4')
        self.book_5 = Book.objects.create(name='Test book 5', price=99, author_name='Author 5')

    def test_get(self):
        url = reverse('book-list')
        response = self.client.get(url)
        serializer_data = BooksSerializer([self.book_1, self.book_2, self.book_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_filter(self):
        url = reverse('book-list')
        response = self.client.get(url, data = {'price': 36})
        serializer_data = BooksSerializer([self.book_2, self.book_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_search(self):
        url = reverse('book-list')
        response = self.client.get(url, data={'search': 'Author 1'})
        serializer_data = BooksSerializer([self.book_1, self.book_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_ordering(self):
        url = reverse('book-list')
        response = self.client.get(url, data={'ordering': 'price'})
        serializer_data = BooksSerializer([self.book_4, self.book_2, self.book_3, self.book_1, self.book_5], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
        print(response.data)