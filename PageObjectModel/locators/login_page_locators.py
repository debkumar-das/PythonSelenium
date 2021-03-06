"""
Created on 27-Apr-2020
@author: Lavendra rajput
"""
from seleniumpagefactory.Pagefactory import PageFactory


class LoginPageLocators(PageFactory):
    
    def __init__(self, driver):
        # It is necessary to to initialise driver as page class member to implement Page Factory
        self.driver = driver
        
    locators = {
        "userId": ('NAME', 'uid'),
        "password": ('NAME', 'password'),
        "loginButton": ('NAME', 'btnLogin'),
        "resetButton": ('XPATH', 'btnReset')
     }
    
    def get_user_id_locator(self):
        """
        Return the locator of user id !
        """
        return self.userId;
    
    def get_password_locator(self):
        """
        Return the locator of password !
        """
        return self.password;
    
    def get_login_button_locator(self):
        """
        Return the locator of login button !
        """
        return self.loginButton;
    
    def get_reset_button_locator(self):
        """
        Return the locator of reset button !
        """
        return self.resetButton;
