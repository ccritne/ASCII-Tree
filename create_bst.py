from create_tree import *

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(r, key):
    if r is None:
        return Node(key)

    if key < r.key:
        if r.left is None:
            r.left = Node(key)
        else:
            insert(r.left, key)
    else:
        if r.right is None:
            r.right = Node(key)
        else:
            insert(r.right, key)

def height(radix):
    if radix is None:
        return -1

    h_l = height(radix.left)
    h_r = height(radix.right)

    return 1 + max(h_l, h_r)

def bst_to_arr(radix):

    A = []

    radix_levels = [radix]
    
    count_none = 0

    while count_none < len(radix_levels):

        radix = radix_levels.pop(0)

        if radix is not None:
            
            A.append(radix.key)
            
            radix_levels.append(radix.left)
            radix_levels.append(radix.right)

            count_none += radix.left is None 
            count_none += radix.right is None 
        else:
            A.append(None)
            radix_levels.append(None)
            radix_levels.append(None)
            count_none += 1

    return A

def create_bst_from_arr(A):
    
    radix = insert(None, A[0])

    for i in range(1, len(A)):
        insert(radix, A[i])

    return radix

if __name__ == "__main__":

  character = " "
  character_transform = "#"
  max_digits = 5

  size = int(input("Size: "))

  A = generate_random_array(size, max_digits)

  print(A)
  
  bst = create_bst_from_arr(A)

  binary = bst_to_arr(bst)

  height = math.frexp(len(binary))[1] - 1

  digits = get_max_digits_of(binary)

  string_tree = show_tree(binary, 0, height, digits, character, character_transform, True)

  print(string_tree)
  print()
