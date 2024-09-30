class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def has_path_sum(root, target_sum):
    if not root:
        return False
    
    target_sum -= root.val
    
    if not root.left and not root.right:
        return target_sum == 0
    
    return has_path_sum(root.left, target_sum) or has_path_sum(root.right, target_sum)

# Example usage:
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

target_sum = 22
print(has_path_sum(root, target_sum))  # Output: True
