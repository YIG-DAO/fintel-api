from flask import Blueprint
from controller import cryptoController

VERSION = '/v1/crypto'
crypto_blueprint = Blueprint('crypto_blueprint', __name__, url_prefix=VERSION)

@crypto_blueprint.route('/usd/<crypto_symbol>')
def get_crypto_usd(crypto_symbol):
    return cryptoController.get_crypto_usd(crypto_symbol)

@crypto_blueprint.route('/usd/all')
def get_crypto_usd_all():
    return cryptoController.get_crypto_usd_all()

@crypto_blueprint.route('/eur/<crypto_symbol>')
def get_crypto_eur(crypto_symbol):
    return cryptoController.get_crypto_usd(crypto_symbol)

@crypto_blueprint.route('/eur/all')
def get_crypto_eur_all():
    return cryptoController.get_crypto_eur_all()