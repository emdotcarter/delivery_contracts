from flask import Flask, jsonify

from delivery_contract_system.core_system import DeliveryContractSystem
from json_encoder import JSONEncoder

app = Flask(__name__)
app.config["DEBUG"] = True
app.json_encoder = JSONEncoder


@app.route("/request_contract", methods=["GET"])
def request_contract():
    return jsonify(DeliveryContractSystem.request_contract())


if __name__ == "__main__":
    app.run()
