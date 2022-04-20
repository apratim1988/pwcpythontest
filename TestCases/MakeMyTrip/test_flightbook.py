import time
import sys
sys.path.append("../../../")
import pytest
from Pages.HomePage import HomePage
from TestCases.MakeMyTrip.BaseTest import BaseTest
from Utilities import dataProvider


class Test_FLightBook(BaseTest):
    @pytest.mark.parametrize("fromcity,tocity,firstname,lastname,mobileno,email",dataProvider.get_data("makemytrip"))
    def test_flightbooking(self,fromcity,tocity,firstname,lastname,mobileno,email,):

        try:
            home = HomePage(self.driver)
            home.SelectFromCity(fromcity)
            time.sleep(2)
            home.SelectToCity(tocity)
            time.sleep(2)
            home.SelectDate()
            time.sleep(2)
            flightselectionpage = home.ClickSearch()
            time.sleep(15)
            flightselectionpage.ClickCrossButton()
            time.sleep(2)
            inputdetailspage = flightselectionpage.SelectFlight()
            time.sleep(5)
            self.windowhandles()
            inputdetailspage.AddNewAdult()
            inputdetailspage.InputFirstName(firstname)
            inputdetailspage.InputLastName(lastname)
            inputdetailspage.InputEmail(email)
            inputdetailspage.InputMobileNo()
        except Exception as e:
            raise e


