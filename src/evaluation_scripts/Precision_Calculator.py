import pandas as pd
from collections import Counter

# Read the CSV file
df = pd.read_csv('output_E1.csv', delimiter=';')

# Initialize sums
permission_sum = 0
role_sum = 0

# Group by 'prompt'
for prompt, group in df.groupby('request'):
    # Count permissions and roles for this prompt
    permission_counter = Counter(group['permission'])
    role_counter = Counter(group['role'])

    # Get the most common permission count
    most_common_permission_count = permission_counter.most_common(1)[0][1]
    permission_sum += most_common_permission_count / 5  # Divide by 5

    # Get the most common role count
    most_common_role_count = role_counter.most_common(1)[0][1]
    role_sum += most_common_role_count / 5  # Divide by 5

# Print the results
print("E1")
print(f"Precision Ratio: {permission_sum/100}")
print(f"Precision Ratio: {role_sum/100}")

# Read the CSV file
df = pd.read_csv('output_E2.csv', delimiter=';')

# Initialize sums
permission_sum = 0
role_sum = 0

# Group by 'prompt'
for prompt, group in df.groupby('request'):
    # Count permissions and roles for this prompt
    permission_counter = Counter(group['permission'])
    role_counter = Counter(group['role'])

    # Get the most common permission count
    most_common_permission_count = permission_counter.most_common(1)[0][1]
    permission_sum += most_common_permission_count / 5  # Divide by 5

    # Get the most common role count
    most_common_role_count = role_counter.most_common(1)[0][1]
    role_sum += most_common_role_count / 5  # Divide by 5

# Print the results
print("E2")
print(f"Precision Ratio: {permission_sum/100}")
print(f"Precision Ratio: {role_sum/100}")

# Read the CSV file
df = pd.read_csv('output_E3.csv', delimiter=';')

# Initialize sums
permission_sum = 0
role_sum = 0

# Group by 'prompt'
for prompt, group in df.groupby('request'):
    # Count permissions and roles for this prompt
    permission_counter = Counter(group['permission'])
    role_counter = Counter(group['role'])

    # Get the most common permission count
    most_common_permission_count = permission_counter.most_common(1)[0][1]
    permission_sum += most_common_permission_count / 5  # Divide by 5

    # Get the most common role count
    most_common_role_count = role_counter.most_common(1)[0][1]
    role_sum += most_common_role_count / 5  # Divide by 5

# Print the results
print("E3")
print(f"Precision Ratio: {permission_sum/100}")
print(f"Precision Ratio: {role_sum/100}")

# Read the CSV file
df = pd.read_csv('output_E4.csv', delimiter=';')

# Initialize sums
permission_sum = 0
role_sum = 0

# Group by 'prompt'
for prompt, group in df.groupby('request'):
    # Count permissions and roles for this prompt
    permission_counter = Counter(group['permission'])
    role_counter = Counter(group['role'])

    # Get the most common permission count
    most_common_permission_count = permission_counter.most_common(1)[0][1]
    permission_sum += most_common_permission_count / 5  # Divide by 5

    # Get the most common role count
    most_common_role_count = role_counter.most_common(1)[0][1]
    role_sum += most_common_role_count / 5  # Divide by 5

# Print the results
print("E4")
print(f"Precision Ratio: {permission_sum/100}")
print(f"Precision Ratio: {role_sum/100}")

# Read the CSV file
df = pd.read_csv('output_E5.csv', delimiter=';')

# Initialize sums
permission_sum = 0
role_sum = 0

# Group by 'prompt'
for prompt, group in df.groupby('request'):
    # Count permissions and roles for this prompt
    permission_counter = Counter(group['permission'])
    role_counter = Counter(group['role'])

    # Get the most common permission count
    most_common_permission_count = permission_counter.most_common(1)[0][1]
    permission_sum += most_common_permission_count / 5  # Divide by 5

    # Get the most common role count
    most_common_role_count = role_counter.most_common(1)[0][1]
    role_sum += most_common_role_count / 5  # Divide by 5

# Print the results
print("E5")
print(f"Precision Ratio: {permission_sum/100}")
print(f"Precision Ratio: {role_sum/100}")

# Read the CSV file
df = pd.read_csv('output_E6.csv', delimiter=';')

# Initialize sums
permission_sum = 0
role_sum = 0

# Group by 'prompt'
for prompt, group in df.groupby('request'):
    # Count permissions and roles for this prompt
    permission_counter = Counter(group['permission'])
    role_counter = Counter(group['role'])

    # Get the most common permission count
    most_common_permission_count = permission_counter.most_common(1)[0][1]
    permission_sum += most_common_permission_count / 5  # Divide by 5

    # Get the most common role count
    most_common_role_count = role_counter.most_common(1)[0][1]
    role_sum += most_common_role_count / 5  # Divide by 5

# Print the results
print("E6")
print(f"Precision Ratio: {permission_sum/100}")
print(f"Precision Ratio: {role_sum/100}")

# Read the CSV file
df = pd.read_csv('output_E7.csv', delimiter=';')

# Initialize sums
permission_sum = 0
role_sum = 0

# Group by 'prompt'
for prompt, group in df.groupby('request'):
    # Count permissions and roles for this prompt
    permission_counter = Counter(group['permission'])
    role_counter = Counter(group['role'])

    # Get the most common permission count
    most_common_permission_count = permission_counter.most_common(1)[0][1]
    permission_sum += most_common_permission_count / 5  # Divide by 5

    # Get the most common role count
    most_common_role_count = role_counter.most_common(1)[0][1]
    role_sum += most_common_role_count / 5  # Divide by 5

# Print the results
print("E7")
print(f"Precision Ratio: {permission_sum/100}")
print(f"Precision Ratio: {role_sum/100}")

# Read the CSV file
df = pd.read_csv('output_E8.csv', delimiter=';')

# Initialize sums
permission_sum = 0
role_sum = 0

# Group by 'prompt'
for prompt, group in df.groupby('request'):
    # Count permissions and roles for this prompt
    permission_counter = Counter(group['permission'])
    role_counter = Counter(group['role'])

    # Get the most common permission count
    most_common_permission_count = permission_counter.most_common(1)[0][1]
    permission_sum += most_common_permission_count / 5  # Divide by 5

    # Get the most common role count
    most_common_role_count = role_counter.most_common(1)[0][1]
    role_sum += most_common_role_count / 5  # Divide by 5

# Print the results
print("E8")
print(f"Precision Ratio: {permission_sum/100}")
print(f"Precision Ratio: {role_sum/100}")