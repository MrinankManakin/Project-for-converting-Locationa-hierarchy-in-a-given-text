# Project-for-converting-Locationa-hierarchy-in-a-given-text

# Multilingual Location Extraction and Geospatial Analysis

This project performs geospatial analysis and extracts location information from multilingual text. The project leverages various libraries and services such as spaCy for natural language processing, OpenCage Geocode API for geocoding, and GeoPandas for geospatial data manipulation.

## Project Structure

- `UoA_Project_Multilingual_texts_for_Non_Eurocentric_locations.ipynb`: Jupyter Notebook containing the main code for the project.
- `UoA Project Multilingual texts for Non-Eurocentric locations.py`: Original Python script.

## Setup

### Prerequisites

- Python 3.6+
- Required Python packages: `spacy`, `opencage`, `langdetect`, `googletrans==4.0.0-rc1`, `geopandas`, `matplotlib`, `shapely`

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/multilingual-location-extraction.git
    cd multilingual-location-extraction
    ```

2. Install the required Python packages:

    ```bash
    pip install spacy opencage langdetect googletrans==4.0.0-rc1 geopandas matplotlib shapely
    ```

3. Download the spaCy English language model:

    ```bash
    python -m spacy download en_core_web_sm
    ```

## Usage

### Jupyter Notebook

1. Open the Jupyter Notebook:

    ```bash
    jupyter notebook UoA_Project_Multilingual_texts_for_Non_Eurocentric_locations.ipynb
    ```

2. Follow the steps in the notebook to perform geospatial analysis and extract location information from text.

### Python Script

1. Open the Python script `UoA Project Multilingual texts for Non-Eurocentric locations.py` in your preferred editor or IDE.
2. Run the script:

    ```bash
    python "UoA Project Multilingual texts for Non-Eurocentric locations.py"
    ```

## Example

Here is an example of how to use the location extraction function within the notebook:

```python
# Load spaCy's English language model
import spacy
nlp = spacy.load('en_core_web_sm')

# Extract location entities from a sample sentence
sentence = "القاهرة هي عاصمة مصر."
lang = detect(sentence)
locations = extract_location_entities(sentence, lang)
print(locations)

# Get location information for the extracted entities
api_key = "your_opencagedata_api_key"
for location in locations:
    info = get_location_info(location[0], api_key)
    if info:
        print(info)
