#!/usr/bin/python
import os
import sys
import psycopg2 as pg
import redis
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

from configparser import ConfigParser


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
load_dotenv()

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

def redis_config():
    r_config = {
        'host': os.getenv('REDIS_HOST'),
        'port': os.getenv('REDIS_PORT'),
        'db': os.getenv('REDIS_DB'),
        'protocol': 3
    }

    # Check for missing configuration details
    missing_configs = [key for key, value in r_config.items() if not value]
    if missing_configs:
        raise Exception(f"Missing Redis configuration for: {', '.join(missing_configs)}")
    return r_config

def test_gds_connection():
    try:
        gds_params = gds_config()
        print('Connecting to Gnosis Data Store...')
        with create_engine(gds_params['jdbc']).connect() as gds_connection:
            gds_version = gds_connection.execute(text('SELECT version()')).fetchone()
            print(f'Gnosis Data Store PostgreSQL database version: {gds_version[0]}')
    except Exception as error:
        print(f"GDS Error: {error}")
    finally:
        print('Gnosis DB connection closed.')

def test_redis_connection():
    redis_conn = None
    try:
        redis_params = redis_config()
        print('Connecting to Redis...')
        redis_conn = redis.Redis(host=redis_params['host'], port=redis_params['port'], db=redis_params['db'])
        if redis_conn.ping():
            print('Connected to Redis successfully!')
        else:
            print('Failed to connect to Redis.')
    except redis.ConnectionError as error:
        print(f"Redis Error: {error}")
    finally:
        if redis_conn:
            redis_conn.close()
            print('Redis connection closed.')


def test_connect():
    """ Connect to the PostgreSQL and Redis database servers """
    test_gds_connection()
    test_redis_connection()
