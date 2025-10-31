# ASCII Tree

## Requirements

- python3

## Usage

```bash
python3 create_tree.py
```


It asks you the tree size and if you want to collapse the tree. 
It generates a random array with that size.
It shows you the ascii drawing.

## Function
If you have the array you can use `show_tree` and pass (in order):
  - array
  - 0
  - height
  - digits of your numbers (you can use get_max_digits_of(A))
  - character (for spacing, default "#")
  - character_transform (for fill number with less digits, default="#")
  - collapsed (if you want a tree collapsed or not, default=False)

If you have a BST you can pass, in show_tree, `bst_to_arr(create_bst_from_arr(A))` from create_bst module 

## Examples
Collapsed Random Tree 
![Collapsed](imgs/collapsed.png)

Not Collapsed Random Tree
![Not collapsed](imgs/not-collapsed.png)

BST Collapsed Random Tree  
![BST Collapsed](imgs/bst-collapsed.png)

