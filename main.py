from antlr4 import *
from Code.RADENNLexer import RADENNLexer
from Code.RADENNParser import RADENNParser
from graphviz import Digraph
from Code.TreeNode import *
from Code.ANTLRtoSimpleTree import *
from Code.ConvertToGraphviz import *
from Code.radenn_nodes import *

input_stream=InputStream("""
if (number > 0) {
print("Positive number")
} elif (number < 0) {
print("Negative number")
} else {
print("Zero")
}
""")

lexer=RADENNLexer(input_stream)
token_stream=CommonTokenStream(lexer)
parser=RADENNParser(token_stream)

tree=parser.start()



custom_tree_root =build_custom_tree(tree)

draw_tree(custom_tree_root)



# def statements(node:TreeNode):
#     node_elements=[]
#     for items in node.children:
#         node_elements.append(statement(items))
        
# def statement(node:TreeNode):
    
    