# Notes
## Definitions

`height_of_node = 1 + max(get_height(left_child), get_height(right_child))`

`balance_factor = get_height(left_child) - get_height(right_child)`

Balance factor of a balanced tree should always be in [-1, 0, 1].

## Insert a new node
Insertion is the same as standard BST.

## Maintain balance after insertion
![alt text](./AVL-tree-insert.png "decision tree of rotations to take for balancing after insetion")

## Delete a node
Deletion is similar to standard BST with slight differences:

### Case 1: node that going to be deleted has no child
Just remove the targeted node.


### Case 2: node which going to be deleted has single child
For a balanced tree, a node has single child should not have any grandchild. Thus, we can:

1. Replace the value of targeted node with the child's value.
2. Delete the child node.

### Case 3: node which going to be deleted has two children
Same reason as case 2, we can:

1. Find the inorder successor.
2. Replace the value of targeted node with the successor's value.
3. Delete the successor recursively.


## Maintain balance after deletion
