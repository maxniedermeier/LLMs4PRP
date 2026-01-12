# LLM-based Permission Request Processing

This repository contains data and Python scripts used for a scientific publication. Once the paper is published, a link to the publication will be provided here.
In this README file, contents of this publication are referenced.

The article explores the use of Large Language Models (LLMs) for translating natural-language permission requests into RBAC permissions and roles.
To illustrate this, assume that an employee sends a permission request "I need to start the database" to an LLM.
In the ideal scenario, the LLM: 

1. Returns exactly the permission required to start the database.
2. Suggests a role that includes this permission.

## Overview

In our study, we conducted a series of experiments to quantitatively evaluate how model size and document embeddings influence an LLM's ability to translate permission requests into the corresponding permissions and roles (see Section 4 of the publication). Also, we conducted experiments to evaluate the impact of a hybrid approach that combines an LLM-based permission translation with a role-search algorithm (see Section 5 of the publication).

The following list summarizes our experiment setup:

LLM-Only Experiments:
1. **E1**: Dataset A, Large Model, Document Embedding -> Allows LLM to lookup existing permissions and roles
2. **E2**: Dataset A, Small Model, Document Embedding -> Allows LLM to lookup existing permissions and roles
3. **E3**: Dataset A, Large Model, No Document Embedding
4. **E4**: Dataset A, Small Model, No Document Embedding
5. **E5**: Dataset E, Large Model, Document Embedding -> Allows LLM to lookup existing permissions and roles
6. **E6**: Dataset E, Small Model, Document Embedding -> Allows LLM to lookup existing permissions and roles
7. **E7**: Dataset E, Large Model, No Document Embedding
8. **E8**: Dataset E, Small Model, No Document Embedding

Hybrid Experiments:

9. **E1H_MIN**: Dataset A, Large Model, MIN Version of algorithm
10. **E1H_MAX**: Dataset A, Large Model, MAX Version of algorithm
11. **E2H_MIN**: Dataset A, Small Model, MIN Version of algorithm
12. **E2H_MAX**: Dataset A, Small Model, MAX Version of algorithm
13. **E5H_MIN**: Dataset E, Large Model, MIN Version of algorithm
14. **E5H_MAX**: Dataset E, Large Model, MAX Version of algorithm
15. **E6H_MIN**: Dataset E, Small Model, MIN Version of algorithm
16. **E6H_MAX**: Dataset E, Small Model, MAX Version of algorithm

Experiments 1-8 use LLMs to generate both permission translations and role suggestions.
Experiments 9-16 copy the permission translations from the LLM-Only experiments.
For example, E5H_MIN copies the LLM-based permission translations from E5.
However, instead of letting an LLM suggest a role, we apply an Algorithm to perform a structured search for a role (see Subsection 5.1 of the publication).

There are two different version of the algorithm:

MIN Version: Traverse the enterprise RBAC document and return the smallest role that contains the permission translated by the LLM.

MAX Version: Traverse the enterprise RBAC document and return the largest role that contains the permission translated by the LLM.

Both algorithm versions are covered by the find_role algorithm, but with a different input parameter.

## Data Provided to an LLM

Each LLM-Only experiment involved prompting the LLM with:

1. A **System Prompt** to instruct the LLM on how to process permission requests.
2. A set of **User Prompts** simulating permission requests in natural language.

When using Document Embedding, the LLM also received:

3. An **Enterprise RBAC Structure** (referred to as the "Enterprise Document" in the paper), to look up existing roles, permission names, and their assignments.
This RBAC Structure is also used by the find_role algorithm to detect a role that contains a specific permission.

## Repository Structure

### System Prompts (see /data/system_prompts)

Each txt file contains a single system prompt, which was used for two different experiments.
The filename suffix indicates which experiments the prompt was used in (e.g., *system_prompt_e1e2.txt* was used in the LLM-Only experiments E1 and E2).

### User Prompts (see /data/user_prompts)

Each file contains 100 simulated permission requests. These were transformed from existing permission descriptions found in Microsoft repositories:

- *user_prompts_entra.txt* contains permission requests which are based on permission descriptions found in the **Microsoft Entra built-in roles**.
- *user_prompts_azure_storage.txt* contains permission requests which are based on permission descriptions found in the **Azure built-in roles for Storage**.

Example transformation:
The original permission description "Create and manage backup jobs" was transformed to the permission request "I need to create and manage backup jobs."
The detailed transformation process is described in Subsection 4.1 of the publication (Data Preprocessing: Creating Permission Requests).

### RBAC Structures (see /data/enterprise_documents)

These two JSON-structured text files represent role-to-permission mappings from the same two data sources:

- *enterprise_document_entra.txt* contains the RBAC structure of the **Microsoft Entra built-in roles**.
- *enterprise_document_azure_storage.txt* contains the RBAC structure of the **Azure built-in roles for Storage**.

These files were used...
- as document embeddings provided to LLMs in some experiments.
- in the find_role algorithm (hybrid approach!), to find a role that contains the translated permission.

See Subsection 4.1 (Data Preprocessing: Creating Enterprise Documents) for more information on how we created these RBAC structures).

### Request-to-Permission Mapping (see /data/solution_mappings)

Each file contains a ground-truth mapping between user prompts and the corresponding permission names.

- *solution_mapping_entra.csv* contains a mapping between the user prompts from *user_prompts_entra.txt* and permissions from the **Microsoft Entra built-in roles**.
- *solution_mapping_azure_storage.csv* contains a mapping between user prompts from *user_prompts_azure_storage.txt* and permissions from the **Azure built-in roles for Storage**.

### Outputs (see /data/output)

This directory contains two sub-directories: /llm_only contains the permission and role suggestions solely generated by LLMs **by prompting those**.
The file names indicate the corresponding experiments (e.g., *output_e1.csv* describes the results of experiment E1).

The subdirectory /hybrid contains the output files from our hybrid experiments. While the permission translations are copied from the experiments that can be found in the /llm_only subdirectory, the role suggestions were created **by applying the find_role algorithm**. The file names indicate the corresponding experiments (e.g., *output_E1h_max.csv* describes the results of applying the RoleFind algorithm with boolean parameter POLP = False and using the permission translations from experiment E1).

### Evaluation Output (see /data/evaluation_runenr_output)

This directory contains a single file that shows the evaluation results, which are (re-)created when running main.py.

### Main Script (see /src/main.py)

Run main.py in order to re-generate the hybrid experiment results as well as the evaluation output.
 
### Find Role (see /src/find_role.py)

Includes a Python script that implements the find_role algorithm as introduced in Subsection 5.1. -> Called from main.py

### Evaluation Runner (see /src/evaluation_runner.py)

Includes a Python script that implements the evaluation logics as introduced in Section 3. -> Called from main.py

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
