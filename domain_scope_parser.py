#!/usr/bin/python3

import csv
import os
import sys

# Check if the input file is provided
if len(sys.argv) != 2:
    print("Usage: python parse_scope.py <input_csv_file>")
    sys.exit(1)

# Input CSV file from the first argument
input_file = sys.argv[1]

# Output files
in_scope_domains = "domains.txt"
in_scope_wildcards = "wildcards.txt"
out_scope_domains = "out_scope_domains.txt"
out_scope_wildcards = "out_scope_wildcards.txt"

# Temporary files to hold data before final output
tmp_in_scope_domains = "tmp_" + in_scope_domains
tmp_in_scope_wildcards = "tmp_" + in_scope_wildcards
tmp_out_scope_domains = "tmp_" + out_scope_domains
tmp_out_scope_wildcards = "tmp_" + out_scope_wildcards

# Clear temporary files if they exist
for tmp_file in [tmp_in_scope_domains, tmp_in_scope_wildcards, tmp_out_scope_domains, tmp_out_scope_wildcards]:
    open(tmp_file, 'w').close()

# Read the CSV file line by line
with open(input_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        asset = row['identifier'].strip()
        type = row['asset_type'].strip()
        coverage = row['eligible_for_bounty'].strip()

        # Process in-scope assets
        if coverage == "true":
            if type == "WILDCARD":
                # Remove the '*' from the wildcard and write to in_scope_wildcards file
                with open(tmp_in_scope_wildcards, 'a') as f:
                    f.write(f"{asset[2:]}\n")
            else:
                # Write to in_scope_domains file
                with open(tmp_in_scope_domains, 'a') as f:
                    f.write(f"{asset}\n")
        else:
            # Process out-of-scope assets
            if type == "WILDCARD":
                # Remove the '*' from the wildcard and write to out_scope_wildcards file
                with open(tmp_out_scope_wildcards, 'a') as f:
                    f.write(f"{asset[2:]}\n")
            else:
                # Write to out_scope_domains file
                with open(tmp_out_scope_domains, 'a') as f:
                    f.write(f"{asset}\n")

# Move non-empty temporary files to final output files
for tmp_file, final_file in [(tmp_in_scope_domains, in_scope_domains), 
                             (tmp_in_scope_wildcards, in_scope_wildcards), 
                             (tmp_out_scope_domains, out_scope_domains), 
                             (tmp_out_scope_wildcards, out_scope_wildcards)]:
    if os.path.getsize(tmp_file) > 0:
        os.rename(tmp_file, final_file)
    else:
        os.remove(tmp_file)

print("Files generated successfully:")
for file in [in_scope_domains, in_scope_wildcards, out_scope_domains, out_scope_wildcards]:
    if os.path.exists(file):
        print(f"- {file}")
