import math
import random

def parent(i):
  return math.floor((i-1)/2)

def left(i):
  return 2*i + 1

def right(i):
  return 2*(i+1)

def transform(number, digits, character="#"):
  return character*(digits-(len(str(number)))) + str(number)

def show_tree_leafs(root, left, right, digits, character="#", character_transform="#"):

  string = character*(digits+1)
  if root is not None:
    string += transform(root, digits, character_transform)
  else:
    string += character*digits
  string += character*(digits+1) 
  string += "\n"

  string += character*(digits)
  if left != None:
    string += "/"
  else:
    string += character
  string += character*(digits)
  if right != None: 
    string += "\\"
  else:
    string += character
  string += character*(digits) 
  string += "\n"
  
  if left != None:
    string += transform(left, digits, character_transform)
  else:
    string += character*digits
  string += character*(digits+2) 
  if right != None:
    string += transform(right, digits, character_transform)
  else:
    string += character*digits
  
  return string

def show_tree(A, index, level, digits, character="#", character_transform="#",collapsed=False):

  if level == 1:
    right_leaf = None
    left_leaf = None
    
    if left(index) < len(A):
      left_leaf = A[left(index)]

    if right(index) < len(A):
      right_leaf = A[right(index)]

    return show_tree_leafs(A[index], left_leaf, right_leaf, digits, character, character_transform)
  
  numbers = 2**level - 1

  string = character*(numbers*(digits+1)) 
  
  if A[index] is not None:
    string += transform(A[index], digits, character_transform)
  else:
    string += character*digits

  string += character*(numbers*(digits+1)) + "\n"
 
  low_numbers = 2**(level - 1) - 1
  
  has_left = left(index) < len(A) and A[left(index)] is not None
  has_right = right(index) < len(A) and A[right(index)] is not None

  if collapsed:
    
    middle_string = character*(numbers*(digits + 1) - 1)

    if has_left:
      middle_string += "/"
    else:
      middle_string += character

    middle_string +=  character*digits

    if has_right:
        middle_string += "\\"
    else:
        middle_string += character

    middle_string += character*(numbers*(digits + 1) - 1)
    string += middle_string + "\n"
    
    steps = 2*(low_numbers*(digits+1)) - 2

    string += character*((numbers - low_numbers)*(digits + 1))

    character_sep = character

    if has_left:
        character_sep = "-"

    string += character_sep*int(steps/2) 

    string += character*(digits + 2)
    
    character_sep = character

    if has_right:
        character_sep = "-"

    string += character_sep*int(steps/2) 
    string += character*((numbers - low_numbers)*(digits + 1))
    string += "\n"

    string += character*((numbers - low_numbers)*(digits + 1) - 1)
    
    if has_left:
        string += "/" 
    else:
        string += character

    string += character*(steps + digits + 2)
    
    if has_right:
        string += "\\"
    else:
        string += character

    string += character*((numbers - low_numbers)*(digits + 1) - 1)
    string += "\n"

  else:
    for i in range(1, low_numbers*(digits + 1) + 2):
      string += character*(numbers*(digits+1) - i)
      if has_left:
        string += "/"
      else:
        string += character
      string += character*(digits + (i-1)*2)
      if has_right:
        string += "\\"
      else:
        string += character
      string += character*(numbers*(digits+1) - i) 
      string += "\n"

  string_left = show_tree(A, left(index), level - 1, digits, character, character_transform, collapsed).split("\n")
  string_right = show_tree(A, right(index), level - 1, digits, character, character_transform, collapsed).split("\n")

  for i in range(len(string_left)):
    string += string_left[i] 
    string += character*(digits + 2) 
    string += string_right[i] 
    string += "\n"

  return string[:-1]

def generate_random_array(size, max_digits):

  A = []

  for i in range(size):
    A.append(random.randrange(0, 10**(max_digits) - 1))
  
  return A

def get_max_digits_of(A):
  max_digits = 1

  for x in A:
    if x is not None:
      max_digits = max(max_digits, len(str(x)))
  
  return max_digits

character = " "
character_transform = "#"
max_digits = 5

size = int(input("Size: "))

collapsed = input("Collapsed? (y/n) ").lower()[0] == "y"

A = generate_random_array(size, max_digits) 
height = math.frexp(size)[1] - 1

digits = get_max_digits_of(A)

string_tree = show_tree(A, 0, height, digits, character, character_transform, collapsed)

print(string_tree)
print()
