# Input - string s consisting of words and spaces
# ootput - the length of the last word in the string.

# A word is a substring consisting of non-space characters only.

# Example 1:

# Input: s = "Hello World"
# Output: 5

# Input: s = "   fly me   to   the moon  "
# Output: 4

# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6

# Constraints:
# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.

def length_of_last_word(s):
  if s == " ":
    return None
  else:
    string = s.strip().split() #returns a list of words in the string
  return len(string[-1])