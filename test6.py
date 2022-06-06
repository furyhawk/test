# Codeland Username Validation
# Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine if the string is a valid username according to the following rules:

# 1. The username is between 4 and 25 characters.
# 2. It must start with a letter.
# 3. It can only contain letters, numbers, and the underscore character.
# 4. It cannot end with an underscore character.

# If the username is valid then your program should return the string true, otherwise return the string false.
# Examples
# Input: "aa_"
# Output: false
# Input: "u__hello_world123"
# Output: true 

def CodelandUsernameValidation(string):
  if string[-1] == '_' or not string[0].isalpha(): return 'false'
  length = len(string)
  string = string.replace('_', '')
  return 'true' if 4 <= length <= 25 and string.isalnum() else 'false'

# keep this function call here 
print(CodelandUsernameValidation(input()))