# Day 2

# Check weather the number is peterson or not
# n = input('Enter the number:')
# s = 0
# for i in str(n):
#     f = 1
#     for j in range(1, int(i) + 1):
#         f = f * j
#     s = s + f
# if s == n:
#     print("Peterson number")
# else:
#     print("Not a Peterson number")

# Number to reverse using loop
# n = int(input("Enter a number: "))
# rev = 0
# while n > 0:
#     rem = n % 10
#     rev = rev * 10 + rem
#     n = n // 10
# print("Reverse no. is:", rev)

# Case study
# no = int(input("Enter number: "))
# rev = 0
# i = 0
# print("Pass", i, ": no =", no, "rev =", rev)
# while no:
#     rem = no % 10
#     rev = rev * 10 + rem
#     no //= 10
#     i += 1
#     print("Pass", i, ": no =", no, "rev =", rev, "rem =", rem)
# print("Reverse no is", rev)

# Count number of digits
# n = int(input("Enter a number: "))
# count = 0
# while n > 0:
#     n = n // 10
#     count = count + 1
# print("Number of digits:", count)

# Sum of digits
# n = int(input("Enter a number: "))
# sum = 0
# while n > 0:
#     rem = n % 10
#     sum = sum + rem
#     n = n // 10
# print("Sum of digits:", sum)

# Check number is palidrome
# n = int(input("Enter a number: "))
# n1 = n
# rev = 0
# while n > 0:
#     rem = n % 10
#     rev = rev * 10 + rem
#     n = n // 10
# if n1 == rev:
#     print("Number is Palindrome")
# else:
#     print("Number is not Palindrome")

# Check number is armstrong number
# n = int(input("Enter a number: "))
# temp = n
# sum = 0

# while n > 0:
#     rem = n % 10
#     sum = sum + rem**3
#     n = n // 10

# if temp == sum:
#     print("Number is Armstrong")
# else:
#     print("Number is not Armstrong")
    
# Check number is armstrong number with count logic
# n = int(input("Enter a number: "))
# temp = n
# count = 0
# while n > 0:
#     n = n // 10
#     count = count + 1
# n = temp
# sum = 0
# while n > 0:
#     rem = n % 10
#     sum = sum + rem**count
#     n = n // 10
# if temp == sum:
#     print("Number is Armstrong")
# else:
#     print("Number is not Armstrong")

# Print armstrong number between 1 to 10000
# for num in range(1, 10001):
#     n1 = num
#     n = num
#     count = 0
#     while n > 0:
#         n = n // 10
#         count += 1
#     n = num
#     sum = 0
#     while n > 0:
#         rem = n % 10
#         sum += rem ** count
#         n = n // 10
#     if sum == n1:
#         print(n1)