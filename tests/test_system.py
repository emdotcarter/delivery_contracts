import pytest
import re
import unittest

from delivery_contract_system.system import DeliveryContractSystem


def patch_system_params(mocker, timeout_rate=0, timeout_sleep=0, error_rate=0):
    mocker.patch.object(DeliveryContractSystem, "_TIMEOUT_RATE", timeout_rate)
    mocker.patch.object(DeliveryContractSystem, "_TIMEOUT_SLEEP", timeout_sleep)
    mocker.patch.object(DeliveryContractSystem, "_ERROR_RATE", error_rate)


def test_request_contract_success(mocker):
    patch_system_params(mocker)

    response = DeliveryContractSystem.request_contract()
    assert response["response_code"] == 200

    contract = response["contract"]
    assert contract["id"]
    assert contract["item"]
    assert contract["crew_requirements"]["size"] > 0
    assert type(contract["crew_requirements"]["conditions"]) is list
    for r in contract["crew_requirements"]["conditions"]:
        assert r
    assert contract["destination"]


def test_request_contract_timeout(mocker):
    patch_system_params(mocker, timeout_rate=1)

    response = DeliveryContractSystem.request_contract()
    assert response["response_code"] == 408

    error = response["error"]
    assert error == "Timeout"


def test_request_contract_error(mocker):
    patch_system_params(mocker, error_rate=1)

    response = DeliveryContractSystem.request_contract()
    assert response["response_code"] == 500

    error = response["error"]
    assert error == "Unable to generate delivery manifest"
