# Agrofile-Webmapping
Python scripts to work KML and GeoJSON files to be used for Leaflet web map generation using QGIS.

## How to use it?
- **GeoJSON to QGIS**: `python3 geojson_to_qgis.py input_form.json output_form.json`: transforms some data in the GeoJSON form `input_form.json` to create a GeoJSON form `output_form.json` that will be supported by the qgis2web plugin in QGIS;
- **KML to GeoJSON**: `python3 kml_to_geojson.py input_form.json output_form.json kml`: merges GeoJSON data (form data) in `input_form.json` with KML data (polygonal geometry) in every KLM file in the `kml` directory (using the GeoJSON `id` property and the KML `name` feature) to create a complete form (form data and polygonal geometry) in a GeoJSON file `output_form.json` that can be opened in QGIS and exported as a web map by the qgis2web plugin.