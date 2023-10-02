import argparse
import sys
import json
import hashlib

# Load the mapping data
def load_mapping_data():
    files = ["ax", "bx", "dx", "fx", "gx", "lx", "rx", "tx", "ux", "vx"]
    mappings = {}

    for file in files:
        with open(f"data/{file}.json", 'r') as f:
            mappings[file] = json.load(f)

    return mappings

# Expand the minified data
def expand_data(minified_data, mappings):
    abbreviations_used = []  # to store abbreviations used while expanding
    expanded_data = {}
    for key, value in minified_data.items():
        expanded_list = []
        starting_list = value.split("; ")
        mapping = None
        for entry in starting_list:
            if not entry:  # Skip empty entries
                continue
            if mapping is None:
                _key = entry.split('_')[0].lower()  # current key
                mapping = mappings[_key]  # set mapping
            data_parts = entry.split("-")
            expanded_entry = {}
            for m in mapping:
                if m["abbreviation"] == data_parts[0]:
                    abbreviations_used.append(data_parts[0])  # add abbreviation to the list
                    expanded_entry["name"] = m["name"]
                    if _key in ["rx", "bx", "vx", "gx"]:
                        value = float(data_parts[1]) / float(data_parts[2])
                        unit = next(u["name"] for u in mappings["ux"] if u["abbreviation"] == data_parts[3])
                        expanded_entry["value"] = f"{value} {unit}"
                        expanded_entry["date"] = data_parts[-1]
                    elif _key in ["dx", "tx"]:
                        expanded_entry["times"] = int(data_parts[1])
                        locations = data_parts[2].split(", ")
                        location_names = [next(l["name"] for l in mappings["lx"] if l["abbreviation"] == loc) for loc in locations]
                        expanded_entry["locations"] = location_names
                    else:
                        if data_parts[1:]:
                            expanded_entry["data"] = data_parts[1:]
                    break
            expanded_list.append(expanded_entry)
        expanded_data[key] = expanded_list

    return expanded_data, abbreviations_used

# Generate hash for verification
def generate_hash(data):
    # Extract all abbreviations from minified data
    abbreviations = [item.split('-')[0] for key in data for item in data[key].split('; ')]
    # Sort abbreviations and join them into a single string
    ordered_abbreviations = ''.join(sorted(abbreviations))
    return hashlib.md5(ordered_abbreviations.encode()).hexdigest()

# Main
def main(input_data=None):
    mappings = load_mapping_data()
    if input_data:
        minified_input = json.loads(input_data)
    else:
        with open(args.input_file, 'r') as f:
            minified_input = json.load(f)

    expanded_output, abbrevs_from_expanded = expand_data(minified_input, mappings)
    hash_from_minified = generate_hash(minified_input)  
    hash_from_expanded = generate_hash({"abbreviations": '; '.join(abbrevs_from_expanded)})
    assert hash_from_minified == hash_from_expanded, "Hash mismatch: Data integrity is compromised!"
    verification_status = "PASSED" if hash_from_minified == hash_from_expanded else "FAILED"
    return expanded_output, hash_from_minified, verification_status

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='MSPS medical data expansion.')
    parser.add_argument('-i', '--input-file', type=str, help='Path to the input JSON file with minified data.')
    parser.add_argument('-o', '--output-file', type=str, help='Path to the output JSON file to save expanded data.')
    args = parser.parse_args()

    # If input file is provided
    if args.input_file:
        expanded_result, checksum, verification_status = main()
    # If no file, check for piped input
    elif not sys.stdin.isatty():
        input_data = sys.stdin.read()
        expanded_result, checksum, verification_status = main(input_data)
    # Handle case when no input is provided
    else:
        print("Please provide input either as a file using -i or through piping.")
        sys.exit(1)

    # If output file is provided
    if args.output_file:
        with open(args.output_file, 'w') as f:
            json.dump(expanded_output, f, indent=4)
    else:
        print(json.dumps(expanded_result, indent=4))

    print("Verification:", verification_status)
    print("Checksum:", checksum)

