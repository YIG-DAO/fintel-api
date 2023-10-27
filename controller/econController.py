from flask import jsonify
import json
from model import econ
from helper.redis import fetch_and_cache_data

def getFinanceSources():
    data, from_cache = fetch_and_cache_data(econ.getEconSources, "getFinanceSources")
    return jsonify({'data': data, 'from_cache': from_cache}), 200

def getGovFinanceSources():
    data, from_cache = fetch_and_cache_data(econ.getGovEconSources, "getGovFinanceSources")
    return jsonify({'data': data, 'from_cache': from_cache}), 200

def getEconomicEvents():
    data, from_cache = fetch_and_cache_data(econ.getEconomicEvents, "getEconomicEvents", True)
    return jsonify({'data': data, 'from_cache': from_cache}), 200

def getEconomicOverview():
    data, from_cache = fetch_and_cache_data(econ.getEconomicOverview, "getEconomicOverview", True)
    return jsonify({'data': data, 'from_cache': from_cache}), 200

def getTrendingStocks():
    data, from_cache = fetch_and_cache_data(econ.getTrendingStocks, "getTrendingStocks", True)
    return jsonify({'data': data, 'from_cache': from_cache}), 200

def getStocksNews():
    data, from_cache = fetch_and_cache_data(econ.getStocksNews, "getStocksNews", True)
    return jsonify({'data': data, 'from_cache': from_cache}), 200

def getCovidCases(country):
    """
    TODO MODIFY PAYLOAD FOR PROPER CONSUMPTION
    """
    data = econ.getCovidCases(country)
    prepped_data = json.loads(data.to_json())
    payload = jsonify({'data':prepped_data})
    return payload