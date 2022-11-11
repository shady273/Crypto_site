import pprint

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

crypto_dict = {
    'btc': 'bitcoin',
    'eth': 'ethereum',
    'xrp': 'ripple',
    'bnb': 'binancecoin',
    'ada': 'cardano',
    'doge': 'dogecoin',
    'matic': 'matic-network',
    'dot': 'polkadot'
}


# Create your views here.

def index(request):
    crypto = list(crypto_dict)
    li_elemens = str()
    for sing in crypto:
        redirect_path = reverse('crypto_name', args=[sing])
        li_elemens += f'<li><a href={redirect_path}>{sing.upper()}</a></li>'
    response = f'''
    <BODY BGCOLOR=#1A1A1A TEXT=WHITE>
    <H1 ALIGN= CENTER><BIG>
    <ul>
        {li_elemens}
    </ul>
    </H1></BODY>
    '''
    return HttpResponse(response)


def get_crypto_info(request, crypto_symbol: str):
    coin_id = crypto_dict.get(crypto_symbol, None)
    if coin_id:
        coin_data = cg.get_coin_by_id(coin_id)
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
            <TITLE>✅ {name}</TITLE>
            </HEAD>
            <BODY BGCOLOR=#1A1A1A TEXT=WHITE>
            <H1 ALIGN= CENTER><BIG>✅ {name}</BIG><BR>
            <P ALIGN= CENTER>❇ Ціна {price} - USD<BR>
            <P ALIGN= CENTER>📈 Зміна ціни 24h  {price_change_24h} %<BR>
            <P ALIGN= CENTER>💰 Капіталізація {market_cap} - USD</P></H1>
            </BODY>'''
        return HttpResponse(text)
    else:
        page404 = f'''
        <TITLE>ERROR 404</TITLE> 
        <BODY BGCOLOR=#1A1A1A TEXT=WHITE>
        <H1 ALIGN= CENTER><BIG>У нас немає данних про {crypto_symbol}</H1></BODY>'''
        return HttpResponse(page404)


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
