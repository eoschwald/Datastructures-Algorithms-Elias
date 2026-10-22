import random

from AVL import AVLTree


def check_avl(node):
    """Returns the height of the subtree and asserts the AVL + BST invariants."""
    if node is None:
        return 0
    if node.left is not None:
        assert node.left.value < node.value
    if node.right is not None:
        assert node.right.value > node.value
    left_height = check_avl(node.left)
    right_height = check_avl(node.right)
    assert abs(left_height - right_height) <= 1, f"unbalanced at {node.value}"
    assert node.height == 1 + max(left_height, right_height), f"wrong height at {node.value}"
    return node.height


# Left-Left case -> single right rotation
t = AVLTree()
for v in [3, 2, 1]:
    t.insert(v)
assert t.bfs() == [2, 1, 3]

# Right-Right case -> single left rotation
t = AVLTree()
for v in [1, 2, 3]:
    t.insert(v)
assert t.bfs() == [2, 1, 3]

# Left-Right case -> double rotation
t = AVLTree()
for v in [3, 1, 2]:
    t.insert(v)
assert t.bfs() == [2, 1, 3]

# Right-Left case -> double rotation
t = AVLTree()
for v in [1, 3, 2]:
    t.insert(v)
assert t.bfs() == [2, 1, 3]

# sorted input would turn a plain BST into a linked list, AVL stays balanced
t = AVLTree()
for v in range(1, 16):
    t.insert(v)
assert t.dfs() == list(range(1, 16))
assert t.bfs() == [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
assert check_avl(t.root) == 4

# delete triggers rebalancing
t = AVLTree()
for v in [2, 1, 3, 4]:
    t.insert(v)
t.delete(1)  # left side becomes too short -> rotate left at 2
assert t.bfs() == [3, 2, 4]
check_avl(t.root)

# delete root with two children
t = AVLTree()
for v in [5, 3, 8, 1, 4, 7, 9]:
    t.insert(v)
t.delete(5)
assert t.search(5) is False
assert t.dfs() == [1, 3, 4, 7, 8, 9]
check_avl(t.root)

# duplicates and missing values are ignored
t.insert(4)
t.delete(999)
assert t.dfs() == [1, 3, 4, 7, 8, 9]

# empty tree
empty = AVLTree()
empty.delete(42)
assert empty.dfs() == []
assert empty.bfs() == []
assert empty.search(1) is False

# random inserts/deletes compared against a python set
random.seed(42)
t = AVLTree()
expected = set()
for _ in range(2000):
    v = random.randint(0, 300)
    if random.random() < 0.6:
        t.insert(v)
        expected.add(v)
    else:
        t.delete(v)
        expected.discard(v)
    check_avl(t.root)
assert t.dfs() == sorted(expected)

print("All tests passed")
