# Create Dictionary
student = {
    "name": "Rahul",
    "age": 21,
    "city": "Hyderabad",
    "marks": 90
}

print(type(student))
print(student)
print(student["name"])
print(student["age"])
print(student.get("age"))
print(student.get("phone", "Not Found"))
print(student.get("marks"))
student["course"] = "Python"
print(student)
student["age"] = 22
print(student)
student.update({"city": "Mumbai", "marks": 85})
print(student)
print("name" in student)
print(student.keys())
print(student.values())
print(student.items())
print(len(student))
removed = student.pop("marks")
print(student)
del student["course"]
print(student)
student.clear()
print(student)
# Iteration over dictionary
for key in student:
    print(key)
for value in student.values():
    print(value)
for key, value in student.items():
    print(key, ":", value)