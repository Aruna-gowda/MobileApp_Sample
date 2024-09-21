import time
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.BasePage import BasePage
from Utilities import ReadConfigurations

platformName = ReadConfigurations.read_configuration("basic info","platformName")
if platformName == "Android":
    from Locators.Android import *
else:
    from Locators.iOS import *

class LoginPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    @allure.step("Login into the Iceridge application")
    def Login(self):
        Email = ReadConfigurations.read_configuration("basic info", "Email")
        Password = ReadConfigurations.read_configuration("basic info", "Password")
        self.Click("Button_Security_XPATH", Login.Button_Security_XPATH)
        # self.Type(Email, "Input_Email_XPATH", Login.Input_Email_XPATH)
        # self.Type(Password, "Input_Password_XPATH",Login.Input_Password_XPATH)
        # self.Click("Button_Login_XPATH", Login.Button_Login_XPATH)
        # WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((AppiumBy.XPATH, Home.Verify_Welcome_XPATH)))
        # self.check_display_status_of_element("Verify_Welcome_XPATH",Home.Verify_Welcome_XPATH)

    @allure.step("Login into the Iceridge application")
    def InValid_Login(self):
        self.Type("xyz@test.com", "Input_Email_XPATH", Login.Input_Email_XPATH)
        self.Type("abc@123", "Input_Password_XPATH", Login.Input_Password_XPATH)
        self.Click("Button_Login_XPATH", Login.Button_Login_XPATH)
        self.check_display_status_of_element("Verify_InvalidLogin_XPATH",Login.Verify_InvalidLogin_XPATH)

    # @allure.step("Verify Forgot Pasword on login page")
    # def Verify_ForgotPassword(self):
    #     self.Click("Button_Forgot_XPATH",Login.Button_Forgot_XPATH)
    #     self.check_display_status_of_element("Verify_ForgotPage_XPATH",Login.Verify_ForgotPage_XPATH)
    #
    # @allure.step("Verify SignUp on Login Page")
    # def Verify_SIgnUp(self):
    #     self.Click("Button_SignUp_XPATH",Login.Button_SignUp_XPATH)
    #     self.check_display_status_of_element("Verify_Register_XPATH",Login.Verify_Register_XPATH)
    #
    # @allure.step("Verify Contact Us info on footer of Login page")
    # def Verify_ContactUs(self):
    #     self.check_display_status_of_element("Verify_ContactUs_XPATH",Login.Verify_ContactUs_XPATH)
    #
    # @allure.step("Verify Language change from English to Arabic on Longin Page")
    # def Change_Language_EN_Arabic(self):
    #     self.Click("Button_ArabicLang_XPATH",Login.Button_ArabicLang_XPATH)
    #     self.check_display_status_of_element("Verify_ArabicLang_XPATH",Login.Verify_ArabicLoginTitle_XPATH)
    #
    # @allure.step("Verify Language chnage from Arabic to English on Longin Page")
    # def Change_Language_Arabic_EN(self):
    #     self.Click("Button_ArabicLang_XPATH", Login.Button_ArabicLang_XPATH)
    #     self.Click("Button_EnglishLang_XPATH",Login.Button_EnglishLang_XPATH)
    #     self.check_display_status_of_element("Verify_LoginTitle_XPATH",Login.Verify_LoginTitle_XPATH)
    #
    # @allure.step("Verify Aldar Header on Login Page")
    # def Verify_AldarHeader(self):
    #     self.check_display_status_of_element("Verify_LoginTitle_XPATH", Login.Verify_LoginTitle_XPATH)
    #
    # @allure.step("Verify T&C on Registration page")
    # def Verify_TermsAndConditions(self):
    #     self.Click("Button_SignUp_XPATH",Login.Button_SignUp_XPATH)
    #     self.check_display_status_of_element("Verify_TC_XPATH",Login.Verify_TC_XPATH)
    #
    # @allure.step("Verify error with invalid email ID on registrationpage")
    # def Verify_InvalidEmail_RegisterPage(self):
    #     self.Click("Button_SignUp_XPATH", Login.Button_SignUp_XPATH)
    #     self.Type("xyz@test.com","Input_Email_XPATH",Login.Input_SigUpEmail_XPATH)
    #     self.Click("Verify_TC_XPATH", Login.Verify_TC_XPATH)
    #     time.sleep(2)
    #     self.Scroll_ByDistance(5000)
    #     # self.Scroll_ByElement("Button_Accept_XPATH",Login.Button_Accept_XPATH)
    #     self.Click("Button_Accept_XPATH",Login.Button_Accept_XPATH)
    #     self.Click("Button_Register_XPATH",Login.Button_Register_XPATH)
    #     self.check_display_status_of_element("Verify_InvalidEmailError_XPATH",Login.Verify_InvalidEmailError_XPATH)