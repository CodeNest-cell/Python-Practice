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

# Day02 - Question 14

products = [
    {"name": "Laptop", "cost": 800, "price": 1200},
    {"name": "Mouse", "cost": 20, "price": 40},
    {"name": "Monitor", "cost": 250, "price": 350},
    {"name": "Keyboard", "cost": 90, "price": 150}
]

# Write Python code to:
# 1. Calculate the profit for each product (price - cost).
# 2. Store each profit in a new list called profits.
# 3. Calculate the total profit.
# 4. Print the list and the total profit.
# 5. Use a for loop.

profits = []
total = 0

for key in products:
    profits.append(key["price"] - key["cost"])

for i in profits:
    total += i

print(profits)
print(total)

# Day02 - Question 15

products = [
    {"name": "Laptop", "cost": 800, "price": 1200},
    {"name": "Mouse", "cost": 20, "price": 40},
    {"name": "Monitor", "cost": 250, "price": 350},
    {"name": "Keyboard", "cost": 90, "price": 150},
    {"name": "Tablet", "cost": 400, "price": 700}
]

# Write Python code to:
# 1. Calculate the profit for each product.
# 2. Find products with profit greater than 100.
# 3. Store their names in a new list called high_profit.
# 4. Print the list.
# 5. Use a for loop and an if statement.

high_profit = []

for key in products:
    if key["price"] - key["cost"] > 100:
        high_profit.append(key["name"])

print(high_profit)

# Day02 - Question 16

sales = [
    {"department": "IT", "revenue": 5000},
    {"department": "Sales", "revenue": 3000},
    {"department": "IT", "revenue": 7000},
    {"department": "HR", "revenue": 2000},
    {"department": "Sales", "revenue": 4000}
]

# Task:

# Write Python code to:
# 1. Calculate total revenue for each department.
# 2. Store the results in a new dictionary called totals.
# 3. Print the dictionary.
# 4. Use a for loop.

IT = 0
Sales = 0
HR = 0

totals = {}

for key in sales:
    if key["department"] == "IT":
        IT += key["revenue"]
    if key["department"] == "Sales":
        Sales += key["revenue"]
    if key["department"] == "HR":
        HR += key["revenue"]

totals["IT"] = IT
totals["Sales"] = Sales
totals["HR"] = HR

print(totals)

# Day02 - Question 17

employees = [
    {"name": "Alice", "department": "IT"},
    {"name": "Bob", "department": "Sales"},
    {"name": "Charlie", "department": "IT"},
    {"name": "David", "department": "HR"},
    {"name": "Emma", "department": "Sales"},
    {"name": "Frank", "department": "IT"}
]

# Write Python code to:
# 1. Count the number of employees in each department.
# 2. Store the results in a dictionary called counts.
# 3. Print the dictionary.
# 4. Use a for loop.
# 5. Do not create separate variables for IT, Sales, and HR.

counts = {}

for key in employees:
    dept = key["department"]

    if dept not in counts:
        counts[dept] = 0

    counts[dept] += 1

print(counts)

# Day02 - Question 18

counts = {"IT": 3, "Sales": 2}

# Write Python code to:
# 1. Add a new department "HR" with 1 employee.
# 2. Increase the "Sales" employee count by 2.
# 3. Print the updated dictionary.

counts["HR"] = 1
counts["Sales"] += 2

print(counts)

# Day02 - Question 19

inventory = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15
}

# Write Python code to:
# 1. Increase the Laptop stock by 5.
# 2. Decrease the Mouse stock by 10.
# 3. Add a new product "Monitor" with stock 8.
# 4. Print the updated dictionary.

inventory["Laptop"] += 5
inventory["Mouse"] -= 10
inventory["Monitor"] = 8

print(inventory)

# Day02 - Question 20

products = [
    {"name": "Laptop", "category": "Electronics"},
    {"name": "Desk", "category": "Furniture"},
    {"name": "Mouse", "category": "Electronics"},
    {"name": "Chair", "category": "Furniture"},
    {"name": "Monitor", "category": "Electronics"}
]

# Write Python code to:
# 1. Count the number of products in each category.
# 2. Store the results in a dictionary called counts.
# 3. Use a for loop and an if statement.
# 4. Do not create separate variables for each category.
# 5. Print the dictionary.

counts = {}

for key in products:
    category = key["category"]

    if category not in counts:
        counts[category] = 0

    counts[category] += 1

