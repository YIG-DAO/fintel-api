from flask import Blueprint
from controller import cyberController

VERSION = '/v1/cyber'
cyber_blueprint = Blueprint('cyber_blueprint', __name__, url_prefix=VERSION)


@cyber_blueprint.route('/cti/sources')
def getCTISources():
    return cyberController.getCTISources()

@cyber_blueprint.route('/cti/gov/sources')
def getGovCTISources():
    return cyberController.getGovCTISources()

