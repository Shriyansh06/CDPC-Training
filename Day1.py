# DAY 1

# Find last digit
# n = int(input("Enter a number: "))
# res= n % 10
# print("Last digit is:", res)

# Sum of two digit
# n1 = int(input("Enter a number: "))
# n2 = n1%10 #5
# n3 = n1//10 #4
# res= n2 + n3
# print(res)
# logic 54 : 5+4= 9

# Sum of 3 digit
# n1 = int(input("Enter a number: "))
# n2 = n1%10 #5
# n1 = n1//10 #34
# n3 = n1%10 #4
# n4 = n1//10 #3
# res= n2 + n3 + n4
# print(res)

# Sum of 5 digit
# n1 = int(input("Enter a 5 digit number: "))
# n2 = n1 % 10      --
# n1 = n1 // 10
# n3 = n1 % 10
# n1 = n1 // 10
# n4 = n1 % 10
# n1 = n1 // 10
# n5 = n1 % 10
# n1 = n1 // 10
# n6 = n1 % 10
# res = n2 + n3 + n4 + n5 + n6
# print(res)

# Reverse of 5 digit number
# n = int(input("Enter a 5 digit number: "))
# d1 = n % 10
# n = n // 10
# d2 = n % 10
# n = n // 10
# d3 = n % 10
# n = n // 10
# d4 = n % 10
# n = n // 10
# d5 = n % 10
# rev = d1*10000 + d2*1000 + d3*100 + d4*10 + d5
# print("Reverse number is:", rev)

# Accept 9 digit number & find sum of 1st and last digit (in 3 step)
# n = int(input("Enter a 9 digit number: "))
# last = n % 10
# first = n // 100000000
# print("Sum =", first + last)

# Accept basic salary and calculate gross salary where 
# TA=20%
# DA=30%
# HRA=40% 
# basic = int(input("Enter Basic Salary: "))
# TA = basic * 0.20
# DA = basic * 0.30
# HRA = basic * 0.40
# gross = basic + TA + DA + HRA
# print(TA)
# print(DA)
# print( HRA)
# print(gross)

# Sum of 9 Digit number and reverse it 
# n = int(input("Enter a 9 digit number: "))
# d1 = n % 10
# n = n // 10
# d2 = n % 10
# n = n // 10
# d3 = n % 10
# n = n // 10
# d4 = n % 10
# n = n // 10
# d5 = n % 10
# n = n // 10
# d6 = n % 10
# n = n // 10
# d7 = n % 10
# n = n // 10
# d8 = n % 10
# n = n // 10
# d9 = n % 10
# sum = d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
# n = sum
# d1 = n % 10
# n = n // 10
# d2 = n % 10
# n = n // 10
# d3 = n % 10
# n = n // 10
# d4 = n % 10
# n = n // 10
# d5 = n % 10
# n = n // 10
# d6 = n % 10
# n = n // 10
# d7 = n % 10
# n = n // 10
# d8 = n % 10
# n = n // 10
# d9 = n % 10
# res = d1*100000000 + d2*10000000 + d3*1000000 + d4*100000 + d5*10000 + d6*1000 + d7*100 + d8*10 + d9
# print(sum)
# print(res)
