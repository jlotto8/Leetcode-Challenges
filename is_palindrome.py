# Anna Jess

# def is_palindrome(s):
#     # left = 0
#     s = s.upper()
#     for i in range(len(s)):
#         if s[i] != s[(len(s),i,-1)]:
#             return False
#     return True

# print(is_palindrome("Anna"))

# def is_palindrome(s):
  
#   half = int(len(s)/2)
#   for i in range(half):
#     right = -1
#     # print(s[i],s[right])
#     if s[i] != s[right]:
#       return False
#     elif i == half:
#         # print(s[i],s[right])
#         right -=1
#         i += 1
#         return True
# print(is_palindrome('racecar'))

# def two_pointers(array):
#     left = 0
#     right = len(array) - 1
#     while left <= right:
#         print(array[left], array[right])
#         if array[left] != array[right]:
#             return False
#         else:
#             left += 1
#             right -= 1
#     return True 
# print(two_pointers('raceacar'))