# LLM-based Permission Request Processing

This repository contains data and evaluation scripts used for a scientific publication. Once the paper is published, a link to the publication will be provided here.
In this README file, contents of this publication are referenced.

The article explores the use of Large Language Models (LLMs) for translating natural-language permission requests into RBAC permissions and roles.
To illustrate this, assume that an employee sends a permission request "I need to start the database" to an LLM.
In the ideal scenario, the LLM: 

1. Returns exactly the permission required to start the database.
2. Suggests a role that includes this permission.

## Overview

In our study, we conducted a series of experiments to quantitatively evaluate how model size and document embeddings influence an LLM's ability to translate permission requests into the corresponding permissions and roles (see Section 4 of the publication).
Also, we conducted experiments to evaluate the impact of a hybrid approach that combines a LLM-based permission translation with a role-search algorithm (see Section 5 of the publication).

The following list summarizes our experiment setup:

LLM-Only Experiments:
1. **E1**: Dataset A, Large Model, Document Embedding -> Allows LLM to lookup existing permissions and roles
2. **E2**: Dataset A, Small Model, Document Embedding -> Allows LLM to lookup existing permissions and roles
3. **E3**: Dataset A, Large Model, No Document Embedding
4. **E4**: Dataset A, Small Model, No Document Embedding
5. **E5**: Dataset B, Large Model, Document Embedding -> Allows LLM to lookup existing permissions and roles
6. **E6**: Dataset B, Small Model, Document Embedding -> Allows LLM to lookup existing permissions and roles
7. **E7**: Dataset B, Large Model, No Document Embedding
8. **E8**: Dataset B, Small Model, No Document Embedding

Hybrid Experiments:

9. **E1H_MIN**: Dataset A, Large Model, MIN Version of algorithm
10. **E1H_MAX**: Dataset A, Large Model, MAX Version of algorithm
11. **E2H_MIN**: Dataset A, Small Model, MIN Version of algorithm
12. **E2H_MAX**: Dataset A, Small Model, MAX Version of algorithm
13. **E5H_MIN**: Dataset B, Large Model, MIN Version of algorithm
14. **E5H_MAX**: Dataset B, Large Model, MAX Version of algorithm
15. **E6H_MIN**: Dataset B, Small Model, MIN Version of algorithm
16. **E6H_MAX**: Dataset B, Small Model, MAX Version of algorithm

Experiments 1-8 use LLMs to generate both permission translations and role suggestions.
Experiments 9-16 copy the permission translations from the LLM-Only experiments.
For example, E5H_MIN copies the translated permission from E5.
However, instead of letting an LLM suggest a role, we apply an Algorithm to perform a structured search for a role (see Subsection 5.1 of the publication).

There are two different version of the algorithm:

MIN Version: Traverse the enterprise RBAC document and return the smallest role that contains the permission translated by the LLM.

MAX Version: Traverse the enterprise RBAC document and return the largest role that contains the permission translated by the LLM.

Both algorithm versions are covered by the FindRole algorithm, but with a different input parameter.

## Data Provided to an LLM

Each LLM-Only experiment involved prompting the LLM with:

1. A **System Prompt** to instruct the LLM on how to process permission requests.
2. A set of **User Prompts** simulating permission requests in natural language.

Sometimes (E1,E2,E5,E6), the LLM also received:

3. An **Enterprise RBAC Structure** (referred to as the "Enterprise Document" in the paper), to look up existing roles, permission names, and their assignments.
This RBAC Structure is also used by the FindRole algorithm to detect a role that contains a specific permission.

## Repository Structure

### System Prompts (see /src/system_prompts)

Each txt file contains a single system prompt, which was used for two different experiments.
The filename suffix indicates which experiments the prompt was used in (e.g., *SystemPrompt_E1E2.txt* was used in the LLM-Only experiments E1 and E2).

### User Prompts (see /data/user_prompts)

Each file contains 100 simulated permission requests. These were transformed from existing permission descriptions found in Microsoft repositories:

- *UserPrompts_Entra.txt* contains permission requests which are based on permission descriptions found in the **Microsoft Entra built-in roles**.
- *UserPrompts_AzureStorage.txt* contains permission requests which are based on permission descriptions found in the **Azure built-in roles for Storage**.

Example transformation:
The original permission description "Create and manage backup jobs" was transformed to the permission request "I need to create and manage backup jobs."
The detailed transformation process is described in Subsection 4.1 of the publication (Data Preprocessing: Creating Permission Requests).

