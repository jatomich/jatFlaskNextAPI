import unittest
from app.models import NetflixContent

class NetflixContentTestCase(unittest.TestCase):
    def setUp(self):
        # Create a sample NetflixContent object for testing
        self.content = NetflixContent(
            id=1,
            show_id=123,
            type='movie',
            title='Example Movie',
            director='John Doe',
            cast='Jane Smith',
            country='USA',
            date_added='2022-01-01',
            release_year=2021,
            rating='PG',
            runtime=120,
            time_denomination='min',
            listed_in='Action, Drama',
            description='An example movie',
            year_added=2022,
            month_added='January',
            day_added='1'
        )

    def test_init(self):
        # Test the initialization of NetflixContent object
        self.assertEqual(self.content.id, 1)
        self.assertEqual(self.content.show_id, 123)
        self.assertEqual(self.content.type, 'movie')
        self.assertEqual(self.content.title, 'Example Movie')
        self.assertEqual(self.content.director, 'John Doe')
        self.assertEqual(self.content.cast, 'Jane Smith')
        self.assertEqual(self.content.country, 'USA')
        self.assertEqual(self.content.date_added, '2022-01-01')
        self.assertEqual(self.content.release_year, 2021)
        self.assertEqual(self.content.rating, 'PG')
        self.assertEqual(self.content.runtime, 120)
        self.assertEqual(self.content.time_denomination, 'min')
        self.assertEqual(self.content.listed_in, 'Action, Drama')
        self.assertEqual(self.content.description, 'An example movie')
        self.assertEqual(self.content.year_added, 2022)
        self.assertEqual(self.content.month_added, 'January')
        self.assertEqual(self.content.day_added, '1')

    def test_repr(self):
        # Test the __repr__ method of NetflixContent object
        expected_repr = "<NetflixContent Example Movie>"
        self.assertEqual(repr(self.content), expected_repr)

    def test_query_all(self):
        # Test the query_all method of NetflixContent object
        # You can add your own assertions here based on your database setup
        result = self.content.query_all()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)

if __name__ == '__main__':
    unittest.main()