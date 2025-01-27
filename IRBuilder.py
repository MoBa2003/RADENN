from antlr4 import *
from Code.RADENNLexer import RADENNLexer
from Code.RADENNParser import RADENNParser
from graphviz import Digraph
from Code.TreeNode import *
from Code.ANTLRtoSimpleTree import *
from Code.ConvertToGraphviz import *
from Code.radenn_nodes import *



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
    # print("dbg: statement",node)
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
    # print('dbg expr: ',node)
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
    # print("dbg atom: " ,node) 
    if node.val=='[]':
        return ListNode([])
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
    if (node.children[0].val).lower()=="matexpr":
        return matExpr(node.children[0])
    if (node.children[0].val).lower()=="datasetexpr":
        return datasetExpr(node.children[0])
    if (node.children[0].val).lower()=="optimizerexpr":
        return optimizerExpr(node.children[0])
    if (node.children[0].val).lower()=="inputlayerexpr":
        return inputLayerExpr(node.children[0])
    if (node.children[0].val).lower()=="hiddenlayerexpr":
        return hiddenLayerExpr(node.children[0])
    if (node.children[0].val).lower()=="outputlayerexpr":
        return outputLayerExpr(node.children[0])
    if (node.children[0].val).lower()=="networkexpr":
        return networkExpr(node.children[0])
    if (node.children[0].val).lower()=="forexpr":
        return forExpr(node.children[0])
    if (node.children[0].val).lower()=="whileexpr":
        return whileExpr(node.children[0])
    if (node.children[0].val).lower()=="dowhileexpr":
        return doWhileExpr(node.children[0])
    if (node.children[0].val).lower()=="funcdef":
        return funcDef(node.children[0])
    if (node.children[0].val).lower()=="ifexpr":
        return ifExpr(node.children[0])
    if (node.children[0].val).lower()=="matexpr":
        return matExpr(node.children[0])
    pass    
    

def listExpr(node:TreeNode):
    if len(node.children)==2:
        return ListNode([])
    items=[]
    for i in range(1,len(node.children)-1):
        # print(node.children[i])
        items.append(expr(node.children[i]))
    return ListNode(items)

def matExpr(node:TreeNode)->MatrixNode:
    rows=[]
    for i in range(len(node.children)):
        rows.append(matRow(node.children[i]))
    # print("dbg matExpr: " ,rows)
    return MatrixNode(rows)
def matRow(node: TreeNode)->List:
    row=[]
    for i in range(len(node.children)):
        row.append(expr(node.children[i]))
    return row
        
def datasetExpr(node:TreeNode):
    pass
def optimizerExpr(node:TreeNode):
    return OptimizerNode(expr(node.children[1]),expr(node.children[2]))

def inputLayerExpr(node:TreeNode):
    items=[]
    for i in range(1,7):
        items.append(expr(node.children[i]))
    return InputLayerNode(items[0],items[1],items[2],items[3],items[4],items[5])
def hiddenLayerExpr(node:TreeNode):
    items=[]
    for i in range(1,6):
        items.append(expr(node.children[i]))
        # print(type(items[i-1]))
    return HiddenLayerNode(items[0],items[1],items[2],items[3],items[4]) 
def outputLayerExpr(node:TreeNode):
    items=[]
    for i in range(1,4):
        items.append(expr(node.children[i]))
    return OutputLayerNode(items[0],items[1],items[2])

def networkExpr(node:TreeNode):
    items=[]
    for i in range(1,len(node.children)):
        items.append(expr(node.children[i]))
    # print(items)
    return NetworkNode(items[0],items[1:-1],items[-1])

def forExpr(node:TreeNode):
    cr=1
    id_tok=node.children[cr].val
    cr+=1
    init_val_node=expr(node.children[cr])
    cr+=1
    end_val_node=expr(node.children[cr])
    cr+=1
    step_value=None
    if (node.children[cr].val).lower()=="expr":
        step_value=expr(node.children[cr])
        cr+=1
    body_node=None
    # print(id_tok,init_val_node,end_val_node,step_value)
    if (node.children[cr].val).lower()=="statement":
        body_node=statement(node.children[cr])
    else:
        body_node=statements(node.children[cr])
    return ForNode(id_tok,init_val_node,end_val_node,step_value,body_node)  
    
def whileExpr(node:TreeNode):
    cond_node=expr(node.children[1])
    body_node=None
    if (node.children[2].val).lower()=="statement":
        body_node=statement(node.children[2])
    else:
        body_node=statements(node.children[2])
    return WhileNode(cond_node,body_node)

def doWhileExpr(node:TreeNode):
    body_node=None
    if (node.children[1].val).lower()=="statement":
        body_node=statement(node.children[1])
    else:
        body_node=statement(node.children[1])
    cond_node=expr(node.children[3])
    return DoWhileNode(body_node,cond_node)

def funcDef(node:TreeNode):
    cr=1
    var_name_tok=node.children[cr].val
    cr+=1
    arg_name_toks=[]
    body_node=None
    should_auto_return=None
    while (node.children[cr].val).lower() not in ['statements','statement']:
        arg_name_toks.append(node.children[cr].val)
        cr+=1
    if (node.children[cr].val).lower() =='statement':
        body_node=statement(node.children[cr])
        should_auto_return=True
    else:
        body_node=statements(node.children[cr])
        should_auto_return=False
    # print("dbg funcDef: ",var_name_tok,arg_name_toks)
        
    return FuncDefNode(var_name_tok,arg_name_toks,body_node,should_auto_return)


def ifExpr(node:TreeNode):
    curr=node
    cases=[]
    else_case=None
    while len(curr.children)==4: 
        cond_expr=expr(curr.children[1])
        body_stmt=None
        if (curr.children[2].val).lower() =='statement':
            body_stmt=statement(curr.children[2])
        else:
            body_stmt=statements(curr.children[2])
        cases.append((cond_expr,body_stmt))
        curr=curr.children[3]
    if (curr.val).lower() =='elseexpr':
        if (curr.children[1].val).lower()=='statement':
            else_case=statement(curr.children[1])
        else:
            else_case=statements(curr.children[1])
    else:
        cond_expr=expr(curr.children[1])
        body_stmt=None
        if (curr.children[2].val).lower() =='statement':
            body_stmt=statement(curr.children[2])
        else:
            body_stmt=statements(curr.children[2])
        cases.append((cond_expr,body_stmt))
    # print("dbg ifexpr: ",cases,else_case)
    return IfNode(cases,else_case)
    