print(counts)

# Day02 - Question 21

sales = [
    {"category": "Electronics", "revenue": 1200},
    {"category": "Furniture", "revenue": 500},
    {"category": "Electronics", "revenue": 800},
    {"category": "Clothing", "revenue": 300},
    {"category": "Furniture", "revenue": 700}
]

# Write Python code to:
# 1. Calculate total revenue for each category.
# 2. Store the results in a dictionary called totals.
# 3. Use a for loop and an if statement.
# 4. Print the dictionary.

totals = {}

for key in sales:
    category = key["category"]

    if category not in totals:
        totals[category] = 0

    totals[category] += key["revenue"]

print(totals)

# Day02 - Question 22

totals = {
    "Electronics": 2000,
    "Furniture": 1200,
    "Clothing": 300
}

# Write Python code to:
# 1. Find the category with the highest total revenue.
# 2. Print the category name and revenue.
# 3. Use a for loop and an if statement.
# 4. Do not use max().

largest = 0
name = ""

for key in totals:
    if totals[key] > largest:
        largest = totals[key]
        name = key

print(name, largest)

# Day02 - Question 23

salaries = {
    "Alice": 70000,
    "Bob": 45000,
    "Charlie": 85000,
    "David": 55000
}

# Write Python code to:
# 1. Find the employee with the lowest salary.
# 2. Print the employee's name and salary.
# 3. Use a for loop and an if statement.
# 4. Do not use min().

lowest = float("inf")
name = ""

for key in salaries:
    if salaries[key] < lowest:
        lowest = salaries[key]
        name = key
print(name, lowest)

# Day02 - Question 24

employees = [
    {"name": "Alice", "department": "IT", "salary": 70000},
    {"name": "Bob", "department": "Sales", "salary": 55000},
    {"name": "Charlie", "department": "IT", "salary": 80000},
    {"name": "David", "department": "Sales", "salary": 65000},
    {"name": "Emma", "department": "IT", "salary": 75000}
]

# Write Python code to:
# 1. Calculate the average salary for each department.
# 2. Store the results in a dictionary called averages.
# 3. Use for loops.
# 4. Do not create separate variables for IT and Sales.
# 5. Print the dictionary.

averages = {}
counts = {}

for key in employees:
    dept = key["department"]

    if dept not in averages:
        averages[dept] = 0
        counts[dept] = 0

    averages[dept] += key["salary"]
    counts[dept] += 1

for dept in averages:
    averages[dept] /= counts[dept]

print(averages)

# Day02 - Question 25

sales = [
    {"category": "Food", "amount": 100},
    {"category": "Drink", "amount": 50},
    {"category": "Food", "amount": 200},
    {"category": "Drink", "amount": 150}
]

# Write Python code to:
# 1. Calculate the total sales for each category.
# 2. Count the number of sales records in each category.
# 3. Store the average sales in a dictionary called averages.
# 4. Print the dictionary.

averages = {}
counts = {}

for key in sales:
    category = key["category"]

    if category not in averages:
        averages[category] = 0
        counts[category] = 0

    averages[category] += key["amount"]
    counts[category] += 1

for category in averages:
    averages[category] /= counts[category]

print(averages)

# Day02 - Question 26

employees = [
    {"name": "Alice", "department": "IT", "salary": 70000},
    {"name": "Bob", "department": "Sales", "salary": 55000},
    {"name": "Charlie", "department": "IT", "salary": 80000},
    {"name": "David", "department": "Sales", "salary": 65000},
    {"name": "Emma", "department": "IT", "salary": 75000}
]

averages = {
    "IT": 75000,
    "Sales": 60000
}

# Write Python code to:
# 1. Find employees earning more than their department's average salary.
# 2. Store their names in a list called high_earners.
# 3. Use a for loop and an if statement.
# 4. Print the list.

high_earners = []

for key in employees:
    dept = key["department"]

    if key["salary"] > averages[dept]:
        high_earners.append(key["name"])

print(high_earners)

# Day02 - Question 27

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 40},
    {"name": "Monitor", "price": 350},
    {"name": "Keyboard", "price": 150},
    {"name": "Tablet", "price": 760}
]

# Write Python code to:
# 1. Calculate the average price of all products.
# 2. Find products with a price below the average.
# 3. Store their names in a list called cheap_products.
# 4. Print the list.
# 5. Use for loops and an if statement.

