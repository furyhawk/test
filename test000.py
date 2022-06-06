# String Challenge
# Have the function StringChallenge(str) take the str parameter being passed and return the string in reversed order. For example: if the input string is "Hello World and Coders" then your program should return the string sredoC dna dlroW olleH.
# Once your function is working, take the final output string and concatenate it with your ChallengeToken, and then replace every third character with an X.

# Your ChallengeToken: gfjc25e3
# Examples
# Input: "coderbyte"
# Output: etybredoc
# Final Output: etXbrXdoXgfXc2Xe3
# Input: "I Love Code"
# Output: edoC evoL I
# Final Output: edXC XvoX IXfjX25X3

def StringChallenge(strParam):

  # code goes here
  reversed_str = strParam[::-1] + 'gfjc25e3'

  output = (
    'X' if i % 3 == 0 else char
    for i, char in enumerate(reversed_str, 1)
  )

  return ''.join(output)

# keep this function call here 
print(StringChallenge(input()))