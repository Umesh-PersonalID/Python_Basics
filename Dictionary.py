empty_dict = {}  
empty_dict_alt = dict()  

# Key-value pairs  
person = {"name": "Alice", "age": 30, "city": "NY"}  

# From sequence of tuples  
dict_from_tuples = dict((("a", 1), ("b", 2)))  # {'a': 1, 'b': 2}  

# Dict comprehension  
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}  

# Keys must be hashable (immutable: int, str, tuple)  
# Values can be any type  

print(squares)


d = {"name": "Bob", "age": 25}  

# Get value by key (O(1) avg, O(n) worst-case due to hash collisions)  
print(d["name"])  # "Bob"  

# get() method (safe, returns None/default if key missing)  
print(d.get("age"))      # 25  
print(d.get("salary",34000))    # None  
print(d.get("salary", 0)) # 0 (default)  

# Keys(), values(), items() views (O(1) to create, iteration is O(n))  
print(d.keys())    # dict_keys(['name', 'age'])  
print(d.values())  # dict_values(['Bob', 25])  
print(d.items())   # dict_items([('name', 'Bob'), ('age', 25)])  



d = {"a": 1, "b": 2}  

# Add/update (O(1) avg)  
d["c"] = 3           # {'a': 1, 'b': 2, 'c': 3}  
d.update({"b": 99})  # Updates 'b' to 99  
print(d)
d["b"] = 23
print(d)

# Remove (O(1) avg)  
del d["a"]           # Removes 'a'  
val = d.pop("b")     # Removes 'b' and returns 99  
d.popitem()          # Removes and returns last inserted (Python 3.7+)  

# Clear (O(1))  
d.clear()            # {}  

# setdefault() (get or set if missing)  
d.setdefault("x", 100)  # Sets 'x':100 if not present  



d = {"a": 1, "b": 2}  

# Membership (O(1) avg)  
print("a" in d)      # True  
print(1 in d)        # False (checks keys, not values)  

# Length (O(1))  
print(len(d))        # 2  


d = {"x": 10, "y": 20}  
keys = d.keys()  
values = d.values()  

# Views reflect live changes  
d["z"] = 30  
print(keys)    # dict_keys(['x', 'y', 'z'])  
print(values)  # dict_values([10, 20, 30])  

# Can be converted to lists  
list_keys = list(keys)  # ['x', 'y', 'z']  

d1 = {"a": 1, "b": 2}  
d2 = {"b": 99, "c": 3}  

# Merge (O(n), new dict)  
merged = d1 | d2        # {'a': 1, 'b': 99, 'c': 3}  
print(merged)
# Update in-place (O(m), m=len(d2))  
d1 |= d2                # d1 = {'a': 1, 'b': 99, 'c': 3}  



# Transform keys/values (O(n))  
d = {"a": 1, "b": 2}  
flipped = {v: k for k, v in d.items()}  # {1: 'a', 2: 'b'}  

# Filter items  
filtered = {k: v for k, v in d.items() if v > 1}  # {'b': 2}  


flipped = {v: k for k, v in d1.items()}
