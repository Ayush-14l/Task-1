# Creating tuples
tuple1 = (10, 20, 30, 40, 50)
tuple2 = (60, 70, 80)

# Accessing elements
print("First element:", tuple1[0])
print("Last element:", tuple1[-1])

# Slicing
print("Sliced tuple (1 to 4):", tuple1[1:4])

# Concatenation
combined_tuple = tuple1 + tuple2
print("Concatenated tuple:", combined_tuple)

# Repetition
repeated_tuple = tuple2 * 3
print("Repeated tuple:", repeated_tuple)

# Count
numbers = (1, 2, 3, 2, 4, 2, 5)
print("Count of 2:", numbers.count(2))

# Index
print("Index of 4:", numbers.index(4))