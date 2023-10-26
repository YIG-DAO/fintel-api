from sqlalchemy import Column, String, Integer, DECIMAL, TIMESTAMP, BIGINT
from sqlalchemy.sql import func

from .base import Base

class Crypto(Base):

    __tablename__ = 'crypto_usd'

    id = Column(BIGINT, primary_key=True)
    name = Column(String)
    symbol = Column(String)
    slug = Column(String)
    num_market_pairs = Column(Integer)
    date_added = Column(TIMESTAMP)
    tags = Column(String)
    max_supply = Column(Integer)
    circulating_supply = Column(DECIMAL)
    total_supply = Column(DECIMAL)
    cmc_rank = Column(Integer)
    self_reported_circulating_supply = Column(DECIMAL)
    tvl_ratio = Column(DECIMAL)
    last_updated = Column(TIMESTAMP)
    quote_usd_price = Column(DECIMAL)
    quote_usd_volume_24h = Column(DECIMAL)
    quote_usd_volume_change_24h = Column(DECIMAL)
    quote_usd_percent_change_1h = Column(DECIMAL)
    quote_usd_percent_change_24h = Column(DECIMAL)
    quote_usd_percent_change_7d = Column(DECIMAL)
    quote_usd_percent_change_30d = Column(DECIMAL)
    quote_usd_percent_change_60d = Column(DECIMAL)
    quote_usd_percent_change_90d = Column(DECIMAL)
    quote_usd_market_cap = Column(DECIMAL)
    quote_usd_fully_diluted_market_cap = Column(DECIMAL)
    quote_usd_tvl = Column(DECIMAL)
    quote_usd_last_updated = Column(TIMESTAMP, onupdate=func.now())
    inserted_at = Column(TIMESTAMP, onupdate=func.now())
    

    def __init__(self, id, name, symbol, slug, num_market_pairs, date_added, tags, max_supply, circulating_supply,
                 total_supply, cmc_rank, self_reported_circulating_supply, tvl_ratio, last_updated, quote_usd_price,
                 quote_usd_volume_24h, quote_usd_volume_change_24h, quote_usd_percent_change_1h,
                 quote_usd_percent_change_24h, quote_usd_percent_change_7d, quote_usd_percent_change_30d,
                 quote_usd_percent_change_60d, quote_usd_percent_change_90d, quote_usd_market_cap,
                 quote_usd_fully_diluted_market_cap, quote_usd_tvl, quote_usd_last_updated, inserted_at):

        self.id = id
        self.name = name
        self.symbol = symbol
        self.slug = slug
        self.num_market_pairs = num_market_pairs
        self. date_added = date_added
        self.tags = tags
        self.max_supply = max_supply
        self.circulating_supply = circulating_supply
        self.total_supply = total_supply
        self.cmc_rank = cmc_rank
        self.self_reported_circulating_supply = self_reported_circulating_supply
        self.tvl_ratio = tvl_ratio
        self.last_updated = last_updated
        self.quote_usd_price = quote_usd_price
        self.quote_usd_volume_24h = quote_usd_volume_24h
        self.quote_usd_volume_change_24h = quote_usd_volume_change_24h
        self.quote_usd_percent_change_1h = quote_usd_percent_change_1h
        self.quote_usd_percent_change_24h = quote_usd_percent_change_24h
        self.quote_usd_percent_change_7d = quote_usd_percent_change_7d
        self.quote_usd_percent_change_30d = quote_usd_percent_change_30d
        self.quote_usd_percent_change_60d = quote_usd_percent_change_60d
        self.quote_usd_percent_change_90d = quote_usd_percent_change_90d
        self.quote_usd_market_cap = quote_usd_market_cap
        self.quote_usd_fully_diluted_market_cap = quote_usd_fully_diluted_market_cap
        self.quote_usd_tvl = quote_usd_tvl
        self.quote_usd_last_updated = quote_usd_last_updated,
        self.inserted_at = inserted_at

    def __repr__(self):
        return '<Crypto(name={self.name!r})>'.format(self=self)


    def json(self):
        return {
            'id': self.id, 
            'name': self.name,
            'symbol': self.symbol,
            'slug': self.slug,
            'num_market_pairs' : self.num_market_pairs,
            'date_added' : self.date_added,
            'tags' : self.tags,
            'max_supply' : self.max_supply,
            'circulating_supply' : self.circulating_supply,
            'total_supply' : self.total_supply,
            'cmc_rank' : self.cmc_rank,
            'self_reported_circulating_supply' : self.self_reported_circulating_supply,
            'tvl_ratio' : self.tvl_ratio,
            'last_updated' : self.last_updated,
            'quote_usd_price' : self.quote_usd_price,
            'quote_usd_volume_24h' : self.quote_usd_volume_24h,
            'quote_usd_volume_change_24h' : self.quote_usd_volume_change_24h,
            'quote_usd_percent_change_1h' : self.quote_usd_percent_change_1h,
            'quote_usd_percent_change_24h' : self.quote_usd_percent_change_24h,
            'quote_usd_percent_change_7d' : self.quote_usd_percent_change_7d,
            'quote_usd_percent_change_30d' : self.quote_usd_percent_change_30d,
            'quote_usd_percent_change_60d' : self.quote_usd_percent_change_60d,
            'quote_usd_percent_change_90d' : self.quote_usd_percent_change_90d,
            'quote_usd_market_cap' : self.quote_usd_market_cap,
            'quote_usd_fully_diluted_market_cap' : self.quote_usd_fully_diluted_market_cap,
            'quote_usd_tvl' : self.quote_usd_tvl,
            'quote_usd_last_updated' : self.quote_usd_last_updated,
            'inserted_at' : self.inserted_at
        }

