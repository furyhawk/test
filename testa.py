def SearchingChallenge(strParam):

  # code goes here
  counter = {}
  seq = []
  output = None

  for word in strParam:
    if word in counter:
      counter[word] += 1
    else:
      counter[word] = 1
      seq.append(word)

  for s in seq:
    if counter[s] == 1:
      output = s
      break
  
  orig_mask = ['w', 'v', 't', 'k', 'b', 'p', 'd', '9', 'e', '2']
  mask = orig_mask + [ s.lower() for s in orig_mask ]
  filtered_string = filter( lambda char: char not in mask, output)
  final_output = ''.join(filtered_string)

  return 'EMPTY' if final_output == '' else final_output

# keep this function call here 
print(SearchingChallenge(input()))