"""A scent-based source category must not turn a non-incense product into incense."""
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'site'))
import sitecopy


class ProductCopyTests(unittest.TestCase):
    def copy(self, title, aisle):
        return ' '.join(sitecopy.describe(SimpleNamespace(BRAND_NAME={}),
                                        {'title': title, 'aisle': aisle, 'brand': ''}))

    def test_non_incense_formats_do_not_inherit_burning_instructions(self):
        for title, aisle in (
            ('Murray & Lanman Palo Santo Cologne', 'palo'),
            ('Murray & Lanman White Sage with Lavender Cologne', 'smudge'),
            ('Kamini White Sage Soap 100g', 'smudge'),
            ('Satya Frankincense fragrance oil', 'incense'),
        ):
            with self.subTest(title=title):
                text = self.copy(title, aisle)
                self.assertIn('product label', text)
                self.assertNotRegex(text.lower(), r'flame|light the|lit charcoal|smolder|burns|lights directly')

    def test_incense_scented_with_essential_oils_keeps_incense_instructions(self):
        self.assertIn('lights directly', self.copy('White Sage Incense With Essential Oils', 'incense'))

    def test_soapstone_is_not_mistaken_for_soap(self):
        self.assertIn('vessel', self.copy('Black Soapstone Cone Burner', 'burners'))
