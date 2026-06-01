# Creating a dictionary
student = {
    "name": "Ayush",
    "age": 18,
    "course": "AI & ML"
}

print("Original Dictionary:", student)

# get()
print("Name:", student.get("name"))

# keys()
print("Keys:", student.keys())

# values()
print("Values:", student.values())

# items()
print("Items:", student.items())

# update()
student.update({"age": 19, "city": "Pune"})
print("After update:", student)

# pop()
removed_value = student.pop("course")
print("Removed Value:", removed_value)
print("After pop:", student)