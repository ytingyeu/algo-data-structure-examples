class DisjointSet:
    def __init__(self, size: int):
        self.nodes = {i: i for i in range(size)}
        self.rank = {i: 1 for i in range(size)}

        # when there is no one connected, every node is a single-member group
        self.num_of_groups = size

    def find(self, x: int) -> int:
        if x not in self.nodes:
            print(f'{x} is not found.')
            return None

        root = self.nodes[x]

        while root != self.nodes[root]:
            root = self.nodes[root]

        return root

    def union(self, x: int, y: int) -> None:
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root != y_root:
            if self.rank[x_root] > self.rank[y_root]:
                self.nodes[y_root] = x_root

            elif self.rank[x_root] < self.rank[y_root]:
                self.nodes[x_root] = y_root

            else:
                self.nodes[y_root] = x_root
                self.rank[x_root] += 1

            # num of groups minus one for removing the sigle-member group
            self.num_of_groups -= 1

    def get_num_of_groups(self):
        return self.num_of_groups


isConnected = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

n = len(isConnected)
disjoint_set = DisjointSet(n)

for row in range(n):
    for col in range(n):
        if isConnected[row][col] == 1:
            disjoint_set.union(row, col)

print(disjoint_set.nodes)
print(disjoint_set.num_of_groups)
assert disjoint_set.num_of_groups == 2
