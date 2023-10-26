import datetime as dt

from marshmallow import Schema, fields
from enum import Enum


class Source(object):
    def __init__(self, description, url, type):
        self.description = description
        self.url = url
        self.created_at = dt.datetime.now()
        self.type = type

    def __repr__(self):
        return '<Source(name={self.description!r})>'.format(self=self)


class SourceSchema(Schema):
    description = fields.Str()
    url = fields.Str()
    created_at = fields.Date()
    type = fields.Str()

class SourceType(Enum):
    CYBER = "CYBER"
    GOV_CYBER = "GOV_CYBER"
    CRYPTO = "CRYPTO"
    MACRO = "MACRO"
    NATSEC = "NATSEC"
    FINANCE = "FINANCE"
    GOV_FINANCE = "GOV_FINANCE"