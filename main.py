from antlr4 import *
from Code.RADENNLexer import RADENNLexer
from Code.RADENNParser import RADENNParser
from graphviz import Digraph
from Code.TreeNode import *
from Code.ANTLRtoSimpleTree import *
from Code.ConvertToGraphviz import *
from Code.radenn_nodes import *

input_stream=InputStream("""

var x=[]
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

def bin_op_compExpr_compExpr(cur_childs:List[TreeNode]):
    if len(cur_childs)==1:
        return compExpr(cur_childs[0])
    return BinOpNode(bin_op_compExpr_compExpr(cur_childs[:-2]),cur_childs[-2].val,compExpr(cur_childs[-1]))


def expr(node:TreeNode):
    if node.children[0].val=='var':
        return VarAssignNode(node.children[1].val,expr(node.children[3]))
    if len(node.children)==1:
        return compExpr(node.children[0])
    curr_childs=node.children.copy()
    return bin_op_compExpr_compExpr(curr_childs)

def bin_op_arithExpr_arithExpr(cur_childs:List[TreeNode]):
    if len(cur_childs)==1:
        return arithExpr(cur_childs[0])
    return BinOpNode(bin_op_arithExpr_arithExpr(cur_childs[:-2]),cur_childs[-2].val,arithExpr(cur_childs[-1]))
   
def compExpr(node:TreeNode):
    if node.children[0].val=='@':
        return UnaryOpNode('not',compExpr(node.children[1]))
    if len(node.children)==1:
        return arithExpr(node.children[0])
    cur_childs=node.children.copy()
    return bin_op_arithExpr_arithExpr(cur_childs)

def bin_op_term_term(cur_childs:List[TreeNode]):
    if len(cur_childs)==1:
        return term(cur_childs[0])
    return BinOpNode(bin_op_term_term(cur_childs[:-2]),cur_childs[-2].val,term(cur_childs[-1]))
   
def arithExpr(node:TreeNode):
    cur_childs=node.children.copy()
    return bin_op_term_term(cur_childs)
    pass

def bin_op_factor_factor(cur_childs:List[TreeNode]):
    if len(cur_childs)==1:
        return factor(cur_childs[0])
    return BinOpNode(bin_op_factor_factor(cur_childs[:-2]),cur_childs[-2].val,factor(cur_childs[-1]))
   
def term(node:TreeNode):
    cur_childs=node.children.copy()
    return bin_op_factor_factor(cur_childs)
    

def factor(node:TreeNode):
    if node.children[0].val in '+-':
        return UnaryOpNode(node.children[0].val,factor(node.children[1]))
    return power(node.children[0])
    pass


def power(node: TreeNode):
    if len(node.children)==1:
        return call(node.children[0])
    return BinOpNode(call(node.children[0]),node.children[1].val,factor(node.children[2]))



def call(node: TreeNode):
    if len(node.children)==1: return atom(node.children[0])
    node.children.pop(1)
    node.children.pop(-1)
    nodetocall=atom(node.children[0])
    args=[]
    for i in node.children[1:]:
        args.append(expr(i))
    return CallNode(nodetocall,args)
    
    
def atom(node:TreeNode):
    
    if (node.children[0].lexrulename in ["INT","FLOAT"]):

        return NumberNode(node.children[0].val)
    if (node.children[0].lexrulename=="STR"):

        return StringNode(node.children[0].val)
    if (node.children[0].lexrulename=="IDENTIFIER"):

        return VarAccessNode(node.children[0].val)
    
    if (node.children[0].val).lower()=="expr":
        # print('s')
        return expr(node.children[0])
    if (node.children[0].val).lower()=="listexpr":
        
        return listExpr(node.children[0]) 
    
    
    return NumberNode(node.children[0].val)

def listExpr(node:TreeNode):
    if len(node.children)==2:
        return ListNode([])
    items=[]
    for i in range(1,len(node.children)+1):
        items.append(expr(node.children[i]))
    return ListNode(items)
    
ast:ListNode=start(custom_tree_root)
# print(type(ast.element_nodes[0]))
dot = draw_ast(ast)
dot.render("ast_output", format="png", view=False)  