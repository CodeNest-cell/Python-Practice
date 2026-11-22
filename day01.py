# Day01 - Question 1/3

# Task: Create two variables, a = 100 and b = 40. Print their difference.

a = 100
b = 40

print(a-b)

# Day01 - Question 2/3

# Task: Given the following list:

numbers = [10, 20, 30, 40, 50]

# Write Python code to calculate and print the average of the numbers.

total = 0 

for i in numbers:
    total += i
average = total / len(numbers)
print(average)

# Day01 - Question 3/3

# Task: Given the following list:

numbers = [15, 42, 8, 67, 23]

# Write Python code to print the largest number in the list.

largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i
print(largest)

# Day01 - Question 4

# Task: Given the following list:

numbers = [12, 45, 8, 67, 23, 90, 14]

# Write Python code to print only the numbers greater than 30.

for i in numbers:
    if i > 30:
        print(i)

# Day01 - Question 5

# Task: Given the following list:

numbers = [10, 25, 30, 45, 50, 65]

# Write Python code to count how many numbers are 
# greater than or equal to 30.

count = 0
for i in numbers:
    if i >= 30:
        count += 1
print(count)

# Day01 - Question 6

# Task: Given the following list:

numbers = [10, 20, 30, 40, 50]

# Write Python code to create a new list 
# containing each number multiplied by 2.

# Print the new list.

result = []

for i in numbers:
    result.append(i*2)

print(result)

# Day01 - Question 7

# Task: Given the following list:

numbers = [5, 12, 18, 7, 24, 9, 30]

# Create a new list containing only the even numbers.

# Print the new list.

result = []
for i in numbers:
    if i % 2 == 0:
        result.append(i)
print(result)

# Day01 - Question 8

# Task: Given the following dictionary:

employee = {
    "name": "John",
    "department": "Finance",
    "salary": 75000
}

# Write Python code to print the employee's name and salary.

print(employee["name"])
print(employee["salary"])

# Day01 - Question 9

# Task: Given the following dictionary:

prices = {
    "apple": 3,
    "banana": 2,
    "orange": 4
}

# Write Python code to increase every price by 
# 10% and print the updated dictionary.

for key in prices:
    prices[key] *= 1.10

print(prices)

# Day01 - Question 10

# Task: Given the following dictionary:

scores = {
    "Alice": 85,
    "Bob": 62,
    "Charlie": 91,
    "David": 74
}

# Write Python code to print only the names of 
# students whose scores are 80 or higher.

for key in scores:
    if scores[key] >= 80:
        print(key)

# Day01 - Question 11

# Task: Given the following dictionary:

sales = {
    "January": 1200,
    "February": 1500,
    "March": 1800
}

# Write Python code to calculate and print the total sales.

total = 0

for key in sales:
    total += sales[key]

print(total)