import os
import shutil
import pandas as pd
import json
from find_role import find_role
from openpyxl import Workbook
import csv
from evaluation_runner import evaluation_runner

def main() -> None:
    # First, check if all the necessary data is available
    # If not, exit the program and print an error message
    # Note: Outputs of hybrid experiments are not necessary because the csv files are created later
    # System/user prompts are not necessary because they just show which prompts were used in the experiments

    # Get absolute path to main.py
    current_file = os.path.abspath(__file__)

    # Get project root directory
    project_root = os.path.dirname(os.path.dirname(current_file))

    # Define paths to each necessary file
    # Llm-only output files
    output_e1 = os.path.join(project_root, "data", "output", "llm_only", "output_e1.csv")
    output_e2 = os.path.join(project_root, "data", "output", "llm_only", "output_e2.csv")
    output_e3 = os.path.join(project_root, "data", "output", "llm_only", "output_e3.csv")
    output_e4 = os.path.join(project_root, "data", "output", "llm_only", "output_e4.csv")
    output_e5 = os.path.join(project_root, "data", "output", "llm_only", "output_e5.csv")
    output_e6 = os.path.join(project_root, "data", "output", "llm_only", "output_e6.csv")
    output_e7 = os.path.join(project_root, "data", "output", "llm_only", "output_e7.csv")
    output_e8 = os.path.join(project_root, "data", "output", "llm_only", "output_e8.csv")

    # enterprise document files
    enterprise_document_azure_storage = os.path.join(project_root, "data", "enterprise_documents", "enterprise_document_azure_storage.txt")
    enterprise_document_entra = os.path.join(project_root, "data", "enterprise_documents", "enterprise_document_entra.txt")

    # solution mapping files
    solution_mapping_azure_storage = os.path.join(project_root, "data", "solution_mappings", "solution_mapping_azure_storage.csv")
    solution_mapping_entra = os.path.join(project_root, "data", "solution_mappings", "solution_mapping_entra.csv")

    # Put the paths to the necessary files in a directory
    required_files = {
        "output_e1": output_e1,
        "output_e2": output_e2,
        "output_e3": output_e3,
        "output_e4": output_e4,
        "output_e5": output_e5,
        "output_e6": output_e6,
        "output_e7": output_e7,
        "output_e8": output_e8,
        "enterprise_document_azure_storage": enterprise_document_azure_storage,
        "enterprise_document_entra": enterprise_document_entra,
        "solution_mapping_azure_storage": solution_mapping_azure_storage,
        "solution_mapping_entra": solution_mapping_entra,
    }

    # Find missing files
    missing_files = [name for name, path in required_files.items() if not os.path.isfile(path)]

    if missing_files:
        print("There is at least one file missing:")
        for name in missing_files:
            print(f"  - {name}: {required_files[name]}")
        exit(1)

    # Next, check if evaluation_runner_output directory exists. If not -> error and exit
    evaluation_runner_output_directory = os.path.join(project_root, "data", "evaluation_runner_output")

    if not os.path.isdir(evaluation_runner_output_directory):
        print("The /data/evaluation_runner_output directory is missing.")
        exit(1)

    # Check if hybrid directory exists, if not -> error and exit.
    # # If yes -> empty the directory
    hybrid_directory = os.path.join(project_root, "data", "output", "hybrid")

    if not os.path.isdir(hybrid_directory):
        print("The /data/output/hybrid directory is missing.")
        exit(1)

    for entry in os.listdir(hybrid_directory):
        path = os.path.join(hybrid_directory, entry)

        if os.path.isfile(path) or os.path.islink(path):
            os.unlink(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)

    # Mapping showing which hybrid experiment files originate from what llm-only experiments
    experiment_mapping = [
        ("output_e1.csv", "output_e1h_min.csv"),
        ("output_e1.csv", "output_e1h_max.csv"),
        ("output_e2.csv", "output_e2h_min.csv"),
        ("output_e2.csv", "output_e2h_max.csv"),
        ("output_e5.csv", "output_e5h_min.csv"),
        ("output_e5.csv", "output_e5h_max.csv"),
        ("output_e6.csv", "output_e6h_min.csv"),
        ("output_e6.csv", "output_e6h_max.csv")
    ]

    # path to llm-only experiment outputs
    llm_only_directory = os.path.join(project_root, "data", "output", "llm_only")

    # Copy output of llm-only experiments into hybrid experiment output files
    # Then, empty the role column of the hybrid experiment output files

    for src_name, target_name in experiment_mapping:
        src_file = os.path.join(llm_only_directory, src_name)
        target_file = os.path.join(hybrid_directory, target_name)

        # Copy file
        shutil.copy2(src_file, target_file)

        # Load csv in pandas, the csv files use a semicolon as a delimiter
        df = pd.read_csv(target_file, sep=';')

        # Empty the role column
        df['role'] = ""

        # Write back to csv file
        df.to_csv(target_file, sep=';', index=False)

    # Next, we use the find_role.py script to algorithmically search for suitable roles
    # To use the find_role.py script, we need the enterprise documents
    with open(enterprise_document_azure_storage, encoding='utf-8') as ed_azure_storage_file:
        ed_azure_storage = json.load(ed_azure_storage_file)

    with open(enterprise_document_entra, encoding='utf-8') as ed_entra_file:
        ed_entra = json.load(ed_entra_file)

    # Loop through all the files in the /data/output/hybrid directory
    for filename in os.listdir(hybrid_directory):
        file_path = os.path.join(hybrid_directory, filename)
        # Load csv in pandas, the csv files use a semicolon as a delimiter
        df = pd.read_csv(file_path, sep=';')
        # First, define empty list of roles
        roles = []
        # Based on the filename, use different parameters!
        if filename == "output_e1h_min.csv":
            # For each permission, apply the find_roly.py script and add the result to roles
            for permission in df['permission']:
                role = find_role(permission, ed_azure_storage, True)
                roles.append(role)
        elif filename == "output_e1h_max.csv":
            for permission in df['permission']:
                role = find_role(permission, ed_azure_storage, False)
                roles.append(role)
        elif filename == "output_e2h_min.csv":
            for permission in df['permission']:
                role = find_role(permission, ed_azure_storage, True)
                roles.append(role)
        elif filename == "output_e2h_max.csv":
            for permission in df['permission']:
                role = find_role(permission, ed_azure_storage, False)
                roles.append(role)
        elif filename == "output_e5h_min.csv":
            for permission in df['permission']:
                role = find_role(permission, ed_entra, True)
                roles.append(role)
        elif filename == "output_e5h_max.csv":
            for permission in df['permission']:
                role = find_role(permission, ed_entra, False)
                roles.append(role)
        elif filename == "output_e6h_min.csv":
            for permission in df['permission']:
                role = find_role(permission, ed_entra, True)
                roles.append(role)
        elif filename == "output_e6h_max.csv":
            for permission in df['permission']:
                role = find_role(permission, ed_entra, False)
                roles.append(role)
        else:
            # Should never happen
            print("There was file found which does not follow the naming conventions of the hybrid experiments.")
            exit(1)
        # Update the role column
        df['role'] = roles
        # Write back to csv file
        df.to_csv(file_path, sep=';', index=False)

    # Empty the evaluation_runner_output directory
    for entry in os.listdir(evaluation_runner_output_directory):
        path = os.path.join(evaluation_runner_output_directory, entry)

        if os.path.isfile(path) or os.path.islink(path):
            os.unlink(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)

    # Create empty Excel file with metrics in each column
    evaluation_output = os.path.join(evaluation_runner_output_directory, "evaluation_output.xlsx")
    wb = Workbook()
    ws = wb.active

    # Static header list written in the first line of the Excel file
    metrics = [
        "",
        "Permission Accuracy",
        "Permission Accuracy (Wildcard Logic)",
        "Role Accuracy",
        "Role Accuracy (Wildcard Logic)",
        "Permission Precision",
        "Role Precision",
        "Permission Hallucination",
        "Role Hallucination",
        "Permission Modesty",
        "Role Modesty",
        "PoLP Violation"
    ]

    ws.append(metrics)

    # Add experiment evaluations in the following rows
    # evaluation_runner script receives path to output, solution_mapping and enterprise_document
    # Therefore, first open the solution_mappings and write contents into a dict
    sm_azure_storage = {}
    with open(solution_mapping_azure_storage, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=';')
        for line_num, row in enumerate(reader, start=2):
            prompt = row["prompt"].strip().lower()
            perm = row["permission"].strip().lower()
            # Build solution mapping dictionary
            sm_azure_storage[prompt] = perm

    sm_entra = {}
    with open(solution_mapping_entra, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=';')
        for line_num, row in enumerate(reader, start=2):
            prompt = row["prompt"].strip().lower()
            perm = row["permission"].strip().lower()
            # Build solution mapping dictionary
            sm_entra[prompt] = perm

    # evaluate e1 and add results to the Excel file
    row = evaluation_runner(output_e1, sm_azure_storage, ed_azure_storage, True)
    row = ["E1"] + row
    ws.append(row)

    # evaluate e2 and add results to the Excel file
    row = evaluation_runner(output_e2, sm_azure_storage, ed_azure_storage, True)
    row = ["E2"] + row
    ws.append(row)

    # evaluate e3 and add results to the Excel file
    row = evaluation_runner(output_e3, sm_azure_storage, ed_azure_storage, True)
    row = ["E3"] + row
    ws.append(row)

    # evaluate e4 and add results to the Excel file
    row = evaluation_runner(output_e4, sm_azure_storage, ed_azure_storage, True)
    row = ["E4"] + row
    ws.append(row)

    # evaluate e5 and add results to the Excel file
    row = evaluation_runner(output_e5, sm_entra, ed_entra, False)
    row = ["E5"] + row
    ws.append(row)

    # evaluate e6 and add results to the Excel file
    row = evaluation_runner(output_e6, sm_entra, ed_entra, False)
    row = ["E6"] + row
    ws.append(row)

    # evaluate e7 and add results to the Excel file
    row = evaluation_runner(output_e7, sm_entra, ed_entra, False)
    row = ["E7"] + row
    ws.append(row)

    # evaluate e8 and add results to the Excel file
    row = evaluation_runner(output_e8, sm_entra, ed_entra, False)
    row = ["E8"] + row
    ws.append(row)

    # evaluate e1h_min and add results to the Excel file
    row = evaluation_runner(os.path.join(hybrid_directory, "output_e1h_min.csv"), sm_azure_storage, ed_azure_storage, True)
    row = ["E1H_MIN"] + row
    ws.append(row)

    # evaluate e1h_max and add results to the Excel file
    row = evaluation_runner(os.path.join(hybrid_directory, "output_e1h_max.csv"), sm_azure_storage, ed_azure_storage, True)
    row = ["E1H_MAX"] + row
    ws.append(row)

    # evaluate e2h_min and add results to the Excel file
    row = evaluation_runner(os.path.join(hybrid_directory, "output_e2h_min.csv"), sm_azure_storage, ed_azure_storage, True)
    row = ["E2H_MIN"] + row
    ws.append(row)

    # evaluate e2h_max and add results to the Excel file
    row = evaluation_runner(os.path.join(hybrid_directory, "output_e2h_max.csv"), sm_azure_storage, ed_azure_storage, True)
    row = ["E2H_MAX"] + row
    ws.append(row)

    # evaluate e5h_min and add results to the Excel file
    row = evaluation_runner(os.path.join(hybrid_directory, "output_e5h_min.csv"), sm_entra, ed_entra, False)
    row = ["E5H_MIN"] + row
    ws.append(row)

    # evaluate e5h_max and add results to the Excel file
    row = evaluation_runner(os.path.join(hybrid_directory, "output_e5h_max.csv"), sm_entra, ed_entra, False)
    row = ["E5H_MAX"] + row
    ws.append(row)

    # evaluate e6h_min and add results to the Excel file
    row = evaluation_runner(os.path.join(hybrid_directory, "output_e6h_min.csv"), sm_entra, ed_entra, False)
    row = ["E6H_MIN"] + row
    ws.append(row)

    # evaluate e6h_max and add results to the Excel file
    row = evaluation_runner(os.path.join(hybrid_directory, "output_e6h_max.csv"), sm_entra, ed_entra, False)
    row = ["E6H_MAX"] + row
    ws.append(row)

    # save workbook
    wb.save(evaluation_output)

    print("Finished generating the evaluation file. Check: " + evaluation_output)
if __name__ == "__main__":
    main()