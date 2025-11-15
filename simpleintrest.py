import sys 
# Program to calculate Simple Interest 
# Usage: 
# python simple_interest.py 1000 5 2 
# If arguments are not given, default values will be used. 
if len(sys.argv) == 4: 
# Take input from system arguments 
principal = float(sys.argv[1]) 
rate = float(sys.argv[2]) 
time = float(sys.argv[3]) 
else: 
# Default values if user does not give arguments 
print("No command-line inputs provided. Using default values:") 
principal = float(input("Enter Principal Amount: ")) 
rate = float(input("Enter Rate of Interest: ")) 
time = float(input("Enter Time Period (in years): ")) 
simple_interest = (principal * rate * time) / 100 
print("Simple Interest =", simple_interest)