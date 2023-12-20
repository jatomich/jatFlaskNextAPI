import unittest
from flask import Flask
from app import create_app
from config import TestConfig

class CreateAppTestCase(unittest.TestCase):
    """
    Test case for creating the Flask app.
    """

    def test_create_app(self):
        app = create_app(TestConfig)
        ctx = app.app_context()
        ctx.push()
        self.assertIsInstance(app, Flask)
        self.assertEqual(app.static_url_path, '/home/at/Documents/CODE/jatFlaskNextAPI/flask-server/app/static')
        self.assertEqual(app.static_folder, '/app/static')
        self.assertEqual(app.config['TESTING'], True)
        self.assertNotEqual(app.config['SECRET_KEY'], 'better-fix-this-asap')

if __name__ == '__main__':
    unittest.main()