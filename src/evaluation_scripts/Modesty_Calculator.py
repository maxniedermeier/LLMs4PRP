import csv

# Initialize counters
none_in_permission = 0
none_in_role = 0

# Open the CSV file
with open('../../data/output/LLM-Only/Output_E1.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')  # delimiter is ;
    
    for row in reader:
        # Check if 'NONE' appears
        if row['permission'].strip().lower() == 'none':
            none_in_permission += 1
        if row['role'].strip().lower() == 'none':
            none_in_role += 1

print("E1")
print(f"NONE Ratio {none_in_permission/500} in 'permission' column.")
print(f"NONE Ratio {none_in_role/500} in 'role' column.")

# Initialize counters
none_in_permission = 0
none_in_role = 0

# Open the CSV file
with open('../../data/output/LLM-Only/Output_E2.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')  # delimiter is ;
    
    for row in reader:
        # Check if 'NONE' appears
        if row['permission'].strip().lower() == 'none':
            none_in_permission += 1
        if row['role'].strip().lower() == 'none':
            none_in_role += 1

print("E2")
print(f"NONE Ratio {none_in_permission/500} in 'permission' column.")
print(f"NONE Ratio {none_in_role/500} in 'role' column.")

# Initialize counters
none_in_permission = 0
none_in_role = 0

# Open the CSV file
with open('../../data/output/LLM-Only/Output_E3.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')  # delimiter is ;
    
    for row in reader:
        # Check if 'NONE' appears
        if row['permission'].strip().lower() == 'none':
            none_in_permission += 1
        if row['role'].strip().lower() == 'none':
            none_in_role += 1

print("E3")
print(f"NONE Ratio {none_in_permission/500} in 'permission' column.")
print(f"NONE Ratio {none_in_role/500} in 'role' column.")

# Initialize counters
none_in_permission = 0
none_in_role = 0

# Open the CSV file
with open('../../data/output/LLM-Only/Output_E4.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')  # delimiter is ;
    
    for row in reader:
        # Check if 'NONE' appears
        if row['permission'].strip().lower() == 'none':
            none_in_permission += 1
        if row['role'].strip().lower() == 'none':
            none_in_role += 1

print("E4")
print(f"NONE Ratio {none_in_permission/500} in 'permission' column.")
print(f"NONE Ratio {none_in_role/500} in 'role' column.")

# Initialize counters
none_in_permission = 0
none_in_role = 0

# Open the CSV file
with open('../../data/output/LLM-Only/Output_E5.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')  # delimiter is ;
    
    for row in reader:
        # Check if 'NONE' appears
        if row['permission'].strip().lower() == 'none':
            none_in_permission += 1
        if row['role'].strip().lower() == 'none':
            none_in_role += 1

print("E5")
print(f"NONE Ratio {none_in_permission/500} in 'permission' column.")
print(f"NONE Ratio {none_in_role/500} in 'role' column.")

# Initialize counters
none_in_permission = 0
none_in_role = 0

# Open the CSV file
with open('../../data/output/LLM-Only/Output_E6.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')  # delimiter is ;
    
    for row in reader:
        # Check if 'NONE' appears
        if row['permission'].strip().lower() == 'none':
            none_in_permission += 1
        if row['role'].strip().lower() == 'none':
            none_in_role += 1

print("E6")
print(f"NONE Ratio {none_in_permission/500} in 'permission' column.")
print(f"NONE Ratio {none_in_role/500} in 'role' column.")

# Initialize counters
none_in_permission = 0
none_in_role = 0

# Open the CSV file
with open('../../data/output/LLM-Only/Output_E7.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')  # delimiter is ;
    
    for row in reader:
        # Check if 'NONE' appears
        if row['permission'].strip().lower() == 'none':
            none_in_permission += 1
        if row['role'].strip().lower() == 'none':
            none_in_role += 1

print("E7")
print(f"NONE Ratio {none_in_permission/500} in 'permission' column.")
print(f"NONE Ratio {none_in_role/500} in 'role' column.")

# Initialize counters
none_in_permission = 0
none_in_role = 0

# Open the CSV file
with open('../../data/output/LLM-Only/Output_E8.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')  # delimiter is ;
    
    for row in reader:
        # Check if 'NONE' appears
        if row['permission'].strip().lower() == 'none':
            none_in_permission += 1
        if row['role'].strip().lower() == 'none':
            none_in_role += 1

print("E8")
print(f"NONE Ratio {none_in_permission/500} in 'permission' column.")
print(f"NONE Ratio {none_in_role/500} in 'role' column.")

###################################################
# Now doing the same thing for the hybrid outputs #
###################################################

