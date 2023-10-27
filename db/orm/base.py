import os, sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import db.config
import redis

Base = declarative_base()
gds_params = db.config.gds_config()
gds_engine = create_engine(gds_params['jdbc'])
Base.metadata.create_all(gds_engine)

redis_params = db.config.redis_config()
redis_conn = redis.Redis(host=redis_params['host'], port=redis_params['port'], db=redis_params['db'])
# create a configured "Session" class
Session = sessionmaker(bind=gds_engine)

# create a Session
session = Session()