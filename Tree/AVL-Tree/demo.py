from AVLTree import AVLTree

nums = [2, 9, 4, 8, 5, 0, 7]

avl_tree = AVLTree()

for n in nums:
    avl_tree.insert(n)

avl_tree.visualize()
