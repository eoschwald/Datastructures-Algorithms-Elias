from collections import deque


class TreeElement:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeElement(value)
            return

        current = self.root
        while True:
            if value == current.value:
                return
            elif value < current.value:
                if current.left is None:
                    current.left = TreeElement(value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeElement(value)
                    return
                current = current.right

    def search(self, value):
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            current = current.left if value < current.value else current.right
        return False

    def delete(self, value):
        self.root = self.delete_recursive(self.root, value)

    def delete_recursive(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self.delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self.delete_recursive(node.right, value)
        else:
            if node.left is None and node.right is None:
                return None
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            successor = self.find_min(node.right)
            node.value = successor.value
            node.right = self.delete_recursive(node.right, successor.value)

        return node

    def find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def dfs(self):
        result = []

        def walk(node):
            if node is None:
                return
            walk(node.left)
            result.append(node.value)
            walk(node.right)

        walk(self.root)
        return result

    def bfs(self):
        if self.root is None:
            return []
        result = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.value)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return result