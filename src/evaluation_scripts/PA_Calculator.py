import csv

# File paths
input_file = '<input>.csv' # LLM-generated output as input
solution_file = '<solution>.csv' # Use a request-to-permission file here
output_file = '<output>.csv'  # Save output file and **manually check accuracy values**

# Read the solution file and build a mapping: request -> correct permission
solution_map = {}
with open(solution_file, newline='', encoding='utf-8') as sol_csv:
    reader = csv.DictReader(sol_csv, delimiter=';')
    print(reader.fieldnames)
    for row in reader:
        request = row['prompt'].strip().lower()
        permission = row['permission'].strip().lower()
        # If multiple permissions per request, store as set
        if request not in solution_map:
            solution_map[request] = set()
        solution_map[request].add(permission)

# Process the input file and check mappings
results = []
with open(input_file, newline='', encoding='utf-8') as inp_csv:
    reader = csv.DictReader(inp_csv, delimiter=';')
    print(reader.fieldnames)
    for row in reader:
        original_request = row['request'].strip()
        original_permission = row['permission'].strip()
        request = original_request.lower()
        permission = original_permission.lower()
        correct_permissions = solution_map.get(request, set())
        is_correct = permission in correct_permissions
        results.append({
            'request': original_request,
            'permission': original_permission,
            'is_correct': is_correct
        })

# Print results
for res in results:
    print(f"Request: {res['request']}\nPermission: {res['permission']}\nCorrect: {res['is_correct']}\n")

# Optional: Save results to a new CSV
with open(output_file, 'w', newline='', encoding='utf-8') as out_csv:
    fieldnames = ['request', 'permission', 'is_correct']
    writer = csv.DictWriter(out_csv, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()
    for res in results:
        writer.writerow(res)