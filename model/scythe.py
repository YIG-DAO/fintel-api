from openbb_terminal.sdk import openbb

""" 
def getStockRecomendation(asset):
    data = openbb.stocks.ta.recom(asset)
    if data is not None:
        return data
    else: 
        return "Empty Response"

def getStockSummary(asset):
    data = openbb.stocks.ta.summary(asset)
    if data is not None:
        return data
    else: 
        return "Empty Response" 
"""

def getLatestGovContracts():
    query = openbb.stocks.gov.lastcontracts(past_transaction_days=7)
    if query is not None:
        data = query
        return data
    else:
        data = "OpenBB query issue"
        return data

def getTickerGovContracts(ticker):
    query = openbb.stocks.gov.contracts(symbol=ticker, past_transaction_days=360)
    if query is not None:
        data = query
        return data
    else:
        data = "OpenBB query issue"
        return data

def getCorpLobbying():
    query = openbb.stocks.gov.toplobbying()
    if query is not None:
        data = query
        return data
    else:
        data = "OpenBB query issue"
        return data

def getCongressTrades():
    query = openbb.stocks.gov.topbuys(gov_type="congress", past_transactions_months=2)
    if query is not None:
        data = query
        return data
    else:
        data = "OpenBB query issue"
        return data