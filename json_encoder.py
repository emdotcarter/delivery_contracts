import flask

from delivery_contract_system.contract import Contract


class JSONEncoder(flask.json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Contract):
            return obj.serialize()

        return super(MyJSONEncoder, self).default(obj)
