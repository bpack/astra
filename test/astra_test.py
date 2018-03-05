import sys
sys.path.append('../astra')

import astra 
import unittest
import tempfile

class AstraTestCase(unittest.TestCase):

    def setUp(self):
        self.app = astra.create_app(env_name='test')

        self.app.app_context().push()
        self.db = astra.db
        self.client = self.app.test_client()

        astra.db.drop_all()
        astra.db.create_all()

    def tearDown(self):
        pass

    def test_get_user(self):
        user = astra.models.User('testuser', 'email@example.com')
        self.db.session.add(user)
        self.db.session.commit()
#        print('Created user', user.id)

        response = self.client.get('/users')
#        print(response.data)
        self.assertEqual(response.status_code, 200)

    def test_get_user_duplicate(self):
        user = astra.models.User('testuser', 'email@example.com')
        self.db.session.add(user)
        self.db.session.commit()

        response = self.client.post('/users/', data='{ "email": "email@example.com", "username": "testuser" }', content_type='application/json')
#        print(response.data)
        self.assertEqual(response.status_code, 400)


       

if __name__ == '__main__':
    unittest.main()