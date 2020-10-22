
import unittest
from tests.test_user import User
from tests.test_component import Component
from tests.test_product import Product


def suite():
    suite = unittest.TestSuite()
    suite.addTest(User('test_register_user'))
    suite.addTest(User('test_login'))
    suite.addTest(User('test_delete_user'))
    suite.addTest(Product('test_add_product'))
    suite.addTest(Product('test_get_products'))
    suite.addTest(Product('test_get_one_product'))
    suite.addTest(Product('test_edit_product'))
    suite.addTest(Product('test_delete_product'))
    suite.addTest(Component('test_add_component'))
    suite.addTest(Component('test_get_all_components'))
    suite.addTest(Component('test_get_component'))
    suite.addTest(Component('test_edit_component'))
    suite.addTest(Component('test_delete_component'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    suite = suite()
    runner.run(suite)
