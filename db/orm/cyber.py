from marshmallow import post_load
from .source import Source, SourceSchema, SourceType

'''
#TODO: Create ORM db tables and schema for finance data mining
'''

class Cyber(Source):
    def __init__(self, description, url):
        super(Cyber, self).__init__(description, url, SourceType.CYBER)

    def __repr__(self):
        return '<Cyber(name={self.description!r})>'.format(self=self)

class GovCyber(Source):
    def __init__(self, description, url):
        super(GovCyber, self).__init__(description, url, SourceType.GOV_CYBER)

    def __repr__(self):
        return '<GovCyber(name={self.description!r})>'.format(self=self)


class CyberSchema(SourceSchema):
    @post_load
    def make_Cyber(self, data, **kwargs):
        return Cyber(**data)

class GovCyberSchema(SourceSchema):
    @post_load
    def make_GovCyber(self, data, **kwargs):
        return GovCyber(**data)