# Initialize counters
none_in_permission = 0
none_in_role = 0

# Open the CSV file
with open('../../data/output/Hybrid/Output_E1H_MIN.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')  # delimiter is ;
    
    for row in reader:
        # Check if 'NONE' appears
        if row['permission'].strip().lower() == 'none':
            none_in_permission += 1
        if row['role'].strip().lower() == 'none':
            none_in_role += 1

print("E1H_MIN")
print(f"NONE Ratio {none_in_permission/500} in 'permission' column.")
print(f"NONE Ratio {none_in_role/500} in 'role' column.")

# Initialize counters
none_in_permission = 0
none_in_role = 0

# Open the CSV file
with open('../../data/output/Hybrid/Output_E1H_MAX.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')  # delimiter is ;
    
    for row in reader:
        # Check if 'NONE' appears
        if row['permission'].strip().lower() == 'none':
            none_in_permission += 1
        if row['role'].strip().lower() == 'none':
            none_in_role += 1

print("E1H_MAX")
print(f"NONE Ratio {none_in_permission/500} in 'permission' column.")
print(f"NONE Ratio {none_in_role/500} in 'role' column.")

# Initialize counters
none_in_permission = 0
none_in_role = 0

# Open the CSV file
with open('../../data/output/Hybrid/Output_E2H_MIN.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')  # delimiter is ;
    
    for row in reader:
        # Check if 'NONE' appears
        if row['permission'].strip().lower() == 'none':
            none_in_permission += 1
        if row['role'].strip().lower() == 'none':
            none_in_role += 1

print("E2H_MIN")
print(f"NONE Ratio {none_in_permission/500} in 'permission' column.")
print(f"NONE Ratio {none_in_role/500} in 'role' column.")

# Initialize counters
none_in_permission = 0
none_in_role = 0

# Open the CSV file
with open('../../data/output/Hybrid/Output_E2H_MAX.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')  # delimiter is ;
    
    for row in reader:
        # Check if 'NONE' appears
        if row['permission'].strip().lower() == 'none':
            none_in_permission += 1
        if row['role'].strip().lower() == 'none':
            none_in_role += 1

print("E2H_MAX")
print(f"NONE Ratio {none_in_permission/500} in 'permission' column.")
print(f"NONE Ratio {none_in_role/500} in 'role' column.")

# Initialize counters
none_in_permission = 0
none_in_role = 0

# Open the CSV file
with open('../../data/output/Hybrid/Output_E5H_MIN.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')  # delimiter is ;
    
    for row in reader:
        # Check if 'NONE' appears
        if row['permission'].strip().lower() == 'none':
            none_in_permission += 1
        if row['role'].strip().lower() == 'none':
            none_in_role += 1

print("E5H_MIN")
print(f"NONE Ratio {none_in_permission/500} in 'permission' column.")
print(f"NONE Ratio {none_in_role/500} in 'role' column.")

# Initialize counters
none_in_permission = 0
none_in_role = 0

# Open the CSV file
with open('../../data/output/Hybrid/Output_E5H_MAX.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')  # delimiter is ;
    
    for row in reader:
        # Check if 'NONE' appears
        if row['permission'].strip().lower() == 'none':
            none_in_permission += 1
        if row['role'].strip().lower() == 'none':
            none_in_role += 1

print("E5H_MAX")
print(f"NONE Ratio {none_in_permission/500} in 'permission' column.")
print(f"NONE Ratio {none_in_role/500} in 'role' column.")

# Initialize counters
none_in_permission = 0
none_in_role = 0

# Open the CSV file
with open('../../data/output/Hybrid/Output_E6H_MIN.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')  # delimiter is ;
    
    for row in reader:
        # Check if 'NONE' appears
        if row['permission'].strip().lower() == 'none':
            none_in_permission += 1
        if row['role'].strip().lower() == 'none':
            none_in_role += 1

print("E6H_MIN")
print(f"NONE Ratio {none_in_permission/500} in 'permission' column.")
print(f"NONE Ratio {none_in_role/500} in 'role' column.")

# Initialize counters
none_in_permission = 0
none_in_role = 0

# Open the CSV file
with open('../../data/output/Hybrid/Output_E6H_MAX.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')  # delimiter is ;
    
    for row in reader:
        # Check if 'NONE' appears
        if row['permission'].strip().lower() == 'none':
            none_in_permission += 1
        if row['role'].strip().lower() == 'none':
            none_in_role += 1

print("E6H_MAX")
print(f"NONE Ratio {none_in_permission/500} in 'permission' column.")
print(f"NONE Ratio {none_in_role/500} in 'role' column.")
