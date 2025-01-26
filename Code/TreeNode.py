from typing import List

class TreeNode:
    def __init__(self, val, is_rule):
        self.val = val
        self.is_rule = is_rule
        self.children:List[TreeNode] = []

    def __repr__(self):
        return f"TreeNode(val={self.val}, is_rule={self.is_rule}, children={len(self.children)})"

