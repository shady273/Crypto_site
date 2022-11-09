from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()


# Create your views here.

def get_crypto_info(request, crypto_symbol):
    check_symbol = cg.get_coins_list()
    filtered = filter(lambda x: x['symbol'] == crypto_symbol.lower(), check_symbol)
    statuses = [x['id'] for x in filtered]
    statuses.sort(key=len)
    coin_data = cg.get_coin_by_id(id=statuses[0])
    name = coin_data['name']
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

    text = f'''
    ✅ {name}
    ❇ Ціна {price} - USD
    📈 Зміна ціни 24h  {price_change_24h} %
    💰 Капіталізація {market_cap} - USD
    '''
    print(text)

    return HttpResponse(text)

