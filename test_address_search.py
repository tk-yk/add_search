import unittest
from search_address import search_address


class TestSearchAddress(unittest.TestCase):
    def test_郵便番号から地名を検索できる(self):
        self.assertEqual('岩手県八幡平市大更', search_address(zipcode='0287111'))


if __name__ == '__main__':
    unittest.main()
