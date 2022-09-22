"""This module contains constants across the APIs."""
from enum import Enum


class SBDBCloseApproachDataAPIOutputFields(Enum):
    """This class contains the full list of fields expected in any given CAD record received as
    a response of the close-approach data API endpoint.

    Current version of API: Version: 1.4 (2021 July).
    TODO: Improve this so that the list of fields for a given version is retrieved via the API.
     if such an endpoint comes to exist at some point.

    Notes
    -----
    This list should be kept up-to-date as it is the source of truth for the auto tests as to what
    is the expected list of fields in a given response.
    """

    DES = "des"
    ORBIT_ID = "orbit_id"
    JD = "jd"
    CD = "cd"
    DIST = "dist"
    DIST_MIN = "dist_min"
    DIST_MAX = "dist_max"
    V_REL = "v_rel"
    V_INF = "v_inf"
    T_SIGMA_F = "t_sigma_f"
    BODY = "body"
    H = "h"
    DIAMETER = "diameter"
    DIAMETER_SIGMA = "diameter_sigma"
    FULLNAME = "fullname"