### RBAC Structures (see /data/RBAC_structure)

These two JSON-structured text files represent role-to-permission mappings from the same two data sources:

- *ED_Entra.txt* contains the RBAC structure of the **Microsoft Entra built-in roles**.
- *ED_AzureStorage.txt* contains the RBAC structure of the **Azure built-in roles for Storage**.

These files were used...
- as document embeddings provided to LLMs in some experiments.
- in the FindRole algorithm (hybrid approach!), to find a role that contains the translated permission.

See Subsection 4.1 (Data Preprocessing: Creating Enterprise Documents) for more information on how we created these RBAC structures).

### Outputs and Evaluation (see /data/output)

This directory contains two sub-directories: /LLM-Only contains the permission and role suggestions solely generated by LLMs.
The file names indicate the corresponding experiments (e.g., *Output_E1.csv* describes the results of experiment E1).

The subdirectory /Hybrid contains the output files from our hybrid experiments. While the permission translations are copied from the experiments that can be found in the /LLM-Only subdirectory, the role suggestions were created by applying the FindRole algorithm. The file names indicate the corresponding experiments (e.g., *Output_EH1_MAX.csv* describes the results of applying the RoleFind algorithm with boolean parameter POLP = False and using the permission translations from experiment E1).

### Request-to-Permission Mapping (see /data/request_permission_mappings)

Each file contains a ground-truth mapping between user prompts and the corresponding permission names.

- *SolutionMapping_Entra.csv* contains a mapping between the user prompts from *UserPrompts_Entra.txt* and permissions from the **Microsoft Entra built-in roles**.
- *SolutionMapping_AzureStorage.csv* contains a mapping between user prompts from *UserPrompts_AzureStorage.txt* and permissions from the **Azure built-in roles for Storage**.

### Evaluation Scripts (see /src/evaluation_scripts)

Python scripts which helped us to evaluate the performance of our output files. The specific evaluation metrics are described in Section 3 of the paper.
Note that:

- the Hallucination_Calculator.py calculates the PHall and RHall values.
- the Modesty_Calculator.py calculates the PMod and RMod values.
- the Precision_Calculator.py calculates the PPrec and RPrec values.
- the RoleSize_Creator.py is a helper function that creates a new csv file, required for the Polp_Calculator.py to run.
- the PA_Calculator.py creates a new csv file per run, it calculates the PAcc values.
- the RA_Calculator.py creates a new csv file per run, it calculates the RAcc values.
- the Polp_Calculator.py creates a new csv file per run. This script requires you to run the RA_Calculator.py and the RoleSize_Creator.py in advance. Calculates the PoLPV values.
- the PA_Wildcard_Calculator_Azure.py and PA_Wildcard_Calculator_Entra.py require the output generated by PA_Calculator.py and add the wildcard logics of the respective datasets to the permission accuracy evaluation (see Section 6 for more information on wildcard logics).
- the RA_Wildcard_Calculator adds wildcard logics to the role accuracy evaluation (see Section 6 for more information on wildcard logics).

For more information on how to run the scripts, check below.
 
### FindRole (see /src/FindRole)

Includes a Python script that implements the FindRole Algorithm as introduced in Subsection 5.1.

## How to Run the Evaluation Scripts?

