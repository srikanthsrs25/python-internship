import csv
# Data
students = {
    "Amit": [80, 90, 85, 88, 92],
    "Sara": [70, 75, 72, 78, 80],
    "John": [60, 65, 68, 70, 75],
    "maya": [90, 95, 92, 88, 94],
    "sarah": [85, 80, 82, 88, 90],
    "Ravi": [75, 80, 78, 82, 85],
    "Ram": [65, 70, 68, 72, 75],
    "Priya": [95, 98, 92, 90, 94],
    "Anita": [80, 85, 88, 90, 92],
    "Suresh": [70, 75, 78, 80, 85],
    "sam": [85, 90, 88, 92, 95],
    "Nina": [60, 65, 68, 70, 75],
    "sourav": [90, 95, 92, 88, 94],
    "Rohit": [80, 85, 88, 90, 92],
    "arun": [70, 75, 78, 80, 85],
    "sri ": [95, 98, 92, 90, 94],
    "maira": [80, 85, 88, 90, 92],
    "suman": [70, 75, 78, 80, 85],
    "kavya": [85, 90, 88, 92, 95]

}
with open("results.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name" "\t\t\taverage"])

    for name, marks in students.items():
        average = sum(marks) / len(marks)
        writer.writerow([name, "\t\t\t" + str(round(average, 2))])

print("CSV file created successfully!")