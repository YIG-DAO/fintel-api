from flask import jsonify
import json
from model import econ

def getFinanceSources():
    data = econ.getEconSources()
    payload = jsonify({'data':data}), 200
    return payload

def getGovFinanceSources():
    data = econ.getGovEconSources()
    payload = jsonify({'data':data}), 200
    return payload

def getEconomicEvents():
    data = econ.getEconomicEvents()
    prepped_data = json.loads(data.to_json(orient='table'))
    payload = jsonify(prepped_data), 200
    return payload

def getEconomicOverview():
    data = econ.getEconomicOverview()
    prepped_data = json.loads(data.to_json(orient='table'))
    payload = jsonify(prepped_data), 200
    return payload

def getTrendingStocks():
    data = econ.getTrendingStocks()
    prepped_data = json.loads(data.to_json(orient='table'))
    payload = jsonify(prepped_data), 200
    return payload

def getCovidCases(country):
    """
    TODO MODIFY PAYLOAD FOR PROPER CONSUMPTION
    """
    data = econ.getCovidCases(country)
    prepped_data = json.loads(data.to_json())
    payload = jsonify({'data':prepped_data})
    return payload