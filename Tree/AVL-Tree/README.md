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
Deletion is the same as standard BST:

### Case 1: node that going to be deleted has no child
Just remove the targeted node.

### Case 2: node that going to be deleted has single child

1. Replace the targeted node with its child.
2. Delete the child node.

In a balanced tree, a node with single child should not have any grandchild.
Thus, we can simply delete the child node.

### Case 3: node that going to be deleted has two children

1. Find the inorder successor.
2. Replace the targeted node with the successor.
3. Delete the successor recursively.

Note that the successor has at most one child (right child)

## Maintain balance after deletion
