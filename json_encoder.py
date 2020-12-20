import flask

from delivery_contract_system.contract import Contract
from location_system.location import Location

SERIALIZABLE_CUSTOM_CLASSES = [Contract, Location]


class JSONEncoder(flask.json.JSONEncoder):
    def default(self, obj):
        if any([isinstance(obj, c) for c in SERIALIZABLE_CUSTOM_CLASSES]):
            return obj.serialize()

        return super(JSONEncoder, self).default(obj)
