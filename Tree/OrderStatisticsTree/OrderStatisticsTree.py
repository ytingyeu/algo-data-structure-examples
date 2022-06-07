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


class OSTree(object):
    """
    Order Statistic Tree

    Notice: 
    Assume the values of its nodes are unique, i.e. no mutiple nodes share the same value.
    """

    def __init__(self, root: OSTreeNode = None) -> None:
        self.root = root

    def insert(self, new_node: OSTreeNode) -> None:

        def _insert_node(root: OSTreeNode, new_node: OSTreeNode):
            if root.val > new_node.val:
                if not root.left:
                    root.left = new_node

                else:
                    _insert_node(root.left, new_node)

            else:

                if not root.right:
                    root.right = new_node

                else:
                    _insert_node(root.right, new_node)

            # size of the currnet node increase one after insert
            root.size += 1

        _insert_node(self.root, new_node)

    def delete(self, target: int) -> None:

        def _delete_node(target: int, descendants_need_fix: List) -> bool:

            curr = self.root
            parent = None

            while curr and curr.val != target:
                parent = curr
                descendants_need_fix.append(parent)

                if curr.val > target:
                    curr = curr.left

                elif curr.val < target:
                    curr = curr.right

            if not curr:
                print(f'Delete failed: {target} not found.')
                return False

            # Node to be delted has no child
            if not curr.left and not curr.right:
                # if deleted node is not root
                if curr != self.root:
                    if parent.left == curr:
                        parent.left = None
                    else:
                        parent.right = None
                else:
                    self.root = None

            # Node to be deleted has two children
            elif curr.left and curr.right:
                # Find inorder successor or predecessor of the node
                # here we use successor
                successor = self._find_inorder_successor(curr)

                # store successor value
                successor_val = successor.val

                # Recursively delete the successor.
                # Note that the successor has at most one child (right child)
                _delete_node(successor.val, descendants_need_fix)

                # copy value of the successor to the current node
                curr.val = successor_val

            # Node to be deleted has one child:
            else:
                # Copy the child to the node and delete the child
                if curr.left:
                    child = curr.left
                else:
                    child = curr.right

                # if deleted node is not root
                if curr != self.root:
                    if curr == parent.left:
                        parent.left = child

                    else:
                        parent.right = child
                else:
                    self.root = child

            return True

        # Record the nodes that is on descendants path.
        # The size of these nodes are impacted because of node deletion.
        descendants_need_fix = []

        if _delete_node(target, descendants_need_fix):
            print(f'Delete {target}')
            print('Nodes to be fixed: ', end='')
            print(' '.join(str(item.val) for item in descendants_need_fix))

            self._fix_all_sum(self.root, descendants_need_fix)

    def _find_inorder_successor(self, curr: OSTreeNode) -> OSTreeNode:
        curr = curr.right

        while curr.left:
            curr = curr.left
        return curr

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

        return _select_kth_node(self.root, k)

    def get_rank(self, target: int) -> int:
        """Find the rank of the node with a specific value.

        Ref: https://www.cs.yale.edu/homes/aspnes/pinewiki/OrderStatisticsTree.html

        Args:
            target (int): value that target node has

        Returns:
            int: the rank of the target node.
        """

        curr = self.root
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
