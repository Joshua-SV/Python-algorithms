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
 / \   /
 6  4 7
"""


def dfsLeftMax(node,depth):
	if not node:
		return depth
	depth += 1
	maxLeftDepth = dfsLeftMax(node.left, depth)
	maxRightDepth = dfsLeftMax(node.right, depth)
	return max(maxRightDepth, maxLeftDepth)

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

Max = dfsLeftMax(root, 0)

print(Max)
