import csv
import json
import sys

# File paths
csv_file_path = "../../data/output/LLM-Only/Output_E1.csv"
json_file_path = "../../data/RBAC_structure/ED_AzureStorage.txt"

# Load roles and permissions from JSON
try:
    with open(json_file_path, "r", encoding="utf-8") as f:
        role_permission_data = json.load(f)
except json.JSONDecodeError as e:
    print(f"Error reading JSON: {e}")
    sys.exit(1)

# Create sets for lookup (lowercased for case-insensitive comparison)
all_permissions = set()
all_roles = set()

for entry in role_permission_data:
    all_roles.add(entry["role"].strip().lower())
    all_permissions.update([p.strip().lower() for p in entry["permissions"]])

# Initialize counters and invalid lists
invalid_permission_count = 0
invalid_role_count = 0

invalid_permissions = set()
invalid_roles = set()

# Read CSV and process
with open(csv_file_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=";")
    
    for row in reader:
        permission = row["permission"].strip()
        role = row["role"].strip()

        # Normalize to lowercase for comparison
        permission_lower = permission.lower()
        role_lower = role.lower()

        # Check permission
        if permission_lower != "none" and permission_lower not in all_permissions:
            invalid_permission_count += 1
            invalid_permissions.add(permission)
        
        # Check role
        if role_lower != "none" and role_lower not in all_roles:
            invalid_role_count += 1
            invalid_roles.add(role)

# Output results
print("E1")
print(f"Hallucination Ratio {invalid_permission_count/500} in 'permission' column.")
print(f"Hallucination Ratio {invalid_role_count/500} in 'role' column.\n")

print("List of invalid permissions:")
for perm in sorted(invalid_permissions, key=lambda x: x.lower()):
    print(f"- {perm}")

print("\nList of invalid roles:")
for r in sorted(invalid_roles, key=lambda x: x.lower()):
    print(f"- {r}")
    
# File paths
csv_file_path = "../../data/output/LLM-Only/Output_E2.csv"
json_file_path = "../../data/RBAC_structure/ED_AzureStorage.txt"

# Load roles and permissions from JSON
try:
    with open(json_file_path, "r", encoding="utf-8") as f:
        role_permission_data = json.load(f)
except json.JSONDecodeError as e:
    print(f"Error reading JSON: {e}")
    sys.exit(1)

# Create sets for lookup (lowercased for case-insensitive comparison)
all_permissions = set()
all_roles = set()

for entry in role_permission_data:
    all_roles.add(entry["role"].strip().lower())
    all_permissions.update([p.strip().lower() for p in entry["permissions"]])

# Initialize counters and invalid lists
invalid_permission_count = 0
invalid_role_count = 0

invalid_permissions = set()
invalid_roles = set()

# Read CSV and process
with open(csv_file_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=";")
    
    for row in reader:
        permission = row["permission"].strip()
        role = row["role"].strip()

        # Normalize to lowercase for comparison
        permission_lower = permission.lower()
        role_lower = role.lower()

        # Check permission
        if permission_lower != "none" and permission_lower not in all_permissions:
            invalid_permission_count += 1
            invalid_permissions.add(permission)
        
        # Check role
        if role_lower != "none" and role_lower not in all_roles:
            invalid_role_count += 1
            invalid_roles.add(role)

# Output results
print("E2")
print(f"Hallucination Ratio {invalid_permission_count/500} in 'permission' column.")
print(f"Hallucination Ratio {invalid_role_count/500} in 'role' column.\n")

print("List of invalid permissions:")
for perm in sorted(invalid_permissions, key=lambda x: x.lower()):
    print(f"- {perm}")

print("\nList of invalid roles:")
for r in sorted(invalid_roles, key=lambda x: x.lower()):
    print(f"- {r}")
    
# File paths
csv_file_path = "../../data/output/LLM-Only/Output_E3.csv"
json_file_path = "../../data/RBAC_structure/ED_AzureStorage.txt"

# Load roles and permissions from JSON
try:
    with open(json_file_path, "r", encoding="utf-8") as f:
        role_permission_data = json.load(f)
except json.JSONDecodeError as e:
    print(f"Error reading JSON: {e}")
    sys.exit(1)

# Create sets for lookup (lowercased for case-insensitive comparison)
all_permissions = set()
all_roles = set()

