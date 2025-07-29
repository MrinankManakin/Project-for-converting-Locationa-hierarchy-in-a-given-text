import click
import geopandas as gpd
from shapely.geometry import Point

from location_extractor import extract_location_entities
from geocoder import get_location_info
from geospatial_analyzer import filter_non_eurocentric_locations


@click.group()
def cli():
    pass


@cli.command()
@click.argument('sentence')
@click.option('--lang', default='en', help='Language of the sentence.')
def extract(sentence, lang):
    """Extracts location entities from a sentence."""
    locations = extract_location_entities(sentence, lang)
    if locations:
        click.echo("Location Entities:")
        for location in locations:
            click.echo(location[0])
    else:
        click.echo("No location entities found in the sentence.")


@cli.command()
@click.argument('location')
def geocode(location):
    """Geocodes a location."""
    info = get_location_info(location)
    if info:
        click.echo(f"Name: {info['name']}")
        click.echo(f"Country: {info['country']}")
        click.echo(f"Latitude: {info['latitude']}")
        click.echo(f"Longitude: {info['longitude']}")
    else:
        click.echo(f"Location '{location}' not found.")


@cli.command()
@click.argument('input_file')
@click.argument('output_file')
def filter(input_file, output_file):
    """Filters a shapefile to exclude locations within Europe."""
    gdf = gpd.read_file(input_file)
    non_eurocentric_gdf = filter_non_eurocentric_locations(gdf)
    non_eurocentric_gdf.to_file(output_file)
    click.echo(f"Filtered shapefile saved to {output_file}")


if __name__ == '__main__':
    cli()
