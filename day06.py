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

# Day06 - Question 4

# Save name and over amount of department that exceeded budget in 
# dictionary over-budget. 

# Print the dictionary.

# Result: {'IT': 30, 'Sales': 50} 

totals = {"IT": 180, "HR": 80, "Sales": 250}
budgets = {"IT": 150, "HR": 100, "Sales": 200}
over_budget = {}

for dept in totals:
    if totals[dept] > budgets[dept]:
        over_budget[dept] = totals[dept] - budgets[dept]

print(over_budget)

# Day06 - Question 5

# Calculate total over amount of two departments using above dictionary. 

# Result: 80

over_budget = {"IT": 30, "Sales": 50}
total_over = 0

for dept in over_budget:
    total_over += over_budget[dept]

print(total_over)

# Day06 - Question 6

# Find the department with largest over mamount. 

# Result: Sales 50

over_budget = {"IT": 30, "Sales": 50, "HR": 20}
highest = 0
highest_dept = ""

for dept in over_budget:
    if over_budget[dept] > highest:
        highest = over_budget[dept]
        highest_dept = dept

print(highest_dept, highest)

# Day06 - Question 7

# Print name of department with over % = 20% or more. 

# over % = over amount / budget * 100

# Result: 
# IT
# Sales

over_budget = {"IT": 30, "Sales": 50, "HR": 20}
budgets = {"IT": 150, "Sales": 200, "HR": 200}

for dept in over_budget:
    rate = over_budget[dept] / budgets[dept] * 100
    if rate >= 20:
        print(dept)

# Day06 - Question 8

# Save name and rate of department with rate 20% or more in a dictionary selected.

# Result: {'IT': 20.0, 'Sales': 25.0}

rates = {"IT": 20.0, "Sales": 25.0, "HR": 10.0}
selected = {}

for dept in rates:
    if rates[dept] >= 20:
        selected[dept] = rates[dept]

print(selected)

# Day06 - Question 9

# Save name and remaining amount of department that has remaining budget.

# Result: {'HR': 20, 'Admin': 50}

totals = {"IT": 180, "HR": 80, "Sales": 200, "Admin": 70}
budgets = {"IT": 150, "HR": 100, "Sales": 200, "Admin": 120}
remaining = {}

for dept in totals:
    if totals[dept] < budgets[dept]:
        remaining[dept] = budgets[dept] - totals[dept]

print(remaining)