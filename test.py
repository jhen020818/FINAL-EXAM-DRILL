import unittest
from api import app

class usingFlask_MySql(unittest.TestCase):
 def setup(self):
  app.testing =True
  self.app = app.test_client()

  def test_get_customers(self):
   response = self.app.get('/api/customers')
   self.assertEqual(response.status_code, 200)

  def test_create_customers(self):
   data = {'age': 21}
   response = self.app.post('/api/customers', json=data)
   self.assertEqual(response.status_code, 201)

  def test_delete_customers(self):
   data = {'customerNumber'}
   response = self.app.delete('/api/customers', json=data)
   self.assertEqual(response.status_code, 202)

   def test_update_customers(self):
    state = "Victoria"
    data ={'state': 'New York'}
    response = self.app.put('/api/customers/<VARCHAR:state', json=data)
    self.assertEqual(response.status_code, 203)

if __name__ == "__main__":
 unittest.main()
