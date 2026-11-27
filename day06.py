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

# Day06 - Question 10

# Calculate what percentage of budget is remaining for each department. 

# Save name and percentage of department with percentage 20% or more 
# in dictionary selected.

# Result: {'HR': 20.0, 'Admin': 40.0}

remaining = {"HR": 20, "Admin": 50, "IT": 10}
budgets = {"HR": 100, "Admin": 125, "IT": 200}
selected = {}

for dept in remaining:
    rate = remaining[dept] / budgets[dept] * 100
    if rate >= 20:
        selected[dept] = rate

print(selected)

# Day 6 - Question 11

# Calculate what percentage is remaining from company total budget
# by dividing total remaining by total budget.

# Result: 20.0

remaining = {"HR": 20, "Admin": 50, "IT": 10}
budgets = {"HR": 100, "Admin": 125, "IT": 175}

total_remaining = 0
total_budget = 0

for dept in remaining:
    total_remaining += remaining[dept]

for dept in budgets:
    total_budget += budgets[dept]

print(total_remaining / total_budget * 100)

# Day 6 - Question 12

# Pick accounts payable (paid = False) 
# and add accounts payable of each department into dictionary unpaid.

# Result: {'IT': 150, 'HR': 80}

invoices = [
    {"dept": "IT", "amount": 120, "paid": False},
    {"dept": "HR", "amount": 50, "paid": True},
    {"dept": "IT", "amount": 30, "paid": False},
    {"dept": "HR", "amount": 80, "paid": False},
]

unpaid = {}

for invoice in invoices:
    if invoice["paid"] == False:
        dept = invoice["dept"]

        if dept not in unpaid:
            unpaid[dept] = 0

        unpaid[dept] += invoice["amount"]

print(unpaid)

# Day 6 - Question 13

# Pick invoice where paid == True and 
# Calculate total amount of each department in dictionary paid_totals.

# Result: {'IT': 140, 'HR': 70}

invoices = [
    {"dept": "IT", "amount": 100, "paid": True},
    {"dept": "HR", "amount": 50, "paid": False},
    {"dept": "IT", "amount": 40, "paid": True},
    {"dept": "HR", "amount": 70, "paid": True},
]

paid_totals = {}

for invoice in invoices:
    if invoice["paid"] == True:
        dept = invoice["dept"]

        if dept not in paid_totals:
            paid_totals[dept] = 0

        paid_totals[dept] += invoice["amount"]

print(paid_totals)

# Day 6 - Question 14

# Count "paid" = True for each department
# and save in dictionary paid_counts.

# Result: {'IT': 2, 'HR': 1}

invoices = [
    {"dept": "IT", "amount": 100, "paid": True},
    {"dept": "HR", "amount": 50, "paid": False},
    {"dept": "IT", "amount": 40, "paid": True},
    {"dept": "HR", "amount": 70, "paid": True},
]

paid_counts = {}

for invoice in invoices:
    if invoice["paid"] == True:
        dept = invoice["dept"]

        if dept not in paid_counts:
            paid_counts[dept] = 0

        paid_counts[dept] += 1

print(paid_counts)

# Day 6 - Practice 1

# Fill in the blank to print whether each invoice has been paid.

invoices = [
    {"dept": "IT", "amount": 120, "paid": False},
    {"dept": "HR", "amount": 50, "paid": True},
]

for invoice in invoices:
    print(invoice["paid"])

# Expected output
# False
# True

# Day 6 - Practice 2

# Print the amount of each unpaid invoice.

invoices = [
    {"dept": "IT", "amount": 120, "paid": False},
    {"dept": "HR", "amount": 50, "paid": True},
]

for invoice in invoices:
    if invoice["paid"] == False:
        print(invoice["amount"])

# Expected output
# 120

# Day 6 - Practice 3

# Add up the amounts of all unpaid invoices. 

# Expected output
# 150

invoices = [
    {"dept": "IT", "amount": 120, "paid": False},
    {"dept": "HR", "amount": 50, "paid": True},
    {"dept": "IT", "amount": 30, "paid": False},
]

total_unpaid = 0

for invoice in invoices:
    if invoice["paid"] == False:
        total_unpaid += invoice["amount"]

print(total_unpaid)

# Day 6 - Practice 4

# Calculate the unpaid total for each department. 

# Expected output
# {'IT': 150, 'HR': 80}

invoices = [
    {"dept": "IT", "amount": 120, "paid": False},
    {"dept": "HR", "amount": 50, "paid": True},
    {"dept": "IT", "amount": 30, "paid": False},
    {"dept": "HR", "amount": 80, "paid": False},
]

unpaid = {}

for invoice in invoices:
    if invoice["paid"] == False:
        dept = invoice["dept"]

        if dept not in unpaid:
            unpaid[dept] = 0

        unpaid[dept] += invoice["amount"]
        

print(unpaid)

# Question 1 of 10

# Each payment has an amount and a status. 
# Write a loop that counts the pending payments and prints the count.

payments = [
    {"amount": 90, "status": "pending"},
    {"amount": 60, "status": "completed"},
    {"amount": 40, "status": "pending"},
    {"amount": 70, "status": "cancelled"},
]

count = 0

