import csv
import json

# Load file: role-to-size mapping (normalize keys to lowercase for comparison)
# RoleSizes_AzureStorage.csv or RoleSizes_Entra.csv
# Important: You need to run RoleSize_Creator.py first, in order to be able to open the respective file here
role_sizes = {}
with open("../../data/RBAC_structure/RoleSizes_YYY.csv", newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        role_sizes[row['role'].strip().lower()] = int(row['size'])

# Load the JSON file: role-to-permissions (normalize both role and permissions to lowercase)
# ED_AzureStorage.txt or ED_Entra.txt
role_permissions = {}
with open("../../data/RBAC_structure/ED_YYY.txt", encoding='utf-8') as f:
    data = json.load(f)
    for item in data:
        role = item['role'].strip().lower()
        permissions = set(p.strip().lower() for p in item['permissions'])
        role_permissions[role] = permissions

# Build permission-to-role reverse index
permission_to_roles = {}
for role, perms in role_permissions.items():
    for perm in perms:
        permission_to_roles.setdefault(perm, set()).add(role)

# Process file and augment with new columns
# Important: You need to run the RA_Calculator.py first, in order to to able to open and augment the respective file here
# e.g. RoleAccuracy_E1.csv of Experiment Type LLM-Only or RoleAccuracy_E1H_MIN.csv of Experiment Type Hybrid
output_rows = []
with open("../../data/output/ExperimentType/RoleAccuracy_EX.csv", newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        original_role = row['role']
        original_perm = row['correct_permission']

        # Normalize for comparison
        role_key = original_role.strip().lower()
        perm_key = original_perm.strip().lower()

        # Column E: size of the suggested role
        suggested_size = role_sizes.get(role_key, "N/A")

        # Column F & G: find the smallest role that contains the correct permission
        roles_with_perm = permission_to_roles.get(perm_key, [])
        smallest_role = None
        smallest_size = float('inf')

        for role in roles_with_perm:
            size = role_sizes.get(role)
            if size is not None and size < smallest_size:
                smallest_role = role
                smallest_size = size

        row['suggested_role_size'] = suggested_size
        row['smallest_fitting_role'] = smallest_role if smallest_role else "None"
        row['smallest_fitting_role_size'] = smallest_size if smallest_role else "N/A"

        output_rows.append(row)

# Write output CSV with original structure + 3 new columns
with open("../../data/output/ExperimentType/Polp_EX.csv", "w", newline='', encoding='utf-8') as f:
    fieldnames = ['request', 'role', 'correct_permission', 'is_correct',
                  'suggested_role_size', 'smallest_fitting_role', 'smallest_fitting_role_size']
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()
    writer.writerows(output_rows)

print("CSV output written to output.csv")
