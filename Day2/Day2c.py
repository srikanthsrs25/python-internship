
school_name = "Green Valley School"

def calculate_grade(name, marks, bonus=5):

    """
    Calculates total marks and assigns a grade.

    Parameters:
        name (str): Student name
        marks (int): Base marks obtained
        bonus (int, optional): Bonus marks (default = 5)

    Returns:
        str: Final result message with grade
    """

    total_marks = marks + bonus

    if total_marks >= 90:
        grade = "A+"
    elif total_marks >= 75:
        grade = "A"
    elif total_marks >= 60:
        grade = "B"
    else:
        grade = "C"

    result = f"{name} from {school_name} scored {total_marks} and got grade {grade}"

    return result

student1 = calculate_grade("Arjun", 85)        
student2 = calculate_grade("Meena", 70, 10) 
student3 = calculate_grade("Ravi", 55)
student4 = calculate_grade("Sita", 92, 8)   

print(student1)
print(student2)
print(student3)
print(student4)