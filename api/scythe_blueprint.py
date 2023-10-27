from flask import Blueprint, request
from controller import scytheController

VERSION = '/v1/scythe'
scythe_blueprint = Blueprint('scythe_blueprint', __name__, url_prefix=VERSION)

""" @scythe_blueprint.route('/stocks/recommend')
def getStockRecommendation():
    if request.args is None:
        return "Invalid API Call", 400
    else:
        asset = request.args['asset']
        return scytheController.getStockRecommendation(asset)

@scythe_blueprint.route('/stocks/summary')
def getStockSummary():
    if request.args is None:
        return "Invalid API Call", 400
    else:
        asset = request.args['asset']
        return scytheController.getStockSummary(asset) """

@scythe_blueprint.route('/gov/contracts/latest')
def getLatestGovContracts():
    return scytheController.getLatestGovContracts()

@scythe_blueprint.route('/gov/contracts/<ticker>')
def getTickerGovContracts(ticker):
    return scytheController.getTickerGovContracts(ticker=ticker)

@scythe_blueprint.route('/corp/lobbying')
def getCorpLobbying():
    return scytheController.getCorpLobbying()

@scythe_blueprint.route('/gov/congress/trades')
def getCongressTrades():
    return scytheController.getCongressTrades()