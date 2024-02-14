# Secret Santa Game

## Introduction

This Python program automates the process of assigning Secret Santa within a company. It reads employee information from a CSV file, assigns secret children to each employee, and generates a new CSV file with the assignments.

## Requirements

- Python 3.11
- pandas
- random

## Installation

1. Clone this repository:

```
git clone https://github.com/abishekchandran/secret_santa.git
```

2. Navigate to the project directory:

```
cd secret_santa
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

1. Place your employee list CSV file (`Employee-list.csv`) and the previous year's Secret Santa assignments CSV file (`Secret-Santa-Game-Result-<year>.csv`) in the project directory.

2. Run the program:

```
python secret_santa.py
```

3. After execution, the program will generate a new CSV file named `output_secret_santa.csv` containing the Secret Santa assignments.

## Input Format

The employee list CSV file should contain the following columns:

- `Employee_Name`: Name of the employee.
- `Employee_EmailID`: Email ID of the employee.

The previous year's Secret Santa assignments CSV file should contain the following columns:

- `Employee_Name`: Name of the employee.
- `Employee_EmailID`: Email ID of the employee.
- `Secret_Child_Name`: Name of the assigned secret child.
- `Secret_Child_EmailID`: Email ID of the assigned secret child.

## Output Format

The output CSV file will contain the following columns for each employee:

- `Employee_Name`: Name of the employee.
- `Employee_EmailID`: Email ID of the employee.
- `Secret_Child_Name`: Name of the assigned secret child.
- `Secret_Child_EmailID`: Email ID of the assigned secret child.

## Error Handling

- If an employee from the current year's list is not found in the previous year's Santa list, an error message will be printed, and the program will continue.
- If there are no available employees for a particular individual, an error message will be printed, and the program will skip the assignment for that employee.
- Handles file-not-found errors for input files.
