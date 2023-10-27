from flask import jsonify
from model import cyber

from helper.redis import fetch_and_cache_data

def getCTISources():
    data, from_cache = fetch_and_cache_data(cyber.getAllCTISources, "getCTISources", False)
    return jsonify({'data': data, 'from_cache': from_cache}), 200

def getGovCTISources():
    data, from_cache = fetch_and_cache_data(cyber.getGovCTISources, "getGovCTISources", False)
    return jsonify({'data': data, 'from_cache': from_cache}), 200
