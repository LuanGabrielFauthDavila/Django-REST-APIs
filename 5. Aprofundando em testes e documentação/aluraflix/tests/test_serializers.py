from django.test import TestCase 
from aluraflix.models import Programa 
from aluraflix.serializers import ProgramaSerializer

class ProgramaSerializerTestCase(TestCase):
    
    def setUp(self):
        self.programa = Programa(
            titulo = "Procurando ninguem em latim",
            data_lancamento = '2003-07-04',
            tipo = 'F',
            likes = 2340,
            dislikes = 40,
        )
        self.serializer = ProgramaSerializer(instance=self.programa)
    
    def test_verifica_campos_serializados(self):
        """Verifica se os campos estão sendo serializados corretamente"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['titulo', 'tipo', 'data_lancamento', 'likes']))

    def test_verifica_conteudo(self):
        """Verificar o conteudo dos campos serializados"""
        data = self.serializer.data
        self.assertEqual(data['titulo'], self.programa.titulo)
        self.assertEqual(data['data_lancamento'], self.programa.data_lancamento)
        self.assertEqual(data['tipo'], self.programa.tipo)
        self.assertEqual(data['likes'], self.programa.likes)
        # self.assertEqual(data['dislikes'], self.programa.dislikes)   # este campo não existe no serializer
