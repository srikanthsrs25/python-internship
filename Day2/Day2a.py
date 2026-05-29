"""
age = int(input("Enter your age: "))
if age <= 17:
    print("You are a minor.")
elif age <= 60:
    print("You are an adult.")
else:
    print("You are a senior.")

"""
"""
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

"""
"""
password = input("Enter your password: ")
if len(password) < 8:
    print("Password is too short.") 
elif len(password) > 15:
    print("Password is too long.")  
else:
    print("Password is valid.")
"""
"""
number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")       
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)
"""
"""
prime = int(input("Enter a number: "))
if prime > 1:
    for i in range(2, int(prime**0.5) + 1):
        if prime % i == 0:
            print("The number is not prime.")
            break
    else:
        print("The number is prime.")
else:
    print("The number is not prime.")
"""
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")