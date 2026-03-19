# 1. Find Product
# n = int(input())
# arr = list(map(int, input().split()))
# MOD = 1000000007
# product = 1
# for i in arr:
#     product = (product * i) % MOD
# print(product)

# 2. Palindrome Number
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False       
#         temp = x
#         rev = 0
#         while x > 0:
#             rem = x % 10
#             rev = rev * 10 + rem
#             x = x // 10
#         return temp == rev

# 3. Richest Customer Wealth
# class Solution:
#     def maximumWealth(self, accounts: list[list[int]]) -> int:
#         max_wealth = 0
#         for customer in accounts:
#             total = sum(customer)
#             if total > max_wealth:
#                 max_wealth = total
#         return max_wealth

# 4. Staircase
#!/bin/python3
# import math
# import os
# import random
# import re
# import sys
# #
# # Complete the 'staircase' function below.
# #
# # The function accepts INTEGER n as parameter.
# #
# def staircase(n):
#     for i in range(1, n+1):
#         print(" " * (n - i) + "#" * i)
# if __name__ == '__main__':
#     n = int(input().strip())
#     staircase(n)

# 5. Mini-Max Sum
#!/bin/python3
# import math
# import os
# import random
# import re
# import sys
# #
# # Complete the 'miniMaxSum' function below.
# #
# # The function accepts INTEGER_ARRAY arr as parameter.
# #
# def miniMaxSum(arr):
#     total = sum(arr)
#     min_sum = total - max(arr)
#     max_sum = total - min(arr)
    
#     print(min_sum, max_sum)
# if __name__ == '__main__':
#     arr = list(map(int, input().rstrip().split()))
#     miniMaxSum(arr)

# 6. Time Conversion
#!/bin/python3
# import math
# import os
# import random
# import re
# import sys
# #
# # Complete the 'timeConversion' function below.
# #
# # The function is expected to return a STRING.
# # The function accepts STRING s as parameter.
# #
# def timeConversion(s):
#     # Extract the period (AM/PM), the hour, and the rest of the time
#     period = s[-2:]
#     hour = s[:2]
#     minutes_seconds = s[2:8]  
#     # Handle the AM case
#     if period == 'AM':
#         if hour == '12':
#             hour = '00'        
#     # Handle the PM case
#     else: 
#         if hour != '12':
#             hour = str(int(hour) + 12)        
#     # Combine the converted hour with the original minutes and seconds
#     return hour + minutes_seconds
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     s = input()
#     result = timeConversion(s)
#     fptr.write(result + '\n')
#     fptr.close()
