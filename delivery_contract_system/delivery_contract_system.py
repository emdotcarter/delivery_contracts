import random


class DeliveryContractSystem:
    _ERROR_RATE = 0.5

    @classmethod
    def request_contract(cls):
        if cls._generate_random_error():
            return {"error": "Unable to generate delivery manifest"}

        return cls._build_contract("Prizes (Crane Claw)", 4, [], "Moon")

    @classmethod
    def _build_contract(cls, payload, crew_size, crew_conditions, destination):
        return {
            "payload": payload,
            "crew_requirements": {
                "size": crew_size,
                "conditions": crew_conditions,
            },
            "destination": destination,
        }

    @classmethod
    def _generate_random_error(cls):
        return random.random() < cls._ERROR_RATE
