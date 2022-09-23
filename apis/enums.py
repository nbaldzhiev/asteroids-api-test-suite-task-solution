"""This module contains constants across the APIs."""
from enum import Enum


class SBDBCloseApproachDataAPIGETResponseProperties(Enum):
    """This class contains the full list of properties expected in a GET response of the
    close-approach data API endpoint.

    Current version of API: Version: 1.4 (2021 July).
    TODO: Improve this so that the list of fields for a given version is retrieved via the API.
     if such an endpoint comes to exist at some point.

    Notes
    -----
    This list should be kept up-to-date as it is the source of truth for the auto tests as to what
    is the expected list of properties in a given response.
    """

    SIGNATURE = "signature"
    COUNT = "count"
    FIELDS = "fields"
    DATA = "data"


class SBDBCloseApproachDataAPIQueryParameters(Enum):
    """Contains constants for accepted query parameters for the close-approach data API request.

    Notes
    -----
    The list here does not contain all available query parameters but only those currently tested.
    """

    DES = "des"
    DIST_MAX = "dist-max"
    DATE_MIN = "date-min"
    DATE_MAX = "date-max"
