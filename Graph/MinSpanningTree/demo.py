from KruskalsAlgo import kruskals_algo
from PrimsAlgo import prims_algo


def demo_kruskals():
    edges = [
        [1, 2], [2, 3], [2, 7], [3, 4], [4, 5],
        [4, 7], [5, 6], [5, 7], [6, 1]
    ]

    weights = [28, 16, 14, 12, 22, 18, 25, 24, 10]

    res = kruskals_algo(edges, weights)
    print(res)


def demo_prims():
    edges = [
        [1, 2], [2, 3], [2, 7], [3, 4], [4, 5],
        [4, 7], [5, 6], [5, 7], [6, 1]
    ]

    weights = [28, 16, 14, 12, 22, 18, 25, 24, 10]

    res = prims_algo(edges, weights)
    print(res)


def main():
    demo_kruskals()
    demo_prims()


if __name__ == "__main__":
    main()
