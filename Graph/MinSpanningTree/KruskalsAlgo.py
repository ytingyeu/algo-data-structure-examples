from typing import DefaultDict, List, Tuple
from collections import defaultdict


class UnionFindSet(object):

    def __init__(self):
        self.root_of_nodes: DefaultDict[int, int] = defaultdict(int)
        self.rank_of_nodes: DefaultDict[int, int] = defaultdict(int)

    def size(self):
        return len(self.root_of_nodes)

    def add(self, new_val: int):
        if new_val not in self.root_of_nodes:
            self.root_of_nodes[new_val] = new_val
            self.rank_of_nodes[new_val] = 1

    def find(self, target: int):
        if target not in self.root_of_nodes:
            print(f'{target} not found in the UFS.')
            return None

        root = self.root_of_nodes[target]

        while root != self.root_of_nodes[root]:
            root = self.root_of_nodes[root]

        return root

    def union(self, node_x: int, node_y: int):
        root_x = self.find(node_x)
        root_y = self.find(node_y)

        if root_x != root_y:
            rank_x = self.rank_of_nodes[root_x]
            rank_y = self.rank_of_nodes[root_y]

            if rank_x > rank_y:
                self.root_of_nodes[root_y] = root_x

            elif rank_x < rank_y:
                self.root_of_nodes[root_x] = root_y

            else:
                self.root_of_nodes[root_y] = root_x
                self.rank_of_nodes[root_x] += 1


def kruskals_algo(edges: List[List[int]], weights: int) -> List[List[int]]:
    """
    1. Sort edges by weight.
    2. Select the edge with smallest cost. 
    3. If the candidate edge forms cycles, then ignore it and select the next smallest edge.
    4. Repeat 2 and 3 until all vertices are selected.

    To detect cycles, we can use an union-find-set.
    """
    result: List[int] = []
    candidates: List[Tuple[int, List[int]]] = []

    uf = UnionFindSet()

    for edge, cost in zip(edges, weights):
        uf.add(edge[0])
        uf.add(edge[1])
        candidates.append((cost, edge))

    candidates.sort()

    # The number of edges to form a MST equals to N - 1,
    # where N is the number of nodes
    while len(result) < uf.size() - 1:
        _, edge = candidates.pop(0)

        if uf.find(edge[0]) == uf.find(edge[1]):
            continue

        uf.union(edge[0], edge[1])
        result.append(edge)

    return result
