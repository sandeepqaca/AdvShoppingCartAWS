import unittest
import adshopcart_methods as methods
import adshopcart_locators as locators

class AdShopAppPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_aos_tests():
        methods.setUp()
        methods.navigate_homepage()
        methods.check_contact_us()
        methods.register()
        methods.log_out()
        methods.log_in()
        methods.delete_user()
        methods.login_with_deleted_cred()
        methods.tearDown()

