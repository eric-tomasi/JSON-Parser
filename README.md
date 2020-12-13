# JSON-Parser
Simple JSON parser using Python which takes JSON file as input and returns a csv
<br>
<br>

## Usage
Simply run the following: <br>
`python json_parser.py birds_north_america.json` <br>
The only command line argument should be a json file. If you do not input a json file, the program will terminate with asking the user to supply a json file instead. <br>

Next, the user will be promted to define which property they would like to parse. That is, you can select any property from your json file that is at the top level. In our birds_north_america example, I would like to parse the "birds" property. <br>

Thus, fully exectuting the program would look like this: <br>
`python json_parser.py birds_north_america.json` <br>
`Which property would you like to parse? birds` <br>

## Results
All of the parsed results will be in csv format in a file called Parsed_JSON.csv. 
<br>

## Data
The JSON data used for this project can be found at https://github.com/dariusk/corpora/blob/master/data/animals/birds_north_america.json