for entry in role_permission_data:
    all_roles.add(entry["role"].strip().lower())
    all_permissions.update([p.strip().lower() for p in entry["permissions"]])

# Initialize counters and invalid lists
invalid_permission_count = 0
invalid_role_count = 0

invalid_permissions = set()
invalid_roles = set()

# Read CSV and process
with open(csv_file_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=";")
    
    for row in reader:
        permission = row["permission"].strip()
        role = row["role"].strip()

        # Normalize to lowercase for comparison
        permission_lower = permission.lower()
        role_lower = role.lower()

        # Check permission
        if permission_lower != "none" and permission_lower not in all_permissions:
            invalid_permission_count += 1
            invalid_permissions.add(permission)
        
        # Check role
        if role_lower != "none" and role_lower not in all_roles:
            invalid_role_count += 1
            invalid_roles.add(role)

# Output results
print("E3")
print(f"Hallucination Ratio {invalid_permission_count/500} in 'permission' column.")
print(f"Hallucination Ratio {invalid_role_count/500} in 'role' column.\n")

print("List of invalid permissions:")
for perm in sorted(invalid_permissions, key=lambda x: x.lower()):
    print(f"- {perm}")

print("\nList of invalid roles:")
for r in sorted(invalid_roles, key=lambda x: x.lower()):
    print(f"- {r}")
    
# File paths
csv_file_path = "../../data/output/LLM-Only/Output_E4.csv"
json_file_path = "../../data/RBAC_structure/ED_AzureStorage.txt"

# Load roles and permissions from JSON
try:
    with open(json_file_path, "r", encoding="utf-8") as f:
        role_permission_data = json.load(f)
except json.JSONDecodeError as e:
    print(f"Error reading JSON: {e}")
    sys.exit(1)

# Create sets for lookup (lowercased for case-insensitive comparison)
all_permissions = set()
all_roles = set()

for entry in role_permission_data:
    all_roles.add(entry["role"].strip().lower())
    all_permissions.update([p.strip().lower() for p in entry["permissions"]])

# Initialize counters and invalid lists
invalid_permission_count = 0
invalid_role_count = 0

invalid_permissions = set()
invalid_roles = set()

# Read CSV and process
with open(csv_file_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=";")
    
    for row in reader:
        permission = row["permission"].strip()
        role = row["role"].strip()

        # Normalize to lowercase for comparison
        permission_lower = permission.lower()
        role_lower = role.lower()

        # Check permission
        if permission_lower != "none" and permission_lower not in all_permissions:
            invalid_permission_count += 1
            invalid_permissions.add(permission)
        
        # Check role
        if role_lower != "none" and role_lower not in all_roles:
            invalid_role_count += 1
            invalid_roles.add(role)

# Output results
print("E4")
print(f"Hallucination Ratio {invalid_permission_count/500} in 'permission' column.")
print(f"Hallucination Ratio {invalid_role_count/500} in 'role' column.\n")

print("List of invalid permissions:")
for perm in sorted(invalid_permissions, key=lambda x: x.lower()):
    print(f"- {perm}")

print("\nList of invalid roles:")
for r in sorted(invalid_roles, key=lambda x: x.lower()):
    print(f"- {r}")
    
# File paths
csv_file_path = "../../data/output/LLM-Only/Output_E5.csv"
json_file_path = "../../data/RBAC_structure/ED_Entra.txt"

# Load roles and permissions from JSON
try:
    with open(json_file_path, "r", encoding="utf-8") as f:
        role_permission_data = json.load(f)
except json.JSONDecodeError as e:
    print(f"Error reading JSON: {e}")
    sys.exit(1)

# Create sets for lookup (lowercased for case-insensitive comparison)
all_permissions = set()
all_roles = set()

for entry in role_permission_data:
    all_roles.add(entry["role"].strip().lower())
    all_permissions.update([p.strip().lower() for p in entry["permissions"]])

# Initialize counters and invalid lists
invalid_permission_count = 0
invalid_role_count = 0

invalid_permissions = set()
invalid_roles = set()

