import random
import time

from .contracts import contracts


class DeliveryContractSystem:
    _TIMEOUT_RATE = 0.2
    _TIMEOUT_SLEEP = 10
    _ERROR_RATE = 0.1

    @classmethod
    def request_contract(cls):
        if cls._generate_random_error():
            return {
                "response_code": 500,
                "error": "Unable to generate delivery manifest",
            }
        elif cls._generate_timeout():
            time.sleep(cls._TIMEOUT_SLEEP)
            return {"response_code": 408, "error": "Timeout"}

        return {
            "response_code": 200,
            "contract": cls._select_contract(),
        }

    @classmethod
    def _generate_random_error(cls):
        return random.random() < cls._ERROR_RATE

    @classmethod
    def _generate_timeout(cls):
        return random.random() < cls._TIMEOUT_RATE

    @classmethod
    def _select_contract(cls):
        return cls._build_contract(*random.choice(contracts))

    @classmethod
    def _build_contract(cls, id, item, crew_size, crew_conditions, destination):
        return {
            "id": id,
            "item": item,
            "crew_requirements": {
                "size": crew_size,
                "conditions": crew_conditions,
            },
            "destination": destination,
        }
