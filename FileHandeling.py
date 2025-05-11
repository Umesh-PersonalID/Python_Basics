"""
=========================
PYTHON FILE HANDLING
=========================

File handling allows you to read, write, and manage files in Python.

Built-in functions: `open()`, `read()`, `write()`, `close()`
Use context manager (`with open(...) as f:`) to handle files safely.
"""

# ========== PART 1: OPENING A FILE ==========

# Syntax: open(filename, mode)
# Modes:
#   'r' → read (default)
#   'w' → write (truncates file)
#   'a' → append
#   'x' → create (error if file exists)
#   'b' → binary mode
#   't' → text mode (default)

print("Reading file contents:")

# Make a sample file
with open("sample.txt", "w") as f:
    f.write("Hello, Umesh!\nWelcome to file handling.\nPython is fun.")

# Read the file
with open("sample.txt", "r") as f:
    content = f.read()  # Reads the whole file as a string
    print(content)


# ========== PART 2: READING LINE BY LINE ==========

print("\nReading line by line:")

with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())  # strip removes \n



# ========== PART 4: APPENDING TO FILE ==========

print("\nAppending to the file:")

with open("sample.txt", "a") as f:
    f.write("\nAppended line 3\n")

# Confirm appended
with open("sample.txt", "r") as f:
    print(f.read())
