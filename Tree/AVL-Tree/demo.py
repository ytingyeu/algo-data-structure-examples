from AVLTree import AVLTree


def main():
    nums = [2, 9, 4, 8, 5, 0, 7]

    avl_tree = AVLTree()

    for n in nums:
        avl_tree.insert(n)

    avl_tree.visualize()

    avl_tree.delete(8)
    avl_tree.visualize()


if __name__ == "__main__":
    main()
