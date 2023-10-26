#!/usr/bin/python
import os
import sys
import psycopg2 as pg

from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from configparser import ConfigParser


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

def gds_config(filename=BASE_DIR+'/db/database.ini', section='gds'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

def test_connect():
    """ Connect to the PostgreSQL database server """
    gds_conn = None
    try:
        # read connection parameters
        gds_params = gds_config()

        # connect to GDS DB
        print('Connecting to Gnosis Data Store')
        gds_engine = create_engine(gds_params['jdbc'])
        print('Gnosis Data Store PostgreSQL database version:')
        with gds_engine.connect() as gds_connection:
            gds_version = gds_connection.execute(text('SELECT version()'))
            for i in gds_version:
                print(i)
       
    except (Exception, pg.DatabaseError) as error:
        print(error)

    finally:
        if gds_engine is not None:
            gds_engine.dispose()
            print('Gnosis DB connection closed.')
