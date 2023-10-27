from flask import jsonify
import json
from model import scythe

def getStockRecommendation(asset):
    data = scythe.getStockRecomendation(asset)
    prepped_data = json.loads(data.to_json(orient='table'))
    payload = jsonify(prepped_data["data"])
    return payload, 200

def getStockSummary(asset):
    data = scythe.getStockSummary(asset)
    #prepped_data = json.loads(data.to_json(orient='table'))
    payload = jsonify(data)
    return payload

def getLatestGovContracts():
    data = scythe.getLatestGovContracts()
    prepped_data = json.loads(data.to_json(orient='table'))
    payload = jsonify(prepped_data["data"])
    return payload

def getTickerGovContracts(ticker):
    data = scythe.getTickerGovContracts(ticker)
    prepped_data = json.loads(data.to_json(orient='table'))
    payload = jsonify(prepped_data["data"])
    return payload

def getCorpLobbying():
    data = scythe.getCorpLobbying()
    prepped_data = json.loads(data.to_json(orient='table'))
    payload = jsonify(prepped_data["data"])
    return payload

def getCongressTrades():
    data = scythe.getCongressTrades()
    prepped_data = json.loads(data.to_json(orient='table'))
    payload = jsonify(prepped_data["data"])
    return payload