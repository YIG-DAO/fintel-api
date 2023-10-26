import os, sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import db.config

Base = declarative_base()
gds_params = db.config.gds_config()
gds_engine = create_engine(gds_params['jdbc'])
Base.metadata.create_all(gds_engine)

# create a configured "Session" class
Session = sessionmaker(bind=gds_engine)

# create a Session
session = Session()