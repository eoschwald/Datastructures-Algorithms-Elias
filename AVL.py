from BST import Tree, TreeElement


class AVLElement(TreeElement):
    def __init__(self, value):
        super().__init__(value)
        self.height = 1


class AVLTree(Tree):
    """BST from the previous exercise, extended with AVL rebalancing.

    search, dfs, bfs and find_min are inherited unchanged from Tree.
    """

    def height(self, node):
        return node.height if node is not None else 0

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    #     y              x
    #    / \            / \
    #   x   C   ->     A   y
    #  / \                / \
    # A   B              B   C
    def rotate_right(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        self.update_height(y)
        self.update_height(x)
        return x

    #   x                y
    #  / \              / \
    # A   y     ->     x   C
    #    / \          / \
    #   B   C        A   B
    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        self.update_height(x)
        self.update_height(y)
        return y

    def rebalance(self, node):
        self.update_height(node)
        balance = self.balance_factor(node)

        if balance > 1:
            # Left-Right case: turn it into a Left-Left case first
            if self.balance_factor(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1:
            # Right-Left case: turn it into a Right-Right case first
            if self.balance_factor(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def insert(self, value):
        self.root = self.insert_recursive(self.root, value)

    def insert_recursive(self, node, value):
        if node is None:
            return AVLElement(value)

        if value == node.value:
            return node
        elif value < node.value:
            node.left = self.insert_recursive(node.left, value)
        else:
            node.right = self.insert_recursive(node.right, value)

        return self.rebalance(node)

    def delete_recursive(self, node, value):
        node = super().delete_recursive(node, value)
        if node is None:
            return None
        return self.rebalance(node)
