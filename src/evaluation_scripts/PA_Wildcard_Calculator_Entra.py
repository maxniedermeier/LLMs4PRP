import csv

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

# Check if required permission is covered by wildcard-like segments
# In Entra, wildcard segments are "allEntities", "allProperties" and "allTasks"
def custom_permission_match(wildcard_perm, required_perm):
    wildcard_parts = wildcard_perm.lower().split('/')
    required_parts = required_perm.lower().split('/')

    # If they differ in length, they can't match exactly
    if len(wildcard_parts) != len(required_parts):
        return False

    for w, r in zip(wildcard_parts, required_parts):
        if w in {"allentities", "allproperties", "alltasks"}:
            continue  # treat these as wildcards — match any value
        if w != r:
            return False  # mismatch
    return True

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

                if required_permission and any(
                    kw in actual_permission.lower() 
                    for kw in ["allentities", "allproperties", "alltasks"]
                ):
                    covered = custom_permission_match(actual_permission, required_permission)
                    print(f"Request: {prompt}")
                    print(f"Actual: {actual_permission}")
                    print(f"Required: {required_permission}")
                    print(f"Covered by wildcard? {'YES' if covered else 'NO'}\n")

# === Run the analysis ===
csv_path = 'Accuracy_EX.csv'
mapping_path = 'SolutionMapping_Entra.csv'
analyze_csv(csv_path, mapping_path)
