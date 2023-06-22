import json
import sys
import os
from fastkml import kml

if len(sys.argv) != 4:
	print("Error: wrong argument count, expected three: input_form.json, output_form.json and dir; i.e. the input GeoJSON file to be completed, the output completed GeoJSON file and the directory containing KML files.")
	sys.exit(-1)
input_form_filename = sys.argv[1]
output_form_kml_filename = sys.argv[2]
dir_filename = sys.argv[3]

input_form_file = open(input_form_filename, "r")
input_form = json.load(input_form_file)
input_form_file.close()

geojson_features = input_form["features"]
for geojson_feature in geojson_features:
	geojson_feature["geometry"]["type"] = "Polygon"
	geojson_id = geojson_feature["id"]
	print("Linking GeoJSON id \"{0}\" to a KML file...".format(geojson_id))

	GeoJSON_and_KML_matched = False
	for kml_filename in os.listdir(dir_filename):
		with open(kml_filename, 'rt', encoding="utf-8") as f:
			doc = f.read()
			k = kml.KML()
			k.from_string(doc)
			kml_features = list(k.features())
			if len(kml_features) != 1:
				print("Error: KML syntax unsupported: file must have one <Document> feature")
				sys.exit()
			kml_Document = kml_features[0]
			if kml_Document.name == geojson_id: # Here we match the kml and the GeoJSON
				print("- Found {0}".format(kml_filename))
				GeoJSON_and_KML_matched = True
				kml_Document_features = list(kml_Document.features())
				print("- Found {0} Placemark features".format(len(kml_Document_features)))
				geojson_coordinates = []
				for kml_Placemark in kml_Document_features:
					kml_Polygon = kml_Placemark.geometry
					coords = []
					for coord in kml_Polygon.exterior.coords:
						coord_l = list(coord)[0:2]
						coords.append(coord_l)
					geojson_coordinates.append(coords)
				geojson_feature["geometry"]["coordinates"] = geojson_coordinates
				break
	if GeoJSON_and_KML_matched != True:
		print("Error: no KML file matched the GeoJSON")
		sys.exit()

with open(output_form_kml_filename, "w", encoding="utf-8") as f:
	json.dump(input_form, f, separators=(',', ':'), ensure_ascii=False)

print("\nSuccessfully created", output_form_kml_filename)
