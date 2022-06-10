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

            self.visualize()

            u = z.parent.parent.left if z.parent is z.parent.parent.right else z.parent.parent.right

            # note: the color of NIL node is BLACK
            if u.color == Color.RED:
                u.color = Color.BLACK
                z.parent.color = Color.BLACK
                z.parent.parent.color = Color.RED
                z = z.parent.parent

            else:
                # z, parent, and grandparent forms a triangle
                # rotate parent in the opposite direction of z
                if z.parent is z.parent.parent.right:
                    if z is z.parent.left:
                        z = z.parent
                        self._right_rotate(z)

                    # z, parent, and grandparent forms a line
                    # rotate grand parent in the opposite direction of z
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    self._left_rotate(z.parent.parent)

                else:
                    if z is z.parent.right:
                        z = z.parent
                        self._left_rotate(z)

                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    self._right_rotate(z.parent.parent)

            if z is self.root:
                break

            self.root.color = Color.BLACK

    def _left_rotate(self, z: RedBlackTreeNode) -> None:

        print(z.val)
        y = z.right
        z.right = y.left

        if y.left is not self.NIL_NODE:
            y.left.parent = z

        y.parent = z.parent

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

        if z.parent is None:
            self.root = y

        elif z is z.parent.left:
            z.parent.left = y

        else:
            z.parent.right = y

        y.right = z
        z.parent = y

    # Print the tree
    def visualize(self):
        def _visualize_rec(curr_node: RedBlackTree, break_line: bool = True, indent: str = '', ):
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
