import json
import csv

# Load JSON data from a file, ED_AzureStorage.txt or ED_Entra.txt
with open('ED_YYY.txt', 'r') as f:
    data = json.load(f)

# Open CSV file for writing
with open('RoleSizes_YYY.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(['role', 'size'])  # Header row

    # Write each role and count of permissions
    for item in data:
        role = item.get('role', 'Unknown')
        permissions = item.get('permissions', [])
        writer.writerow([role, len(permissions)])

print("CSV file created successfully.")