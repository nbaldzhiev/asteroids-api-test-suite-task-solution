"""This module contains common test steps, decorated as allure steps"""
from http import HTTPStatus
from typing import Dict

import allure
from requests import Response

from apis import (
    CURRENT_API_VERSION,
    FULL_SOURCE_NAME,
    SBDBCloseApproachDataAPIGETResponseProperties,
)


@allure.step("Verify Request Is Successful")
def verify_request_is_successful(response: Response):
    """Verifies that a given request is successful by verifying that the HTTP status code is 200."""
    assert response.status_code == HTTPStatus.OK, "The GET request was not successful!"


@allure.step('Verify The "signature" Property In The Response')
def verify_signature_property_in_response(signature_property: Dict):
    """Verifies that the 'signature' property in the GET response is as expected."""
    assert (
        signature_property["source"].lower() == FULL_SOURCE_NAME.lower()
    ), 'The "source" is incorrect!'
    assert signature_property["version"] == str(
        CURRENT_API_VERSION
    ), 'The "version" is incorrect!'


@allure.suite("Verify All Properties Are In The Response")
def verify_all_properties_in_response(response: Dict):
    """Verifies that all properties in the GET response are present."""
    exp_properties = sorted(
        [property_.value for property_ in SBDBCloseApproachDataAPIGETResponseProperties]
    )
    actual_properties = sorted(response.keys())
    assert actual_properties == exp_properties, "Incorrect response properties!"
