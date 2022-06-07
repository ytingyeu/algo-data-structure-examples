from typing import Optional


class AVLTreeNode:
    def __init__(self, val):
        self.val: int = val
        self.left: AVLTreeNode = None
        self.right: AVLTreeNode = None
        self.height: int = 1


class AVLTree:
    def __init__(self):
        self._root = None

    def insert(self, val: int) -> AVLTreeNode:
        def _insert_rec(root: AVLTreeNode, val: int) -> AVLTreeNode:
            if not root:
                return AVLTreeNode(val)

            elif val < root.val:
                root.left = _insert_rec(root.left, val)

            else:
                root.right = _insert_rec(root.right, val)

            root.height = 1 + max(self._get_height(root.left),
                                  self._get_height(root.right))

            # start balancing
            b_factor = self._get_balance(root)

            # when left subtree is higher
            if b_factor > 1:

                # case: root, left child, and inserted node forms a straight line
                if val < root.left.val:
                    return self._right_rotate(root)

                # case: root, left child, and inserted node forms a triangle
                else:
                    # left-right rotation:
                    # first left rotate on left child
                    # then right rotate on root
                    root.left = self._left_rotate(root.left)
                    return self._right_rotate(root)

            # when right subtree is higher
            if b_factor < -1:

                # case: root, right child, and inserted node forms a straight line
                if val > root.right.val:
                    return self._left_rotate(root)

                # case: root, right child, and inserted node forms a triangle
                else:
                    # right-left rotation:
                    # first right rotate on right child
                    # then left rotate on root
                    root.right = self._right_rotate(root.right)
                    return self._left_rotate(root)

            return root

        if not self._root:
            self._root = AVLTreeNode(val)

        else:
            self._root = _insert_rec(self._root, val)

    def delete(self, del_val: int):
        def _find_inorder_successor(curr: AVLTreeNode) -> AVLTreeNode:
            curr = curr.right

            while curr.left:
                curr = curr.left

            return curr

        def _delete_rec(root: Optional[AVLTreeNode], del_val: int) -> AVLTreeNode:
            if not root:
                return root

            if del_val < root.val:
                root.left = _delete_rec(root.left, del_val)

            elif del_val > root.val:
                root.right = _delete_rec(root.right, del_val)

            else:
                # if node to be deleted has no child,
                # just delete the root
                if not root.left and not root.right:
                    root = None
                    return root

                # if node to be deleted has single child,
                # replace the deleted node its child
                elif not root.left:
                    temp = root.right
                    root = None
                    return temp

                elif not root.right:
                    temp = root.left
                    root = None
                    return temp

                 # if node to be deleted has two children
                else:
                    # replace the targeted node's value with its inorder successor
                    # then delete the successor recursively
                    successor = _find_inorder_successor(root)
                    root.val = successor.val
                    root.right = _delete_rec(root.right, successor.val)

            root.height = 1 + max(self._get_balance(root.left),
                                  self._get_balance(root.right))

            b_factor = self._get_balance(root)

            if b_factor > 1:
                if self._get_balance(root.left) >= 0:
                    return self._right_rotate(root)

                else:
                    # left-right rotation:
                    # first left rotate on left child
                    # then right rotate on root
                    root.left = self._left_rotate(root.left)
                    return self._right_rotate(root)

            elif b_factor < -1:
                if self._get_balance(root.right) <= 0:
                    return self._left_rotate(root)
                else:
                    # right-left rotation:
                    # first right rotate on right child
                    # then left rotate on root
                    root.right = self._right_rotate(root.right)
                    return self._left_rotate(root)

            return root

        if self._root:
            self._root = _delete_rec(self._root, del_val)

    def _get_balance(self, root: Optional[AVLTreeNode]) -> int:
        if not root:
            return 0

        return self._get_height(root.left) - self._get_height(root.right)

    def _get_height(self, root: Optional[AVLTreeNode]) -> int:
        if not root:
            return 0

        return root.height

    def _left_rotate(self, z: AVLTreeNode) -> AVLTreeNode:
        """Left rotate on passed node.

        Args:
            z (AVLTreeNode): the center of rotation, i.e. the parent/root node before rotation.

        Returns:
            AVLTreeNode: the parent/root node after rotation.
        """
        y = z.right
        y_lc = y.left

        y.left = z
        z.right = y_lc

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        # return the new root of rotated subtree
        return y

    def _right_rotate(self, z: AVLTreeNode) -> AVLTreeNode:
        """Right rotate on passed node.

        Args:
            z (AVLTreeNode): the center of rotation, i.e. the parent/root node before rotation.

        Returns:
            AVLTreeNode: the parent/root node after rotation.
        """
        y = z.left
        y_rc = y.right

        y.right = z
        z.left = y_rc

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        # return the new root of rotated subtree
        return y

    # Print the tree
    def visualize(self):
        def _visualize_rec(curr_node: AVLTreeNode, break_line: bool = True, indent: str = '', ):
            if curr_node:
                print(indent, end='')
                if break_line:
                    print("R----", end='')
                    indent += "     "
                else:
                    print("L----", end='')
                    indent += "|    "

                print(curr_node.val)
                _visualize_rec(curr_node.left, False, indent)
                _visualize_rec(curr_node.right, True, indent)

        if self._root:
            print(self._root.val)
            _visualize_rec(self._root.left, False)
            _visualize_rec(self._root.right, True)

        else:
            print('There is no node in the tree.')
