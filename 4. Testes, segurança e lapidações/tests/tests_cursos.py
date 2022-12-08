from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status

class CursoTestCase(APITestCase):
    def setUp(self):
        self.list_urls = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso="CTT1", descricao="Curso 1", nivel="B")
        self.curso_1 = Curso.objects.create(
            codigo_curso="CTT2", descricao="Curso 2", nivel="B",
        )

    # def test_falhador(self):
    #     self.fail('teste falhou')

    def test_req_get(self):
        """Testando requisições get estão ok"""
        response = self.client.get(self.list_urls)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_req_get(self):
        data = {
            'codigo_curso': 'CCTT',
            'descricao': 'CURSO TESTE',
            'nivel': 'B'
        }
        response = self.client.post(self.list_urls, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_req_delete(self):
        response = self.client.delete('/cursos/1/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)