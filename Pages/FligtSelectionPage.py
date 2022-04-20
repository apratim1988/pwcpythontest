import time

from Pages.BasePage import BasePage
from Pages.InputDetailsPage import InputDetailsPage


class FlightSelectionPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def ClickCrossButton(self):
        self.click("CrossPopUp_XPATH")
        time.sleep(2)

    def SelectFlight(self):
        self.click("ClickViewPrices_XPATH")
        time.sleep(2)
        self.click("BookNowButton_XPATH")
        time.sleep(5)
        inputdetailspage = InputDetailsPage(self.driver)
        return inputdetailspage