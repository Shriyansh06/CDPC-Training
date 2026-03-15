# accept 4 number and find max number
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# d = int(input("Enter fourth number: "))
# max = a
# if b > max:
#     max = b
# if c > max:
#     max = c
# if d > max:
#     max = d
# print("Maximum number is:", max)

# find minimum & maximum in list
# nums = [5,6,8,9]
# minimum = nums[0]
# maximum = nums[0]
# for i in nums:
#     if i < minimum:
#         minimum = i
#     if i > maximum:
#         maximum = i
# print(minimum)
# print(maximum)

# check leap year
# year = int(input("Enter year: "))
# if year % 100 != 0:
#     if year % 4 == 0:
#         print("Non-century Leap Year")
#     else:
#         print("Not a Leap Year")
# else:
#     if year % 400 == 0:
#         print("Century Leap Year")
#     else:
#         print("Not a Leap Year")

# find tech number
# n = 2025
# n1 = n % 100
# n2 = n // 100
# s = n1 + n2
# if s * s == n:
#     print("Tech Number")
# else:
#     print("Not a Tech Number")

# Rearrange positive and negative number
# nums = [3, -2, 5, -7, 8, -1]
# pos = []
# neg = []
# for i in nums:
#     if i >= 0:
#         pos.append(i)
#     else:
#         neg.append(i)
# result = pos + neg
# print(result)

# ** Hackerank**

# 1. Simple Array Sum
#!/bin/python3
# import math
# import os
# import random
# import re
# import sys
# def simpleArraySum(ar):
#     total = 0
#     for i in ar:
#         total = total + i
#     return total
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     ar_count = int(input().strip())
#     ar = list(map(int, input().rstrip().split()))
#     result = simpleArraySum(ar)
#     fptr.write(str(result) + '\n')
#     fptr.close()

# 2. Solve Me First
# def solveMeFirst(a, b):
#     return a + b
# num1 = int(input())
# num2 = int(input())
# res = solveMeFirst(num1, num2)
# print(res)

