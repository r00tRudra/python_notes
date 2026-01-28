# dictionary_methods_demo.py
# Demonstration of common Python dictionary methods and operations
# This for revision
# Must remember all the functions


# -----------------------------
# Dictionary creation
# -----------------------------
student = {
    "name": "Rudra",
    "age": 20,
    "course": "Cyber Security"
}

print("Initial dictionary:")
print(student)

# -----------------------------
# len() → Number of key-value pairs
# -----------------------------
print("\nlen(student):", len(student))

# -----------------------------
# Access value by key
# -----------------------------
print("\nstudent['name']:", student["name"])

# -----------------------------
# .get() → Safe access (no KeyError)
# -----------------------------
print("\nstudent.get('age'):", student.get("age"))
print("student.get('grade'):", student.get("grade"))          # None
print("student.get('grade', 'Not found'):", student.get("grade", "Not found"))

# -----------------------------
# Add / Update item
# -----------------------------
student["grade"] = "A"
student["age"] = 21
print("\nAfter adding/updating keys:")
print(student)

# -----------------------------
# in operator → Check if key exists
# -----------------------------
print("\nIs 'name' in student?", "name" in student)
print("Is 'email' in student?", "email" in student)

# -----------------------------
# .keys() → Get all keys
# -----------------------------
print("\nKeys:", student.keys())

# -----------------------------
# .values() → Get all values
# -----------------------------
print("Values:", student.values())

# -----------------------------
# .items() → Get key-value pairs
# -----------------------------
print("Items:", student.items())

# -----------------------------
# for loop → Iterate dictionary
# -----------------------------
print("\nIterating over dictionary:")
for key, value in student.items():
    print(f"{key} → {value}")

# -----------------------------
# .update() → Merge another dictionary
# -----------------------------
extra_info = {"email": "rudra@example.com", "city": "Kolkata"}
student.update(extra_info)
print("\nAfter update():")
print(student)

# -----------------------------
# .pop() → Remove & return value by key
# -----------------------------
removed_age = student.pop("age")
print("\nRemoved age:", removed_age)
print("After pop('age'):", student)

# -----------------------------
# .popitem() → Remove & return last inserted item
# -----------------------------
last_item = student.popitem()
print("\nPopitem():", last_item)
print("After popitem():", student)

# -----------------------------
# del → Delete key
# -----------------------------
del student["city"]
print("\nAfter del student['city']:", student)

# -----------------------------
# .setdefault() → Get or set default value
# -----------------------------
student.setdefault("phone", "Not provided")
student.setdefault("name", "Unknown")  # won't overwrite
print("\nAfter setdefault():")
print(student)

# -----------------------------
# .copy() → Shallow copy
# -----------------------------
student_copy = student.copy()
print("\nCopied dictionary:")
print(student_copy)

# -----------------------------
# .clear() → Remove all items
# -----------------------------
temp = student.copy()
temp.clear()
print("\nAfter clear():", temp)

# -----------------------------
# Dictionary comprehension
# -----------------------------
squares = {x: x**2 for x in range(1, 6)}
print("\nDictionary comprehension (squares):")
print(squares)

# -----------------------------
# Nested dictionary
# -----------------------------
users = {
    "user1": {"role": "admin", "active": True},
    "user2": {"role": "guest", "active": False}
}

print("\nNested dictionary access:")
print("user1 role:", users["user1"]["role"])

# -----------------------------
# End of demo
# -----------------------------
print("\nAll dictionary methods demonstrated successfully!")
