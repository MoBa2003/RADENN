from Code.TreeNode import TreeNode
from antlr4 import *
from Code.RADENNLexer import RADENNLexer
from Code.RADENNParser import RADENNParser

mp = {21: "INT", 22: "FLOAT", 23: "STR", 24: "IDENTIFIER"}

def build_custom_tree(node, parent_val=None):
    # Preserve '(' and ')' when the parent node is 'call'
    if node.getText() in "()":
        if parent_val.lower() == "call":
            return TreeNode(node.getText(), False)

    # Skip unwanted tokens (e.g., "\n", "{}", "[]", ",") unless explicitly preserved
    if node.getText() in "\n(){},": 
        return
    
    # Handle leaf nodes (tokens with specific lexical rule names)
    if not isinstance(node, RuleContext):
        if node.symbol.type in mp:
            return TreeNode(node.getText(), False, mp[node.symbol.type])
        
    # Handle rule context nodes
    if isinstance(node, RuleContext):
        val = type(node).__name__.replace("Context", "")
        is_rule = True
    else:
        val = node.getText()
        is_rule = False

    tree_node = TreeNode(val, is_rule)

    # Recursively process children, passing the current node's value as parent_val
    for i in range(node.getChildCount()):
        child = node.getChild(i)
        child_tree_node = build_custom_tree(child, parent_val=val)

        # Add the child to the parent node only if it isn't None
        if child_tree_node:
            tree_node.children.append(child_tree_node)

    return tree_node