cheap_products = []

total = 0
count = 0

for key in products:
    total += key["price"]
    count += 1
average = total / count

for key in products:
    if key["price"] < average:
        cheap_products.append(key["name"])

print(cheap_products)

# Day02 - Question 28

products = [
    {"name": "Laptop", "category": "Electronics", "cost": 800, "price": 1200},
    {"name": "Desk", "category": "Furniture", "cost": 200, "price": 350},
    {"name": "Mouse", "category": "Electronics", "cost": 20, "price": 50},
    {"name": "Chair", "category": "Furniture", "cost": 100, "price": 180},
    {"name": "Tablet", "category": "Electronics", "cost": 400, "price": 700}
]

# Write Python code to:
# 1. Calculate the profit (price - cost) for each product.
# 2. Calculate the total profit for each category.
# 3. Store the results in a dictionary called profits.
# 4. Use a for loop and an if statement.
# 5. Print the dictionary.

profits = {}

for key in products:
    category = key["category"]
    profit = key["price"] - key["cost"]

    if category not in profits:
        profits[category] = 0

    profits[category] += profit

print(profits)

# Day02 - Question 29

expenses = [
    {"department": "IT", "amount": 500},
    {"department": "HR", "amount": 300},
    {"department": "IT", "amount": 700},
    {"department": "Sales", "amount": 400},
    {"department": "HR", "amount": 200}
]

# Write Python code to:
# 1. Calculate total expenses for each department.
# 2. Store the results in a dictionary called totals.
# 3. Use a for loop and an if statement.
# 4. Print the dictionary.

totals = {}

for key in expenses:
    dept = key["department"]

    if dept not in totals:
        totals[dept] = 0

    totals[dept] += key["amount"]

print(totals)

# Day02 - Question 30

totals = {
    "IT": 1200,
    "HR": 500,
    "Sales": 400,
    "Marketing": 1500
}

# Write Python code to:
# 1. Find the department with the highest total expenses.
# 2. Print the department name and its total expenses.
# 3. Use a for loop and an if statement.
# 4. Do not use max().

highest = 0
name = ""

for key in totals:
    if totals[key] > highest:
        highest = totals[key]
        name = key

print(name, highest)

# Day02 - Question 31

employees = [
    {"name": "Alice", "salary": 70000, "performance": 85},
    {"name": "Bob", "salary": 55000, "performance": 92},
    {"name": "Charlie", "salary": 80000, "performance": 78},
    {"name": "David", "salary": 65000, "performance": 90},
    {"name": "Emma", "salary": 75000, "performance": 88}
]

# Write Python code to:
# 1. Find employees whose salary is at least 60,000 
# AND performance score is at least 85.
# 2. Store their names in a list called eligible.
# 3. Use a for loop and an if statement.
# 4. Print the list.

eligible = []

for key in employees:
    if key["salary"] >= 60000 and key["performance"] >= 85:
        eligible.append(key["name"])

print(eligible)

# Day02 - Question 32

inventory = [
    {"name": "Laptop", "stock": 5, "price": 1200},
    {"name": "Mouse", "stock": 20, "price": 40},
    {"name": "Monitor", "stock": 3, "price": 350},
    {"name": "Keyboard", "stock": 8, "price": 150},
    {"name": "Tablet", "stock": 2, "price": 800}
]

# Write Python code to:
# 1. Find products with stock less than 10 AND price greater than 200.
# 2. Store their names in a list called restock.
# 3. Use a for loop and an if statement.
# 4. Print the list.

restock = []

for key in inventory:
    if key["stock"] < 10 and key["price"] > 200:
        restock.append(key["name"])

print(restock)

# Day02 - Question 33

employees = [
    {"name": "Alice", "department": "IT", "performance": 85},
    {"name": "Bob", "department": "Sales", "performance": 65},
    {"name": "Charlie", "department": "IT", "performance": 55},
    {"name": "David", "department": "HR", "performance": 72},
    {"name": "Emma", "department": "Sales", "performance": 60}
]

# Write Python code to:
# 1. Find employees whose performance score is below 70 OR whose department is HR.
# 2. Store their names in a list called training.
# 3. Use a for loop and an if statement.
# 4. Print the list.

training = []

for key in employees:
    if key["performance"] < 70 or key["department"] == "HR":
        training.append(key["name"])

print(training)