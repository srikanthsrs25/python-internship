# Bug 1 - Incorrect Average Calculation

# Error
Code:

for name in students:
    average = sum(name) / len(name)

Traceback:
text
TypeError: unsupported operand type


# Information Shared with AI

Sanitized snippet only:

python
for name in students:
    average = sum(name) / len(name)


No file paths, usernames, API keys, or sensitive data were shared.

# AI Suggestion

Use `.items()` to access both student name and marks.

python
for name, marks in students.items():
    average = sum(marks) / len(marks)


# Why the Fix Works

The original code attempted to calculate the sum of a string (`name`), which is invalid. The corrected code calculates the sum of the marks list.

# Verification

* Program executed successfully.
* No TypeError occurred.
* Average values were correctly written to CSV.


# Bug 2 - Wrong File Mode

# Error

Code:

python
with open("results.csv", "r") as file:

Program attempted to write to a file opened in read mode.

# Information Shared with AI

Only the relevant snippet and error message were shared.

# AI Suggestion

Change mode from `"r"` to `"w"`.

python
with open("results.csv", "w", newline="") as file:


# Why the Fix Works

Write operations require write mode. Read mode does not allow writing.

# Verification

* CSV file was generated successfully.
* Data was written correctly.


# Bug 3 - Missing CSV Import

# Error
`python
writer = csv.writer(file)


Traceback:
text
NameError: name 'csv' is not defined

# Information Shared with AI

Only the relevant code snippet and traceback were shared.

# AI Suggestion

Add:

python
import csv

at the beginning of the program.

# Why the Fix Works

The csv module must be imported before its functions can be used.

# Verification

* Program executed without errors.
* CSV file was created successfully.
* Output was verified manually.


