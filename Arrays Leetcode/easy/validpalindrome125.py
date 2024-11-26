# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

# Constraints:
# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

def is_palindrome(s):
  # Convert the string to lowercase
  s = s.lower()

  # Remove all non-alphanumeric characters
  s = ''.join(cha for cha in s if cha.isalnum())

  i = 0
  j = len(s) - 1

  if s == " ":
      return True

  while i < len(s):
      if s[i] != s[j]:
          return False
      i = i + 1
      j = j - 1

  return True
  
  

