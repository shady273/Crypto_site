import pprint

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

crypto_dict = {
    'btc': 'bitcoin',
    'eth': 'ethereum',
    'usdt': 'tether',
    'bnb': 'binancecoin',
    'usdc': 'usd-coin',
    'busd': 'binance-usd',
    'xrp': 'ripple',
    'ada': 'cardano',
    'doge': 'dogecoin',
    'matic': 'matic-network',
    'dot': 'polkadot',
    'dai': 'dai',
}

type_coin = {
    'base': ['btc', 'eth'],
    'altcoins': ['xrp', 'bnb', 'ada', 'doge', 'matic', 'dot'],
    'stablecoins': ['usdt', 'usdc', 'busd', 'dai']
}


# Create your views here.

def index(request):
    crypto = list(crypto_dict)
    data = {
        'crypto': crypto
    }
    return render(request, 'crypto/home_page.html', context=data)


def get_crypto_info(request, crypto_symbol: str):
    data = {}
    coin_id = crypto_dict.get(crypto_symbol, None)
    if coin_id in crypto_dict.values():
        coin_data = cg.get_coin_by_id(coin_id)
        # pprint.pprint(coin_data)
        name = coin_data['name']
        image = coin_data['image']['small']
        tickers = coin_data['tickers']
        pprint.pprint(tickers)
        try:
            price = "{:,.3f}".format(coin_data['market_data']['current_price']['usd'])
        except Exception:
            price = 0
        try:
            market_cap = "{:,.2f}".format(coin_data['market_data']['market_cap']['usd'])
        except Exception:
            market_cap = 0
        try:
            price_change_24h = "{:,.2f}".format(coin_data['market_data']['price_change_percentage_24h'])
        except Exception:
            price_change_24h = 0
        data = {
            'name': name,
            'price': price,
            'market_cap': market_cap,
            'price_change_24h': price_change_24h,
            'image': image,
            'tickers': tickers
        }
    return render(request, 'crypto/info_crypto.html', context=data)


def get_crypto_info_by_id(request, crypto_id: int):
    crypto = list(crypto_dict)
    if crypto_id > len(crypto):
        page404 = f'''
        <TITLE>ERROR 404</TITLE> 
        <BODY BGCOLOR=#1A1A1A TEXT=WHITE>r
        <H1 ALIGN= CENTER><BIG>У нас немає данних про {crypto_id}</H1></BODY>'''
        return HttpResponseNotFound(page404)
    name_crypto = crypto[crypto_id - 1]
    redirect_url = reverse('crypto_name', args=[name_crypto])
    return HttpResponseRedirect(redirect_url)


def get_type_info(request):
    crypto = list(type_coin)
    data = {
        'type_crypto': crypto
    }
    return render(request, 'crypto/type_crypto.html', context=data)


def get_type(request, type_crypto: str):
    coin_type = type_coin.get(type_crypto, None)
    if coin_type in type_coin.values():
        data = {
            'title': coin_type,
            'type_crypto': type_crypto
        }
        return render(request, 'crypto/list_type.html', context=data)
