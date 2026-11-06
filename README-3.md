# Citizen Complaint Management System

A small, beginner-friendly Python program that lets citizens submit complaints to a government office and lets staff track them. It was written for **PROG211 – Object-Oriented Programming 1** and is designed around Digital Public Good (DPG) principles: open source, accessible, privacy-respecting, modular and reusable.

> **Educational demo.** Records are held in memory only and are lost when the program exits. Do not enter real personal or sensitive data.

## Features

- Anonymous citizen records that use a reference ID (for example `C001`) and a general location instead of personal details
- Create complaints with an ID, category and description
- Track status: `Pending`, `In Progress` or `Resolved`
- Reject duplicate complaint IDs
- Display all complaints or search for one by ID
- Count the complaints created in the current run

## Requirements

- Python 3.8 or newer
- No third-party packages

## Getting started

```bash
git clone <your-repository-url>
cd <your-repository-folder>
python citizen_complaint_system.py
```

## Example output

```text
CITIZEN INFORMATION
Citizen Reference: C001
Location: Freetown

Complaint added successfully.
Complaint added successfully.
Complaint added successfully.

ALL GOVERNMENT COMPLAINTS
---------------------------------------------
Complaint ID: G001
Citizen Reference: C001
Category: Road Maintenance
Description: A road in the community needs repair.
Status: Pending
...

UPDATING COMPLAINT G001
Complaint status updated successfully.

TOTAL COMPLAINTS CREATED: 3
```

## Project structure

```text
.
├── citizen_complaint_system.py   # Program source code
├── LICENSE                       # MIT License
└── README.md                     # This file
```

## Design

| Class | Responsibility |
|---|---|
| `Citizen` | Holds an anonymous reference ID and a location. |
| `Complaint` | Holds a complaint, validates and updates its status, and keeps a class-level count of complaints created. |
| `GovernmentComplaintSystem` | Stores complaints in a list; adds (with duplicate check), displays and searches them. |

## Usage in your own code

```python
from citizen_complaint_system import Citizen, Complaint, GovernmentComplaintSystem

system = GovernmentComplaintSystem()
citizen = Citizen("C010", "Makeni")
complaint = Complaint("G010", citizen.citizen_id, "Water Supply", "No water for three days.")

system.add_complaint(complaint)
complaint.update_status("In Progress")
system.search_complaint("G010")
```

## Digital Public Good principles

| Principle | How it is applied |
|---|---|
| Open source | Released under the MIT License. |
| Accessible | Plain Python, no dependencies, runs on any computer with Python. |
| Privacy-respecting | Citizens are identified by a reference ID; no names or contact details are stored. |
| Modular | Each class has one clear job and can be changed independently. |
| Reusable | Classes can be imported into other programs. |

## Known limitations and ideas for future work

- Data is stored in memory only; add a file or database for persistence.
- There is no user menu; the program runs a fixed demonstration.
- Add automated tests and input validation.
- Add user roles (citizen and officer) and a notification feature.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
