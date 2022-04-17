from graphene_django.utils.testing import GraphQLTestCase
from django.test import TestCase, Client
from elements.models import Elements
from elements.schema import schema
from django.urls import reverse
import json


class ElementViewTest(TestCase):
  def setUp(self):
    self.client = Client()
  
  def test_index(self):
    response = self.client.get(reverse('elements:index'))
    self.assertEqual(response.status_code, 200)
    
  def test_guide(self):
    response = self.client.get(reverse('elements:guide'))
    self.assertEqual(response.status_code, 200)
    
    
def build_url(element):
    url = reverse('elements:data', args=(element,))
    return url   
    

class RestfulApiTest(TestCase):
  def setUp(self):
    self.client = Client()
  
  
  def test_DataView(self):
    response = self.client.get(build_url('Helium'))
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.json()['symbol'], 'He')

    response = self.client.get(build_url('Gold'))
    self.assertNotEqual(response.status_code, 200)
    self.assertEqual(response.status_code, 404)

"""
class GraphApiTest(GraphQLTestCase):
    def test_graph(self):
        response = self.query(
          '''
            query myModel($name: Str!){
              element(name: $name) {
                symbol
                mass_no
                group
              }
            }
            ''',
            op_name = "myModel", 
            variables = {'name': 'Neon'}
           
          )
         
        content = json.loads(response.content)
        
        self.assertResponseNoErrors(response)
        self.assertEqual(content['group'], 'noble gas')
"""