1. **Hallucination_Calculator.py**: Simply change to this directory via command line and run the command *python .\Hallucination_Calculator.py*
2. **Modesty_Calculator.py**: Simply change to this directory via command line and run the command *python .\Modesty_Calculator.py*
3. **Precision_Calculator.py**: Simply change to this directory via command line and run the command *python .\Precision_Calculator.py*
4. **RoleSize_Creator.py**: Change to this directory via command line and run the command *python .\RoleSize_Creator.py* -> Important: For each run (2 runs in total), adjust *ED_YYY.txt* and *RoleSizes_YYY.csv* -> As a result, for each data set a new CSV file is created that shows the cardinality of all roles.
5. **PA_Calculator.py**: Change to this directory via command line and run the command *python .\PA_Calculator.py* -> Important: For each run (8 runs in total as the permission translations do not change for the hybrid experiments), adjust *Output_EX.csv*, *SolutionMapping_YYY.csv* and *Accuracy_EX.csv*. Executing this file returns a new output file. Via Excel, you can count how often the permission was translated correctly. Afterwards, divide this number by 500 (total number of permission translations).
6. **RA_Calculator.py**: Change to this directory via command line and run the command *python .\RA_Calculator.py* -> Important: For each run (16 runs in total), adjust *Output_EX.csv* and *RoleAccuracy_EX.csv*. You may also have to adjust *ExperimentType*, *SolutionMapping_YYY.csv* and *ED_YYY.txt*. Executing this file returns a new output file. Via Excel, you can count how often a correct role was suggested. Afterwards, divide this number by 500 (total number of permission translations).
7. **Polp_Calculator.py**: Change to this directory and run the command *python .\Polp_Calculator.py* -> Important: For each run (16 runs in total), adjust *RoleAccuracy_EX.csv* and *Polp_EX.csv*. You may also have to adjust *ExperimentType*, *RoleSizes_YYY.csv* and *ED_YYY.txt*. Executing this file returns a new output file. Via Excel, for each **role-accurate row**, you can now calculate (A) the suggested_role_size - 1 and (B) the smallest_fitting_role_size - 1. Then, sum up all values of (A) and (B) independently and afterwards divide the sum of (A) through the sum of (B) values.
8. **PA_Wildcard_Calculator_Azure.py**: Change to this directory via command line and run the command *python .\PA_Wildcard_Calculator_Azure.py* -> Important: For each run (4 runs in total), adjust *Accuracy_EX.csv*. Executing this file directly outputs which permission requests were translated correctly using the wildcard logics of Microsoft Azure. Add this number to the number of correct permission translations found by the PA_Calculator.py file, and then divide the sum by 500 (total number of permission translations) to retrieve the total share of permission translations which were translated correctly using the wildcard logics of Microsoft Azure.
9. **PA_Wildcard_Calculator_Entra.py**: Change to this directory via command line and run the command *python .\PA_Wildcard_Calculator_Entra.py* -> Important: For each run (4 runs in total), adjust *Accuracy_EX.csv*. Executing this file directly outputs which permission requests were translated correctly using the wildcard logics of Microsoft Entra. Add this number to the number of correct permission translations found by the PA_Calculator.py file, and then divide the sum by 500 (total number of permission translations) to retrieve the total share of permission translations which were translated correctly using the wildcard logics of Microsoft Entra.
10. **RA_Wildcard_Calculator.py**: Change to this directory via command line and run the command *python .\RA_Wildcard_Calculator.py* -> Important: For each run (16 runs in total), adjust *Output_EX.csv* and *RoleAccuracy_Wildcards__EX.csv*. You may also have to adjust *ExperimentType*, *SolutionMapping_YYY.csv* and *ED_YYY.txt*. Executing this file returns a new output file. Via Excel, you can count how often a correct role was suggested, and how often a correct role was suggested when additionally considering wildcard logics. Afterwards, divide the sum of both numbers by 500 (total number of permission translations) to retrieve the total share of correct role suggestions when applying wildcard logics.

## Licensing and Attribution

As described in this README file, this repository includes modified content derived from Microsoft documentations.
These modified files **retain their original licenses** and are subject to their respective terms:

### Azure built-in roles for Storage

Portions of this repository are derived from the [Azure built-in roles for Storage](https://github.com/MicrosoftDocs/azure-docs/blob/main/articles/role-based-access-control/built-in-roles/storage.md), provided by Microsoft and licensed under the [Create Commons Attribution 4.0 International (CC BY 4.0)](https://github.com/MicrosoftDocs/azure-docs/blob/main/LICENSE) license. (You can also check the file *LICENSE_AZURE_CC_BY_4_0* in this repository).

**Modifications have been made.**

© Microsoft Corporation.

### Microsoft Entra built-in roles

Portions of this repository are derived from the [Microsoft Entra built-in roles](https://github.com/MicrosoftDocs/entra-docs/blob/main/docs/identity/role-based-access-control/permissions-reference.md), provided by Microsoft and licensed under the [MIT](https://github.com/MicrosoftDocs/entra-docs/blob/main/LICENSE) license. (You can also check the file *LICENSE_ENTRA_MIT* in this repository).

**Modifications have been made.**

© Microsoft Corporation.

### License for Original Content

All other materials (which are the evaluation scripts, the system prompts and the FindRole implementation) are licensed under the MIT license (see LICENSE file in this repository).

## Notes

- The permission requests are **not actual user queries**, but generated prompts based on modified permission descriptions.
- The data sets as well as the code are provided for academic and research purposes only.
- The Microsoft data was retrieved on **April 17, 2025**. We will **not track or incorporate future updates** made to the original data sources.

## Contact

If you have any questions about the publication or the shown material, please contact max.niedermeier@tum.de

## Citation 

Paper is not yet published.
