from typing import List

class TreeNode:
    def __init__(self, val, is_rule, lexrulename=None): 
        self.val = val
        self.is_rule = is_rule
        self.lexrulename = lexrulename  # Name of the lexical rule (e.g., 'INT', 'IDENTIFIER')
        self.children: List[TreeNode] = []

    def __repr__(self):
        return f"TreeNode(val={self.val}, is_rule={self.is_rule}, lexrulename={self.lexrulename}, children={len(self.children)})"