# Read CSV and process
with open(csv_file_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=";")
    
    for row in reader:
        permission = row["permission"].strip()
        role = row["role"].strip()

        # Normalize to lowercase for comparison
        permission_lower = permission.lower()
        role_lower = role.lower()

        # Check permission
        if permission_lower != "none" and permission_lower not in all_permissions:
            invalid_permission_count += 1
            invalid_permissions.add(permission)
        
        # Check role
        if role_lower != "none" and role_lower not in all_roles:
            invalid_role_count += 1
            invalid_roles.add(role)

# Output results
print("E5")
print(f"Hallucination Ratio {invalid_permission_count/500} in 'permission' column.")
print(f"Hallucination Ratio {invalid_role_count/500} in 'role' column.\n")

print("List of invalid permissions:")
for perm in sorted(invalid_permissions, key=lambda x: x.lower()):
    print(f"- {perm}")

print("\nList of invalid roles:")
for r in sorted(invalid_roles, key=lambda x: x.lower()):
    print(f"- {r}")
    
# File paths
csv_file_path = "../../data/output/LLM-Only/Output_E6.csv"
json_file_path = "../../data/RBAC_structure/ED_Entra.txt"

# Load roles and permissions from JSON
try:
    with open(json_file_path, "r", encoding="utf-8") as f:
        role_permission_data = json.load(f)
except json.JSONDecodeError as e:
    print(f"Error reading JSON: {e}")
    sys.exit(1)

# Create sets for lookup (lowercased for case-insensitive comparison)
all_permissions = set()
all_roles = set()

for entry in role_permission_data:
    all_roles.add(entry["role"].strip().lower())
    all_permissions.update([p.strip().lower() for p in entry["permissions"]])

# Initialize counters and invalid lists
invalid_permission_count = 0
invalid_role_count = 0

invalid_permissions = set()
invalid_roles = set()

# Read CSV and process
with open(csv_file_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=";")
    
    for row in reader:
        permission = row["permission"].strip()
        role = row["role"].strip()

        # Normalize to lowercase for comparison
        permission_lower = permission.lower()
        role_lower = role.lower()

        # Check permission
        if permission_lower != "none" and permission_lower not in all_permissions:
            invalid_permission_count += 1
            invalid_permissions.add(permission)
        
        # Check role
        if role_lower != "none" and role_lower not in all_roles:
            invalid_role_count += 1
            invalid_roles.add(role)

# Output results
print("E6")
print(f"Hallucination Ratio {invalid_permission_count/500} in 'permission' column.")
print(f"Hallucination Ratio {invalid_role_count/500} in 'role' column.\n")

print("List of invalid permissions:")
for perm in sorted(invalid_permissions, key=lambda x: x.lower()):
    print(f"- {perm}")

print("\nList of invalid roles:")
for r in sorted(invalid_roles, key=lambda x: x.lower()):
    print(f"- {r}")
    
# File paths
csv_file_path = "../../data/output/LLM-Only/Output_E7.csv"
json_file_path = "../../data/RBAC_structure/ED_Entra.txt"

# Load roles and permissions from JSON
try:
    with open(json_file_path, "r", encoding="utf-8") as f:
        role_permission_data = json.load(f)
except json.JSONDecodeError as e:
    print(f"Error reading JSON: {e}")
    sys.exit(1)

# Create sets for lookup (lowercased for case-insensitive comparison)
all_permissions = set()
all_roles = set()

for entry in role_permission_data:
    all_roles.add(entry["role"].strip().lower())
    all_permissions.update([p.strip().lower() for p in entry["permissions"]])

# Initialize counters and invalid lists
invalid_permission_count = 0
invalid_role_count = 0

invalid_permissions = set()
invalid_roles = set()

# Read CSV and process
with open(csv_file_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=";")
    
    for row in reader:
        permission = row["permission"].strip()
        role = row["role"].strip()

        # Normalize to lowercase for comparison
        permission_lower = permission.lower()
        role_lower = role.lower()

        # Check permission
        if permission_lower != "none" and permission_lower not in all_permissions:
            invalid_permission_count += 1
            invalid_permissions.add(permission)
        
        # Check role
        if role_lower != "none" and role_lower not in all_roles:
            invalid_role_count += 1
            invalid_roles.add(role)

# Output results
print("E7")
print(f"Hallucination Ratio {invalid_permission_count/500} in 'permission' column.")
print(f"Hallucination Ratio {invalid_role_count/500} in 'role' column.\n")

print("List of invalid permissions:")
for perm in sorted(invalid_permissions, key=lambda x: x.lower()):
    print(f"- {perm}")

