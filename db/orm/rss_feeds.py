from sqlalchemy import Column, String, Integer, DECIMAL, TIMESTAMP, BIGINT
from sqlalchemy.sql import func

from .base import Base

class CTIFeed(Base):
    __tablename__ = 'cti_rss_feeds'

    id = Column(BIGINT, primary_key=True)
    description = Column(String)
    type = Column(String)
    url = Column(String)
    last_updated = Column(TIMESTAMP, onupdate=func.now())

    def __init__(self, id, description, type, url, last_updated):
        self.id = id
        self.description = description
        self.type = type
        self.url = url
        self.last_updated = last_updated

    def __repr__(self):
        return '<CTIFeed(description={self.description!r})>'.format(self=self)

    def json(self):
        return {
            'type': self.type,
            'url' : self.url,
        }

class MarketFeed(Base):
    __tablename__ = 'market_rss_feeds'

    id = Column(BIGINT, primary_key=True)
    description = Column(String)
    type = Column(String)
    url = Column(String)
    last_updated = Column(TIMESTAMP, onupdate=func.now())

    def __init__(self, id, description, type, url, last_updated):
        self.id = id
        self.description = description
        self.type = type
        self.url = url
        self.last_updated = last_updated

    def __repr__(self):
        return '<MarketFeed(description={self.description!r})>'.format(self=self)

    def json(self):
        return {
            'type': self.type,
            'url' : self.url,
        }
        
TreasuryGovRss = [
    ['https://treasurydirect.gov/TA_WS/securities/announced/rss', 'US Treasury Offering Announcement'],
    ['https://treasurydirect.gov/TA_WS/securities/auctioned/rss', 'US Treasury Auction Results'],
    ['https://treasurydirect.gov/NP_WS/debt/feeds/recent', 'US Treasury Debt to Penny'],
    ['https://www.treasurydirect.gov/rss/mspd.xml', 'US Treasury Monthly Statement of the Public Debt'],
    ['https://www.treasurydirect.gov/rss/sbpro.xml', 'US Savings Bond Pro Updates']
]
ThreatIntel = [
    ['https://grahamcluley.com/feed/', 'Graham Cluley'],
    ['https://threatpost.com/feed/', 'Threatpost'],
    ['https://krebsonsecurity.com/feed/', 'Krebs on Security'],
    ['https://www.darkreading.com/rss.xml', 'Dark Reading'],
    ['http://feeds.feedburner.com/eset/blog', 'We Live Security'],
    ['https://davinciforensics.co.za/cybersecurity/feed/', 'DaVinci Forensics'],
    ['https://blogs.cisco.com/security/feed', 'Cisco'],
    ['https://www.infosecurity-magazine.com/rss/news/', 'Information Security Magazine'],
    ['http://feeds.feedburner.com/GoogleOnlineSecurityBlog', 'Google'],
    ['http://feeds.trendmicro.com/TrendMicroResearch', 'Trend Micro'],
    ['https://www.bleepingcomputer.com/feed/', 'Bleeping Computer'],
    ['https://www.proofpoint.com/us/rss.xml', 'Proof Point'],
    ['http://feeds.feedburner.com/TheHackersNews?format=xml', 'Hacker News'],
    ['https://www.schneier.com/feed/atom/', 'Schneier on Security'],
    ['https://www.binarydefense.com/feed/', 'Binary Defense'],
    ['https://securelist.com/feed/', 'Securelist'],
    ['https://research.checkpoint.com/feed/', 'Checkpoint Research'],
    ['https://www.virusbulletin.com/rss', 'VirusBulletin'],
    ['https://modexp.wordpress.com/feed/', 'Modexp'],
    ['https://www.tiraniddo.dev/feeds/posts/default', 'James Forshaw'],
    ['https://blog.xpnsec.com/rss.xml', 'Adam Chester'],
    ['https://msrc-blog.microsoft.com/feed/', 'Microsoft Security'],
    ['https://www.recordedfuture.com/feed', 'Recorded Future'],
    ['https://www.sentinelone.com/feed/', 'SentinelOne'],
    ['https://redcanary.com/feed/', 'RedCanary'],
    ['https://cybersecurity.att.com/site/blog-all-rss', 'ATT']
]

GovThreatIntel = [
    ['https://www.cisa.gov/uscert/ncas/alerts.xml', 'US-CERT CISA'],
    ['https://www.ncsc.gov.uk/api/1/services/v1/report-rss-feed.xml', 'NCSC'],
    ['https://www.cisecurity.org/feed/advisories', 'Center of Internet Security']
]

Reuters = [
    ['https://www.reutersagency.com/feed/?best-types=the-big-picture&post_type=best', 'Reuters Big Picture'],
    ['https://www.reutersagency.com/feed/?best-topics=tech&post_type=best', 'Reuters Tech'],
    ['https://www.reutersagency.com/feed/?best-topics=business-finance&post_type=best', 'Reuters Business & Finance']
]