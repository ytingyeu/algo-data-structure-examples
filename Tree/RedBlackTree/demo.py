from RedBlackTree import RedBlackTree


def main():
    nums = [2, 9, 4, 8, 5, 0, 7]

    rb_tree = RedBlackTree()

    for n in nums:
        rb_tree.insert(n)

    rb_tree.visualize()


if __name__ == "__main__":
    main()
