from antlr4 import *
from Code.RADENNLexer import RADENNLexer
from Code.RADENNParser import RADENNParser
from graphviz import Digraph
from Code.TreeNode import *
from Code.ANTLRtoSimpleTree import *
from Code.ConvertToGraphviz import *
from Code.radenn_nodes import *
from IRBuilder import start
input_stream=InputStream("""
var x=10
do {
    print(x)
    var x=x-1
} while (x>0)
""")

lexer=RADENNLexer(input_stream)
token_stream=CommonTokenStream(lexer)
parser=RADENNParser(token_stream)

tree=parser.start()



custom_tree_root =build_custom_tree(tree)

draw_tree(custom_tree_root)


ast=start(custom_tree_root)

dot = draw_ast(ast)
dot.render("ast_output", format="png", view=False) 