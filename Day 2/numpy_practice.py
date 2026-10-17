
# Day 2 - NumPy Practice

import numpy as np

print("Welcome to NumPy Practice!")

# Creating an array
marks = np.array([70, 80, 90, 60, 100])
print("Marks:", marks)

# Sum and Average
print("Total Marks:", np.sum(marks))
print("Average Marks:", np.mean(marks))

# Multiplication and Addition
print("Marks multiplied by 2:", marks * 2)
print("Marks plus 2:", marks + 2)

# Creating another array
numbers = np.array([10, 20, 30, 40, 50])
print("Numbers:", numbers)
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))
