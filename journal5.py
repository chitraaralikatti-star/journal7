import sys

# Program to calculate Simple Interest without using data types explicitly
# Usage:
# python simple_interest.py 1000 5 2

if len(sys.argv) == 4:
    principal = sys.argv[1]
    rate = sys.argv[2]
    time = sys.argv[3]
    print("User provided input values:")
else:
    print("No input given - using default values:")
    principal = "1000"
    rate = "5"
    time = "2"

# Calculation
simple_interest = (eval(principal) * eval(rate) * eval(time)) / 100

# Output
print("Principal Amount:", principal)
print("Rate of Interest:", rate)
print("Time Period (years):", time)
print("Simple Interest =", simple_interest)
