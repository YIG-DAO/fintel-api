from flask import jsonify
import json
from model import crypto

def get_crypto_usd(crypto_symbol):
    data = crypto.get_crypto_usd(crypto_symbol)
    payload = jsonify({'data':data}), 200
    return payload

def get_crypto_usd_all():
    data = crypto.get_crypto_usd_all()
    payload = jsonify({'data':data}), 200
    return payload

def get_crypto_eur(crypto_symbol):
    data = crypto.get_crypto_eur(crypto_symbol)
    payload = jsonify({'data':data}), 200
    return payload

def get_crypto_eur_all():
    data = crypto.get_crypto_eur_all()
    payload = jsonify({'data':data}), 200
    return payload

def get_crypto_trending():
    data = crypto.getTrendingCrypto()
    prepped_data = json.loads(data.to_json(orient='table'))
    payload = jsonify({'data':prepped_data["data"]}), 200
    return payload