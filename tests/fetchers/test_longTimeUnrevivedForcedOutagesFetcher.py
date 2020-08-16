import unittest
import datetime as dt
from src.config.appConfig import getConfig
from src.fetchers.longTimeUnrevivedForcedOutagesFetcher import fetchlongTimeUnrevivedForcedOutages
from src.typeDefs.outage import IOutage
from typing import List


class TestFetchlongTimeUnrevivedForcedOutages(unittest.TestCase):
    appDbConStr: str = ''

    def setUp(self):
        appConfig = getConfig()
        self.appDbConStr = appConfig['appDbConStr']

    def test_run(self) -> None:
        """tests the function that fetches the ouatges from reporting software
        """
        startDate = dt.datetime(2020, 8, 2)
        endDate = dt.datetime(2020, 8, 8)

        outages: List[IOutage] = fetchlongTimeUnrevivedForcedOutages(
            self.appDbConStr, startDate, endDate)
        # print(outages)
        self.assertTrue(len(outages) > 0)
