import unittest
from src.services.search_service import search_unspsc_code

class TestSearchService(unittest.TestCase):

    def test_exact_match(self):
        result = search_unspsc_code("Scanning electron microscope")
        self.assertEqual(result, "41111720 - Scanning electron microscopes")

    def test_partial_match(self):
        result = search_unspsc_code("SEM")
        self.assertEqual(result, "41111720 - Scanning electron microscopes")

    def test_synonym_match(self):
        result = search_unspsc_code("SE Microscope")
        self.assertEqual(result, "41111720 - Scanning electron microscopes")

    def test_no_match(self):
        result = search_unspsc_code("Nonexistent equipment")
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()