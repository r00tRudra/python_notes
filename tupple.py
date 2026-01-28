# tuple_operations_demo.py
# Demonstration of common Python tuple operations and methods

# -----------------------------
# Tuple creation
# -----------------------------
numbers = (1, 2, 3, 4)
colors = ("red", "green", "blue")
days = ("Mon", "Tue", "Wed", "Thu", "Fri")
fruits = ("apple", "banana", "orange", "apple")
grades = (10, 9, 10, 8)
months = ("January", "February", "March", "July", "August")
coordinates = (10, 20, 30)

print("Initial tuples:")
print("numbers:", numbers)
print("colors:", colors)
print("days:", days)

# -----------------------------
# len() → Number of elements
# -----------------------------
print("\nlen(numbers):", len(numbers))  # 4

# -----------------------------
# Indexing [i] → Access element
# -----------------------------
print("\ncolors[1]:", colors[1])  # green

# -----------------------------
# Slicing [start:end] → Sub-tuple
# -----------------------------
print("\ndays[1:4]:", days[1:4])  # ('Tue', 'Wed', 'Thu')

# -----------------------------
# in operator → Membership test
# -----------------------------
print("\nIs 'apple' in fruits?", "apple" in fruits)
print("Is 'cherry' in fruits?", "cherry" in fruits)

# -----------------------------
# count() → Count occurrences
# -----------------------------
print("\ngrades.count(10):", grades.count(10))  # 2

# -----------------------------
# index() → Find first position
# -----------------------------
print("\nIndex of 'July' in months:", months.index("July"))

# -----------------------------
# Concatenation + → Join tuples
# -----------------------------
combined = (1, 2) + (3, 4)
print("\n(1, 2) + (3, 4):", combined)

# -----------------------------
# Repetition * → Repeat tuple
# -----------------------------
pattern = ("-",) * 3
print("\n('-',) * 3:", pattern)

# -----------------------------
# Unpacking → Assign multiple values
# -----------------------------
x, y, z = coordinates
print("\nUnpacking coordinates:")
print("x =", x, "y =", y, "z =", z)

# -----------------------------
# * Unpacking (extended)
# -----------------------------
numbers2 = (1, 2, 3, 4, 5, 6)
head, *middle, tail = numbers2
print("\nExtended unpacking:")
print("head:", head)
print("middle:", middle)
print("tail:", tail)

# -----------------------------
# tuple() → Convert to tuple
# -----------------------------
list_data = [1, 2, 3]
range_data = range(4)
string_data = "abc"

print("\ntuple([1,2,3]):", tuple(list_data))
print("tuple(range(4)):", tuple(range_data))
print("tuple('abc'):", tuple(string_data))

# -----------------------------
# Single element tuple
# -----------------------------
single = (42,)
not_a_tuple = (42)

print("\nSingle element tuple:", single)
print("Type of (42,):", type(single))
print("Type of (42):", type(not_a_tuple))  # int, not tuple

# -----------------------------
# for loop → Iterate over tuple
# -----------------------------
print("\nIterating over coordinates:")
for item in coordinates:
    print(item)

# -----------------------------
# End of demo
# -----------------------------
print("\nAll tuple operations demonstrated successfully!")
