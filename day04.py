# Day04 - Question 1/3

# Complete the loop to calculate the total salary for each department.

employees = [
    {"name": "Alice", "department": "IT", "salary": 60000},
    {"name": "Bob", "department": "Sales", "salary": 50000},
    {"name": "Charlie", "department": "IT", "salary": 70000}
]

totals = {}

for employee in employees:
    dept = employee["department"]

    if dept not in totals:
        totals[dept] = 0

    # Write one line here
    totals[dept] += employee["salary"]

print(totals)

# Day04 - Question 2/3

# Using the same employees list, 
# count how many employees work in each department. Fill in the missing line.

employees = [
    {"name": "Alice", "department": "IT", "salary": 60000},
    {"name": "Bob", "department": "Sales", "salary": 50000},
    {"name": "Charlie", "department": "IT", "salary": 70000}
]

counts = {}

for employee in employees:
    dept = employee["department"]

    if dept not in counts:
        counts[dept] = 0

    # Write one line here
    counts[dept] += 1

print(counts)

# Day04 - Question 3/3

students = [
    {"name": "Mia", "class": "A"},
    {"name": "Leo", "class": "B"},
    {"name": "Zoe", "class": "A"},
    {"name": "Kai", "class": "A"}
]

counts = {}

# Count how many students are in each class. 
# Store the result in counts and print it.

for student in students:
    clas = student["class"]

    if clas not in counts:
        counts[clas] = 0

    counts[clas] += 1

print(counts)

# Day04 - Question 4

students = [
    {"name": "Mia", "class": "A", "score": 80},
    {"name": "Leo", "class": "B", "score": 90},
    {"name": "Zoe", "class": "A", "score": 75},
    {"name": "Kai", "class": "A", "score": 85}
]

totals = {}

# Calculate the total score for each class. Store the result in totals and print it.

for student in students:
    clas = student["class"]

    if clas not in totals:
        totals[clas] = 0

    totals[clas] += student["score"]

print(totals)

# Day04 - Question 5

# Use totals and counts to calculate the average score for each class. 
# Store the results in averages and print it.

totals = {"A": 240, "B": 90}
counts = {"A": 3, "B": 1}
averages = {}

for clas in totals:
    averages[clas] = totals[clas] / counts[clas]

print(averages)