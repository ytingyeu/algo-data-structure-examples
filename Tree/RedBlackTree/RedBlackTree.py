from enum import Enum


class Color(Enum):
    BLACK = 0
    RED = 1


class RedBlackTreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.parent: RedBlackTreeNode = None
        self.left: RedBlackTreeNode = None
        self.right: RedBlackTreeNode = None
        self.color: Color = Color.RED


class RedBlackTree:
    def __init__(self):
        self.NIL_NODE = RedBlackTreeNode(0)
        self.NIL_NODE.color = Color.BLACK
        self.root = self.NIL_NODE

    def insert(self, insert_val: int) -> None:
        inserted_node = RedBlackTreeNode(insert_val)
        inserted_node.left = self.NIL_NODE
        inserted_node.right = self.NIL_NODE

        parent: RedBlackTreeNode = None
        curr: RedBlackTreeNode = self.root

        while curr is not self.NIL_NODE:
            parent = curr

            if insert_val < curr.val:
                curr = curr.left

            else:
                curr = curr.right

        inserted_node.parent = parent

        # if parent is None then it indicates the inserted node will be the root of RB tree
        if parent is None:
            inserted_node.color = Color.BLACK
            self.root = inserted_node
            return

        elif insert_val < parent.val:
            parent.left = inserted_node

        else:
            parent.right = inserted_node

        if inserted_node.parent.parent is None:
            return

        self._fix_insertion(inserted_node)

    def _fix_insertion(self, z: RedBlackTreeNode) -> None:
        while z.parent.color == Color.RED:

            u = z.parent.parent.left if z.parent is z.parent.parent.right else z.parent.parent.right

            # note: the color of NIL node is BLACK
            if u.color == Color.RED:
                u.color = Color.BLACK
                z.parent.color = Color.BLACK
                z.parent.parent.color = Color.RED
                z = z.parent.parent

            else:
                # if parent is leaning right
                if z.parent is z.parent.parent.right:

                    # z, parent, and grandparent forms a triangle
                    # rotate parent in the opposite direction of z
                    # which makes them in a line
                    if z is z.parent.left:
                        z = z.parent
                        self._right_rotate(z)

                    # z, parent, and grandparent forms a line
                    # rotate grand parent in the opposite direction of z
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    self._left_rotate(z.parent.parent)

                # if parent is leaning left
                else:
                    # z, parent, and grandparent forms a triangle
                    # rotate parent in the opposite direction of z
                    # which makes them in a line
                    if z is z.parent.right:
                        z = z.parent
                        self._left_rotate(z)

                    # z, parent, and grandparent forms a line
                    # rotate grand parent in the opposite direction of z
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    self._right_rotate(z.parent.parent)

            if z is self.root:
                break

            self.root.color = Color.BLACK

    def delete(self, deleted_val: int) -> None:
        target_node = self.root

        while target_node is not self.NIL_NODE:

            if deleted_val < target_node.val:
                target_node = target_node.left

            elif deleted_val > target_node.val:
                target_node = target_node.right

            else:
                break

        if target_node is self.NIL_NODE:
            print(f'Value {deleted_val} is not found.')

        original_color = target_node.color

        if target_node.left is self.NIL_NODE:
            replacement = target_node.right
            self._transplant(target_node, replacement)

        elif target_node.right is self.NIL_NODE:
            replacement = target_node.left
            self._transplant(target_node, replacement)

        # target node has two children
        else:
            successor = self._find_inorder_successor(target_node)
            # TO-DO

    def _fix_deletion(self, z: RedBlackTreeNode) -> None:
        # TO-DO
        pass

    def _left_rotate(self, z: RedBlackTreeNode) -> None:
        y = z.right
        z.right = y.left

        if y.left is not self.NIL_NODE:
            y.left.parent = z

        y.parent = z.parent

        # find out y should be left or right child of the origin parent of z
        # if z was root then update root
        # else links parent with y
        if z.parent is None:
            self.root = y

        elif z is z.parent.left:
            z.parent.left = y

        else:
            z.parent.right = y

        y.left = z
        z.parent = y

    def _right_rotate(self, z: RedBlackTreeNode) -> None:
        y = z.left
        z.left = y.right

        if y.right is not self.NIL_NODE:
            y.right.parent = z

        y.parent = z.parent

        # find out y should be left or right child of the origin parent of z
        # if z was root then update root
        # else links parent with y
        if z.parent is None:
            self.root = y

        elif z is z.parent.left:
            z.parent.left = y

        else:
            z.parent.right = y

        y.right = z
        z.parent = y

    def _transplant(self, to_be_deleted: RedBlackTreeNode, replacement: RedBlackTreeNode):
        # if node to be deleted is the root of tree
        # then update root
        if to_be_deleted.parent is None:
            self.root = replacement

        elif to_be_deleted is to_be_deleted.parent.left:
            to_be_deleted.parent.left = replacement

        else:
            to_be_deleted.parent.right = replacement

        replacement.parent = to_be_deleted.parent

    def _find_inorder_successor(self, root: RedBlackTreeNode) -> RedBlackTreeNode:
        curr = root.right

        while curr.left:
            curr = curr.left

        return curr

    # Print the tree

    def visualize(self):
        def _visualize_rec(curr_node: RedBlackTreeNode, break_line: bool = True, indent: str = '', ):
            if curr_node:
                print(indent, end='')
                if break_line:
                    print("R----", end='')
                    indent += "     "
                else:
                    print("L----", end='')
                    indent += "|    "

                if curr_node is self.NIL_NODE:
                    print(f'NIL ({curr_node.color})')
                else:
                    print(f'{curr_node.val} ({curr_node.color})')

                _visualize_rec(curr_node.left, False, indent)
                _visualize_rec(curr_node.right, True, indent)

        if self.root:
            print(self.root.val)
            _visualize_rec(self.root.left, False)
            _visualize_rec(self.root.right, True)

        else:
            print('There is no node in the tree.')

        print('\n')
