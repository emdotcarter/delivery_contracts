import pytest
import re
import unittest

from delivery_contract_system.delivery_contract_system import DeliveryContractSystem


def test_request_contract_success(mocker):
    mocker.patch.object(DeliveryContractSystem, "_ERROR_RATE", 0)

    contract = DeliveryContractSystem.request_contract()

    assert contract["payload"]
    assert contract["crew_requirements"]["size"] > 0
    assert type(contract["crew_requirements"]["conditions"]) is list
    assert contract["destination"]


def test_request_contract_error(mocker):
    mocker.patch.object(DeliveryContractSystem, "_ERROR_RATE", 1)

    contract = DeliveryContractSystem.request_contract()

    assert contract == {"error": "Unable to generate delivery manifest"}
