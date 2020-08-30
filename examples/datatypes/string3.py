# Finding length of a string
name = "Kapil Sharma"
print(len(name))  # Output: 12 (Note: Space is also a character)

# String indexing
# String index starts with 0
print(name[0])  # Output: K
print(name[3])  # Output: i

# Negative index: Starting with -1, negative index are index in reverse order like
# (String)       :   K   a   p   i   l       S   h   a   r   m   a
# (Index)        :   0   1   2   3   4   5   6   7   8   9  10  11
# (Reverse index): -12 -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1
print(name[-2])  # Output: m

# Slicing
# In Python, we use index for slicing as well. Index is [start:end(excluding):step
print(name[3])   # Output: i
# If we do not provide 'end'(Number after first :), it mean end of string.
print(name[3:])  # Output: il Sharma
# If wo do not provide 'start'(Number before first :), it mean start of string.
# Note: 'end' (3) is exclusive. This output will be 'Kap', not 'Kapi'.
print(name[:3])  # Output: Kap
# We can also use negative index
print(name[-3:])  # Output: rma
print(name[:-3])  # Output: Kapil Sha

# Step - Default 1
print(name[::1])  # Output: Kapil Sharma
print(name[::2])  # Output: KplSam
# Trick: We can use step as -1 to reverse string
print(name[::-1])  # Output: amrahS lipaK
