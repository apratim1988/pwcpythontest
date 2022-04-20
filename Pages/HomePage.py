import time

from Pages.BasePage import BasePage
from Pages.FligtSelectionPage import FlightSelectionPage

class HomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def SelectFromCity(self,fromcity):
        self.click("FromCityCLick_XPATH")
        time.sleep(2)
        self.type("FromCityInputText_XPATH",fromcity)
        time.sleep(3)
        self.click("SelectFromCity_XPATH")
        time.sleep(2)

    def SelectToCity(self,tocity):
        self.click("ToCityClick_XPATH")
        time.sleep(2)
        self.type("ToCityInputText_XPATH",tocity)
        time.sleep(3)
        self.click("SelectToCity_XPATH")
        time.sleep(2)


    def SelectDate(self):
        self.click("CalenderClick_XPATH")
        time.sleep(2)
        self.click("SelectDate_XPATH")
        time.sleep(2)

    def ClickSearch(self):
        self.click("Search_XPATH")
        time.sleep(10)
        flightselectionpage = FlightSelectionPage(self.driver)
        return flightselectionpage