class CryptoEUR(Base):

    __tablename__ = 'crypto_eur'

    id = Column(BIGINT, primary_key=True)
    name = Column(String)
    symbol = Column(String)
    slug = Column(String)
    num_market_pairs = Column(Integer)
    date_added = Column(TIMESTAMP)
    tags = Column(String)
    max_supply = Column(Integer)
    circulating_supply = Column(DECIMAL)
    total_supply = Column(DECIMAL)
    cmc_rank = Column(Integer)
    self_reported_circulating_supply = Column(DECIMAL)
    tvl_ratio = Column(DECIMAL)
    last_updated = Column(TIMESTAMP)
    quote_eur_price = Column(DECIMAL)
    quote_eur_volume_24h = Column(DECIMAL)
    quote_eur_volume_change_24h = Column(DECIMAL)
    quote_eur_percent_change_1h = Column(DECIMAL)
    quote_eur_percent_change_24h = Column(DECIMAL)
    quote_eur_percent_change_7d = Column(DECIMAL)
    quote_eur_percent_change_30d = Column(DECIMAL)
    quote_eur_percent_change_60d = Column(DECIMAL)
    quote_eur_percent_change_90d = Column(DECIMAL)
    quote_eur_market_cap = Column(DECIMAL)
    quote_eur_fully_diluted_market_cap = Column(DECIMAL)
    quote_eur_tvl = Column(DECIMAL)
    quote_eur_last_updated = Column(TIMESTAMP, onupdate=func.now())
    inserted_at = Column(TIMESTAMP, onupdate=func.now())
    

    def __init__(self, id, name, symbol, slug, num_market_pairs, date_added, tags, max_supply, circulating_supply,
                 total_supply, cmc_rank, self_reported_circulating_supply, tvl_ratio, last_updated, quote_eur_price,
                 quote_eur_volume_24h, quote_eur_volume_change_24h, quote_eur_percent_change_1h,
                 quote_eur_percent_change_24h, quote_eur_percent_change_7d, quote_eur_percent_change_30d,
                 quote_eur_percent_change_60d, quote_eur_percent_change_90d, quote_eur_market_cap,
                 quote_eur_fully_diluted_market_cap, quote_eur_tvl, quote_eur_last_updated, inserted_at):

        self.id = id
        self.name = name
        self.symbol = symbol
        self.slug = slug
        self.num_market_pairs = num_market_pairs
        self. date_added = date_added
        self.tags = tags
        self.max_supply = max_supply
        self.circulating_supply = circulating_supply
        self.total_supply = total_supply
        self.cmc_rank = cmc_rank
        self.self_reported_circulating_supply = self_reported_circulating_supply
        self.tvl_ratio = tvl_ratio
        self.last_updated = last_updated
        self.quote_eur_price = quote_eur_price
        self.quote_eur_volume_24h = quote_eur_volume_24h
        self.quote_eur_volume_change_24h = quote_eur_volume_change_24h
        self.quote_eur_percent_change_1h = quote_eur_percent_change_1h
        self.quote_eur_percent_change_24h = quote_eur_percent_change_24h
        self.quote_eur_percent_change_7d = quote_eur_percent_change_7d
        self.quote_eur_percent_change_30d = quote_eur_percent_change_30d
        self.quote_eur_percent_change_60d = quote_eur_percent_change_60d
        self.quote_eur_percent_change_90d = quote_eur_percent_change_90d
        self.quote_eur_market_cap = quote_eur_market_cap
        self.quote_eur_fully_diluted_market_cap = quote_eur_fully_diluted_market_cap
        self.quote_eur_tvl = quote_eur_tvl
        self.quote_eur_last_updated = quote_eur_last_updated,
        self.inserted_at = inserted_at

    def __repr__(self):
        return '<CryptoEUR(name={self.name!r})>'.format(self=self)


    def json(self):
        return {
            'id': self.id, 
            'name': self.name,
            'symbol': self.symbol,
            'slug': self.slug,
            'num_market_pairs' : self.num_market_pairs,
            'date_added' : self.date_added,
            'tags' : self.tags,
            'max_supply' : self.max_supply,
            'circulating_supply' : self.circulating_supply,
            'total_supply' : self.total_supply,
            'cmc_rank' : self.cmc_rank,
            'self_reported_circulating_supply' : self.self_reported_circulating_supply,
            'tvl_ratio' : self.tvl_ratio,
            'last_updated' : self.last_updated,
            'quote_usd_price' : self.quote_eur_price,
            'quote_usd_volume_24h' : self.quote_eur_volume_24h,
            'quote_usd_volume_change_24h' : self.quote_eur_volume_change_24h,
            'quote_usd_percent_change_1h' : self.quote_eur_percent_change_1h,
            'quote_usd_percent_change_24h' : self.quote_eur_percent_change_24h,
            'quote_usd_percent_change_7d' : self.quote_eur_percent_change_7d,
            'quote_usd_percent_change_30d' : self.quote_eur_percent_change_30d,
            'quote_usd_percent_change_60d' : self.quote_eur_percent_change_60d,
            'quote_usd_percent_change_90d' : self.quote_eur_percent_change_90d,
            'quote_usd_market_cap' : self.quote_eur_market_cap,
            'quote_usd_fully_diluted_market_cap' : self.quote_eur_fully_diluted_market_cap,
            'quote_usd_tvl' : self.quote_eur_tvl,
            'quote_usd_last_updated' : self.quote_eur_last_updated,
            'inserted_at' : self.inserted_at
        }