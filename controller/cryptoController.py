from flask import jsonify
import json
from model import crypto

from helper.redis import fetch_and_cache_data

def get_crypto_usd(crypto_symbol):
    data, from_cache = fetch_and_cache_data(crypto.get_crypto_usd, f"get_crypto_usd:{crypto_symbol}", False, crypto_symbol)
    return jsonify({'data': data, 'from_cache': from_cache}), 200

def get_crypto_usd_all():
    data, from_cache = fetch_and_cache_data(crypto.get_crypto_usd_all, "get_crypto_usd_all", False)
    return jsonify({'data': data, 'from_cache': from_cache}), 200

def get_crypto_eur(crypto_symbol):
    data, from_cache = fetch_and_cache_data(crypto.get_crypto_eur, f"get_crypto_eur:{crypto_symbol}", False, crypto_symbol)
    return jsonify({'data': data, 'from_cache': from_cache}), 200

def get_crypto_eur_all():
    data, from_cache = fetch_and_cache_data(crypto.get_crypto_eur_all, "get_crypto_eur_all", False)
    return jsonify({'data': data, 'from_cache': from_cache}), 200

def get_crypto_trending():
    data, from_cache = fetch_and_cache_data(crypto.getTrendingCrypto, "get_crypto_trending", True)
    return jsonify({'data': data, 'from_cache': from_cache}), 200