import flask

from delivery_contract_system.contract import Contract

SERIALIZABLE_CUSTOM_CLASSES = [Contract]


class JSONEncoder(flask.json.JSONEncoder):
    def default(self, obj):
        if any([isinstance(obj, c) for c in SERIALIZABLE_CUSTOM_CLASSES]):
            return obj.serialize()

        return super(MyJSONEncoder, self).default(obj)
