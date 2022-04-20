import time

from Pages.BasePage import BasePage


class InputDetailsPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def AddNewAdult(self):
        self.click("AddNewAdult_XPATH")
        time.sleep(2)

    def InputFirstName(self,firstname):
        self.type("FirstName_XPATH",firstname)
        time.sleep(1)

    def InputLastName(self,lastname):
        self.type("LastName_XPATH",lastname)
        time.sleep(1)

    def InputMobileNo(self,mobileno):
        self.type("MobileNo_XPATH",mobileno)
        time.sleep(1)

    def InputEmail(self,email):
        self.type("Email_XPATH",email)
        time.sleep(1)

