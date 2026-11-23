# Day02 - Question 1/3

# Given the following dictionary:

salaries = {
    "Alice": 55000,
    "Bob": 72000,
    "Charlie": 48000,
    "David": 85000,
    "Emma": 63000
}

# Write Python code to print the names of all employees 
# whose salary is greater than 60,000.

for key in salaries:
    if salaries[key] > 60000:
        print(key)

# Day02 - Question 2/3

# Given the following dictionary:

sales = {
    "Monday": 120,
    "Tuesday": 250,
    "Wednesday": 180,
    "Thursday": 300,
    "Friday": 150
}

# Write Python code to:
# 1. Calculate the total sales.
# 2. Calculate the average daily sales.
# 3. Print both results.

total = 0
for key in sales:
    total += sales[key]
    
average = total/len(sales)

print(total)
print(average)

# Day02 - Question 3/3

# Given the following dictionary:

salaries = {
    "Alice": 55000,
    "Bob": 72000,
    "Charlie": 48000,
    "David": 85000,
    "Emma": 63000
}

# Write Python code to:
# 1. Find the employee with the highest salary.
# 2. Print the employee's name and salary.
# 3. Use a for loop and an if statement.

largest = 0
name = "key"

for key in salaries:
    if salaries[key] > largest:
        largest = salaries[key]
        name = key

print(name, largest)


# Day02 - Question 4

# Given the following dictionary:

prices = {
    "Laptop": 1200,
    "Mouse": 40,
    "Keyboard": 150,
    "Monitor": 350,
    "USB": 25
}

# Write Python code to:
# 1. Count how many products cost more than 100.
# 2. Print the number of products.
# 3. Use a for loop and an if statement.

count = 0

for key in prices:
    if prices[key] > 100:
        count += 1

print(count)

# Day02 - Question 5

prices = [100, 250, 80, 400, 150]

# Write Python code to:
# 1. Apply a 20% discount to every price.
# 2. Store the discounted prices in a new list called discounted.
# 3. Print the new list.
# 4. Use a for loop.

discounted = []

for i in prices:
    discounted.append(i * 0.8)

print(discounted)

# Day02 - Question 6

scores = {
    "Alice": 85,
    "Bob": 42,
    "Charlie": 73,
    "David": 38,
    "Emma": 91
}

# Write Python code to:
# 1. Find students who scored 50 or higher.
# 2. Store their names in a new list called passed.
# 3. Print the list.
# 4. Use a for loop and an if statement.

passed = []

for key in scores:
    if scores[key] >= 50:
        passed.append(key)

print(passed)

# Day02 - Question 7

employees = [
    {"name": "Alice", "department": "IT", "salary": 70000},
    {"name": "Bob", "department": "Sales", "salary": 55000},
    {"name": "Charlie", "department": "IT", "salary": 80000},
    {"name": "David", "department": "HR", "salary": 60000},
    {"name": "Emma", "department": "IT", "salary": 75000}
]

# Write Python code to:
# 1. Calculate the total salary of employees in the IT department.
# 2. Print the total salary.
# 3. Use a for loop and an if statement.

total = 0

for key in employees:
    if key["department"] == 'IT':
        total += key["salary"]

print(total)

# Day02 - Question 8

employees = [
    {"name": "Alice", "salary": 70000},
    {"name": "Bob", "salary": 45000},
    {"name": "Charlie", "salary": 85000},
    {"name": "David", "salary": 55000}
]

# Write Python code to:
# 1. Find employees earning more than 60,000.
# 2. Store their names in a new list called high_salary.
# 3. Print the list.
# 4. Use a for loop and an if statement.

high_salary = []

for key in employees:
    if key["salary"] > 60000:
        high_salary.append(key["name"])

print(high_salary)

# Day02 - Question 9

employees = [
    {"name": "Alice", "department": "IT", "salary": 70000},
    {"name": "Bob", "department": "Sales", "salary": 55000},
    {"name": "Charlie", "department": "IT", "salary": 80000},
    {"name": "David", "department": "HR", "salary": 60000},
    {"name": "Emma", "department": "IT", "salary": 75000}
]

# Write Python code to:
# 1. Calculate the average salary of employees in the IT department.
# 2. Count only employees working in IT.
# 3. Print the average salary.
# 4. Use a for loop and an if statement.

total = 0
count = 0

for key in employees:
    if key["department"] == "IT":
        total += key["salary"]
        count += 1

average = total / count

print(average)

# Day02 - Question 10

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 40},
    {"name": "Monitor", "price": 350},
    {"name": "Keyboard", "price": 150},
    {"name": "Tablet", "price": 800}
]

# Write Python code to:
# 1. Find the most expensive product.
# 2. Print its name and price.
# 3. Use a for loop and an if statement.
# 4. Do not use max().

largest = 0
name = ""

for key in products:
    if key["price"] > largest:
        largest = key["price"]
        name = key["name"]

print(name, largest)

# Day02 - Question 11

orders = [
    {"product": "Laptop", "price": 1200, "quantity": 2},
    {"product": "Mouse", "price": 40, "quantity": 5},
    {"product": "Monitor", "price": 350, "quantity": 3},
    {"product": "Keyboard", "price": 150, "quantity": 4}
]

# Write Python code to:
# 1. Calculate the total revenue from all orders.
# 2. Revenue for each order = price × quantity.
# 3. Use a for loop.
# 4. Print the total revenue.

total = 0

for key in orders:
    total += key["price"] * key["quantity"]

print(total)

# Day02 - Question 12

inventory = [
    {"product": "Laptop", "stock": 15},
    {"product": "Mouse", "stock": 4},
    {"product": "Keyboard", "stock": 8},
    {"product": "Monitor", "stock": 2},
    {"product": "Tablet", "stock": 12}
]

# Write Python code to:
# 1. Find products with stock less than 10.
# 2. Store their names in a new list called low_stock.
# 3. Calculate the total number of low-stock products.
# 4. Print the list and the count.
# 5. Use a for loop and an if statement.

low_stock = []
count = 0

for key in inventory:
    if key["stock"] < 10:
        low_stock.append(key["product"])
        count += 1

print(low_stock)
print(count)

# Day02 - Question 13

sales = [
    {"product": "Laptop", "category": "Electronics", "amount": 1200},
    {"product": "Desk", "category": "Furniture", "amount": 300},
    {"product": "Monitor", "category": "Electronics", "amount": 400},
    {"product": "Chair", "category": "Furniture", "amount": 200},
    {"product": "Tablet", "category": "Electronics", "amount": 800}
]

# Write Python code to:
# 1. Calculate the total sales amount for the Electronics category.
# 2. Count how many Electronics products were sold.
# 3. Print the total amount and count.
# 4. Use a for loop and an if statement.

total = 0
count = 0

for key in sales:
    if key["category"] == "Electronics":
        total += key["amount"]
        count += 1

print(total)
print(count)