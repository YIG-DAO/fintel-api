from flask import jsonify
from model import cyber

def getCTISources():
    data = cyber.getAllCTISources()
    payload = jsonify({'data':data}), 200
    return payload

def getGovCTISources():
    data = cyber.getGovCTISources()
    payload = jsonify({'data':data}), 200
    return payload
