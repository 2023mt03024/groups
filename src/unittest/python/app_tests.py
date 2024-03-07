from mockito import mock, verify
import unittest

from app import get_group, app
from initdb import initdb

class AppTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        initdb()

    @classmethod
    def tearDownClass(cls):
        initdb()

    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()
    
    def tearDown(self):
        self.ctx.pop()

    def test_get_group(self):
        group = get_group(1)
        self.assertEqual(group['name'], 'Group 1')
    
    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        assert 'Welcome to DevOps Groups' in response.get_data(as_text=True)

    def test_about(self):
        response = self.client.get("/about")
        assert response.status_code == 200
        assert 'Simple web application for CRUD operations on DevOps groups' in response.get_data(as_text=True)

    def test_view_group1(self):
        response = self.client.get("/1")
        assert response.status_code == 200
        assert 'Group 1' in response.get_data(as_text=True)

    def test_create_group_get(self):
        response = self.client.get("/create")
        assert response.status_code == 200
        assert 'Create a New Group' in response.get_data(as_text=True)

    def test_edit_group_get(self):
        response = self.client.get("/1/edit")
        assert response.status_code == 200
        assert 'Edit "Group 1"' in response.get_data(as_text=True)

    def test_create_group3(self):
        response = self.client.post("/create", 
                                    data=dict(name='Group 3', member1='2023MT03122 - VENKATA SAI VISWESWAR.K',
                                               member2 = '2023MT03145 - A.Purnima', member3='2023mt03082 - Harshita kaza', 
                                               member4 = '2023mt03196 - Patil Ajinkya Lalit', member5= ''))
        assert response.status_code == 302
        
    def test_edit_group1(self):
        response = self.client.post("/1/edit", data=dict(name='Group 1', member1='2023MT03122 - VENKATA SAI VISWESWAR.K',
                                               member2 = '2023MT03145 - A.Purnima', member3='2023mt03082 - Harshita kaza', 
                                               member4 = '2023mt03196 - Patil Ajinkya Lalit', member5= '2023mt03196 - Patil Ajinkya Lalit'))
        assert response.status_code == 302  

    def test_delete_group2(self):
        # Define the environment variables before running pyb
        # Windows
        #set FLASK_KEY=SECRET_KEY
        #set FLASK_KEY_VALUE=SECRET_VALUE
        # linux
        # export FLASK_KEY=SECRET_KEY
        # export FLASK_KEY_VALUE=SECRET_VALUE
        response = self.client.post("/2/delete")
        assert response.status_code == 302

