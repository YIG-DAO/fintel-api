from flask import jsonify
import json
from model import scythe

from helper.redis import fetch_and_cache_data

def getStockRecommendation(asset):
    data, from_cache = fetch_and_cache_data(scythe.getStockRecomendation, f"getStockRecommendation:{asset}", True, asset)
    return jsonify({'data': data, 'from_cache': from_cache}), 200

def getStockSummary(asset):
    data, from_cache = fetch_and_cache_data(scythe.getStockSummary, f"getStockSummary:{asset}", False, asset)
    return jsonify({'data': data, 'from_cache': from_cache}), 200

def getLatestGovContracts():
    data, from_cache = fetch_and_cache_data(scythe.getLatestGovContracts, "getLatestGovContracts", True)
    return jsonify({'data': data, 'from_cache': from_cache}), 200

def getTickerGovContracts(ticker):
    data, from_cache = fetch_and_cache_data(scythe.getTickerGovContracts, f"getTickerGovContracts:{ticker}", True, ticker)
    return jsonify({'data': data, 'from_cache': from_cache}), 200

def getCorpLobbying():
    data, from_cache = fetch_and_cache_data(scythe.getCorpLobbying, "getCorpLobbying", True)
    return jsonify({'data': data, 'from_cache': from_cache}), 200

def getCongressTrades():
    data, from_cache = fetch_and_cache_data(scythe.getCongressTrades, "getCongressTrades", True)
    return jsonify({'data': data, 'from_cache': from_cache}), 200