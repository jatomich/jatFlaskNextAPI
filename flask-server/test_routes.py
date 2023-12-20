import unittest
import pandas as pd
from .app import create_app, routes
from config import TestConfig


class RoutesTestCase(unittest.TestCase):
    """
    Test case class for testing routes in the Flask application.
    """

    def setUp(self):
        self.app = create_app(TestConfig)
        self.ctx = self.app.app_context()
        self.ctx.push()
        self.client = self.app.test_client(use_cookies=False)

    def test_clean_netflix_data(self):
        # Create a sample dataframe
        df = pd.DataFrame({
            'title': ['Movie A', 'Movie B', 'Movie C'],
            'show_id': ['s123', 's456', 's789'],
            'date_added': ['2022-01-01', '2022-02-01', '2022-03-01'],
            'duration': ['120 min', '90 min', '150 min']
        })

        # Call the clean_netflix_data function
        cleaned_df = routes.clean_netflix_data(df)

        # Assert that the dataframe is cleaned correctly
        self.assertEqual(len(cleaned_df), 3)
        self.assertEqual(cleaned_df['show_id'].tolist(), [123, 456, 789])
        self.assertEqual(cleaned_df['year_added'].tolist(), [2022, 2022, 2022])
        self.assertEqual(cleaned_df['month_added'].tolist(), ['January', 'February', 'March'])
        self.assertEqual(cleaned_df['day_added'].tolist(), ['Saturday', 'Tuesday', 'Tuesday'])
        self.assertEqual(cleaned_df['runtime'].tolist(), [120, 90, 150])
        self.assertEqual(cleaned_df['time_denomination'].tolist(), ['min', 'min', 'min'])
        self.assertEqual(list(cleaned_df.columns), ['title', 'show_id', 'year_added', 'month_added', 'day_added', 'runtime', 'time_denomination'])

    def test_load_database(self):
        # Send a GET request to the load_database route
        response = self.client.get('/api')

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the response data is not empty
        self.assertIsNotNone(response.json['data'])

        # Assert that the response data is a list of dictionaries
        self.assertIsInstance(response.json['data'], list)
        for item in response.json['data']:
            self.assertIsInstance(item, dict)

        # Assert that the response data contains the expected keys
        expected_keys = ['title', 'show_id', 'year_added', 'month_added', 'day_added', 'runtime', 'time_denomination']
        for item in response.json['data']:
            self.assertCountEqual(list(item.keys()), expected_keys)

    def tearDown(self):
        self.ctx.pop()

if __name__ == '__main__':
    unittest.main()