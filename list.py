# .append()          # add one
# .extend()          # add many
# .pop()             # take from end
# .pop(0)            # take from front (slow)
# .remove(value)     # remove by value
# .clear()           # empty it
# .sort()            # sort in-place
# sorted()           # new sorted version
# [::-1]              # reverse copy
# .copy() / [:]      # proper copy!




# list_methods_demo.py
# Demonstration of common Python list methods

# -----------------------------
# Initial list
# -----------------------------
fruits = ["apple", "orange", "banana"]
print("Initial fruits:", fruits)

# -----------------------------
# .append() → Add one item at the end
# -----------------------------
fruits.append("mango")
print("\nAfter append('mango'):", fruits)

# -----------------------------
# .extend() / += → Add multiple items
# -----------------------------
fruits.extend(["kiwi", "grape"])
print("\nAfter extend(['kiwi', 'grape']):", fruits)

fruits += ["pineapple"]
print("After += ['pineapple']:", fruits)

# -----------------------------
# .insert() → Insert at specific index
# -----------------------------
fruits.insert(1, "pear")
print("\nAfter insert(1, 'pear'):", fruits)

# -----------------------------
# .pop() → Remove & return last item
# -----------------------------
last_item = fruits.pop()
print("\nPopped last item:", last_item)
print("After pop():", fruits)

# -----------------------------
# .pop(0) → Remove & return first item (slow)
# -----------------------------
first_item = fruits.pop(0)
print("\nPopped first item:", first_item)
print("After pop(0):", fruits)

# -----------------------------
# .remove() → Remove first occurrence by value
# -----------------------------
fruits.remove("banana")
print("\nAfter remove('banana'):", fruits)

# -----------------------------
# .clear() → Remove all elements
# -----------------------------
temp_list = fruits.copy()
temp_list.clear()
print("\nAfter clear():", temp_list)

# -----------------------------
# .index() → Find index of value
# -----------------------------
index_orange = fruits.index("orange")
print("\nIndex of 'orange':", index_orange)

# -----------------------------
# .count() → Count occurrences
# -----------------------------
fruits.append("apple")
apple_count = fruits.count("apple")
print("\nApple count:", apple_count)
print("Fruits now:", fruits)

# -----------------------------
# .sort() → Sort list in-place
# -----------------------------
numbers = [5, 1, 4, 2, 3]
numbers.sort()
print("\nSorted numbers (in-place):", numbers)

# -----------------------------
# sorted() → Return new sorted list
# -----------------------------
names = ["Rudra", "Ankit", "Zoya", "Manish"]
sorted_names = sorted(names)
print("\nOriginal names:", names)
print("Sorted names (new list):", sorted_names)

# -----------------------------
# .reverse() → Reverse in-place
# -----------------------------
numbers.reverse()
print("\nReversed numbers:", numbers)

# -----------------------------
# in operator → Membership test
# -----------------------------
print("\nIs 'apple' in fruits?", "apple" in fruits)
print("Is 'cherry' in fruits?", "cherry" in fruits)

# -----------------------------
# len() → Number of elements
# -----------------------------
print("\nNumber of fruits:", len(fruits))

tasks = []
if len(tasks) == 0:
    print("Task list is empty")

# -----------------------------
# List slicing → Sub-lists / copying
# -----------------------------
print("\nOriginal fruits:", fruits)

print("fruits[1:4]:", fruits[1:4])   # slice
print("fruits[:]:", fruits[:])       # copy
print("fruits[::-1]:", fruits[::-1]) # reversed copy

# -----------------------------
# End of demo
# -----------------------------
print("\nAll list methods demonstrated successfully!")
