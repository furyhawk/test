def StringChallenge(strParam):

  reversed_str = strParam[::-1]
  # code goes here
  mask_orig = ['8','0','b','2','a','p','l','9','c']
  mask = mask_orig + [ s.upper() for s in mask_orig ]
  filtered_chars = filter(lambda item: item not in mask, reversed_str)
  # Join remaining characters in the filtered list
  sample_str = ''.join(filtered_chars)
  return sample_str

# keep this function call here 
print(StringChallenge(input()))