from antlr4 import *
from Code.RADENNLexer import RADENNLexer
from Code.RADENNParser import RADENNParser
from graphviz import Digraph
from Code.TreeNode import *
from Code.ANTLRtoSimpleTree import *
from Code.ConvertToGraphviz import *
from Code.radenn_nodes import *

input_stream=InputStream("""
var x=1 and 1 or 1
""")

lexer=RADENNLexer(input_stream)
token_stream=CommonTokenStream(lexer)
parser=RADENNParser(token_stream)

tree=parser.start()



custom_tree_root =build_custom_tree(tree)

draw_tree(custom_tree_root)



def statements(node:TreeNode):
    node_elements=[]
    for items in node.children:
        node_elements.append(statement(items))
    return ListNode(node_elements)
        
def statement(node:TreeNode):
    if node.children[0].isrule==False and node.children[0]=='return':
        if (len(node.children)>1):
            return ReturnNode(expr(node.children[1]))
        else:
            return ReturnNode(None)
    if node.children[0].isrule==False and node.children[0]=='continue':
        return ContinueNode
    if node.children[0].isrule==False and node.children[0]=='break':
        return BreakNode
    
    return expr()

def expr(node:TreeNode):
    if node.children[0].isrule==False and node.children[0].val=='var':
        return VarAssignNode(node.children[1].val,compExpr(node.children[3]))
    
    
    
def compExpr(node:TreeNode):
    pass
        