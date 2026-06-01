# Creating a list
fruits = ["Apple", "Banana", "Mango", "Orange"]

# Accessing elements
print("First element:", fruits[0])
print("Last element:", fruits[-1])
print("Slicing (1 to 3):", fruits[1:3])

# Modifying elements
fruits[1] = "Grapes"
print("After modification:", fruits)

# Adding elements
fruits.append("Pineapple")
print("After append:", fruits)

fruits.insert(2, "Kiwi")
print("After insert:", fruits)

# Removing elements
fruits.remove("Mango")
print("After remove:", fruits)

removed_item = fruits.pop()
print("Popped item:", removed_item)
print("After pop:", fruits)

# Other methods
numbers = [5, 2, 8, 1, 5]

numbers.sort()
print("Sorted list:", numbers)

numbers.reverse()
print("Reversed list:", numbers)

numbers.extend([10, 20, 30])
print("Extended list:", numbers)

print("Count of 5:", numbers.count(5))

print("Index of 8:", numbers.index(8))

copy_list = numbers.copy()
print("Copied list:", copy_list)

# Clear list
numbers.clear()
print("After clear:", numbers)