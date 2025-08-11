import csv
import fnmatch

# Load solution mapping from the csv file
def load_prompt_to_permission_map(mapping_file):
    prompt_to_permission = {}
    with open(mapping_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            prompt = row['prompt'].strip()
            permission = row['permission'].strip()
            prompt_to_permission[prompt] = permission
    return prompt_to_permission

# Check if required permission is covered by a * wildcard
def is_permission_covered(wildcard_permission, required_permission):
    return fnmatch.fnmatchcase(
        required_permission.lower(), 
        wildcard_permission.lower()
    )

# Process the CSV and perform the checks
def analyze_csv(csv_file, mapping_file):
    prompt_to_permission = load_prompt_to_permission_map(mapping_file)

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            is_correct = row['is_correct'].strip().lower() == 'true'
            if not is_correct:
                prompt = row['request'].strip()
                actual_permission = row['permission'].strip()
                required_permission = prompt_to_permission.get(prompt)

                if "*" in actual_permission and required_permission:
                    covered = is_permission_covered(actual_permission, required_permission)
                    print(f"Request: {prompt}")
                    print(f"Actual: {actual_permission}")
                    print(f"Required: {required_permission}")
                    print(f"Covered by wildcard? {'YES' if covered else 'NO'}\n")

# === Run the analysis ===
csv_path = 'Accuracy_EX.csv'
mapping_path = 'SolutionMapping_AzureStorage.csv'
analyze_csv(csv_path, mapping_path)