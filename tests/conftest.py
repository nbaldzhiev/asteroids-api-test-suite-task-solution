"""A conftest module for the tests/ package"""
import pytest

from apis import SBDBCloseApproachDataAPI


@pytest.fixture
def fixture_get_sbdb_close_approach_api() -> SBDBCloseApproachDataAPI:
    """A function-level fixture for obtaining a SBDBCloseApproachDataAPI object."""
    return SBDBCloseApproachDataAPI()
