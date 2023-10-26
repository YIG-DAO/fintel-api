from marshmallow import post_load

from .source import Source, SourceSchema, SourceType

'''
#TODO: Create ORM db tables and schema for finance data mining
'''

class Finance(Source):
    def __init__(self, description, url):
        super(Finance, self).__init__(description, url, SourceType.FINANCE)

    def __repr__(self):
        return '<Finance(name={self.description!r})>'.format(self=self)

class GovFinance(Source):
    def __init__(self, description, url):
        super(GovFinance, self).__init__(description, url, SourceType.GOV_FINANCE)

    def __repr__(self):
        return '<GovFinance(name={self.description!r})>'.format(self=self)


class FinanceSchema(SourceSchema):
    @post_load
    def make_Finance(self, data, **kwargs):
        return Finance(**data)

class GovFinanceSchema(SourceSchema):
    @post_load
    def make_GovFinance(self, data, **kwargs):
        return GovFinance(**data)