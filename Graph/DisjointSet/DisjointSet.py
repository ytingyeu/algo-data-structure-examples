class DisjointSet:
    def __init__(self, size: int):
        self.root_of_node = {i: i for i in range(size)}
        self.rank_of_node = {i: 1 for i in range(size)}

        # when there is no one connected, every node is a single-member group
        self.num_of_groups = size

    def find(self, x: int) -> int:
        if x not in self.root_of_node:
            print(f'{x} is not found.')
            return None

        root = self.root_of_node[x]

        while root != self.root_of_node[root]:
            root = self.root_of_node[root]

        return root

    def union(self, x: int, y: int) -> None:
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root != y_root:
            if self.rank_of_node[x_root] > self.rank_of_node[y_root]:
                self.root_of_node[y_root] = x_root

            elif self.rank_of_node[x_root] < self.rank_of_node[y_root]:
                self.root_of_node[x_root] = y_root

            else:
                self.root_of_node[y_root] = x_root
                self.rank_of_node[x_root] += 1

            # num of groups minus one for removing the sigle-member group
            self.num_of_groups -= 1

    def get_num_of_groups(self):
        return self.num_of_groups
