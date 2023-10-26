from db.orm import rss_feeds, finance, base
#from openbb_terminal.sdk import openbb

MarketFeed = rss_feeds.MarketFeed
SESSION = base.session

def getEconSources():
    query = SESSION.query(MarketFeed).all()
    if query is not None:
        data = {}
        for i in query:
            data.update({i.description: i.json()})
        return data
    else:
        data = "Query Failure"
        return data

def getGovEconSources():
    query = SESSION.query(MarketFeed).filter_by(type="Government").all()
    if query is not None:
        data = {}
        for i in query:
            data.update({i.description: i.json()})
        return data
    else:
        data = "Improper query"
        return data

def getEconomicEvents():
    data = openbb.economy.events()
    return data

def getCovidCases(country):
    data = openbb.alt.covid.global_cases(country)
    return data