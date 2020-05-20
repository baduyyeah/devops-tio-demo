from app import app, db
from flask import url_for
import unittest
import xmlrunner


class FlaskTodosTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        """Assert that user successfully lands on homepage"""
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)



if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))