for payment in payments:
    if payment["status"] == "pending":
        count += 1

print(count)

# Question 2 of 10

# Use a loop to calculate the total amount of completed payments and print the total.

payments = [
    {"amount": 80, "status": "completed"},
    {"amount": 45, "status": "pending"},
    {"amount": 30, "status": "cancelled"},
    {"amount": 65, "status": "completed"},
]

total = 0

for payment in payments:
    if payment["status"] == "completed":
        total += payment["amount"]

print(total)

# Question 3 of 10

# Use a loop to calculate the total expense amount for each department. 
# Store the totals in a dictionary called totals and print it.

expenses = [
    {"dept": "Sales", "amount": 45},
    {"dept": "IT", "amount": 80},
    {"dept": "Sales", "amount": 30},
    {"dept": "HR", "amount": 25},
]

totals = {}

for expense in expenses:
    dept = expense["dept"]

    if dept not in totals:
        totals[dept] = 0

    totals[dept] += expense["amount"]

print(totals)

# Question 4 of 10

# Use a loop to count unpaid invoices for each department. 
# Include only departments with at least one unpaid invoice. 
# Store the counts in unpaid_counts and print the dictionary.

invoices = [
    {"dept": "IT", "paid": False},
    {"dept": "Sales", "paid": True},
    {"dept": "HR", "paid": False},
    {"dept": "IT", "paid": True},
    {"dept": "HR", "paid": False},
]

unpaid_counts = {}

for invoice in invoices:
    dept = invoice["dept"]
    
    if invoice["paid"] == False:

        if dept not in unpaid_counts:
                unpaid_counts[dept] = 0

        unpaid_counts[dept] += 1

print(unpaid_counts)

# Question 5 of 10

# Use a loop to calculate the average amount per paid invoice for each department. 
# Store the results in averages and print the dictionary.

paid_totals = {"IT": 240, "HR": 90, "Sales": 300}
paid_counts = {"IT": 3, "HR": 2, "Sales": 5}

averages = {}

for dept in paid_totals:
    averages[dept] = paid_totals[dept] / paid_counts[dept]

print(averages)

# Question 6 of 10

# Use a loop to find every department whose spending exceeded its budget 
# by at least 20%. 
# Store each qualifying department and its excess amount in dollars 
# in a dictionary called over_budget. 
# Print the dictionary.

spending = {"IT": 240, "HR": 115, "Sales": 260, "Admin": 90}
budgets = {"IT": 200, "HR": 100, "Sales": 200, "Admin": 100}

over_budget = {}

for dept in spending:
    if (spending[dept] - budgets[dept])/budgets[dept] * 100 >= 20:
        over_budget[dept] = spending[dept] - budgets[dept]

print(over_budget)

# Question 7 of 10

# Use a loop to find the department with the highest total unpaid amount. 
# Print the department name and its amount.

unpaid_totals = {"IT": 180, "HR": 250, "Sales": 210, "Admin": 90}

largest = 0
name = ""

for dept in unpaid_totals:
    if unpaid_totals[dept] > largest:
        largest = unpaid_totals[dept]
        name = dept

print(name, largest)

# Question 8 of 10

# Use a loop to calculate the percentage of the company’s total budget 
# that remains unspent. 
# Print one percentage for the whole company.

remaining = {"IT": 60, "HR": 30, "Sales": 10}
budgets = {"IT": 200, "HR": 100, "Sales": 200}

total_remaining = 0
total_budget = 0

for dept in remaining:
    total_remaining += remaining[dept]

for dept in budgets:
    total_budget += budgets[dept]

percentage = total_remaining / total_budget * 100

print(percentage)

# Question 9 of 10

# Use a loop to find the largest unpaid invoice. 
# Print its department name and amount.

invoices = [
    {"dept": "Sales", "amount": 240, "paid": False},
    {"dept": "IT", "amount": 400, "paid": True},
    {"dept": "HR", "amount": 310, "paid": False},
    {"dept": "Admin", "amount": 180, "paid": False},
]

largest = 0
name = ""

for invoice in invoices:
    if invoice["paid"] == False:
        if invoice["amount"] > largest:
            largest = invoice["amount"]
            name = invoice["dept"]

print(name, largest)

# Question 10 of 10

# Use loops to calculate the average unpaid invoice amount for each department. 
# Include only departments with at least one unpaid invoice. 
# Store the results in averages and print the dictionary.

invoices = [
    {"dept": "Sales", "amount": 120, "paid": False},
    {"dept": "IT", "amount": 300, "paid": True},
    {"dept": "HR", "amount": 90, "paid": False},
    {"dept": "Sales", "amount": 180, "paid": False},
    {"dept": "HR", "amount": 60, "paid": True},
]

total_unpaid = {}
count_unpaid = {}
averages = {}

for invoice in invoices:
    dept = invoice["dept"]
    
    if invoice["paid"] == False:

        if dept not in total_unpaid:
            total_unpaid[dept] = 0
        
        if dept not in count_unpaid:
            count_unpaid[dept] = 0

        total_unpaid[dept] += invoice["amount"]
        count_unpaid[dept] += 1

for dept in total_unpaid:
    averages[dept] = total_unpaid[dept] / count_unpaid[dept]

print(averages)