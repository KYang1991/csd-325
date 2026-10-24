
import unittest
from city_functions import city_country


class CitiesTestCase(unittest.TestCase):
    """Tests for city_functions.py."""

    def test_city_country(self):
        """Check that Santiago, Chile is formatted correctly."""
        formatted_location = city_country("santiago", "chile")
        self.assertEqual(formatted_location, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()
