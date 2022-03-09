from typing import List
from OrderStatisticsTree import OSTree, OSTreeNode


def to_list_inorder(root: OSTreeNode) -> List[OSTreeNode]:

    def _inorder(root: OSTreeNode):

        if not root:
            return

        _inorder(root.left)
        ret.append(root)
        _inorder(root.right)

    ret = []
    _inorder(root)
    return ret


ostree = OSTree(OSTreeNode(5))
ostree.insert(OSTreeNode(7))
ostree.insert(OSTreeNode(4))
ostree.insert(OSTreeNode(6))
ostree.insert(OSTreeNode(8))

ordered_nodes: List[OSTreeNode] = to_list_inorder(ostree.root)

print('Initialize tree')
for node in ordered_nodes:
    print(f'node: {node.val}, size: {node.size}')

# test select
assert ostree.select(1).val == 4
assert ostree.select(2).val == 5
assert ostree.select(3).val == 6
assert ostree.select(4).val == 7
assert ostree.select(5).val == 8

# test rank
assert ostree.get_rank(4) == 1
assert ostree.get_rank(5) == 2
assert ostree.get_rank(6) == 3
assert ostree.get_rank(7) == 4
assert ostree.get_rank(8) == 5


print("-----------------------------------------------")

ostree.delete(5)
ordered_nodes: List[OSTreeNode] = to_list_inorder(ostree.root)
for node in ordered_nodes:
    print(f'node: {node.val}, size: {node.size}')

# test select after delete
assert ostree.select(1).val == 4
assert ostree.select(2).val == 6
assert ostree.select(3).val == 7
assert ostree.select(4).val == 8
assert ostree.select(5) == None

# test rank after delete
assert ostree.get_rank(4) == 1
assert ostree.get_rank(5) == -1
assert ostree.get_rank(6) == 2
assert ostree.get_rank(7) == 3
assert ostree.get_rank(8) == 4
