# Have the function StringChallenge(sen) take the sen parameter being passed and return the longest word in the string.
#  If there are two or more words that are the same length, return the first word from the string with that length.
#  Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567" 

import string

def StringChallenge(sen):

  # code goes here
  input_str = sen.translate(str.maketrans('','',string.punctuation))
  print(f'{input_str}')
  longest_str = max(input_str.split(), key=len)

  mask_orig = ['8','0','b','2','a','p','l','9','c']
  mask = mask_orig + [ s.upper() for s in mask_orig ]
  filtered_chars = filter(lambda item: item not in mask, longest_str)
  sample_str = ''.join(filtered_chars)
  
  return sample_str #sample_str

# keep this function call here 
print(StringChallenge(input()))


import string

def StringChallenge(sen):

  input_str = sen.translate(str.maketrans('', '', string.punctuation))
  # code goes here
  longest_word = max(input_str.split(), key=len)

  output = (
    'X' if i % 3 == 0 else char for i, char in enumerate(longest_word+'gfjc25e3', 1)
  )

  return ''.join(output)

# keep this function call here 
print(StringChallenge(input()))