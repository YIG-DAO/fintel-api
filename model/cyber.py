import psycopg2 as pg
import db.config
from db.orm import rss_feeds, cyber, base
from model.psql.twitter import GetCyberTweets

CTIFeed = rss_feeds.CTIFeed
SESSION = base.session

def getAllCTISources():
    query = SESSION.query(CTIFeed).all()
    if query is not None:
        data = {}
        for i in query:
            data.update({i.description: i.json()})
        return data
    else:
        data = "Query error"
        return data

def getGovCTISources():
    query = SESSION.query(CTIFeed).filter_by(type="Government").all()
    if query is not None:
        data = {}
        for i in query:
            data.update({i.description: i.json()})
        return data
    else:
        data = "Query error"
        return data
