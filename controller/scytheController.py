from flask import jsonify
import json
from model import scythe

def getStockRecommendation(asset):
    data = scythe.getStockRecomendation(asset)
    prepped_data = json.loads(data.to_json(orient='table'))
    payload = jsonify(prepped_data)
    return payload, 200

def getStockSummary(asset):
    data = scythe.getStockSummary(asset)
    #prepped_data = json.loads(data.to_json(orient='table'))
    payload = jsonify(data)
    return payload