##########################
## Inputs: ###############
## output_path: The path to the output file, which shows the requests, permission translations and role suggestions
## solution_mapping: A dictionary showing which permission actually belongs to what request
## enterprise_document: JSON-structured roles and assigned permissions
## azure_storage_wildcard_logic: True if using the azure storage dataset, False if using the entra dataset
## -> Based on this value, the wildcard logic when evaluating accuracy is adjusted accordingly
##########################
## Return: ###############
## A list of strings showing the evaluation results for each metric
## Order:
# "Permission Accuracy",
# "Permission Accuracy (Wildcard Logic)",
# "Role Accuracy",
# "Role Accuracy (Wildcard Logic)",
# "Permission Precision",
# "Role Precision",
# "Permission Hallucination",
# "Role Hallucination",
# "Permission Modesty",
# "Role Modesty",
# "PoLP Violation"
##########################

import csv
import pandas as pd
from collections import Counter
import fnmatch

def evaluation_runner(output_path, solution_mapping, enterprise_document, azure_storage_wildcard_logic):
    # As defined in the research article
    number_unique_requests = 100
    number_iterations = 5

    #########################################
    # Accuracy
    #########################################

    ########## Permission Accuracy

    # number of correct permission translations
    correct_permissions_sum = 0
    correct_permissions_sum_wildcard_logic = 0

    with open(output_path, newline='', encoding='utf-8') as output_file:
        reader = csv.DictReader(output_file, delimiter=';')
        for row in reader:
            # For case-insensitive comparisons
            request = row['request'].strip().lower()
            permission = row['permission'].strip().lower()

            # Correct translation according to solution_mapping
            # permission and request are lowercased and stripped. So are the entries in solution_mapping
            if permission == solution_mapping.get(request):
                correct_permissions_sum += 1
                correct_permissions_sum_wildcard_logic += 1
            #####################
            # It could happen that the required permission is contained in the translated wildcard permission
            # a wildcard that contains this permission
            #####################
            else:
                if azure_storage_wildcard_logic:
                    # translated permission is wildcard
                    if "*" in permission:
                        # get required permission, request is lowercased, all information in solution_mapping too
                        required_perm = solution_mapping.get(request)
                        # The translated wildcard permission contains the required permission (both lowercased and stripped)
                        if fnmatch.fnmatchcase(required_perm, permission):
                            correct_permissions_sum_wildcard_logic += 1
                else:
                    # translated permission is wildcard
                    if "allentities" in permission or "allproperties" in permission or "alltasks" in permission:
                        # get required permission, request is lowercased, all information in solution_mapping too
                        required_perm = solution_mapping.get(request)
                        # Split wildcard permission and required permission into list
                        wildcard_parts = permission.split('/')
                        required_parts = required_perm.split('/')
                        # Check if length matches
                        if len(wildcard_parts) == len(required_parts):
                            wildcard_matches_required_permission = True
                            for w, r in zip(wildcard_parts, required_parts):
                                # Match any value -> just continue
                                if w in {"allentities", "allproperties", "alltasks"}:
                                    continue
                                # Detect a mismatch, wildcard does not cover required permission
                                if w != r:
                                    wildcard_matches_required_permission = False
                            # No mismatches
                            if wildcard_matches_required_permission:
                                correct_permissions_sum_wildcard_logic += 1

    ########## Role Accuracy

    # number of correct role suggestions
    correct_roles_sum = 0
    correct_roles_sum_wildcard_logic = 0

    # For case-insensitive comparisons, strip and lowercase the enterprise_document
    # solution_mapping was already stripped and lowercased in main.py
    for entry in enterprise_document:
        entry["role"] = entry["role"].strip().lower()
        entry["permissions"] = [
            p.strip().lower() for p in entry["permissions"]
        ]

    # Create role_permissions which contains the permission set of each role
    # Both role names and permission names are already stripped and in lowercase
    role_permissions = {
        entry['role']: set(p for p in entry['permissions'])
        for entry in enterprise_document
    }

    # Sum up correct roles
    with open(output_path, newline='', encoding='utf-8') as output_file:
        reader = csv.DictReader(output_file, delimiter=';')
        for row in reader:
            correct_role = False
            correct_wildcard_role = False
            # need to strip and put in lowercase because it was also done before in the solution_mapping formatting
            # and in the role_permissions data
            request = row['request'].strip().lower()
            role = row['role'].strip().lower()
            # required_permission is stripped and in lowercase
            required_permission = solution_mapping.get(request)
            # Check if the required permission is contained in the suggested role
            # permissions, role and required_permission are lowercased and stripped
            permissions = role_permissions.get(role, set())
            if required_permission in permissions:
                correct_role = True
                correct_wildcard_role = True
            #####################
            # It could happen that the required permission is contained in a wildcard within the role
            #####################
            else:
                if azure_storage_wildcard_logic:
                    # Check if any permission in the role...
                    for perm in permissions:
                        # Which is a wildcard permission...
                        if "*" in perm:
                            # Covers the required permission, both lowercased and stripped (solution_mapping, role_permissions)
                            if fnmatch.fnmatchcase(required_permission, perm):
                                correct_wildcard_role = True
                else:
                    # Check if any permission in the role...
                    for perm in permissions:
                        # Which is a wildcard permission...
                        if "allentities" in perm or "allproperties" in perm or "alltasks" in perm:
                            # Split wildcard permission and required permission into list
                            wildcard_parts = perm.split('/')
                            required_parts = required_permission.split('/')
                            # Check if length matches
                            if len(wildcard_parts) == len(required_parts):
                                wildcard_matches_required_permission = True
                                for w, r in zip(wildcard_parts, required_parts):
                                    # Match any value -> just continue
                                    if w in {"allentities", "allproperties", "alltasks"}:
                                        continue
                                    # Detect a mismatch, wildcard does not cover required permission
                                    if w != r:
                                        wildcard_matches_required_permission = False
                                # No mismatches
                                if wildcard_matches_required_permission:
                                    correct_wildcard_role = True

            if correct_role:
                correct_roles_sum += 1
            if correct_wildcard_role:
                correct_roles_sum_wildcard_logic += 1

    #########################################
    # Precision
    #########################################

    df = pd.read_csv(output_path, delimiter=';')

    # Normalize request, permission and roles
    # permissions and roles are already written in lowercase and stripped
    df['request'] = df['request'].str.strip().str.lower()
    df['permission'] = df['permission'].str.strip().str.lower()
    df['role'] = df['role'].str.strip().str.lower()

    # Initialize result counters
    precision_permission_sum = 0
    precision_role_sum = 0

    # Group by request
    for request, group in df.groupby('request'):
        # For each request, count all the translated permissions and suggested roles, including none
        permission_counter = Counter(group['permission'])
        role_counter = Counter(group['role'])

        # Get the most common permission count -> most_common(1) _> single most common item
        # -> [0] first (permission, count) tuple (most common permission) -> [1] selects count
        most_common_permission_count = permission_counter.most_common(1)[0][1]
        # According to metrics, always add the (most common / number of iterations) e.g. 4/5 or 3/5
        precision_permission_sum += most_common_permission_count / number_iterations

        # Get the most common role count -> most_common(1) _> single most common item
        # -> [0] first (role, count) tuple (most common role) -> [1] selects count
        most_common_role_count = role_counter.most_common(1)[0][1]
        # According to metrics, always add the (most common / number of iterations) e.g. 4/5 or 3/5
        precision_role_sum += most_common_role_count / number_iterations

    #########################################
    # Hallucination
    #########################################

    # Create role and permission sets for lookup (in lowercase and stripped)
    all_roles = set()
    all_permissions = set()

    # Entries in enterprise_document are already stripped and in lowercase
    for entry in enterprise_document:
        all_roles.add(entry["role"])
        all_permissions.update([p for p in entry["permissions"]])

    # Initialize result counters
    invalid_permission_count = 0
    invalid_role_count = 0

    # Read CSV and process
    with open(output_path, "r", newline='', encoding="utf-8") as output_file:
        reader = csv.DictReader(output_file, delimiter=";")
        for row in reader:
            # Strip and lowercase for case-insensitive comparison
            permission = row["permission"].strip().lower()
            role = row["role"].strip().lower()

            # Check permission
            if permission != "none" and permission not in all_permissions:
                invalid_permission_count += 1

            # Check role (lowercased comparison)
            if role != "none" and role not in all_roles:
                invalid_role_count += 1

    #########################################
    # Modesty
    #########################################

    # Initialize result counters
    none_in_permission = 0
    none_in_role = 0

    with open(output_path, mode='r', newline='', encoding='utf-8') as output_file:
        reader = csv.DictReader(output_file, delimiter=';')

        # Simply count how often NONE appears -> Strip and lowercase for case-insensitive comparison
        for row in reader:
            if row['permission'].strip().lower() == "none":
                none_in_permission += 1
            if row['role'].strip().lower() == "none":
                none_in_role += 1

    #########################################
    # Principle of Least Privilege -> Does not yet consider wildcards in this publication!
    #########################################

    # dict of role sizes -> in lowercase and stripped
    role_sizes = {}

    # fill list of role sizes
    for entry in enterprise_document:
        role = entry["role"]
        role_sizes[role] = role_sizes.get(role, 0) + len(entry["permissions"])

    additional_perms_role_accurate = 0
    additional_perms_role_accurate_optimal = 0

    with open(output_path, newline='', encoding='utf-8') as output_file:
        reader = csv.DictReader(output_file, delimiter=';')
        for row in reader:
            correct_role = False
            # need to strip and put in lowercase because it was also done before in the solution_mapping formatting
            # and in the role_permissions data
            request = row['request'].strip().lower()
            role = row['role'].strip().lower()
            # required_permission is stripped and in lowercase
            required_permission = solution_mapping.get(request)
            # Check if the required permission is contained in the suggested role
            # permissions, role and required_permissions are lowercased and stripped
            permissions = role_permissions.get(role, set())
            if required_permission in permissions:
                correct_role = True
            if correct_role:
                # Add additional permissions of the correct, suggested role
                additional_perms_role_accurate += (role_sizes.get(role) - 1)
                # Search sizes of all correct roles
                # Again, required_permission, role and permissions are all lowercased and stripped
                valid_sizes = []
                for role, permissions in role_permissions.items():
                    # required permission is directly contained in the role
                    if required_permission in permissions:
                        # -> add size of this role
                        valid_sizes.append(role_sizes.get(role))
                # Add additional permissions of the smallest correct role
                additional_perms_role_accurate_optimal += (min(valid_sizes) - 1)

    #########################################

    row = [
        # Share of all correct permission translations
        str(correct_permissions_sum / (number_unique_requests * number_iterations)),
        str(correct_permissions_sum_wildcard_logic / (number_unique_requests * number_iterations)),
        # Share of all correct role suggestions
        str(correct_roles_sum / (number_unique_requests * number_iterations)),
        str(correct_roles_sum_wildcard_logic / (number_unique_requests * number_iterations)),
        # Average Precision values across all unique requests
        str(precision_permission_sum / number_unique_requests),
        str(precision_role_sum / number_unique_requests),
        # Share of all hallucinated  values
        str(invalid_permission_count / (number_unique_requests * number_iterations)),
        str(invalid_role_count / (number_unique_requests * number_iterations)),
        # Share of all none values
        str(none_in_permission / (number_unique_requests * number_iterations)),
        str(none_in_role / (number_unique_requests * number_iterations)),
        # Across all requests with a correct role suggestion, sum up additional permissions
        # Across all requests with a correct role suggestion, sum up additional permissions of  optimal role suggestions
        # Then, divide A through B
        str(additional_perms_role_accurate / additional_perms_role_accurate_optimal),
    ]

    return row