import json
import sys

if len(sys.argv) != 3:
	print("Error: wrong argument count, expected two: input.json, output.json")
	sys.exit(-1)
input_filename = sys.argv[1]
output_filename = sys.argv[2]

input_data_file = open(input_filename, "r")
input_data = json.load(input_data_file)
input_data_file.close()

features = input_data["features"]
for feature in features:
	coordinates = feature["geometry"]["coordinates"]
	# print(coordinates)
	coordinates[0] = float(coordinates[0])
	coordinates[1] = float(coordinates[1])
	print("- Switched coordinates from string to float")
	del feature["properties"]["geolocation"]
	print("- Deleted property \"geolocation\" (non supported by qgis2web)")
	del feature["properties"]["html_data"]
	print("- Deleted property \"html_data\" (non supported by qgis2web)")

with open(output_filename, "w", encoding="utf-8") as f:
	json.dump(input_data, f, separators=(',', ':'), ensure_ascii=False)

print("\nSuccessfully created", output_filename)