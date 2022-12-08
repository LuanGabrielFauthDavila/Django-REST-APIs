from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status


class AuthenticationUserTestCase(APITestCase):
    
    def setUp(self):
        self.list_urls = reverse('programas-list')
        self.user = User.objects.create_user('c3po', password='123456')


    def test_auth_user_with_correct_cred(self):
        """Teste que verifica um USER com credenciais corretas"""
        user = authenticate(username='c3po', password='123456')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_req_unauthorized(self):
        """Teste que verifica uma requisição não autorizada"""
        response = self.client.get(self.list_urls)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_auth_user_with_incorrect_cred(self):
        """Teste que verifica autenticação de um USER com dados incorretos"""
        user = authenticate(username='c3poe', password='123456')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_req_user_auth(self):
        """Teste que verifica uma requisição autorizada"""
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_urls)
        self.assertEqual(response.status_code, status.HTTP_200_OK)