import allure
from TestCases.BaseTest import BaseTest
from PageObjects.LoginPage import *

class TestLoginPage(BaseTest):
    global driver

    @allure.title("Verify User able to login with valid Credentials")
    def test_TC001_ValidCredentials(self):
        LoginPage(self.driver).Login()

    # @allure.title("Verify User can't login with Invalid Credentials")
    # def test_TC002_InValidCredentials(self):
    #     LoginPage(self.driver).InValid_Login()

    # @allure.title("Verify Forgot Pasword on login page")
    # def test_TC003_ForgotPassowrd(self):
    #     LoginPage(self.driver).Verify_ForgotPassword()
    #
    # @allure.title("Verify SignUp on Login Page")
    # def test_TC004_SignUp(self):
    #     LoginPage(self.driver).Verify_SIgnUp()
    #
    # @allure.title("Verify Contact Us info on footer of Login page")
    # def test_TC005_ContactUs(self):
    #     LoginPage(self.driver).Verify_ContactUs()
    #
    # @allure.title("Verify Language change from English to Arabic on Longin Page")
    # def test_TC006_Lang_English_To_Arabic(self):
    #     LoginPage(self.driver).Change_Language_EN_Arabic()
    # #
    # @allure.title("Verify Language change from Arabic to English on Longin Page")
    # def test_TC007_Lang_Arabic_To_English(self):
    #     LoginPage(self.driver).Change_Language_Arabic_EN()
    #
    # @allure.title("Verify Aldar Header  on Login Page")
    # def test_TC008_Verify_AldarHeader(self):
    #     LoginPage(self.driver).Verify_AldarHeader()
    #
    # @allure.title("Verify T&C on Registration page")
    # def test_TC009_Verif_TC(self):
    #     LoginPage(self.driver).Verify_TermsAndConditions()
    #
    # @allure.title("Verify error with invalid email ID on registrationpage")
    # def test_TC010_Verify_InvalidEmail_RegisterPage(self):
    #     LoginPage(self.driver).Verify_InvalidEmail_RegisterPage()