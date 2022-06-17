from graphene_django.utils.testing import GraphQLTestCase
from django.test import TestCase, Client
from elements.models import Elements, AllElements, constants, users
from elements.schema import schema
from django.urls import reverse
from io import BytesIO




class modelTest(TestCase):
  def setUp(self):
    self.client = Client()
    users.objects.create(user="sneezy", password="00000", mail="ahmadgbolly97@gmail.com")
    users.objects.create(mail="techscriptdevs@gmail.com")
    
  """
  def testUsers(self):
    count = users.objects.count()
    user1 = users.objects.get(user="sneezy")
    user2 = users.objects.get(mail="techscriptdevs@gmail.com")
    self.assertEqual(user1.password, "00000")
    self.assertFalse(user2.password)
    self.assertEqual(count, 2)
  
  
  def test_index(self):
    response = self.client.get(reverse('elements:index'))
    self.assertEqual(response.status_code, 200)
   
  
  def testVerifyMail(self):
    response1 = self.client.get(reverse('elements:verifyMail'))
    self.assertNotEqual(response1.status_code, 200)
    
    response2 = self.client.post(reverse('elements:verifyMail'), {'mail': 'ismailiqmah@gmail.com'} )
    count = users.objects.count()
    self.assertEqual(response2.status_code, 200)
    self.assertEqual(response2.json()["mail"], "ismailiqmah@gmail.com")
    self.assertEqual(count, 3)
    
    response3 = self.client.post(reverse('elements:verifyMail'), {'mail': 'shhshs@mal.com'} )
    count = users.objects.count()
    self.assertContains(response3, "mail invalid", status_code=404)
    self.assertEqual(count, 3)
    
    
    response4 = self.client.post(reverse('elements:verifyMail'), {'mail': '£√√π|×¢edh@gmail.com'} )
    self.assertContains(response4, "can't validate mail, try again", status_code=400)
    
  
  """
  def testCreate(self):
    response1 = self.client.get(reverse('elements:create'))
    self.assertNotEqual(response1.status_code, 200)
    user = users.objects.get(mail="techscriptdevs@gmail.com")
    date = user.user_age
    response2 = self.client.post(reverse('elements:create'), {'mail': 'techscriptdevs@gmail.com', 'username': 'devs', 'password': '@tech012'} )
    count = users.objects.count()
    user = users.objects.get(mail="techscriptdevs@gmail.com")
    self.assertEqual(response2.status_code, 200)
    self.assertEqual(response2.json()["username"], "devs")
    self.assertEqual(user.user, "devs")
    self.assertEqual(user.user_age, date)
    self.assertEqual(count, 2)
    
    response3 = self.client.post(reverse('elements:create'), {'mail': 'ismailiqmah@gmail.com', 'username': 'dammy', 'password': 'tech012'} )
    count = users.objects.count()
    self.assertContains(response3, "mail invalid", status_code=404)
    self.assertEqual(count, 2)
    
  
    # def testCreateProject(self):
    response1 = self.client.get(reverse('elements:createProject'))
    self.assertNotEqual(response1.status_code, 200)
    
    response2 = self.client.post(reverse('elements:createProject'), {'mail': 'techscriptdevs@gmail.com', 'projectName': 'coming soon',} )
    count = users.objects.count()
    user = users.objects.get(mail="techscriptdevs@gmail.com")
    self.assertEqual(response2.status_code, 200)
    self.assertEqual(response2.json()["username"], "")
    self.assertEqual(user.project_name, "coming soon")
    self.assertEqual(count, 2)
    
    response3 = self.client.post(reverse('elements:createProject'), {'mail': 'ismailiqmah@gmail.com', 'projectName': 'never coming'} )
    count = users.objects.count()
    self.assertContains(response3, "mail invalid", status_code=404)
    self.assertEqual(count, 2)
    

    # def testLogin(self):
    response1 = self.client.get(reverse('elements:login'))
    self.assertNotEqual(response1.status_code, 200)
    
    response2 = self.client.post(reverse('elements:login'), {'mail': 'ismailiqmah@gmail.com', 'password': '@tech012'} )
    self.assertEqual(response2.status_code, 404)
    
    response3 = self.client.post(reverse('elements:login'), {'mail': 'techscriptdevs@gmail.com', 'password': 'tech012'} )
    self.assertContains(response3, "invalid password", status_code=400)
    
    response4 = self.client.post(reverse('elements:login'), {'mail': 'techscriptdevs@gmail.com', 'password': '@tech012'} )
    self.assertEqual(response4.status_code, 200)
    self.assertEqual(response4.json()["projectName"], "coming soon")
    self.assertNotEqual(response4.json()["secretKey"], "")
    user = users.objects.get(mail="techscriptdevs@gmail.com")
    self.assertEqual(response4.json()["projectKey"], user.project_key)
    
    
    
    
    # def testchangePass():
    response1 = self.client.get(reverse('elements:changePass'))
    self.assertNotEqual(response1.status_code, 200)
    
    response2 = self.client.post(reverse('elements:changePass'), {'mail': 'ismailiqmah@gmail.com', 'newPass': '@chem012', 'oldPass': '@tech012'})
    self.assertEqual(response2.status_code, 404)
    
    response3 = self.client.post(reverse('elements:changePass'), {'mail': 'techscriptdevs@gmail.com', 'newPass': '@chem012', 'oldPass': '@tech012'})
    self.assertEqual(response3.status_code, 200)
    
    response4 = self.client.post(reverse('elements:login'), {'mail': 'techscriptdevs@gmail.com', 'password': '@chem012'} )
    self.assertEqual(response4.status_code, 200)
    
    
    
    # def testforgetPass():
    response1 = self.client.get(reverse('elements:forgetPass'))
    self.assertNotEqual(response1.status_code, 200)
    
    response2 = self.client.post(reverse('elements:forgetPass'), {'mail': 'ismailiqmah@gmail.com'} )
    self.assertEqual(response2.status_code, 404)
    
    response3 = self.client.post(reverse('elements:forgetPass'), {'mail': 'techscriptdevs@gmail.com'} )
    self.assertEqual(response3.status_code, 200)
    newPass = response3.json()["newPass"]
    
    response4 = self.client.post(reverse('elements:login'), {'mail': 'techscriptdevs@gmail.com', 'password': newPass} )
    self.assertEqual(response4.status_code, 200)
    
    
    
    
    # def testupload():
    response1 = self.client.get(reverse('elements:upload'))
    self.assertNotEqual(response1.status_code, 200)
    img = BytesIO(b'mybinarydata')
    img.name = 'myimage.jpg'
    
   
    response2 = self.client.post(reverse('elements:upload'), {'mail': 'ismailiqmah@gmail.com', 'mugshot': img}, enctype="multipart/form-data" )
    self.assertEqual(response2.status_code, 404)
   
   
    response3 = self.client.post(reverse('elements:upload'), {'mail': 'techscriptdevs@gmail.com', 'mugshot': img}, enctype="multipart/form-data" )
    self.assertEqual(response3.status_code, 200)
   
        
    
    
    




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