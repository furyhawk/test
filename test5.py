# Tree Constructor
# Have the function TreeConstructor(strArr) take the array of strings stored in strArr, which will contain pairs of integers in the following format: (i1,i2), where i1 represents a child node in a tree and the second integer i2 signifies that it is the parent of i1. For example: if strArr is ["(1,2)", "(2,4)", "(7,2)"], then this forms the following tree:



# which you can see forms a proper binary tree. Your program should, in this case, return the string true because a 
# valid binary tree can be formed. If a proper binary tree cannot be formed with the integer pairs, then return the string false. 
# All of the integers within the tree will be unique, which means there can only be one node in the tree with the given integer value.
# Examples
# Input: ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]
# Output: true
# Input: ["(1["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]
# Output: false 




import re

def TreeConstructor(strArr):
  
  strArr=["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)", "(11,10)"]
  child_parent_value_pairs = []

  for s in strArr:
    temp = re.findall("[-\\d]+", s)

    temp = [int(x) for x in temp]

    child_parent_value_pairs.append(temp)

  child_parent_value_pairs = sorted(child_parent_value_pairs, key = lambda x : x[1])
  
  child_values = []

  parent_values = {}

  parent_child_values = {}

  for pair in child_parent_value_pairs:

    if pair[0] in child_values:
      return "false"

    child_values.append(pair[0])

    if pair[1] in parent_values.keys():
      parent_values[pair[1]] += 1

    else:
      parent_values[pair[1]] = 1   

    if pair[1] not in parent_child_values.keys():
      parent_child_values[pair[1]] = [pair[0]]
    
    else:
      parent_child_values[pair[1]].append(pair[0])     

  for k,v in parent_child_values.items():

    if len(v) > 2 :
      return "false"

    if len(v) == 2:
      if (v[0] < k and v[1] < k) or (v[0] > k and v[1] > k):
        return "false"

  return "true"         
# keep this function call here 
print(TreeConstructor(input()))