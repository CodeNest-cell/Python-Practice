# Day06 - Question 1/3

# Calculate average expense for each department.

# Step 1: Calculate total expense and expense count of each department.

expenses = [
    {"dept": "IT", "amount": 120},
    {"dept": "HR", "amount": 80},
    {"dept": "IT", "amount": 60},
]

totals = {}
counts = {}

for expense in expenses:
    dept = expense["dept"]

    if dept not in totals:
        totals[dept] = 0
        counts[dept] = 0

    totals[dept] += expense["amount"]
    counts[dept] += 1 

print(totals)
print(counts)

# Step 2: Calculate average expense of each department.

averages = {}

for dept in totals:
    averages[dept] = totals[dept] / counts[dept]

print(averages)

# Day06 - Question 2/3

# Print name and average of department with average expense 90 or more. 

averages = {"IT": 90.0, "HR": 80.0}

for dept in averages:
    if averages[dept] >= 90:
        print(dept, averages[dept])

# Day06 - Question 3/3

# totals = expense of each department; budgets = budget of each department

# Print name and over amount of department that exceeded budget.

totals = {"IT": 180, "HR": 80}
budgets = {"IT": 150, "HR": 100}

for dept in totals:
    if totals[dept] > budgets[dept]:
        print(dept, totals[dept] - budgets[dept])