class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


"""
The following code builds a tree that looks like:
    0
  /   \
 1     2
"""


def dfs(node):
	if not node:
		return

	dfs(node.left)
	print(node.val)
	dfs(node.right)


root = TreeNode(0)
one = TreeNode(1)
two = TreeNode(2)
child3 = TreeNode(4)
child4 = TreeNode(6)
child5 = TreeNode(7)

root.left = one
root.right = two
one.left = child4
one.right = child3
two.left = child5

dfs(root)