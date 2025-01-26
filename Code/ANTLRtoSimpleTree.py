from Code.TreeNode import  TreeNode
from antlr4 import *
from Code.RADENNLexer import RADENNLexer
from Code.RADENNParser import RADENNParser


def build_custom_tree(node):

    if isinstance(node, Token) and node.type == RADENNLexer.NEWLINE or node.getText() in "\n(){}[],":
        return

    if isinstance(node, RuleContext):
        val = type(node).__name__.replace("Context", "")
        is_rule = True
    else:
        val = node.getText()
        is_rule = False

    tree_node = TreeNode(val, is_rule)

    for i in range(node.getChildCount()):
        child = node.getChild(i)
        child_tree_node = build_custom_tree(child)

        # Add the child to the parent node only if it isn't None (i.e., not a NEWLINE)
        if child_tree_node:
            tree_node.children.append(child_tree_node)

    return tree_node
