# List and Dict comprehension
# List comprehension
squares = [x**2 for x in range(1, 11)]
print(squares)

even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(even_squares) 

# Dictionary comprehension
cubed_dict = {x: x**3 for x in range(1, 11)}
print(cubed_dict)

even_cubed = {x: x**3 for x in range(1, 11) if x % 2 == 0}
print(even_cubed)
