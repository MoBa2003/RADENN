from antlr4 import *
from Code.RADENNLexer import RADENNLexer
from Code.RADENNParser import RADENNParser
from graphviz import Digraph
from Code.TreeNode import *
from Code.ANTLRtoSimpleTree import *
from Code.ConvertToGraphviz import *
from Code.radenn_nodes import *

input_stream=InputStream("""
@ 1+1
""")

lexer=RADENNLexer(input_stream)
token_stream=CommonTokenStream(lexer)
parser=RADENNParser(token_stream)

tree=parser.start()



custom_tree_root =build_custom_tree(tree)

draw_tree(custom_tree_root)


def start(node:TreeNode):
    return program(node.children[0])

def program(node:TreeNode):
    return statements(node.children[0])
def statements(node:TreeNode):
    node_elements=[]
    for items in node.children:
        node_elements.append(statement(items))
    return ListNode(node_elements)
        
def statement(node:TreeNode):
    # print("dbg: ",node.children)
    if node.children[0].is_rule==False and node.children[0].val=='return':
        
        if (len(node.children)>1):
            return ReturnNode(expr(node.children[1]))
        else:
            return ReturnNode(None)
    if node.children[0].is_rule==False and node.children[0].val=='continue':
        return ContinueNode()
    if node.children[0].is_rule==False and node.children[0].val=='break':
        return BreakNode()
    
    return expr(node.children[0])


def bin_op(cur_childs:List[TreeNode]):
    if len(cur_childs==1):
        return compExpr(cur_childs[0])
    return BinOpNode(cur_childs[0],cur_childs[1].val,bin_op(cur_childs[2:]))

def expr(node:TreeNode):
    if node.children[0].is_rule==False and node.children[0].val=='var':
        return VarAssignNode(node.children[1].val,compExpr(node.children[3]))
    if len(node.children==1):
        return compExpr(node.children[0])
    curr_childs=node.children.copy()
    return bin_op(curr_childs)


    
def compExpr(node:TreeNode):
    if node.children[0].val=='@':
        return UnaryOpNode('not',compExpr(node.children[1]))
    cur_childs=node.children.copy()
    return bin_op()
    pass

ast:ListNode=start(custom_tree_root)
print(type(ast.element_nodes[0]))
dot = draw_ast(ast)
dot.render("ast_output", format="png", view=True)  