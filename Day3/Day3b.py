#Tuple and its properties
colors = ("red", "green", "blue", "yellow", "indigo", "purple","red")
print(type(colors))
print(colors[0])
print(colors[0::1])   
print(colors[::])
print(colors[-1])
print(colors[0:2])
print(colors[:2])   
print(colors[::-1])
print(len(colors))
print(colors.count("red"))
print(colors.index("green"))
# colors[3] = "orange"  # This will raise an error because tuples are immutable
colours = colors + ("orange",)  # This creates a new tuple with the added color
print(colours)
