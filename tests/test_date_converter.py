import sys
import unittest
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from nepali_date_utils.date_converter import converter

class TestDateConverter(unittest.TestCase):

    # Test data sets
    test_data = [
        {"bs_date": "2054/04/1", "ad_date": "1997/07/16"},
        {"bs_date": "2055/09/15", "ad_date": "1998/12/30"},
        {"bs_date": "2077/04/20", "ad_date": "2020/08/04"},
    ]

    def test_bs_to_ad(self):
        for data in self.test_data:
            bs_date = data["bs_date"]
            expected_ad_date = data["ad_date"]
            actual_ad_date = converter.bs_to_ad(bs_date)
            self.assertEqual(actual_ad_date, expected_ad_date)

if __name__ == '__main__':
    unittest.main()