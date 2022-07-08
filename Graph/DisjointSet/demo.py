from DisjointSet import DisjointSet


def main():

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

    print(disjoint_set.root_of_node)
    print(disjoint_set.num_of_groups)
    assert disjoint_set.num_of_groups == 2


if __name__ == "__main__":
    main()
