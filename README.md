# Scope CSV Parser

This Python script parses a CSV file containing asset scope information and generates output files based on the eligibility and type of assets. It categorizes domains into in-scope and out-of-scope, and further differentiates between regular domains and wildcard domains.

## Features

- Parses a CSV file with asset scope information.
- Generates separate files for in-scope domains, in-scope wildcards, out-of-scope domains, and out-of-scope wildcards.
- Only generates non-empty files.

## Prerequisites

- Python 3.x

## Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/scope-csv-parser.git
   cd scope-csv-parser
   ```

2. **Ensure your CSV file is in the correct format:**
   The CSV file should follow the format used by HackerOne, with columns for identifier, asset type, eligibility for bounty, etc. Below is an example:

   ```
   identifier,asset_type,instruction,eligible_for_bounty,eligible_for_submission,availability_requirement,confidentiality_requirement,integrity_requirement,max_severity,system_tags,created_at,updated_at
   example.com,URL,"",true,true,high,high,high,critical,,2023-01-01 00:00:00 UTC,2023-01-01 00:00:00 UTC
   api.example.com,URL,"",true,true,,,,critical,,2023-01-01 00:00:00 UTC,2023-01-01 00:00:00 UTC
   *.wildcard.com,WILDCARD,"",true,true,,,,critical,,2023-01-01 00:00:00 UTC,2023-01-01 00:00:00 UTC
   ```

3. **Run the script with the CSV file as an argument:**
   ```bash
   python parse_scope.py path_to_your_csv_file.csv
   ```

4. **Check the generated files:**
   - `domains.txt`: Contains in-scope regular domains.
   - `wildcards.txt`: Contains in-scope wildcard domains (wildcard `*` stripped).
   - `out_scope_domains.txt`: Contains out-of-scope regular domains.
   - `out_scope_wildcards.txt`: Contains out-of-scope wildcard domains (wildcard `*` stripped).

## Example

```bash
python parse_scope.py scope.csv
```

After running the above command, you will see output files in the current directory if they contain data. Empty files will not be generated.

## Contributing

Feel free to submit issues, fork the repository, and send pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the GNU General Public License (GPL).
