# Split into list of strings
values = input("Enter 3 numbers (space separated): ").split()
print(values)
numbers = [float(num) for num in values]  # Convert to floats

print(numbers)
### IMPORTANT:
# - Default split() uses whitespace
# - Can specify delimiter: split(',') for CSV input
# - List comprehensions efficient for conversion

print(eval("42+41"))
