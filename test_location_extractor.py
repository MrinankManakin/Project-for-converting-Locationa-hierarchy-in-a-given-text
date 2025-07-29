import pytest
from location_extractor import extract_location_entities

def test_extract_location_entities_english():
    sentence = "I am going to London."
    locations = extract_location_entities(sentence)
    assert len(locations) == 1
    assert locations[0][0] == "London"

def test_extract_location_entities_spanish():
    sentence = "Voy a Madrid."
    locations = extract_location_entities(sentence, lang='es')
    assert len(locations) == 1
    assert locations[0][0] == "Madrid"

def test_extract_location_entities_no_location():
    sentence = "There is no location here."
    locations = extract_location_entities(sentence)
    assert len(locations) == 0
