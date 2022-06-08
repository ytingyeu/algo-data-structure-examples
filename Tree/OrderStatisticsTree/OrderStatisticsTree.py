from __future__ import annotations
from typing import List


class OSTreeNode(object):
    """
    Order Statistic Tree Node
    """

    def __init__(self, val=0, left: OSTreeNode = None, right: OSTreeNode = None):
        self.val = val
        self.left = left
        self.right = right

        # the number of its children plus one for itself
        self.size = 1


class OSTree:
    """
    Order Statistic Tree

    Notice: 
    Assume the values of its nodes are unique, i.e. no mutiple nodes share the same value.
    """

    def __init__(self) -> None:
        self._root = None

    def insert(self, insert_val: int) -> None:

        def _insert_rec(root: OSTreeNode, insert_val: int) -> OSTreeNode:
            if not root:
                return OSTreeNode(insert_val)

            if insert_val < root.val:
                root.left = _insert_rec(root.left, insert_val)
            else:
                root.right = _insert_rec(root.right, insert_val)

            # size of the currnet node increase one after insert
            root.size += 1

            return root

        if not self._root:
            self._root = OSTreeNode(insert_val)

        else:
            self._root = _insert_rec(self._root, insert_val)

    def delete(self, target: int) -> None:
        def _find_inorder_successor(curr: OSTreeNode) -> OSTreeNode:
            curr = curr.right

            while curr.left:
                curr = curr.left

            return curr

        def _delete_rec(root: OSTreeNode, target_val: int) -> bool:
            if not root:
                return root

            if target_val < root.val:
                descendants_need_fix.append(root)
                root.left = _delete_rec(root.left, target_val)

            elif target_val > root.val:
                descendants_need_fix.append(root)
                root.right = _delete_rec(root.right, target_val)

            else:
                # case: target node has no child
                # just delete it
                if not root.left and not root.right:
                    root = None
                    return root

                # case: target node has single child
                # backup its child, delete the target node, and then return the child
                # to the parent
                elif not root.right:
                    temp = root.left
                    root = None
                    return temp

                elif not root.left:
                    temp = root.right
                    root = None
                    return temp

                # case: target node has two children
                # replace the node with its inorder successor -- the smallest element on its right subtree
                # then delete the successor recursively
                else:
                    successor = _find_inorder_successor(root)
                    root.val = successor.val
                    _delete_rec(root.right, successor.val)

            root.size -= 1

            return root

        # Record the nodes that is on descendants path.
        # The size of these nodes are impacted because of node deletion.
        descendants_need_fix = []

        self._root = _delete_rec(self._root, target)

        print(f'Delete {target}')
        print('Nodes to be fixed: ', end='')
        print(' '.join(str(item.val) for item in descendants_need_fix))

        self._fix_all_sum(self._root, descendants_need_fix)

    def _fix_all_sum(self, root: OSTreeNode, descendants_need_fix: List[int]) -> None:
        """Maintain size of each tree node after insert, delete, or value change. Start from the passed root.

        Ref: https://www.cs.yale.edu/homes/aspnes/pinewiki/AggregateQueries.html

        Args:
            root (OSTreeNode): root of the subtree.
            descendants_need_fix (List[int]): a list of node value whose size need to be fixed.
        """

        def _fix_sum(root: OSTreeNode) -> None:
            root.size = 1

            if root.left:
                root.size += root.left.size

            if root.right:
                root.size += root.right.size

        # Since not both left and right child node need to fix the size,
        # we only run it on nodes whose descendants have changed.
        if root.left in descendants_need_fix:
            self._fix_all_sum(root.left, descendants_need_fix)

        if root.right in descendants_need_fix:
            self._fix_all_sum(root.right, descendants_need_fix)

        _fix_sum(root)

    def select(self, k: int) -> OSTreeNode:
        """Find the k-th smallest node stored in the tree.

        Ref: https://www.cs.yale.edu/homes/aspnes/pinewiki/OrderStatisticsTree.html

        Returns:
            OSTreeNode: the k-th smallest node.
        """

        def _select_kth_node(root: OSTreeNode, k: int):

            if not root:
                print(f'k={k} is greater than the total number of nodes.')
                return None

            left_size = root.left.size + 1 if root.left else 1

            if k == left_size:
                return root

            if k < left_size:
                return _select_kth_node(root.left, k)

            else:
                return _select_kth_node(root.right, k - left_size)

        return _select_kth_node(self._root, k)

    def get_rank(self, target: int) -> int:
        """Find the rank of the node with a specific value.

        Ref: https://www.cs.yale.edu/homes/aspnes/pinewiki/OrderStatisticsTree.html

        Args:
            target (int): value that target node has

        Returns:
            int: the rank of the target node.
        """

        curr = self._root
        rank = 0

        while curr:

            if target >= curr.val:

                # Get the number of nodes whose value are smaller than the current node,
                # which equals to the size of current node minus the size of right child.
                left_size = left_size = curr.left.size + 1 if curr.left else 1
                rank += left_size

                # end point
                if target == curr.val:
                    break

                curr = curr.right

            else:
                curr = curr.left

        if not curr:
            print(f'Get rank failed: {target} not found')
            return -1

        else:
            return rank

    def visualize(self):
        def _visualize_rec(curr_node: OSTreeNode, break_line: bool = True, indent: str = '', ):
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
