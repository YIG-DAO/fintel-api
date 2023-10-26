""" #from openbb_terminal.sdk import openbb

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
        return "Empty Response" """