def ArrayChallenge(arr):

  # code goes here
  output = 0

  sorted_num = sorted(arr)
  max_four = sorted_num[-4:]
  summed_four = sum(max_four)
  summed_four_str = ''.join(str(summed_four))

  orig_mask = ['w', 'v', 't', 'k', 'b', 'p', 'd', '9', 'e', '2']
  mask = orig_mask + [ s.lower() for s in orig_mask ]
  filter_output = filter(lambda char: char not in mask, summed_four_str)
  return ''.join(filter_output)

# keep this function call here 
print(ArrayChallenge(input()))