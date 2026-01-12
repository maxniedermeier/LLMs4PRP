##########################
## Inputs: ###############
## response_permission: The request-to-permission translation by the LLM
## PA: json-structured roles, showing which roles contain what permissions
## POLP: If true -> Return smallest role containing the response_permission, if false -> Return largest role
##########################
## Return: ###############
## NONE if the permission is none or hallucinated.
## The smallest or largest role that contains the translated  permission.
##########################

def find_role(response_permission, PA, POLP):
    # strip the permission and lowercase it in order to enable a case-insensitive comparison later
    response_permission = response_permission.strip().lower()

    # Case 1: The LLM may return none instead of a permission
    # If permission_result is none -> Return NONE
    if response_permission == "none":
        return "NONE"

    # Case 2: The LLM may return a permission that does not exist
    # Check if permission exists in any of the roles
    permission_exists = any(
        # strip and lowercase the permissions of each role to have a case-insensitive comparison
        response_permission in [p.strip().lower() for p in role.get("permissions", [])]
        for role in PA
    )
    # If not, the permission is hallucinated -> Return NONE
    if not permission_exists:
        return "NONE"

    # Case 3: The permission exists
    # Find all role candidates in roles that contain this permission
    candidate_roles = []
    for role in PA:
        add_role = False
        perms = set(p.strip().lower() for p in role["permissions"])
        # If response_permission (lowercase, stripped) is directly contained in the role perms (lowercase, stripped)
        if response_permission in perms:
            # Then consider this role as a candidate
            add_role = True
        if add_role:
            candidate_roles.append(role)

    # Helper to compute the role sizes
    def role_size(role):
        perms = [p.strip().lower() for p in role.get("permissions", [])]
        return len(perms)

    # The smallest role (fewest permissions)
    smallest_role = min(candidate_roles, key=lambda r: role_size(r))
    # The largest role (most permissions)
    largest_role = max(candidate_roles, key=lambda r: role_size(r))

    # Based on the bool POLP, either return the smallest role or the largest role
    if POLP:
        return smallest_role.get("role")
    else:
        return largest_role.get("role")