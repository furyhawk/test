# Min Window Substring
# Have the function MinWindowSubstring(strArr) take the array of strings stored in strArr, which will contain only two strings, the first parameter being the string N and the second parameter being a string K of some characters, and your goal is to determine the smallest substring of N that contains all the characters in K. For example: if strArr is ["aaabaaddae", "aed"] then the smallest substring of N that contains the characters a, e, and d is "dae" located at the end of the string. So for this example your program should return the string dae.

# Another example: if strArr is ["aabdccdbcacd", "aad"] then the smallest substring of N that contains all of the characters in K is "aabd" which is located at the beginning of the string. Both parameters will be strings ranging in length from 1 to 50 characters and all of K's characters will exist somewhere in the string N. Both strings will only contains lowercase alphabetic characters.
# Examples
# Input: ["ahffaksfajeeubsne", "jefaa"]
# Output: aksfaje
# Input: ["aaffhkksemckelloe", "fhea"]
# Output: affhkkse 



from collections import Counter

EMPTY_COUNTER = Counter()

def MinWindowSubstring(strArr):
  
  strArr = ["ahffaksfajeeubsne", "jefaa"]
  print(type(strArr))
  N, K = strArr
  frequencyK = Counter(K)
  options = []
  for i in range(len(N)):
    curr = Counter()
    for j in range(i, len(N)):
      curr[N[j]] += 1
      print(curr)
      print(N[i:j + 1])
      if frequencyK - curr == EMPTY_COUNTER:
        options.append(N[i:j + 1])
        break
  return min(options, key=len)
      

# keep this function call here 
print(MinWindowSubstring(input()))



# def MinWindowSubstring(a):

#   x = len(a[1])
#   while True:
#     for i in range(x, len(a[0]) + 1):
#       y = a[0][i-x:i]
#       met = True
#       for z in set(list(a[1])):
#         if z not in y or y.count(z) < a[1].count(z):
#           met = False
#           break
#       if met == True:
#         return y
#     x += 1
