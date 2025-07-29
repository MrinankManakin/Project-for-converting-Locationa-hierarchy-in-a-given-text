import geopandas as gpd
import folium
from shapely.geometry import Polygon

def generate_map(location_info):
    """
    Generates a map with a marker on the given location.

    Args:
        location_info (dict): A dictionary containing the location information.
    """
    m = folium.Map(location=[location_info['latitude'], location_info['longitude']], zoom_start=13)
    folium.Marker([location_info['latitude'], location_info['longitude']], popup=location_info['name']).add_to(m)
    m.save("map.html")

def filter_non_eurocentric_locations(gdf):
    """
    Filters a GeoDataFrame to exclude locations within Europe.

    Args:
        gdf (GeoDataFrame): The GeoDataFrame to filter.

    Returns:
        GeoDataFrame: The filtered GeoDataFrame.
    """
    # Define a bounding box for Europe as a single polygon
    europe_bbox_poly = Polygon([(-24, 34), (-24, 71), (40, 71), (40, 34)])
    europe_bbox_gdf = gpd.GeoDataFrame({'geometry': [europe_bbox_poly]}, crs='EPSG:4326')

    # Perform spatial join to find cities outside Europe
    non_eurocentric_cities = gpd.sjoin(gdf, europe_bbox_gdf, how='left', predicate='intersects')
    non_eurocentric_cities = non_eurocentric_cities[non_eurocentric_cities['index_right'].isnull()]

    return non_eurocentric_cities
