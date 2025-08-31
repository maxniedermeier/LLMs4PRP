import csv
import json

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

# Check if permission is in the role's permissions
def permission_in_role(permission_lc, role_permissions):
    return permission_lc in role_permissions

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
            is_correct = permission_in_role(correct_permission_lc, permissions)
            writer.writerow([request, proposed_role, correct_permission, is_correct])

# Example usage
validate_and_export("../../data/output/LLM-Only/Output_EX.csv", "../../data/request_permission_mappings/SolutionMapping_YYY.csv", "../../data/RBAC_structure/ED_YYY.txt", "../../data/output/LLM-Only/RoleAccuracy_EX.csv")
# 1st parameter: LLM-generated output as input, e.g. Output_E1.csv
# 2nd parameter: A request-to-permission file -> SolutionMapping_AzureStorage.csv or SolutionMapping_Entra.csv
# 3rd parameter: JSON-structured ED document -> ED_AzureStorage.txt or ED_Entra.txt
# 4th parameter: New output file
