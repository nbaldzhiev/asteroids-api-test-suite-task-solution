"""This module contains tests for the SBDB Close Approach API."""
import json
from http import HTTPStatus
from typing import Dict

import allure
import pytest
import requests

from apis import SBDBCloseApproachDataAPI, SBDBCloseApproachDataAPIQueryParameters
from tests.steps import (
    verify_all_properties_in_response,
    verify_request_is_successful,
    verify_signature_property_in_response,
)

allure.parent_suite("SBDB API")


@allure.suite("SBDB Close Approach Data API - Positive Test Cases")
class TestSBDBCloseApproachDataAPIPositiveCases:
    """Contains positive test cases for the SBDB Close Approach Data API."""

    @allure.title("Making A GET Request To The Valid API URL Without Parameters")
    def test_successful_get_request(
        self, fixture_get_sbdb_close_approach_api: SBDBCloseApproachDataAPI
    ):
        """Verifies that a GET request towards the correct API URL without parameters is
        successful."""
        verify_request_is_successful(
            response=fixture_get_sbdb_close_approach_api.get_close_approach_data_raw()
        )

    @allure.title("All Expected GET Response Properties Are Present")
    def test_all_expected_get_response_properties_are_present(
        self, fixture_get_sbdb_close_approach_api: SBDBCloseApproachDataAPI
    ):
        """Verifies that all expected JSON properties are present in the response JSON. This
        test case makes a GET request without any query parameters."""
        resp: Dict = (
            fixture_get_sbdb_close_approach_api.get_close_approach_data_deserialized_content()
        )

        verify_all_properties_in_response(response=resp)
        verify_signature_property_in_response(signature_property=resp["signature"])

    @pytest.mark.parametrize(
        "query_parameters",
        [
            pytest.param(
                {SBDBCloseApproachDataAPIQueryParameters.DES.value: 433},
                id=f"One query parameter - {SBDBCloseApproachDataAPIQueryParameters.DES.value}",
            ),
            pytest.param(
                {
                    SBDBCloseApproachDataAPIQueryParameters.DES.value: 433,
                    SBDBCloseApproachDataAPIQueryParameters.DATE_MIN.value: "1900-01-01",
                    SBDBCloseApproachDataAPIQueryParameters.DATE_MAX.value: "2100-01-01",
                    SBDBCloseApproachDataAPIQueryParameters.DIST_MAX.value: 0.2,
                },
                id="Multiple query parameters - 4",
            ),
        ],
    )
    @allure.title("Making A GET Request With Valid Query Parameters")
    def test_get_request_with_valid_query_parameters(
        self,
        query_parameters: Dict,
        fixture_get_sbdb_close_approach_api: SBDBCloseApproachDataAPI,
    ):
        """Verifies that valid query parameters can be fed into the API and the request is
        successful. This test is parameterised."""
        resp: requests.Response = (
            fixture_get_sbdb_close_approach_api.get_close_approach_data_raw(
                **query_parameters
            )
        )
        verify_request_is_successful(response=resp)

        deserialized_response: Dict = (
            fixture_get_sbdb_close_approach_api.deserialize_response(resp)
        )
        verify_signature_property_in_response(deserialized_response["signature"])


@allure.suite("SBDB Close Approach Data API - Negative Test Cases")
class TestSBDBCloseApproachDataAPINegativeCases:
    """Contains negative test cases for the SBDB Close Approach Data API."""

    INCORRECT_PARAMETER_MSG = "one or more query parameter was not recognized"

    @allure.title("Incorrect Query Parameter")
    def test_incorrect_query_parameter(
        self, fixture_get_sbdb_close_approach_api: SBDBCloseApproachDataAPI
    ):
        """Verifies the API response of a GET request with an incorrect query parameter."""
        with pytest.raises(requests.exceptions.HTTPError) as exc_info:
            fixture_get_sbdb_close_approach_api.get_close_approach_data_raw(
                invalid_param=-1
            )

        assert (
            exc_info.value.response.status_code == HTTPStatus.BAD_REQUEST
        ), "The status code is incorrect!"
        assert (
            json.loads(exc_info.value.response.content)["message"].lower()
            == type(self).INCORRECT_PARAMETER_MSG.lower()
        ), "The error message is incorrect"
