from django.test import TestCase, SimpleTestCase, LiveServerTestCase
from django.contrib.auth.models import User
from .models import *
from .views import *
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Create your tests here.
class PostModelTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title='Test Post', post='This is a test', rating='1-Star Rating')
    
    def test_post_str(self):
        self.assertEqual(str(self.post), 'Test Post')

class TeamModelTest(TestCase):
    def setUp(self):
        self.post = Team.objects.create(name='Test Post', city='This is a test')
    
    def test_post_str(self):
        self.assertEqual(str(self.post), 'Test Post')


class HomepageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

class LoginTest(LiveServerTestCase):
    def setUp(self):
        self.browser=driver
    def test_login(self):
        self.browser.get("http://127.0.0.1:8000/")

        login_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'Log In')))
        login_link.click()

        username_input = self.browser.find_element(By.ID,'id_username')
        password_input = self.browser.find_element(By.ID,'id_password')

        username_input.send_keys('test')
        password_input.send_keys('testpassword')

        login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'submit')))
        login_button.click()

        logout_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'Log Out')))
        self.assertIsNotNone(logout_link)
