import json
import csv

# PARAMETERS
# False means searching for the largest role containing the translated permission
# True means searching for the smallest role containing the translated permission
POLP = False
# Load roles JSON, either use ED_AzureStorage.txt or ED_Entra.txt
with open("ED_YYY.txt", "r") as f:
    roles_data = json.load(f)

# roles_data format:
# [
#   {"role": "RoleName", "permissions": ["perm1", "perm2", ...]},
#   ...
# ]

# Define input and output files
input_csv = "Output_EX_NoRole.csv" # LLM-Only output file, but with the suggested role removed!!
output_csv = "Output_EXH_ZZZ.csv" # New output file, e.g. Output_E1H_MIN

with open(input_csv, newline='', encoding="utf-8") as infile, open(output_csv, "w", newline='', encoding="utf-8") as outfile:
    reader = csv.DictReader(infile, delimiter=';')
    fieldnames = reader.fieldnames + ["Candidate_Roles"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()

    for row in reader:
        permission = row["permission"].strip().lower()

        if permission == "none":
            row["role"] = "NONE"
            row["Candidate_Roles"] = "NONE"
        else:
            # Find all roles that have this permission
            candidate_roles = []
            for role_entry in roles_data:
                perms_lower = [p.lower() for p in role_entry["permissions"]]
                if permission in perms_lower:
                    candidate_roles.append((role_entry["role"], len(perms_lower)))

            if not candidate_roles:
                row["role"] = "NONE"
                row["Candidate_Roles"] = "NONE"
            else:
                # Sort roles by size of permissions: ascending if POLP True, descending if False
                candidate_roles.sort(key=lambda x: x[1], reverse=not POLP)

                best_role = candidate_roles[0][0]
                row["role"] = best_role
                row["Candidate_Roles"] = ", ".join([f"{r}({s})" for r, s in candidate_roles])

        writer.writerow(row)

print(f"Processed output written to: {output_csv}")