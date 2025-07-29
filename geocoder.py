from opencage.geocoder import OpenCageGeocode
import config

def get_location_info(location):
    """
    Gets location information from the OpenCage Geocode API.

    Args:
        location (str): The location to get information for.
        api_key (str): The OpenCage Geocode API key.

    Returns:
        dict: A dictionary containing the location information.
    """
    try:
        geocoder = OpenCageGeocode(config.OPENCAGE_API_KEY)
        results = geocoder.geocode(location)

        if results and len(results):
            place = results[0]
            return {
                'name': place['formatted'],
                'country': place['components']['country'],
                'latitude': place['geometry']['lat'],
                'longitude': place['geometry']['lng']
            }
        else:
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None

def get_location_info_with_error_handling(location, api_key):
    """
    Gets location information from the OpenCage Geocode API with error handling.

    Args:
        location (str): The location to get information for.
        api_key (str): The OpenCage Geocode API key.

    Returns:
        dict: A dictionary containing the location information.
    """
    if not api_key:
        raise ValueError("API key is required.")

    if not location:
        return None

    try:
        geocoder = OpenCageGeocode(api_key)
        results = geocoder.geocode(location)

        if results and len(results):
            place = results[0]
            return {
                'name': place['formatted'],
                'country': place['components']['country'],
                'latitude': place['geometry']['lat'],
                'longitude': place['geometry']['lng']
            }
        else:
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None