print("\nList of invalid roles:")
for r in sorted(invalid_roles, key=lambda x: x.lower()):
    print(f"- {r}")
    
# File paths
csv_file_path = "../../data/output/LLM-Only/Output_E8.csv"
json_file_path = "../../data/RBAC_structure/ED_Entra.txt"

# Load roles and permissions from JSON
try:
    with open(json_file_path, "r", encoding="utf-8") as f:
        role_permission_data = json.load(f)
except json.JSONDecodeError as e:
    print(f"Error reading JSON: {e}")
    sys.exit(1)

# Create sets for lookup (lowercased for case-insensitive comparison)
all_permissions = set()
all_roles = set()

for entry in role_permission_data:
    all_roles.add(entry["role"].strip().lower())
    all_permissions.update([p.strip().lower() for p in entry["permissions"]])

# Initialize counters and invalid lists
invalid_permission_count = 0
invalid_role_count = 0

invalid_permissions = set()
invalid_roles = set()

# Read CSV and process
with open(csv_file_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=";")
    
    for row in reader:
        permission = row["permission"].strip()
        role = row["role"].strip()

        # Normalize to lowercase for comparison
        permission_lower = permission.lower()
        role_lower = role.lower()

        # Check permission
        if permission_lower != "none" and permission_lower not in all_permissions:
            invalid_permission_count += 1
            invalid_permissions.add(permission)
        
        # Check role
        if role_lower != "none" and role_lower not in all_roles:
            invalid_role_count += 1
            invalid_roles.add(role)

# Output results
print("E8")
print(f"Hallucination Ratio {invalid_permission_count/500} in 'permission' column.")
print(f"Hallucination Ratio {invalid_role_count/500} in 'role' column.\n")

print("List of invalid permissions:")
for perm in sorted(invalid_permissions, key=lambda x: x.lower()):
    print(f"- {perm}")

print("\nList of invalid roles:")
for r in sorted(invalid_roles, key=lambda x: x.lower()):
    print(f"- {r}")
    
###################################################
# Now doing the same thing for the hybrid outputs #
###################################################

# File paths
csv_file_path = "../../data/output/Hybrid/Output_E1H_MIN.csv"
json_file_path = "../../data/RBAC_structure/ED_AzureStorage.txt"

# Load roles and permissions from JSON
try:
    with open(json_file_path, "r", encoding="utf-8") as f:
        role_permission_data = json.load(f)
except json.JSONDecodeError as e:
    print(f"Error reading JSON: {e}")
    sys.exit(1)

# Create sets for lookup (lowercased for case-insensitive comparison)
all_permissions = set()
all_roles = set()

for entry in role_permission_data:
    all_roles.add(entry["role"].strip().lower())
    all_permissions.update([p.strip().lower() for p in entry["permissions"]])

# Initialize counters and invalid lists
invalid_permission_count = 0
invalid_role_count = 0

invalid_permissions = set()
invalid_roles = set()

# Read CSV and process
with open(csv_file_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=";")
    
    for row in reader:
        permission = row["permission"].strip()
        role = row["role"].strip()

        # Normalize to lowercase for comparison
        permission_lower = permission.lower()
        role_lower = role.lower()

        # Check permission
        if permission_lower != "none" and permission_lower not in all_permissions:
            invalid_permission_count += 1
            invalid_permissions.add(permission)
        
        # Check role
        if role_lower != "none" and role_lower not in all_roles:
            invalid_role_count += 1
            invalid_roles.add(role)

# Output results
print("E1H_MIN")
print(f"Hallucination Ratio {invalid_permission_count/500} in 'permission' column.")
print(f"Hallucination Ratio {invalid_role_count/500} in 'role' column.\n")

print("List of invalid permissions:")
for perm in sorted(invalid_permissions, key=lambda x: x.lower()):
    print(f"- {perm}")

print("\nList of invalid roles:")
for r in sorted(invalid_roles, key=lambda x: x.lower()):
    print(f"- {r}")
    
# File paths
csv_file_path = "../../data/output/Hybrid/Output_E1H_MAX.csv"
json_file_path = "../../data/RBAC_structure/ED_AzureStorage.txt"

# Load roles and permissions from JSON
try:
    with open(json_file_path, "r", encoding="utf-8") as f:
        role_permission_data = json.load(f)
