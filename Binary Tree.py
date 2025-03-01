from collections import deque

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder_traversal(self, node):          # Root -> Left -> Right
        if node:
            print(node.val, end=' ')
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def inorder_traversal(self, node):           # Left -> Root -> Right
        if node:
            self.inorder_traversal(node.left)
            print(node.val, end=' ')
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node):        # Left -> Right -> Root
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.val, end=' ')

    def level_order_traversal(self, node):      # Level order traversal
        if not node:
            return []
        queue = deque([node])
        lst = []
        while queue:
            temp = []
            for i in range(len(queue)):
                current = queue.popleft()
                temp.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            lst.append(temp)
        print(lst)

    def BFS(self, node):
        if not node:
            return []
        queue = deque([node])
        lst = []
        while queue:
            current = queue.popleft()
            lst.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print(lst)

    def DFS(self, node):
        if not node:
            return []
        stack = [node]
        lst = []
        while stack:
            current = stack.pop()
            lst.append(current.val)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        print(lst)

# Example usage:
# Constructing a binary tree
#         1
#        / \
#       2   3
#      / \             
#     4   5

tree = BinaryTree()
tree.root = TreeNode(1)
tree.root.left = TreeNode(2)
tree.root.right = TreeNode(3)
tree.root.left.left = TreeNode(4)
tree.root.left.right = TreeNode(5)

print("Preorder traversal:")
tree.preorder_traversal(tree.root)
print("\nInorder traversal:")
tree.inorder_traversal(tree.root)
print("\nPostorder traversal:")
tree.postorder_traversal(tree.root)
print("\n\nLevel order traversal:")
tree.level_order_traversal(tree.root)
print("\nBFS traversal:")
tree.BFS(tree.root)
print("\nDFS traversal:")
tree.DFS(tree.root)