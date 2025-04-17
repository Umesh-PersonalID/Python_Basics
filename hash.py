# ============================================
# 🔐 PYTHON HASHING - FULL TUTORIAL
# ============================================

# ------------------------------------------------
# 1. WHAT IS HASHING?
# ------------------------------------------------
# Hashing is the process of converting data (like strings or objects)
# into a fixed-size numerical value (the "hash").
# In Python, hashing is widely used in:
# - Dictionaries and Sets
# - Implementing custom keys in dict
# - Cryptographic operations
# - Hash tables and data deduplication

# ------------------------------------------------
# 2. THE `hash()` FUNCTION
# ------------------------------------------------
# Built-in function to return a hash value (integer) for a hashable object.

PYTHONHASHSEED=0
print("Hash of 'hello':", hash("hello"))        # Output: varies by session
print("Hash of number 123:", hash(123))         # Stable output: 123
print("Hash of a tuple:", hash((1, 2, 3)))       # Tuples are hashable

# ⚠️ By default, hash of str objects is randomized between runs for security
# Run Python with PYTHONHASHSEED=0 to make it consistent (for testing)

# ------------------------------------------------
# 3. HASHABLE VS UNHASHABLE OBJECTS
# ------------------------------------------------
# ✅ Immutable objects are hashable (str, int, float, tuple with hashable elements)
# ❌ Mutable objects are NOT hashable (list, dict, set)

try:
    hash([1, 2, 3])  # Will raise TypeError
except TypeError as e:
    print("Error:", e)

# ------------------------------------------------
# 4. USING HASH IN DICTIONARIES / SETS
# ------------------------------------------------
# Hashing is how dict and set find and store keys efficiently (in O(1) time avg.)

my_dict = {}
my_dict["apple"] = 10
my_dict["banana"] = 20

my_dict["apple"] += 10

print(my_dict)
# Internally, keys are hashed:
print("Hash of 'apple' key:", hash("apple"))


# ------------------------------------------------
# 6. HASH COLLISIONS
# ------------------------------------------------
# When two different objects produce the same hash.
# Python handles collisions internally with chaining/probing.
# Good hash functions reduce collisions.

# Example (not forced, but shows principle):
print("Hash of 42:", hash(42))
print("Hash of True:", hash(True))       # True is also 1 → same hash as 1

# ------------------------------------------------
# 7. `hashlib` MODULE FOR CRYPTOGRAPHIC HASHES
# ------------------------------------------------
# Use hashlib for secure hashing (MD5, SHA256, etc.)

import hashlib

# Create a SHA256 hash of a string
data = "mysecretpassword".encode()
sha = hashlib.sha256(data).hexdigest()
print("SHA256 of password:", sha)

# Other common hashes: hashlib.md5(), hashlib.sha1(), hashlib.sha512()

# ------------------------------------------------
# 8. FROZENSET USE CASE
# ------------------------------------------------
# frozenset is a hashable version of set → can be used as dict keys

fs = frozenset([1, 2, 3])
my_map = {fs: "frozen key"}
print(my_map[fs])
print("Using frozenset as key:", my_map[frozenset([1, 2, 3])])  # Works

# ------------------------------------------------
# 9. REHASHING
# ------------------------------------------------
# Dictionaries and sets automatically rehash (resize) as elements grow
# This is why Python dict/set give near-constant time lookup

# ------------------------------------------------
# 10. KEY TIPS & CAVEATS
# ------------------------------------------------
# ✅ Use only immutable (hashable) objects as dict/set keys
# ✅ hash() gives fast lookup but not secure → use hashlib for cryptography
# ✅ Hash collisions are rare but should be handled carefully in custom hash tables

# ------------------------------------------------
# ✅ SUMMARY
# ------------------------------------------------
# - hash() → Fast, built-in hashing for Python objects (dict/set keys)
# - hashlib → Secure, cryptographic hashes (SHA256, MD5)
# - Custom objects need __hash__ and __eq__ to be used in sets/dicts
# - Only immutable objects can be hashed (str, int, tuple, frozenset)
# - Avoid using mutable fields in __hash__ implementation