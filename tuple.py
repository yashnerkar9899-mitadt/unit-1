# Create a nested tuple
tuple1 = (10, 20, (30, 40, 50), 60)
print("Nested Tuple:", tuple1)

# Access elements from nested tuple
print("First element:", tuple1[0])
print("Nested tuple element:", tuple1[2])
print("Element from nested tuple:", tuple1[2][1])

# Repetition of tuple
repeated_tuple = tuple1 * 2
print("\nRepeated Tuple:", repeated_tuple)

# Create another tuple
tuple2 = (70, 80, 90)

# Concatenation of tuples
concatenated_tuple = tuple1 + tuple2
print("\nConcatenated Tuple:", concatenated_tuple)
