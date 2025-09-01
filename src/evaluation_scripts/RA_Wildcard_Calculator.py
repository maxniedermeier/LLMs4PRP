import csv
import json
import fnmatch

# Load the solution CSV
def load_solution(path):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        return {
            row['prompt'].strip().lower(): (
                row['prompt'].strip(),
                row['permission'].strip(),
                row['permission'].strip().lower()
            )
            for row in reader
        }

# Load the roles-permissions JSON
def load_role_permissions(path):
    with open(path, encoding='utf-8') as f:
        role_data = json.load(f)
        return {
            entry['role'].strip().lower(): set(p.strip().lower() for p in entry['permissions'])
            for entry in role_data
        }

# Load the generated CSV
def load_generated(path):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        return [
            (row['request'].strip(), row['role'].strip())
            for row in reader
        ]

# Exact match
def permission_in_role(permission_lc, role_permissions):
    return permission_lc in role_permissions

# Wildcard match using * or allEntities/allProperties/allTasks
def wildcard_covers_permission(wildcard_perm, required_perm):
    if '*' in wildcard_perm:
        return fnmatch.fnmatchcase(required_perm, wildcard_perm)
    return match_single_custom_permission(wildcard_perm, required_perm)

# Match for allEntities, allProperties, allTasks
def match_single_custom_permission(wildcard_perm, required_perm):
    wildcard_parts = wildcard_perm.lower().split('/')
    required_parts = required_perm.lower().split('/')

    if len(wildcard_parts) != len(required_parts):
        return False

    for w, r in zip(wildcard_parts, required_parts):
        if w in {"allentities", "allproperties", "alltasks"}:
            continue  # wildcard match
        if w != r:
            return False
    return True

# Main validation and export function
def validate_and_export(generated_path, solution_path, roles_json_path, output_path):
    solution = load_solution(solution_path)
    role_permissions = load_role_permissions(roles_json_path)
    generated = load_generated(generated_path)

    with open(output_path, 'w', newline='', encoding='utf-8') as out_file:
        writer = csv.writer(out_file, delimiter=';')
        writer.writerow(['request', 'role', 'correct_permission', 'is_correct'])

        for request, proposed_role in generated:
            key = request.strip().lower()
            role_key = proposed_role.strip().lower()

            if key not in solution:
                writer.writerow([request, proposed_role, "PROMPT NOT FOUND", False])
                continue

            original_prompt, correct_permission, correct_permission_lc = solution[key]
            permissions = role_permissions.get(role_key, set())

            # Default: exact match check
            if permission_in_role(correct_permission_lc, permissions):
                result = 'True'
            else:
                # Check if any wildcard permission covers it
                result = 'False'
                for perm in permissions:
                    if wildcard_covers_permission(perm, correct_permission_lc):
                        result = 'True_Wildcard'
                        break

            writer.writerow([request, proposed_role, correct_permission, result])

# === Run it ===
validate_and_export(
    "../../data/output/ExperimentType/Output_EX.csv",                   # LLM-generated output as input, e.g. Output_E1.csv of Experiment Type LLM-Only or Output_E1H_MIN.csv of Experiment Type Hybrid
    "../../data/request_permission_mappings/SolutionMapping_YYY.csv",   # prompt-to-request solution mapping, SolutionMapping_AzureStorage.csv or SolutionMapping_Entra.csv
    "../../data/RBAC_structure/ED_YYY.txt",                             # JSON-structured Enterprise Document, ED_AzureStorage.txt or ED_Entra.txt
    "../../data/output/ExperimentType/RoleAccuracy_Wildcards_EX.csv"    # Output file
)
