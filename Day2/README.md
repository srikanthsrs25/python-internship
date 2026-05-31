# Files

Day2a.py
Day2b.py
Day2c.py
Day2d.py
README.md

# Topics Covered

conditional statements 
looping/Iterative statements 
jumping statements
prime checking 
FrizzBuzz
Functions
Docstring
LLM comparision

# in Gemini AI : 
An array is a fundamental data structure in computer programming used to store a collection of items. Think of it as a row of numbered boxes, where each box holds a single piece of data.

Here is everything you need to know about how they work, broken down simply.

1. Key Characteristics of an Array
Same Data Type: All items in an array must usually be of the same type (e.g., all integers, all strings, or all decimals).

Fixed Size: In most traditional programming languages, you must specify the size of the array when you create it, and it cannot be changed later.

Contiguous Memory: Behind the scenes, the computer stores an array in a continuous, unbroken block of memory. This is what makes arrays incredibly fast to work with.

2. How Arrays Work: Elements and Indexes
To find a specific item in an array, you use two main concepts:

Element: The actual data or value stored inside the slot.

Index: The address or position number of the slot.

# in copilot:
what is an array ?
An array is a way to store multiple items in a single place.
Simple explanation
Think of an array like a row of boxes:

Each box holds one value (like a number, name, or object).
All boxes are stored together under one name.
Each box has a position called an index.


Example
If you have marks of 5 students:
Instead of writing:
mark1 = 80
mark2 = 75
mark3 = 90

You can use an array:
marks = [80, 75, 90, 60, 85]



# in chatgpt :
what is an array ?
An array is a data structure used to store a collection of items in a specific order.

You can think of it like a row of numbered boxes:

each box stores one value
each box has an index (position number)
you can quickly access values using the index

Example array:

[10, 20, 30, 40]

Here:

10 is at index 0
20 is at index 1
30 is at index 2
40 is at index 3

# in claude :
 
what is an array ?
An array is a data structure that stores a collection of elements in a contiguous block of memory, accessible by numeric index.

Key characteristics:

Indexed — Elements are accessed by position (usually starting at 0). arr[2] retrieves the third element.
Fixed or dynamic size — In some languages (C, Java), arrays have a fixed length declared at creation. In others (Python lists, JavaScript arrays), they can grow or shrink.
Homogeneous or heterogeneous — Typed languages often require all elements to be the same type; dynamically typed languages allow mixed types.
Fast access — Retrieving an element by index is O(1) because the memory address can be calculated directly.

Simple example (JavaScript):

javascript

const fruits = ["apple", "banana", "cherry"];
console.log(fruits[1]); // "banana"

 

