
# 1) check number is positive or negative

# number = int(input("enter the number:"))
# if(number> 0):
#     print("number is positive")
# elif(number < 0):
#     print("number is negative")
# else:
#     print("number is zero")

#2) Check even or odd  
  # Write a program to check if a given number is even or odd.

# number = 66
# if(number % 2==0):
#     print("number is even")
# else:
#     print("number is odd")

# 3) Grade Checker  
#    Write a program to display grades based on a percentage:
#    - A: 90-100
#    - B: 70-89
#    - C: 50-69
#    - F: Below 50

# percentage = float(input("enter the percentage:"))

# if 90  <= percentage <=100:
#     print("Grade: A")
# elif 70 <= percentage <=89:
#     print("Grade:B")
# elif 50 <= percentage <=89:
#     print("Grade:C")
# else:
#     print("Below 50 ")

# 4)  Check divisibility  
#    Check if a given number is divisible by 3, 5, or both.

# number = 5
# if(number % 3 == 0 and number % 5 == 0):
#     print("number is divisible by both")
# elif(number % 3 == 0):
#     print("number is divisible by 3")
# elif(number % 5 == 0):
#     print("number is divisible by 5")
# else:
#     print("number is not divisible by 3 and 4")

#5) Minimum of two numbers  
#    Find the smaller number between two given numbers.

# num1 = int(input("enter the num1"))
# num2 = int(input("enter the num2"))

# if(num1 < num2):
#     print("num1 is minimum",{num1})
# elif num2 < num1:
#     print("num2 is minimum",{num2})
# else:
#     print("both numbers are equal")

# 6)Find the largest of three numbers  
#    Given three numbers, find the largest using nested if statements.

# num1 = int(input("enter the num 1 "))
# num2 = int(input("enter the num 2 "))
# num3 = int(input("enter the num3 "))

# if num1 > num2 and num1 > num3:
#     print("num 1 is maximum ",{num1})
# elif num2 > num1 and num2 > num1:
#     print("num 2 is maximum ",{num2})
# else:
#     print("num 3 is maximum",{num3})

# 7) check leap year  
#    Write a program to check if a given year is a leap year or not:
#    - Divisible by 4 and not 100, or divisible by 400.

# year = 2022
# if year % 4 == 0 and year % 100 != 0:
#     print("year is leap year")
# elif year % 400 == 0:
#     print("year is leap year")
# else:
#     print("year is not leap:")

# 8) Nested temperature check  
#    Categorize temperature into:
#    - Cold: Below 15°C
#    - Warm: 15°C to 30°C
#    - Hot: Above 30°C

# temp = float(input("enter the temprature in c"))

# if(temp < 15):
#     print("cold:")
# elif 15 <= temp <= 30:
#     print("warm")
# else:
#     print("hot")

# 9)Vowel or consonant  
#    Check if a given character is a vowel or consonant.

# char = input("Enter a single character: ").lower()

# if char in 'aeiou':
#     print(f"{char} is a vowel.")
# else:
#     print(f"{char} is a consonant.")

#  10) Driving eligibility  
    # Check if a person is eligible to drive:
    # - Must be 18 or older.
    # - Nested ch


# age = int(input("Enter your age: "))
# has_license = input("Do you have a valid driving license? (yes/no): ").lower()


# if age >= 18:
#     if has_license == "yes":
#         print("You are eligible to drive.")
#     else:
#         print("You are not eligible to drive because you do not have a valid license.")
# else:
#     print("You are not eligible to drive because you are under 18.")

# 11) Triangle validation  
    # Check if three sides can form a triangle:
    # - The sum of any two sides must be greater than the third side.

# a=int(input("Enter the three sides of tringle: "))
# b=int(input())
# c=int(input())
# if a+b > c and a+c > b and b+c >a:
#     print("Valid triangle")
# else :
#     print("It is not a valid triangle")


# 12) Calculate tax based on salary  
    # Determine the tax rate:
    # - Salary ≤ 5,00,000: 5%
    # - 5,00,001 - 10,00,000: 10%
    # - Above 10,00,000: 20%


# def calculate_tax(salary):
#     if salary <= 500000:
#         tax_rate = 0.05
#     elif salary <= 1000000:
#         tax_rate = 0.10
#     else:
#         tax_rate = 0.20
    
#     tax = salary * tax_rate
#     return tax

# # Example Usage
# salary = float(input("Enter your salary: "))
# tax = calculate_tax(salary)
# print(f"The tax on a salary of {salary:.2f} is {tax:.2f}.")

#13) # Categorize age
# age=int(input("Enter your age : "))
# if age <= 12:
#     print("Child")
# elif 12 < age <= 19:
#     print("Teen")
# elif 19 < age <= 59:
#     print("Adult")
# else:
#     print("Senior")

# 14) # Logical AND check

# num=int(input("Enter your num : "))
# if num >10 and num %2 ==0:
#     print("number is greater than 10 and divisible by 2")
# else :
#     print("number is not greater than 10 and not divisible by 2")

# logical OR check
# num=int(input("Enter your num : "))
# if num < 5 or num > 20:
#     print("Number is either less than 5 or greater than 20")
# else:
#     print ("condition does not satisfy")

# 15)# logical OR check

# num=int(input("Enter your num : "))
# if num < 5 or num > 20:
#     print("Number is either less than 5 or greater than 20")
# else:
#     print ("condition does not satisfy")


# 16) # electricity bill
# bill=0
# unit=int(input("Enter the usage in unit : "))
# if unit <= 100:
#     bill = unit*5
# elif 100 < unit <=200:
#     bill = unit*10
# elif unit > 200:
#     bill =unit*15
# print("Electricity bill is : ",bill)

# 17) # season finder
# month=input("enter the month: ").lower()
# if month in ["dec","jan",'feb',"december","january", "february"]:
#     print("Winter")
# elif month in ["mar","apr","may","march","april"]:
#     print("Spring")
# elif month in ["jun","jul","aug","june","july","august"]:
#     print("Summer")
# elif month in ["sep","september","oct", "october","nov", "november"]:
#     print("Autumn")
# else:
#     print("invalid month")

# 18) # password validation
# password=input("enter your password : ")
# if len(password) >=8 and "@" in password:
#     print("Password is valid")
# else :
#     print("Password is invalid")

# 19) ategorize bmi
# bmi=float(input("enter your BMI : "))
# if bmi<18.5:
#     print("underweight")
# elif 18.5<= bmi<=24.9:
#     print("Normal")
# elif 25 <= bmi <=29.9:
#     print("Overweight")
# elif 30 <= bmi:
#     print("Obese")

# 20)character type checker
char=input("enter the character: ")
if char.isalpha():
    print("Alphabet")
elif char.isdigit():
    print("Digit")
else:
    print("special character")