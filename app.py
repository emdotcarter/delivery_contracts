from flask import Flask, jsonify, request

from json_encoder import JSONEncoder
from delivery_contract_system.core_system import DeliveryContractSystem
from location_system.location import Location

app = Flask(__name__)
app.config["DEBUG"] = True
app.json_encoder = JSONEncoder


@app.route("/contracts/request/", methods=["GET"])
def request_contract():
    return jsonify(DeliveryContractSystem.request_contract())


@app.route("/locations/", methods=["GET"])
def get_location_by_name():
    location = Location.find_by_name(request.args.get("name", type = str))
    return jsonify(location)


if __name__ == "__main__":
    app.run()