except json.JSONDecodeError as e:
    print(f"Error reading JSON: {e}")
    sys.exit(1)

# Create sets for lookup (lowercased for case-insensitive comparison)
all_permissions = set()
all_roles = set()

for entry in role_permission_data:
    all_roles.add(entry["role"].strip().lower())
    all_permissions.update([p.strip().lower() for p in entry["permissions"]])

# Initialize counters and invalid lists
invalid_permission_count = 0
invalid_role_count = 0

invalid_permissions = set()
invalid_roles = set()

# Read CSV and process
with open(csv_file_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=";")
    
    for row in reader:
        permission = row["permission"].strip()
        role = row["role"].strip()

        # Normalize to lowercase for comparison
        permission_lower = permission.lower()
        role_lower = role.lower()

        # Check permission
        if permission_lower != "none" and permission_lower not in all_permissions:
            invalid_permission_count += 1
            invalid_permissions.add(permission)
        
        # Check role
        if role_lower != "none" and role_lower not in all_roles:
            invalid_role_count += 1
            invalid_roles.add(role)

# Output results
print("E1H_MAX")
print(f"Hallucination Ratio {invalid_permission_count/500} in 'permission' column.")
print(f"Hallucination Ratio {invalid_role_count/500} in 'role' column.\n")

print("List of invalid permissions:")
for perm in sorted(invalid_permissions, key=lambda x: x.lower()):
    print(f"- {perm}")

print("\nList of invalid roles:")
for r in sorted(invalid_roles, key=lambda x: x.lower()):
    print(f"- {r}")
    
# File paths
csv_file_path = "../../data/output/Hybrid/Output_E2H_MIN.csv"
json_file_path = "../../data/RBAC_structure/ED_AzureStorage.txt"

# Load roles and permissions from JSON
try:
    with open(json_file_path, "r", encoding="utf-8") as f:
        role_permission_data = json.load(f)
except json.JSONDecodeError as e:
    print(f"Error reading JSON: {e}")
    sys.exit(1)

# Create sets for lookup (lowercased for case-insensitive comparison)
all_permissions = set()
all_roles = set()

for entry in role_permission_data:
    all_roles.add(entry["role"].strip().lower())
    all_permissions.update([p.strip().lower() for p in entry["permissions"]])

# Initialize counters and invalid lists
invalid_permission_count = 0
invalid_role_count = 0

invalid_permissions = set()
invalid_roles = set()

# Read CSV and process
with open(csv_file_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=";")
    
    for row in reader:
        permission = row["permission"].strip()
        role = row["role"].strip()

        # Normalize to lowercase for comparison
        permission_lower = permission.lower()
        role_lower = role.lower()

        # Check permission
        if permission_lower != "none" and permission_lower not in all_permissions:
            invalid_permission_count += 1
            invalid_permissions.add(permission)
        
        # Check role
        if role_lower != "none" and role_lower not in all_roles:
            invalid_role_count += 1
            invalid_roles.add(role)

# Output results
print("E2H_MIN")
print(f"Hallucination Ratio {invalid_permission_count/500} in 'permission' column.")
print(f"Hallucination Ratio {invalid_role_count/500} in 'role' column.\n")

print("List of invalid permissions:")
for perm in sorted(invalid_permissions, key=lambda x: x.lower()):
    print(f"- {perm}")

print("\nList of invalid roles:")
for r in sorted(invalid_roles, key=lambda x: x.lower()):
    print(f"- {r}")
    
# File paths
csv_file_path = "../../data/output/Hybrid/Output_E2H_MAX.csv"
json_file_path = "../../data/RBAC_structure/ED_AzureStorage.txt"

# Load roles and permissions from JSON
try:
    with open(json_file_path, "r", encoding="utf-8") as f:
        role_permission_data = json.load(f)
except json.JSONDecodeError as e:
    print(f"Error reading JSON: {e}")
    sys.exit(1)

# Create sets for lookup (lowercased for case-insensitive comparison)
all_permissions = set()
all_roles = set()

for entry in role_permission_data:
    all_roles.add(entry["role"].strip().lower())
    all_permissions.update([p.strip().lower() for p in entry["permissions"]])

# Initialize counters and invalid lists
invalid_permission_count = 0
invalid_role_count = 0

