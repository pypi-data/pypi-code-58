
from datetime import datetime, timedelta
import sys
import unittest

# tested component
sys.path.append(".")
from waybackmachine import WaybackMachine

class TestIterate(unittest.TestCase):
    def test_fetcher(self):
        x = WaybackMachine(
            'https://www.gov.pl/web/koronawirus/wykaz-zarazen-koronawirusem-sars-cov-2',
            start = "2020-05-01", end = "2020-04-15")
        x.yield_fetchers()
        
        previous = None
        for fetcher in x:
            # check date order
            if previous is not None:
                self.assertGreater(previous.date(), fetcher.date())
            previous = fetcher
    
    def test_response(self):
        x = WaybackMachine(
            'https://www.gov.pl/web/koronawirus/wykaz-zarazen-koronawirusem-sars-cov-2',
            start = "2020-05-01", end = "2020-04-15")
        previous = None
        for response,version_date in x:
            # check date order
            if previous is not None:
                self.assertLess(version_date, previous)
            previous = version_date
            # check status
            self.assertEqual(response.status_code, 200)
        