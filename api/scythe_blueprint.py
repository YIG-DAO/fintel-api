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