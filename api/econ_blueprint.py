from flask import Blueprint, request
from controller import econController

VERSION = '/v1/economics'
econ_blueprint = Blueprint('econ_blueprint', __name__, url_prefix=VERSION)

@econ_blueprint.route('/sources')
def getEconSources():
    return econController.getFinanceSources()

@econ_blueprint.route('/gov/sources')
def getGovEconSources():
    return econController.getGovFinanceSources()

@econ_blueprint.route('/events')
def getEconomicEvents():
    return econController.getEconomicEvents()

@econ_blueprint.route('/overview')
def getEconomicOverview():
    return econController.getEconomicOverview()

@econ_blueprint.route('/stocks/trending')
def getTrendingStocks():
    return econController.getTrendingStocks()

@econ_blueprint.route('/stocks/news')
def getStocksNews():
    return econController.getStocksNews()

@econ_blueprint.route('/stocks/screener')
def getScreenerData():
    return econController.getScreenerData()

""" 
@econ_blueprint.route('/covid/cases')
def getCovidCases():
    
    Requires ?country=<Country_String>

   
    if request.args is None:
        return "Invalid query", 400
    else:
        country = request.args['country']
        return econController.getCovidCases(country) """