from django.test import TestCase

# Create your tests here.


import pprint

from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

check_symbol = cg.get_coins_list()

pprint.pprint(check_symbol)