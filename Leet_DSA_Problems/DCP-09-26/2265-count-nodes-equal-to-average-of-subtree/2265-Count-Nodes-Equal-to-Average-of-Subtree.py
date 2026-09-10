class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def averageOfSubtree(self, root):
        matching_nodes = 0

        def post_order(node):
            nonlocal matching_nodes

            if not node:
                return 0, 0

            left_sum, left_count = post_order(node.left)
            right_sum, right_count = post_order(node.right)

            current_sum = node.val + left_sum + right_sum
            current_count = 1 + left_count + right_count

            if current_sum // current_count == node.val:
                matching_nodes += 1

            return current_sum, current_count

        post_order(root)
        return matching_nodes