'''
Created on 27-Apr-2020

@author: Lavendra rajput
'''
import json
import unittest
from Actions.LoginPage import LoginPage
from TestBase.Page import Page


class TestLoginPage(unittest.TestCase):
    f = open("E:\Python_Workspace\PageObjectModel\TestData\Data.json")
    data = json.load(f)
    page = Page()
    driver = None
    loginPage = None
    def setUp(self):
        print("setup started")
        self.driver=self.page.initialization()
    
    
    def test_Login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.doLogin(self.data["LoginPage"]["userId"], self.data["LoginPage"]["password"])
        
    
    def tearDown(self):
        self.page.quitSession()
        