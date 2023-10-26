from db.orm import crypto, base
#from openbb_terminal.sdk import openbb

CRYPTO = crypto.Crypto
CRYPTOEUR = crypto.CryptoEUR
SESSION = base.session

def get_crypto_usd(crypto_symbol):
    symbol = crypto_symbol.upper()
    query = SESSION.query(CRYPTO).filter_by(symbol= symbol).first()
    if query is not None:
        data = query.json()
        return data
    else:
        data = "Invalid Crypto Symbol"
        return data

def get_crypto_usd_all():
    query = SESSION.query(CRYPTO).all()
    if query is not None:
        data = {}
        for i in query:
            data.update({i.symbol: i.json()})
        return data
    else:
        data = "Improper Crypto Symbol"
        return data

def get_crypto_eur(crypto_symbol):
    symbol = crypto_symbol.upper()
    query = SESSION.query(CRYPTOEUR).filter_by(symbol= symbol).first()
    if query is not None:
        data = query.json()
        return data
    else:
        data = "Improper Crypto Symbol"
        return data

def get_crypto_eur_all():
    query = SESSION.query(CRYPTOEUR).all()
    if query is not None:
        data = {}
        for i in query:
            data.update({i.symbol: i.json()})
        return data
    else:
        data = "Improper Crypto Symbol"
        return data
