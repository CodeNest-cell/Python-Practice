# Day05 - Question 1/3

# Print the average score for each class.

totals = {"A": 240, "B": 150}
counts = {"A": 3, "B": 2}

for clas in totals:
    average = totals[clas] / counts[clas]
    print(clas, average)

# Day05 - Question 2/3

# Save each class average in the averages dictionary.

totals = {"A": 240, "B": 150}
counts = {"A": 3, "B": 2}
averages = {}

for clas in totals:
    average = totals[clas] / counts[clas]
    averages[clas] = average

print(averages)

# Day05 - Question 3/3

# Print the names of classes with an average score of 80 or higher.

averages = {"A": 80.0, "B": 75.0, "C": 90.0}

for clas in averages:
    if averages[clas] >= 80:
        print(clas)

# Day05 - Question 4

# Add the class name to selected when its average is 80 or higher.

averages = {"A": 80.0, "B": 75.0, "C": 90.0}
selected = []

for clas in averages:
    if averages[clas] >= 80:
        selected.append(clas)

print(selected) 

# Day05 - Question 5

# Save each class with an average of 80 or higher in the selected dictionary. 
# Use the class name as the key and its average as the value.

averages = {"A": 80.0, "B": 75.0, "C": 90.0}
selected = {}

for clas in averages:
    if averages[clas] >= 80:
        selected[clas] = averages[clas]

print(selected)