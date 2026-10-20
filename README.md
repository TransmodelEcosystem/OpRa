# OpRa (Operational Raw Data) XML schema version 1.0
**(C) 2024-2026 OpRa, CEN**

## Included schemas:

- OpRa
- using NeTEx as submodule (https://github.com/TransmodelEcosystem/NeTEx)
- using SIRI as submodule (https://github.com/TransmodelEcosystem//SIRI)

### Overview

- OpRa (Operational Raw Data) - **CEN/TS 17370:2026** complements the Transmodel series (NeTEx for static data, SIRI for dynamic data) to provide a standardized format for exchanging historical data.

This version supports data exchange regarding public transport systems in four data groups:
- Planned service data in PLANNED FRAMEs.
- Actual service data in ACTUAL FRAMEs.
- Standardised indicators in INDICATOR FRAMEs.
- Contextual (non-standard, context and usage dependent) indicators in CONTEXTUAL INDICATOR FRAMEs.

### Folder structure

The individual XML files are organized hierarchically in folders in the **/xsd** subfolder. The structure of the **/xsd** subfolder is: 

- **/opra_framework**: Contains schema definitions for data frames that govern topic separation and versioning, generic log entries and contextual indicators, and reusable data element representations.
- **/opra_imports**: Contains shared imported entries for NeTEx and SIRI inclusion.
- **/opra_indicators**: Contains definitions of the standardised OpRa indicators
- **/opra_services**: Contains definitions to support payload delivery, request/response, discovery and subscription-based collaborations between systems. Mimics the structure generated for SIRI.

### UML models

- You can refer to the Transmodel UML Conceptual models for a detailed UML view of the schema packages.
- These models are available in electronic format.
  
## Getting started

### Main root schema

**opra.xsd**
   - Always-include starting point for OpRa messages.
   - Supports publish, request/response and subscribe collaboration models.

### XML examples

- Explore XML examples in the */examples* subdirectory.

### Support for XML editors

- **Altova XMLSpy Project**: Find an organized view of the schema and examples in the root directory.
   - Project file: OpRa.spp

- **Oxygen Project File**: 
   - Project file: OpRa.xpr

### Note on the schema

The schema is systematically divided into small modular files. XML schema files are following naming convention based on versioning awareness:

- **opra_xxxx_support.xsd**: Contains definitions unaware of versioning, and might be included for systems that don't implement versioning.
- **opra_xxxx_version.xsd**: Contains definitions aware of versioning.

----
## Branches

| Branch Name | Description                                             | Link                                            |
| ----------- | ------------------------------------------------------- | ----------------------------------------------- |
| `master`    | Current head of the project                            | [GitHub](https://github.com/TransmodelEcosystem/OpRa)    |
| `next`      | Work for the next release                              | [GitHub](TBD) |

# Change Log
## Releases
| Release Number | Release Date  | Description                                    | Link | Release Notes                                                                                   |
| -------------- | ------------- | ---------------------------------------------- | ------------- | ----------------------------------------------------------------------------------------------- |
| 1.0            | 08.27.2026    | Initial production version | [Code](https://github.com/TransmodelEcosystem/OpRa/releases/tag/v1.0) | [Release Notes](https://github.com/TransmodelEcosystem/OpRa/blob/v1.0/README.md) |

## Full Version History
The comprehensive versions history is available in [change_log.md](https://github.com/TransmodelEcosystem/OpRa/blob/OpRa/change_log.md)

## CI
The workflow scripts in `.github/scripts` validate the code. The permission to read and write is required for Github Actions, and is set up in "Settings/Actions/General".

While `validate-and-lint.sh` should find every file automatically, `validate-examples.sh` requires to add the new files to a list, as they are created (the files starting with `placeholder*` are starter dummy files).
