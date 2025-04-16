a = 5    # Binary: 0101
b = 3   # Binary: 0011

# AND (Sets bit to 1 if both bits are 1)
print(a & b)   # 1 (0101 & 0011 = 0001) → __and__

# OR (Sets bit to 1 if at least one bit is 1)
print(a | b)   # 7 (0101 | 0011 = 0111) → __or__

# XOR (Sets bit to 1 if bits are different)
print(a ^ b)   # 6 (0101 ^ 0011 = 0110) → __xor__

# NOT (Inverts all bits)
print(~a)      # -6 (Two's complement: ~0101 = 1010 → -6) → __invert__

# Left Shift (Shifts bits left, fills with 0)
print(a << 1)  # 10 (0101 << 1 = 1010) → __lshift__

# Right Shift (Shifts bits right, fills with 0)
print(a >> 1)  # 2 (0101 >> 1 = 0010) → __rshift__

### IMPORTANT NOTES:
# - Works on integers (converted to binary internally)
# - Negative numbers use Two's complement representation
# - Bitwise ops are faster than arithmetic ops for low-level optimizations


x = 5
x &= 3    # x = x & 3 → 1 (__iand__)
x |= 2    # x = x | 2 → 3 (__ior__)
x ^= 1    # x = x ^ 1 → 2 (__ixor__)
x <<= 2  # x = x << 2 → 8 (__ilshift__)
x >>= 1   # x = x >> 1 → 4 (__irshift__)

### IMPORTANT NOTES:
# - Modifies variable in-place
# - Useful for compact bitmask updates


num = 6
if num & 1:  # Last bit check (0=even, 1=odd)
    print("Odd")
else:
    print("Even")  # Output: Even


print(-5 >> 1)


# BITWISE (&, |) work on BITS
print(5 & 3)   # 1 (0101 & 0011 = 0001)

# LOGICAL (and, or) work on BOOLEANS
print(5 and 3 and 6 and 7 and 0 and 6) # 3 (returns last truthy value)

### IMPORTANT NOTES:
# - Bitwise ops have higher precedence than logical ops
# - Use parentheses to avoid confusion: (a & b) == c


# From highest to lowest:
# 1. ~ (Bitwise NOT)
# 2. <<, >> (Shifts)
# 3. & (Bitwise AND)
# 4. ^ (Bitwise XOR)
# 5. | (Bitwise OR)

print(1 << 1 + 2)   # 8 (1 << (1 + 2)), not (1 << 1) + 2    

binary = "1110"
print(int(binary, 2))