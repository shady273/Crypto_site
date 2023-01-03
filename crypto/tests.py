from django.test import TestCase

# Create your tests here.


import pprint

from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

# check_symbol = cg.get_exchanges_by_id('korbit')
# print(check_symbol['image'])
# pprint.pprint(check_symbol)
# coin_data = cg.get_coin_by_id('bitcoin')
# tickers = coin_data['tickers']
# exchange_img = dict()
# for img in tickers:
#     exchange_id = img['market']['identifier']
#     exch_data = cg.get_exchanges_by_id(exchange_id)
#     img_link = exch_data['image']
#     print(img_link)
#     print(exchange_id)
#     if exchange_id in exchange_img:
#         pass
#     else:
#         exchange_img.update({exchange_id: img_link})
# pprint.pprint(exchange_img)

# coin_data = cg.get_coin_by_id('bitcoin')
#
# tickers = coin_data['tickers']
# # pprint.pprint(tickers)
#
# exchange = dict()
# for i in tickers:
#     exchange_name = i['market']['name']
#     base = i['base']
#     target = i['target']
#     trading_pair = f'{base}/{target}'
#     exchange_url = i['trade_url']
#     if exchange_name not in exchange:
#         if exchange_url is None:
#             pass
#         else:
#             exchange.update({exchange_name: {trading_pair: exchange_url}})
#     elif exchange_name in exchange:
#         exchange[exchange_name].update({trading_pair: exchange_url})
#
# pprint.pprint(exchange)
exchange_img = {'bigone': 'https://assets.coingecko.com/markets/images/100/small/qcFFufEY_400x400.jpg?1561103345',
 'binance': 'https://assets.coingecko.com/markets/images/52/small/binance.jpg?1519353250',
 'binance_us': 'https://assets.coingecko.com/markets/images/469/small/Binance.png?1568875842',
 'bingx': 'https://assets.coingecko.com/markets/images/812/small/YtFwQwJr_400x400.jpg?1646056092',
 'bitbank': 'https://assets.coingecko.com/markets/images/122/small/bitbank.jpg?1521186278',
 'bitfinex': 'https://assets.coingecko.com/markets/images/4/small/BItfinex.png?1615895883',
 'bitflyer': 'https://assets.coingecko.com/markets/images/5/small/bitFlyer-logo.png?1643256033',
 'bitforex': 'https://assets.coingecko.com/markets/images/214/small/BitForex-Logo.png?1573808227',
 'bitget': 'https://assets.coingecko.com/markets/images/540/small/Bitget_new_logo_2.png?1630049618',
 'bitmart': 'https://assets.coingecko.com/markets/images/239/small/Bitmart.png?1628066397',
 'bitpanda': 'https://assets.coingecko.com/markets/images/474/small/appicon-ios-pro.png?1622626638',
 'bitstamp': 'https://assets.coingecko.com/markets/images/9/small/bitstamp.jpg?1519627979',
 'bitvavo': 'https://assets.coingecko.com/markets/images/714/small/bitvavo-mark-square-black.png?1633688872',
 'bkex': 'https://assets.coingecko.com/markets/images/293/small/New_BKEX_logo.png?1646724631',
 'btcex': 'https://assets.coingecko.com/markets/images/753/small/C8tiQdwL_400x400.jpg?1641348961',
 'btse': 'https://assets.coingecko.com/markets/images/464/small/BTSE.jpg?1568012415',
 'bybit_spot': 'https://assets.coingecko.com/markets/images/698/small/bybit_spot.png?1629971794',
 'coincheck': 'https://assets.coingecko.com/markets/images/18/small/Coincheck.jpg?1519703836',
 'coinsbit': 'https://assets.coingecko.com/markets/images/267/small/Coinsbit.png?1605153697',
 'coinzoom': 'https://assets.coingecko.com/markets/images/656/small/Up7Yiexp_400x400.png?1619165177',
 'crypto_com': 'https://assets.coingecko.com/markets/images/589/small/h2oMjPp6_400x400.jpg?1669699705',
 'currency': 'https://assets.coingecko.com/markets/images/512/small/Currency.com_200x200.png?1582086630',
 'dcoin': 'https://assets.coingecko.com/markets/images/319/small/%E8%B5%84%E6%BA%90_4_3x_2.png?1590117049',
 'delta_spot': 'https://assets.coingecko.com/markets/images/642/small/delta_spot.jpg?1617283005',
 'dextrade': 'https://assets.coingecko.com/markets/images/380/small/Dex-Trade_logo_new.png?1599629803',
 'digifinex': 'https://assets.coingecko.com/markets/images/225/small/DF_logo.png?1594264355',
 'finexbox': 'https://assets.coingecko.com/markets/images/318/small/finexbox20190920.jpg?1568959220',
 'gate': 'https://assets.coingecko.com/markets/images/60/small/gate_io_logo1.jpg?1654596784',
 'gdax': 'https://assets.coingecko.com/markets/images/23/small/Coinbase_Coin_Primary.png?1621471875',
 'gemini': 'https://assets.coingecko.com/markets/images/50/small/gemini.png?1605704107',
 'gmo_japan': 'https://assets.coingecko.com/markets/images/430/small/gmo_z_com.png?1561112572',
 'huobi': 'https://assets.coingecko.com/markets/images/25/small/logo_V_colour_black.png?1669177364',
 'itbit': 'https://assets.coingecko.com/markets/images/26/small/itbit.png?1519810172',
 'kanga': 'https://assets.coingecko.com/markets/images/852/small/kanga_logo.png?1650269423',
 'kraken': 'https://assets.coingecko.com/markets/images/29/small/kraken.jpg?1584251255',
 'kucoin': 'https://assets.coingecko.com/markets/images/61/small/kucoin.png?1640584259',
 'latoken': 'https://assets.coingecko.com/markets/images/124/small/LA_token.png?1605773251',
 'lbank': 'https://assets.coingecko.com/markets/images/118/small/LBank_logo.png?1666234663',
 'localtrade': 'https://assets.coingecko.com/markets/images/338/small/LT_Icon_Main.png?1664328842',
 'mxc': 'https://assets.coingecko.com/markets/images/409/small/MEXC_GLOBAL_LOGO.png?1669730504',
 'okex': 'https://assets.coingecko.com/markets/images/96/small/WeChat_Image_20220117220452.png?1642428377',
 'p2pb2b': 'https://assets.coingecko.com/markets/images/251/small/ow0xng56_400x400.jpeg?1664939403',
 'phemex': 'https://assets.coingecko.com/markets/images/564/small/Phemex_logo_4.png?1641357471',
 'tidex': 'https://assets.coingecko.com/markets/images/43/small/favicon.png?1651817092',
 'txbit': 'https://assets.coingecko.com/markets/images/366/small/kamyliB.png?1551871576',
 'whitebit': 'https://assets.coingecko.com/markets/images/418/small/whitebit_final.png?1667923522',
 'wootrade': 'https://assets.coingecko.com/markets/images/683/small/wootrade.jpg?1624621149',
 'xt': 'https://assets.coingecko.com/markets/images/404/small/logo400x400.png?1575881839'}

