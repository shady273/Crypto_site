import pprint

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from pycoingecko import CoinGeckoAPI
from .forms import CalculatorForm

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
        # pprint.pprint(tickers)
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
        exchange = dict()
        for i in tickers:
            exchange_name = i['market']['name']
            base = i['base']
            target = i['target']
            trading_pair = f'{base}/{target}'
            exchange_url = i['trade_url']
            if exchange_name not in exchange:
                if exchange_url is None:
                    pass
                else:
                    exchange.update({exchange_name: {trading_pair: exchange_url}})
            elif exchange_name in exchange:
                exchange[exchange_name].update({trading_pair: exchange_url})
        data = {
            'name': name,
            'price': price,
            'market_cap': market_cap,
            'price_change_24h': price_change_24h,
            'image': image,
            'tickers': tickers,
            'exchange': exchange,
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


def calculator(request):
    aver_price = ''
    all_value = ''
    error = ''
    if request.method == 'POST':
        result = CalculatorForm(request.POST)
        if result.is_valid():
            price_1 = float(request.POST['price_1'])
            value_1 = float(request.POST['value_1'])
            price_2 = float(request.POST['price_2'])
            value_2 = float(request.POST['value_2'])
            cost_by = value_1 * price_1 + value_2 * price_2
            all_value = value_1 + value_2
            aver_price = cost_by / all_value
        else:
            error = 'Не вірно введені данні'
    form = CalculatorForm()
    data = {
        'form': form,
        'aver_price': aver_price,
        'all_value': all_value,
        'error': error
    }
    return render(request, 'crypto/calculator.html', data)


def login(request):
    return render(request, 'crypto/login.html')


def register(request):
    return render(request, 'crypto/register.html')