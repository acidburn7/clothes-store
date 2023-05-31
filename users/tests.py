from http import HTTPStatus

from django.test import TestCase, Client
from django.urls import reverse

from users.models import User
from users.forms import UserRegistrationForm


class UserRegistrationViewTestCase(TestCase):

    def setUp(self) -> None:
        self.path = reverse('users:register')

    def test_user_registration_get(self):
        response = self.client.get(path=self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Регистрация')
        self.assertTemplateUsed('users/registration.html')

    def test_user_registration_post(self):
        data = {
            'first_name': 'Ivan',
            'last_name': 'Ivanov',
            'password1': '123456789Ivan',
            'password2': '123456789Ivan',
            'email': 'ivanivanov@mail.ru'
        }

        user = Client()
        response = user.post(self.path, data)

        username = user["usename"]
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse("users:login"))
        self.assertTrue(User.objects.filter(username=username))
