# Day 07 · Practice 1

# Loop through invoices and print the amount of each invoice that is 
# both unpaid and overdue.
# - An invoice is unpaid if paid is False.
# - An invoice is overdue if days_overdue is greater than 0.
# - Print each matching amount on a separate line.

invoices = [
    {"amount": 120, "paid": False, "days_overdue": 4},
    {"amount": 180, "paid": True, "days_overdue": 7},
    {"amount": 250, "paid": False, "days_overdue": 0},
    {"amount": 90, "paid": False, "days_overdue": 2},
]

for invoice in invoices:
    if invoice["paid"] == False and invoice["days_overdue"] > 0:
        print(invoice["amount"])

# Day 07 · Practice 2

# Calculate the total paid invoice amount for each department. 
# Store the totals in a dictionary called paid_totals and print it. 
# Only include departments with at least one paid invoice.

invoices = [
    {"dept": "IT", "amount": 120, "paid": True},
    {"dept": "HR", "amount": 180, "paid": False},
    {"dept": "IT", "amount": 90, "paid": True},
    {"dept": "Sales", "amount": 250, "paid": True},
]

paid_totals = {}

for invoice in invoices:
    dept = invoice["dept"]

    if invoice["paid"] == True:
        if dept not in paid_totals:
            paid_totals[dept] = 0

        paid_totals[dept] += invoice["amount"]

print(paid_totals)

# Day 07 · Test 1

# Calculate the total amount of unpaid, overdue invoices for each department. 
# Store the totals in overdue_totals and print the dictionary.
# An invoice qualifies if paid is False and days_overdue is greater than 0. 
# Exclude departments with no qualifying invoices.

invoices = [
    {"dept": "IT", "amount": 300, "paid": False, "days_overdue": 5},
    {"dept": "HR", "amount": 150, "paid": False, "days_overdue": 0},
    {"dept": "IT", "amount": 200, "paid": False, "days_overdue": 2},
    {"dept": "Sales", "amount": 400, "paid": True, "days_overdue": 8},
    {"dept": "Sales", "amount": 250, "paid": False, "days_overdue": 3},
]

overdue_totals = {}

for invoice in invoices:
    dept = invoice["dept"]

    if invoice["paid"] == False and invoice["days_overdue"] > 0:
        if dept not in overdue_totals:
            overdue_totals[dept] = 0
        overdue_totals[dept] += invoice["amount"]

print(overdue_totals)

# Day 07 · Test 2

# Count the unpaid invoices that are at least 3 days overdue in each department. 
# Store the counts in overdue_counts and print the dictionary. 
# Exclude departments with no qualifying invoices.

invoices = [
    {"dept": "IT", "amount": 300, "paid": False, "days_overdue": 5},
    {"dept": "HR", "amount": 150, "paid": False, "days_overdue": 0},
    {"dept": "IT", "amount": 200, "paid": False, "days_overdue": 2},
    {"dept": "Sales", "amount": 400, "paid": True, "days_overdue": 8},
    {"dept": "Sales", "amount": 250, "paid": False, "days_overdue": 3},
]

overdue_counts = {}

for invoice in invoices:
    dept = invoice["dept"]

    if invoice["paid"] == False and invoice["days_overdue"] >= 3:
        if dept not in overdue_counts:
            overdue_counts[dept] = 0
        overdue_counts[dept] += 1

print(overdue_counts)

# Day 07 · Test 3

# Calculate the average amount of unpaid, overdue invoices for each department.
# An invoice qualifies if paid is False and days_overdue is greater than 0.
# Store the averages in overdue_averages and print the dictionary. 
# Exclude departments with no qualifying invoices.

invoices = [
    {"dept": "IT", "amount": 300, "paid": False, "days_overdue": 5},
    {"dept": "HR", "amount": 150, "paid": False, "days_overdue": 0},
    {"dept": "IT", "amount": 200, "paid": False, "days_overdue": 2},
    {"dept": "Sales", "amount": 400, "paid": True, "days_overdue": 8},
    {"dept": "Sales", "amount": 250, "paid": False, "days_overdue": 3},
]

overdue_totals = {}
overdue_counts = {}
overdue_averages = {}

for invoice in invoices:
    dept = invoice["dept"]

    if invoice["paid"] == False and invoice["days_overdue"] > 0:
        if dept not in overdue_totals:
            overdue_totals[dept] = 0
            overdue_counts[dept] = 0
        overdue_totals[dept] += invoice["amount"]
        overdue_counts[dept] += 1

for dept in overdue_totals:
    overdue_averages[dept] = overdue_totals[dept] / overdue_counts[dept]       

print(overdue_averages)