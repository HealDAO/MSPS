import argparse
import json
import hashlib
import sys

# Load the mapping data
def load_mapping_data():
    files = ["ax", "bx", "dx", "fx", "gx", "lx", "rx", "tx", "ux", "vx"]
    mappings = {}

    for file in files:
        with open(f"data/{file}.json", 'r') as f:
            mappings[file] = json.load(f)

    return mappings

def get_mapping_file_for_entries(entries, mappings):
    file_scores = {}
    for file, file_mappings in mappings.items():
        score = sum(1 for entry in entries if any(mapping_entry["name"] == entry["name"] for mapping_entry in file_mappings))
        file_scores[file] = score
    best_fit_file = max(file_scores, key=file_scores.get)
    return best_fit_file

def generate_abbreviation_hash(mappings):
    all_abbreviations = ''.join(item["abbreviation"] for sublist in mappings.values() for item in sublist)
    return hashlib.md5(all_abbreviations.encode()).hexdigest()

def validate_entries_against_standard(expanded_data, mappings):
    for key, entries in expanded_data.items():
        for entry in entries:
            valid_name = any(any(item["name"] == entry["name"] for item in file_mappings) for file_mappings in mappings.values())
            if not valid_name:
                raise ValueError(f"Entry {entry['name']} not found in standard mappings.")

# Minify the expanded data
def minify_data(expanded_data, mappings):
    minified_data = {}
    for key, entries in expanded_data.items():
        file = get_mapping_file_for_entries(entries, mappings)
        if not file:
            continue
        for entry in entries:
            minified_list = []
            for entry in entries:
                abbreviation = next((item["abbreviation"] for item in mappings[file] if item["name"] == entry["name"]), None)
                if abbreviation is None:
                    print(f"Warning: No abbreviation found for {entry['name']} in {file}. Skipping.")
                    continue
                minified_entry = abbreviation
                if "value" in entry:
                    value, multiplier = (float(val) for val in entry["value"].split(' ')[0].split('.'))
                    unit_abbreviation = next((item["abbreviation"] for item in mappings["ux"] if item["name"] == entry["value"].split(' ')[1]), None)
                    minified_entry += f"-{int(value)}-{int(multiplier)}-{unit_abbreviation}-{entry['date']}"
                elif "times" in entry:
                    location_abbreviations = ','.join(next(item["abbreviation"] for item in mappings["lx"] if item["name"] == loc) for loc in entry["locations"])
                    minified_entry += f"-{entry['times']}-LX_{location_abbreviations}"
                minified_list.append(minified_entry)
            minified_data[key] = "; ".join(minified_list)
    return minified_data

# Main function to drive the minification
def main(input_data):
    mappings = load_mapping_data()
    abbreviation_hash = generate_abbreviation_hash(mappings)
    print(f"Abbreviation Hash: {abbreviation_hash}")
    validate_entries_against_standard(input_data, mappings)
    minified_output = minify_data(input_data, mappings)
    return minified_output

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Minify medical data.')
    parser.add_argument('-i', '--input-file', type=str, help='Path to the input JSON file with expanded data.')
    parser.add_argument('-o', '--output-file', type=str, help='Path to save minified data. If not provided, prints to console.')
    args = parser.parse_args()

    # Load expanded data from file or from piped input
    if args.input_file:
        with open(args.input_file, 'r') as f:
            input_data = json.load(f)
    elif not sys.stdin.isatty():  # Check for piped input
        input_data = json.loads(sys.stdin.read())
    else:
        print("Please provide input either as a file using -i or through piping.")
        sys.exit(1)

    minified_result = main(input_data)
    
    if args.output_file:
        with open(args.output_file, 'w') as f:
            json.dump(minified_result, f)
    else:
        print(minified_result)
