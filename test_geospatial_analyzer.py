import pytest
import geopandas as gpd
from shapely.geometry import Point
from geospatial_analyzer import filter_non_eurocentric_locations

def test_filter_non_eurocentric_locations():
    # Create a GeoDataFrame with some sample data
    data = {'City': ['London', 'New York', 'Tokyo'],
            'geometry': [Point(0, 51), Point(-74, 40), Point(139, 35)]}
    gdf = gpd.GeoDataFrame(data, crs='EPSG:4326')

    # Filter the GeoDataFrame
    non_eurocentric_gdf = filter_non_eurocentric_locations(gdf)

    # Check that the non-Eurocentric locations are correct
    assert len(non_eurocentric_gdf) == 2
    assert 'London' not in non_eurocentric_gdf['City'].values
    assert 'New York' in non_eurocentric_gdf['City'].values
    assert 'Tokyo' in non_eurocentric_gdf['City'].values
