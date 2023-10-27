import datetime
import json

from decimal import Decimal

class ExtendedJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        elif isinstance(obj, Decimal):
            return str(obj)
        return super(ExtendedJSONEncoder, self).default(obj)
