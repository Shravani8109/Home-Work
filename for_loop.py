# # 1) Print Numbers from 1 to 10

# for i in range (1,11):
#     print(i)

# # 2) Print Each Character in a String

# name = "shravani"
# for char in name:
#     print(char)

# # 3)  Iterate Over a List

# fruits = ["apple","orange","mango"]

# for fruit in fruits :
#     print(fruit)

# # 4) Loop with an if Condition

# numbers = [1, 2, 3,4, 10]
# for num in numbers:
#     if num % 2 == 0:
#         print(num, "is even")
#     else:
#         print(num," is odd")

# # 4) Breaking out of a Loop

# for i in range(5):
#     if i == 3:
#         break  
#     print(i)

# # 5) Print Numbers in Reverse
# for i in range (5 , 0, -1):
#     print(i)

# 6) Sum of Numbers in a List

# numbers = [10,20,10]
# sum =0
# for num in numbers:
#     sum += num
# print("sum is: ",sum)

# 7)  Print Multiplication Table of 2
# for i in range(1, 16):
#     print(f"2*{i} = {2*i}")

# 8) Find Length of Each Word

# words = ["apple","orange","mango","banana"]
# for word in words:
#     print(f"{word} :{len(word)} chracters")

# 9) Print "Hello!" 3 Times

# for _ in range(3):
#     print("Hello!")

# 10) star pattern
# rows =6
# for i in range(1,rows+1):
#     print("*"* i)

# # # 11) 
rows = 6
for i in range(rows,0,-1):
    print("*" * i)