"""Protect product-form classification without changing the merchant's catalog."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from catmap import category


class ResinClassificationTests(unittest.TestCase):
    def test_measured_resin_stick_pack_burns_as_sticks(self):
        for title in (
            'Sweetgrass Pure Resin Incense 10 Sticks Per Pack Fred Solls',
            'Frankincense & Myrrh Pure Resin Incense 10 sticks per pack',
        ):
            with self.subTest(title=title):
                self.assertEqual(category({'title': title, 'product_type': 'Resin Incense'}), 'sticks')

    def test_loose_resin_with_sticks_in_brand_stays_resin(self):
        for title in (
            'Jinx Removing Natural Resin Incense 30 Grams - Soul Sticks',
            'Soul Sticks Santa Muerte Natural Resin Incense 30g',
            'Frankincense Resin 1 oz',
        ):
            with self.subTest(title=title):
                self.assertEqual(category({'title': title, 'product_type': 'Resin Incense'}), 'resins')

    def test_charcoal_and_salt_exceptions_remain(self):
        self.assertEqual(category({'title': 'Charcoal 10 Sticks', 'product_type': 'Resin Incense'}), 'burners')
        self.assertIsNone(category({'title': 'Black Ritual Salt', 'product_type': 'Resin Incense'}))