invalid_permissions = set()
invalid_roles = set()

# Read CSV and process
with open(csv_file_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=";")
    
    for row in reader:
        permission = row["permission"].strip()
        role = row["role"].strip()

        # Normalize to lowercase for comparison
        permission_lower = permission.lower()
        role_lower = role.lower()

        # Check permission
        if permission_lower != "none" and permission_lower not in all_permissions:
            invalid_permission_count += 1
            invalid_permissions.add(permission)
        
        # Check role
        if role_lower != "none" and role_lower not in all_roles:
            invalid_role_count += 1
            invalid_roles.add(role)

# Output results
print("E2H_MAX")
print(f"Hallucination Ratio {invalid_permission_count/500} in 'permission' column.")
print(f"Hallucination Ratio {invalid_role_count/500} in 'role' column.\n")

print("List of invalid permissions:")
for perm in sorted(invalid_permissions, key=lambda x: x.lower()):
    print(f"- {perm}")

print("\nList of invalid roles:")
for r in sorted(invalid_roles, key=lambda x: x.lower()):
    print(f"- {r}")
    
# File paths
csv_file_path = "../../data/output/Hybrid/Output_E5H_MIN.csv"
json_file_path = "../../data/RBAC_structure/ED_Entra.txt"

# Load roles and permissions from JSON
try:
    with open(json_file_path, "r", encoding="utf-8") as f:
        role_permission_data = json.load(f)
except json.JSONDecodeError as e:
    print(f"Error reading JSON: {e}")
    sys.exit(1)

# Create sets for lookup (lowercased for case-insensitive comparison)
all_permissions = set()
all_roles = set()

for entry in role_permission_data:
    all_roles.add(entry["role"].strip().lower())
    all_permissions.update([p.strip().lower() for p in entry["permissions"]])

# Initialize counters and invalid lists
invalid_permission_count = 0
invalid_role_count = 0

invalid_permissions = set()
invalid_roles = set()

# Read CSV and process
with open(csv_file_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=";")
    
    for row in reader:
        permission = row["permission"].strip()
        role = row["role"].strip()

        # Normalize to lowercase for comparison
        permission_lower = permission.lower()
        role_lower = role.lower()

        # Check permission
        if permission_lower != "none" and permission_lower not in all_permissions:
            invalid_permission_count += 1
            invalid_permissions.add(permission)
        
        # Check role
        if role_lower != "none" and role_lower not in all_roles:
            invalid_role_count += 1
            invalid_roles.add(role)

# Output results
print("E5H_MIN")
print(f"Hallucination Ratio {invalid_permission_count/500} in 'permission' column.")
print(f"Hallucination Ratio {invalid_role_count/500} in 'role' column.\n")

print("List of invalid permissions:")
for perm in sorted(invalid_permissions, key=lambda x: x.lower()):
    print(f"- {perm}")

print("\nList of invalid roles:")
for r in sorted(invalid_roles, key=lambda x: x.lower()):
    print(f"- {r}")
    
# File paths
csv_file_path = "../../data/output/Hybrid/Output_E5H_MAX.csv"
json_file_path = "../../data/RBAC_structure/ED_Entra.txt"

# Load roles and permissions from JSON
try:
    with open(json_file_path, "r", encoding="utf-8") as f:
        role_permission_data = json.load(f)
except json.JSONDecodeError as e:
    print(f"Error reading JSON: {e}")
    sys.exit(1)

# Create sets for lookup (lowercased for case-insensitive comparison)
all_permissions = set()
all_roles = set()

for entry in role_permission_data:
    all_roles.add(entry["role"].strip().lower())
    all_permissions.update([p.strip().lower() for p in entry["permissions"]])

# Initialize counters and invalid lists
invalid_permission_count = 0
invalid_role_count = 0

invalid_permissions = set()
invalid_roles = set()

# Read CSV and process
with open(csv_file_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=";")
    
    for row in reader:
        permission = row["permission"].strip()
        role = row["role"].strip()

        # Normalize to lowercase for comparison
        permission_lower = permission.lower()
        role_lower = role.lower()

        # Check permission
        if permission_lower != "none" and permission_lower not in all_permissions:
            invalid_permission_count += 1
            invalid_permissions.add(permission)
        
        # Check role
        if role_lower != "none" and role_lower not in all_roles:
            invalid_role_count += 1
            invalid_roles.add(role)

