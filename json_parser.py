from itertools import product
import json
import csv
import sys


# Ensure user is entering one command line arugment that is a json file
if len(sys.argv) != 2 or ".json" not in sys.argv[1]:
    print("Please specify a .json file")
    sys.exit()

#Load file into python using json lib
input_file = open(sys.argv[1], "r")

data = json.load(input_file)

#repeatedly promts user for a property to parse if the property is not in the file
while True:
    prop = input("Which property would you like to parse? ")
    if prop in data:
        break

#Opens and writes the json data into a csv based on the user's input
with open("Parsed_JSON.csv", 'w') as output_file:
    field_names = data[prop][0].keys()
    writer = csv.DictWriter(output_file, fieldnames=field_names, lineterminator = '\n')
    writer.writeheader()
    for dicts in data[prop]:
        ls = ([(k, x) for x in v] for k, v in dicts.items() if isinstance(v, list))
        ls = [{**dicts, **dict(x)} for x in product(*ls)]
        for item in ls:
            writer.writerow(item)

#close out files
input_file.close()
output_file.close()