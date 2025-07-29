import spacy
from googletrans import Translator

# Load spaCy's English language model
nlp = spacy.load('en_core_web_sm')

def extract_location_entities(sentence, lang='en'):
    """
    Extracts location entities from a sentence.

    Args:
        sentence (str): The sentence to extract location entities from.
        lang (str, optional): The language of the sentence. Defaults to 'en'.

    Returns:
        list: A list of location entities.
    """
    if lang != 'en':
        translator = Translator()
        sentence = translator.translate(sentence, src=lang, dest='en').text

    doc = nlp(sentence)
    locations = []

    for ent in doc.ents:
        if ent.label_ == 'GPE':  # GPE: Geo-Political Entity (location)
            locations.append((ent.text, ent.start_char, ent.end_char))

    return locations
