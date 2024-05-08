import pytest

from conftest import *
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("browserSetup")
class Test_Login:

    def setup_class(self):
        self.driver.get(BaseUrl)
        self.login_page = LoginPage(self.driver)

    def test_validLogin(self):
        self.login_page.login(Username, Password)

    def teardown_class(self):
        self.driver.quit()

