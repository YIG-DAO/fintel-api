import sys
import os
from datetime import datetime
from sqlalchemy import update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

from db.orm import crypto, base
import yminer.fetch
from configparser import ConfigParser


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

def yminer_config(filename=BASE_DIR+'/yminer.ini', section='cmc'):

    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return config

CryptoUSD = crypto.Crypto
CryptoEUR = crypto.CryptoEUR
gds_conn = base.session

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
usd_parameters = {
    'start': 1,
    'limit': 50,
  'convert':'USD'
}
eur_parameters = {
    'start': 1,
    'limit': 50,
  'convert':'EUR'
}

def update_usd_crypto():
  payload = yminer.fetch.yeetPayload(url,usd_parameters,headers)
  for i in payload:
    print(f"Headers on get request \n{headers}")
    print(f"Updating table crypto_usd for {i['name']}")
    update_data = update(CryptoUSD)
    update_data.values(i)
    update_data.where(CryptoUSD.id == i['id'])
    gds_conn.execute(update_data)
    gds_conn.commit()

def update_eur_crypto():
  payload = yminer.fetch.yeetPayload(url,eur_parameters,headers)
  for i in payload:
    print(f"Updating table crypto_eur for {i['name']}")
    update_data = update(CryptoEUR)
    update_data.values(i)
    update_data.where(CryptoEUR.id == i['id'])
    gds_conn.execute(update_data)
    gds_conn.commit()

def update_crypto_tables():
  config = yminer_config()
  CMC_KEY = config['key']
  headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': CMC_KEY,
  }
  print(f'Update Crypto Tables starting @ {datetime.now()}')
  usdPayload = yminer.fetch.yeetPayload(url,usd_parameters,headers)
  eurPayload = yminer.fetch.yeetPayload(url,eur_parameters,headers)
  for i in usdPayload:
    print(f"Updating table crypto_usd for {i['name']}")
    updated_usd_data = update(CryptoUSD)
    updated_usd_data.values(i)
    updated_usd_data.where(CryptoUSD.id == i['id'])
    gds_conn.execute(updated_usd_data)

  for i in eurPayload:
    print(f"Updating table crypto_eur for {i['name']}")
    updated_eur_data = update(CryptoEUR)
    updated_eur_data.values(i)
    updated_eur_data.where(CryptoEUR.id == i['id'])
    gds_conn.execute(updated_eur_data)
  
  gds_conn.commit()
  print(f'Update Crypto Tables finished @ {datetime.now()}')

def add_crypto(payload):
  for i in payload:
    print(i)
    crypto = CryptoUSD(i['id'], i['name'], i['symbol'], i['slug'], i['num_market_pairs'], i['date_added'],
                    i['tags'], i['max_supply'], i['circulating_supply'], i['total_supply'], i['cmc_rank'],
                    i['self_reported_circulating_supply'], i['tvl_ratio'], i['last_updated'], i['quote']['USD']['price'],
                    i['quote']['USD']['volume_24h'],i['quote']['USD']['volume_change_24h'], i['quote']['USD']['percent_change_1h'],
                    i['quote']['USD']['percent_change_24h'], i['quote']['USD']['percent_change_7d'], i['quote']['USD']['percent_change_30d'],
                    i['quote']['USD']['percent_change_60d'], i['quote']['USD']['percent_change_90d'], i['quote']['USD']['market_cap'], i['quote']['USD']['fully_diluted_market_cap'],
                    i['quote']['USD']['tvl'], i['quote']['USD']['last_updated'], str(datetime.now())
                    )
    gds_conn.add(crypto)
    gds_conn.commit()