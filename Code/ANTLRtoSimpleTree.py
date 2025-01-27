from Code.TreeNode import TreeNode
from antlr4 import *
from Code.RADENNLexer import RADENNLexer
from Code.RADENNParser import RADENNParser

mp = {21: "INT", 22: "FLOAT", 23: "STR", 24: "IDENTIFIER"}

def build_custom_tree(node, parent_val=None):
    if node.getText() in "()[]":
        if parent_val.lower() in ["call","listexpr"]:
            return TreeNode(node.getText(), False)

    if node.getText() in "\n(){},;": 
        return
    
    if not isinstance(node, RuleContext):
        if node.symbol.type in mp:
            return TreeNode(node.getText(), False, mp[node.symbol.type])
        
    if isinstance(node, RuleContext):
        val = type(node).__name__.replace("Context", "")
        is_rule = True
    else:
        val = node.getText()
        is_rule = False

    tree_node = TreeNode(val, is_rule)

    for i in range(node.getChildCount()):
        child = node.getChild(i)
        child_tree_node = build_custom_tree(child, parent_val=val)

        if child_tree_node:
            tree_node.children.append(child_tree_node)

    return tree_node
