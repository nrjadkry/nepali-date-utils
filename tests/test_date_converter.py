import sys
import unittest
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from nepali_date_utils.date_converter import converter

class TestDateConverter(unittest.TestCase):

    # Test data sets
    test_data = [
        {"bs_date": "2054/04/01", "ad_date": "1997/07/16"},
        {"bs_date": "2055/09/15", "ad_date": "1998/12/30"},
        {"bs_date": "2077/04/20", "ad_date": "2020/08/04"},

        {"bs_date": "2080/02/32", "ad_date": "2023/06/15"},
        {"bs_date": "2080/01/31", "ad_date": "2023/05/14"},

        {"bs_date": "2003/12/31", "ad_date": "1947/04/13"},
        {"bs_date": "2004/01/01", "ad_date": "1947/04/14"},
        {"bs_date": "2003/01/31", "ad_date": "1946/05/13"},


        # This should fail
        # {"bs_date": "2080/01/32", "ad_date": "2023/05/15"},


    ]

    def test_bs_to_ad(self):
        for data in self.test_data:
            bs_date = data["bs_date"]
            ad_date = data["ad_date"]
            actual_ad_date = converter.bs_to_ad(bs_date)
            self.assertEqual(actual_ad_date, ad_date)

if __name__ == '__main__':
    unittest.main()