# Output results
print("E5H_MAX")
print(f"Hallucination Ratio {invalid_permission_count/500} in 'permission' column.")
print(f"Hallucination Ratio {invalid_role_count/500} in 'role' column.\n")

print("List of invalid permissions:")
for perm in sorted(invalid_permissions, key=lambda x: x.lower()):
    print(f"- {perm}")

print("\nList of invalid roles:")
for r in sorted(invalid_roles, key=lambda x: x.lower()):
    print(f"- {r}")
    
# File paths
csv_file_path = "../../data/output/Hybrid/Output_E6H_MIN.csv"
json_file_path = "../../data/RBAC_structure/ED_Entra.txt"

# Load roles and permissions from JSON
try:
    with open(json_file_path, "r", encoding="utf-8") as f:
        role_permission_data = json.load(f)
except json.JSONDecodeError as e:
    print(f"Error reading JSON: {e}")
    sys.exit(1)

# Create sets for lookup (lowercased for case-insensitive comparison)
all_permissions = set()
all_roles = set()

for entry in role_permission_data:
    all_roles.add(entry["role"].strip().lower())
    all_permissions.update([p.strip().lower() for p in entry["permissions"]])

# Initialize counters and invalid lists
invalid_permission_count = 0
invalid_role_count = 0

invalid_permissions = set()
invalid_roles = set()

# Read CSV and process
with open(csv_file_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=";")
    
    for row in reader:
        permission = row["permission"].strip()
        role = row["role"].strip()

        # Normalize to lowercase for comparison
        permission_lower = permission.lower()
        role_lower = role.lower()

        # Check permission
        if permission_lower != "none" and permission_lower not in all_permissions:
            invalid_permission_count += 1
            invalid_permissions.add(permission)
        
        # Check role
        if role_lower != "none" and role_lower not in all_roles:
            invalid_role_count += 1
            invalid_roles.add(role)

# Output results
print("E6H_MIN")
print(f"Hallucination Ratio {invalid_permission_count/500} in 'permission' column.")
print(f"Hallucination Ratio {invalid_role_count/500} in 'role' column.\n")

print("List of invalid permissions:")
for perm in sorted(invalid_permissions, key=lambda x: x.lower()):
    print(f"- {perm}")

print("\nList of invalid roles:")
for r in sorted(invalid_roles, key=lambda x: x.lower()):
    print(f"- {r}")
    
# File paths
csv_file_path = "../../data/output/Hybrid/Output_E6H_MAX.csv"
json_file_path = "../../data/RBAC_structure/ED_Entra.txt"

# Load roles and permissions from JSON
try:
    with open(json_file_path, "r", encoding="utf-8") as f:
        role_permission_data = json.load(f)
except json.JSONDecodeError as e:
    print(f"Error reading JSON: {e}")
    sys.exit(1)

# Create sets for lookup (lowercased for case-insensitive comparison)
all_permissions = set()
all_roles = set()

for entry in role_permission_data:
    all_roles.add(entry["role"].strip().lower())
    all_permissions.update([p.strip().lower() for p in entry["permissions"]])

# Initialize counters and invalid lists
invalid_permission_count = 0
invalid_role_count = 0

invalid_permissions = set()
invalid_roles = set()

# Read CSV and process
with open(csv_file_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=";")
    
    for row in reader:
        permission = row["permission"].strip()
        role = row["role"].strip()

        # Normalize to lowercase for comparison
        permission_lower = permission.lower()
        role_lower = role.lower()

        # Check permission
        if permission_lower != "none" and permission_lower not in all_permissions:
            invalid_permission_count += 1
            invalid_permissions.add(permission)
        
        # Check role
        if role_lower != "none" and role_lower not in all_roles:
            invalid_role_count += 1
            invalid_roles.add(role)

# Output results
print("E6H_MAX")
print(f"Hallucination Ratio {invalid_permission_count/500} in 'permission' column.")
print(f"Hallucination Ratio {invalid_role_count/500} in 'role' column.\n")

print("List of invalid permissions:")
for perm in sorted(invalid_permissions, key=lambda x: x.lower()):
    print(f"- {perm}")

print("\nList of invalid roles:")
for r in sorted(invalid_roles, key=lambda x: x.lower()):
    print(f"- {r}")
