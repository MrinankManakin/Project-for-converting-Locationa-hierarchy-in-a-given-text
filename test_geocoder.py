import pytest
from geocoder import get_location_info_with_error_handling
import config

def test_get_location_info_with_error_handling_valid_location():
    location = "London"
    info = get_location_info_with_error_handling(location, config.OPENCAGE_API_KEY)
    assert info is not None
    assert info['country'] == 'United Kingdom'

def test_get_location_info_with_error_handling_invalid_location():
    location = "InvalidLocation123"
    info = get_location_info_with_error_handling(location, config.OPENCAGE_API_KEY)
    assert info is None

def test_get_location_info_with_error_handling_empty_location():
    location = ""
    info = get_location_info_with_error_handling(location, config.OPENCAGE_API_KEY)
    assert info is None

def test_get_location_info_with_error_handling_no_api_key():
    location = "London"
    with pytest.raises(ValueError):
        get_location_info_with_error_handling(location, "")
