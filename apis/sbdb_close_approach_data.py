"""This module contains a class abstraction of the SBDB Close-Approach Data API."""
import json
import logging
from typing import Dict

import requests

logging.basicConfig(level=logging.INFO)

# TODO: Pull the version dynamically from the SBDB API in case such an endpoint is created
CURRENT_API_VERSION = 1.4
FULL_SOURCE_NAME = "NASA/JPL SBDB Close Approach Data API"


class SBDBCloseApproachDataAPI(requests.Session):
    """This class implement an abstraction of the SBDB Close-Approach Data API."""

    ENDPOINT_URL = "https://ssd-api.jpl.nasa.gov/cad.api"

    def __init__(self, endpoint_url: str = ENDPOINT_URL):
        super().__init__()
        self.endpoint_url = endpoint_url

    def get_close_approach_data_raw(self, **kwargs) -> requests.Response:
        """Makes a GET request to the CAD API endpoint and returns the "raw" response. The method
        can be fed query parameters as keyword arguments, so they would be added to the query
        string of the URL.

        Examples
        --------
        >>> SBDBCloseApproachDataAPI().get_close_approach_data_raw(
            des=433, date_min='1900-01-01', date_max='2100-01-01', dist_max=0.2
        )
        >>> SBDBCloseApproachDataAPI().get_close_approach_data_raw(
            dist_max='10LD', date_min='2018-01-01', sort='dist'
        )

        Returns
        -------
        requests.Response
            A requests `Response` object.
        """
        query_string: str = ""
        if kwargs:
            query_string += "?"
            for key, value in kwargs.items():
                modified_key = key.replace("_", "-")
                query_string += f"{modified_key}={value}"
                if key != list(kwargs)[-1]:
                    query_string += "&"

        resp = self.get(url=self.endpoint_url + query_string)
        logging.info(
            "Made a GET request to the following API endpoint: "
            "%s with the following query string: %s.",
            self.endpoint_url,
            query_string,
        )
        resp.raise_for_status()
        return resp

    def get_close_approach_data_deserialized_content(self, **kwargs) -> Dict:
        """Gets and returns the deserialized content of the response.

        Returns
        -------
        Dict
            The deserialized content of the response.
        """
        return json.loads(self.get_close_approach_data_raw(**kwargs).content)

    @staticmethod
    def deserialize_response(response: requests.Response) -> Dict:
        """Deserializes an existing response

        Parameters
        ----------
        response : requests.Response
            A Response object.

        Returns
        -------
        Dict
            A deserialized Response object.
        """
        return json.loads(response.content)
