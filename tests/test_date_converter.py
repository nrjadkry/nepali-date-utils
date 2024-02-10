# python3 -m unittest tests/test_date_converter.py

import sys
import unittest
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from nepali_date_utils.date_converter import converter

class TestDateConverter(unittest.TestCase):

    # Test data sets
    test_data = [
        {"bs_date": "2054/4/1", "ad_date": "1997/7/16"},
        {"bs_date": "2055/9/15", "ad_date": "1998/12/30"},
        {"bs_date": "2077/4/20", "ad_date": "2020/8/4"},

        {"bs_date": "2080/2/32", "ad_date": "2023/6/15"},
        {"bs_date": "2080/1/31", "ad_date": "2023/5/14"},

        {"bs_date": "2003/12/31", "ad_date": "1947/4/13"},
        {"bs_date": "2004/1/1", "ad_date": "1947/4/14"},
        {"bs_date": "2003/1/31", "ad_date": "1946/5/13"},
    ]

    exception_test_data=[
        {"bs_date": "2080/01/32", "ad_date": "2023/05/15"},
    ]

    def test_bs_to_ad(self):
        for data in self.test_data:
            bs_date = data["bs_date"]
            ad_date = data["ad_date"]
            converted_ad_date = converter.bs_to_ad(bs_date)
            self.assertEqual(converted_ad_date, ad_date)


    def test_ad_to_bs(self):
        for data in self.test_data:
            bs_date = data["bs_date"]
            ad_date = data["ad_date"]
            converted_bs_date = converter.ad_to_bs(ad_date)
            self.assertEqual(converted_bs_date, bs_date)

    # test for Date Out of Range exception
    def test_bs_to_ad_exception(self):
        for data in self.exception_test_data:
            bs_date = data["bs_date"]
            with self.assertRaises(ValueError):
                converter.bs_to_ad(bs_date)


if __name__ == '__main__':
    unittest.main()