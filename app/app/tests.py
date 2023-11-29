"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calc.add(8, 10)

        self.assertEqual(res, 18)

    def test_subtract_numbers(self):
        """Test subtracting numbers."""
        res = calc.subtract(15, 5)

        self.assertEqual(res, 10)
