# Day03 - Question 1/3

employees = [
    {"name": "Mia", "department": "IT", "salary": 65000, "performance": 88},
    {"name": "Leo", "department": "IT", "salary": 58000, "performance": 75},
    {"name": "Ava", "department": "HR", "salary": 62000, "performance": 92},
    {"name": "Noah", "department": "IT", "salary": 70000, "performance": 90},
]

# Task: Use a for loop to calculate and print the total salary of employees 
# in "IT" whose performance score is at least 85.

total = 0

for key in employees:
    if key["department"] == "IT" and key["performance"] >= 85:
        total += key["salary"]

print(total)

# Day03 - Question 2/3

employees = [
    {"name": "Mia", "department": "IT", "salary": 65000, "performance": 88},
    {"name": "Leo", "department": "IT", "salary": 58000, "performance": 75},
    {"name": "Ava", "department": "HR", "salary": 62000, "performance": 92},
    {"name": "Noah", "department": "IT", "salary": 70000, "performance": 90},
]

# Task: Use a for loop to calculate and 
# print the average salary of employees in "IT". 
# Include all IT employees regardless of performance.

total = 0
count = 0

for key in employees:
    if key["department"] == "IT":
        total += key["salary"]
        count += 1

average = total / count

print(average)

# Day03 - Question 3/3

employees = [
    {"name": "Mia", "department": "IT", "salary": 65000, "performance": 88},
    {"name": "Leo", "department": "IT", "salary": 58000, "performance": 75},
    {"name": "Ava", "department": "HR", "salary": 62000, "performance": 92},
    {"name": "Noah", "department": "IT", "salary": 70000, "performance": 90},
]

# Task — Use a for loop to find the IT employee with the highest salary. 
# Print their name and salary.

largest = 0
name = ""

for key in employees:
    if key["department"] == "IT":
        if key["salary"] > largest:
            largest = key["salary"]
            name = key["name"]

print(name, largest)

# Day03 - Question 4

employees = [
    {"name": "Mia", "department": "IT", "salary": 65000, "performance": 88},
    {"name": "Leo", "department": "IT", "salary": 58000, "performance": 75},
    {"name": "Ava", "department": "HR", "salary": 62000, "performance": 92},
    {"name": "Noah", "department": "IT", "salary": 70000, "performance": 90},
]

# Task — Use a for loop and a dictionary to calculate 
# the total salary for each department. 
# Print the dictionary after the loop.

result = {}

for key in employees:
    dept = key["department"]

    if dept not in result:
        result[dept] = 0

    result[dept] += key["salary"]

print(result)