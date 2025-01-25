class NumberNode:
    def __init__(self, tok):
        self.tok = tok
        
        

    def __repr__(self):
        return f"{self.tok}"


class StringNode:
    def __init__(self, tok):
        self.tok = tok
        
        

    def __repr__(self):
        return f"{self.tok}"


class ListNode:
    def __init__(self, element_nodes):
        self.element_nodes = element_nodes
        
        
    def __repr__(self):
        return f"[{', '.join(map(str, self.element_nodes))}]"

class MatrixNode:
    def __init__(self, row_nodes):
        self.row_nodes = row_nodes
        
        
    def __repr__(self):
        return f"Matrix({self.row_nodes})"


class DatasetNode:
    def __repr__(self):
        return f"Dataset(data={self.data_node}, labels={self.labels_node})"
    def __init__(self, data_node, labels_node):
        self.data_node = data_node
        self.labels_node = labels_node
        
        


class OptimizerNode:
    def __repr__(self):
        return f"Optimizer(type={self.type_node}, learning_rate={self.learning_rate_node})"

    def __init__(self, type_node, learning_rate_node):
        self.type_node = type_node
        self.learning_rate_node = learning_rate_node
        
        


class InputLayerNode:
    def __repr__(self):
        return f"InputLayer(input_neurons={self.input_neurons_node}, hidden_neurons={self.hidden_neurons_node}, kernel_initializer={self.kernel_initializer_node}, batch_normalization={self.batch_normalization_node}, dropout={self.dropout_node}, activation_function={self.activation_function_node})"

    def __init__(self, input_neurons_node, hidden_neurons_node, kernel_initializer_node, batch_normalization_node, dropout_node, activation_function_node):
        self.input_neurons_node = input_neurons_node
        self.hidden_neurons_node = hidden_neurons_node
        self.kernel_initializer_node = kernel_initializer_node
        self.batch_normalization_node = batch_normalization_node
        self.dropout_node = dropout_node
        self.activation_function_node = activation_function_node
        
        


class HiddenLayerNode:
    def __repr__(self):
        return f"HiddenLayer(neurons={self.neurons_node}, kernel_initializer={self.kernel_initializer_node}, batch_normalization={self.batch_normalization_node}, dropout={self.dropout_node}, activation_function={self.activation_function_node})"

    def __init__(self, neurons_node, kernel_initializer_node, batch_normalization_node, dropout_node, activation_function_node):
        self.neurons_node = neurons_node
        self.kernel_initializer_node = kernel_initializer_node
        self.batch_normalization_node = batch_normalization_node
        self.dropout_node = dropout_node
        self.activation_function_node = activation_function_node
        
        


class OutputLayerNode:
    def __repr__(self):
        return f"OutputLayer(neurons={self.neurons_node}, kernel_initializer={self.kernel_initializer_node}, activation_function={self.activation_function_node})"

    def __init__(self, neurons_node, kernel_initializer_node, activation_function_node):
        self.neurons_node = neurons_node
        self.kernel_initializer_node = kernel_initializer_node
        self.activation_function_node = activation_function_node
        
        


class NetworkNode:
    def __repr__(self):
        return f"Network(input_layer={self.input_layer_node}, hidden_layers={self.hidden_layers_node}, output_layer={self.output_layer_node})"

    def __init__(self, input_layer_node, hidden_layers_node, output_layer_node):
        self.input_layer_node = input_layer_node
        self.hidden_layers_node = hidden_layers_node
        self.output_layer_node = output_layer_node
        
        


class VarAccessNode:
    def __repr__(self):
        return f"{self.var_name_tok}"
    def __init__(self, var_name_tok):
        self.var_name_tok = var_name_tok
        
        

    def __repr__(self):
        return f"{self.var_name_tok}"


class VarAssignNode:
    def __repr__(self):
        return f"{self.var_name_tok} = {self.value_node}"

    def __init__(self, var_name_tok, value_node):
        self.var_name_tok = var_name_tok
        self.value_node = value_node
        
        

    def __repr__(self):
        return f"{self.var_name_tok} = {self.value_node}"


class BinOpNode:
    def __repr__(self):
        return f"({self.left_node}, {self.op_tok}, {self.right_node})"

    def __init__(self, left_node, op_tok, right_node):
        self.left_node = left_node
        self.op_tok = op_tok
        self.right_node = right_node
        
        

    def __repr__(self):
        return f"({self.left_node}, {self.op_tok}, {self.right_node})"


class UnaryOpNode:
    def __repr__(self):
        return f"({self.op_tok}, {self.node})"

    def __init__(self, op_tok, node):
        self.op_tok = op_tok
        self.node = node
        
        

    def __repr__(self):
        return f"({self.op_tok}, {self.node})"


class IfNode:
    def __repr__(self):
        return f"If(cases={self.cases}, else_case={self.else_case})"

    def __init__(self, cases, else_case):
        self.cases = cases
        self.else_case = else_case
        
        
        self.pos_start = self.cases[0][0].pos_start
        self.pos_end = (self.else_case or self.cases[-1][0]).pos_end


class ForNode:
    def __repr__(self):
        return f"For(var={self.var_name_tok}, start={self.start_value_node}, end={self.end_value_node}, step={self.step_value_node}, body={self.body_node})"

    def __init__(self, var_name_tok, start_value_node, end_value_node, step_value_node, body_node):
        self.var_name_tok = var_name_tok
        self.start_value_node = start_value_node
        self.end_value_node = end_value_node
        self.step_value_node = step_value_node
        self.body_node = body_node
        
        


class WhileNode:
    def __repr__(self):
        return f"While(condition={self.condition_node}, body={self.body_node})"

    def __init__(self, condition_node, body_node):
        self.condition_node = condition_node
        self.body_node = body_node
        
        

class DoWhileNode:
    def __repr__(self):
        return f"DoWhile(body={self.body_node}, condition={self.condition_node})"

    def __init__(self, body_node, condition_node):
        self.body_node = body_node
        self.condition_node = condition_node
        
        

class FuncDefNode:
    def __repr__(self):
        return f"Function(name={self.var_name_tok}, args={self.arg_name_toks}, body={self.body_node}, auto_return={self.should_auto_return})"


    def __init__(self, var_name_tok, arg_name_toks, body_node, should_auto_return):
        self.var_name_tok = var_name_tok
        self.arg_name_toks = arg_name_toks
        self.body_node = body_node
        self.should_auto_return = should_auto_return
        
        


class CallNode:
    def __repr__(self):
        return f"Call(func={self.node_to_call}, args={self.arg_nodes})"

    def __init__(self, node_to_call, arg_nodes):
        self.node_to_call = node_to_call
        self.arg_nodes = arg_nodes
        
        


class ReturnNode:
    def __repr__(self):
        return f"Return(value={self.node_to_return})"

    def __init__(self, node_to_return):
        self.node_to_return = node_to_return
        
        


class ContinueNode:
    def __repr__(self):
        return "Continue"
    def __init__(self):
        pass
        
        


class BreakNode:
    def __repr__(self):
        return "Break"
    def __init__(self):
        pass
        
        
from graphviz import Digraph

def draw_ast(node):
    dot = Digraph()

    def add_node(name, label):
        dot.node(name, label)

    def add_edge(parent, child):
        dot.edge(parent, child)

    def visit(node):
        if isinstance(node, NumberNode):
            node_name = f"NumberNode_{id(node)}"
            add_node(node_name, f"NumberNode({node.tok})")
        elif isinstance(node, StringNode):
            node_name = f"StringNode_{id(node)}"
            add_node(node_name, f"StringNode({node.tok})")
        elif isinstance(node, ListNode):
            node_name = f"ListNode_{id(node)}"
            add_node(node_name, f"ListNode[{len(node.element_nodes)} elements]")
            for elem in node.element_nodes:
                elem_name = visit(elem)
                add_edge(node_name, elem_name)
        elif isinstance(node, MatrixNode):
            node_name = f"MatrixNode_{id(node)}"
            add_node(node_name, f"MatrixNode[{len(node.row_nodes)} rows]")
            for row in node.row_nodes:
                row_name = visit(row)
                add_edge(node_name, row_name)
        elif isinstance(node, DatasetNode):
            node_name = f"DatasetNode_{id(node)}"
            add_node(node_name, f"DatasetNode(data={node.data_node}, labels={node.labels_node})")
            add_edge(node_name, visit(node.data_node))
            add_edge(node_name, visit(node.labels_node))
        elif isinstance(node, OptimizerNode):
            node_name = f"OptimizerNode_{id(node)}"
            add_node(node_name, f"Optimizer(type={node.type_node}, lr={node.learning_rate_node})")
            add_edge(node_name, visit(node.type_node))
            add_edge(node_name, visit(node.learning_rate_node))
        elif isinstance(node, InputLayerNode):
            node_name = f"InputLayerNode_{id(node)}"
            add_node(node_name, f"InputLayerNode(input_neurons={node.input_neurons_node}, hidden_neurons={node.hidden_neurons_node})")
            add_edge(node_name, visit(node.input_neurons_node))
            add_edge(node_name, visit(node.hidden_neurons_node))
        elif isinstance(node, HiddenLayerNode):
            node_name = f"HiddenLayerNode_{id(node)}"
            add_node(node_name, f"HiddenLayerNode(neurons={node.neurons_node})")
            add_edge(node_name, visit(node.neurons_node))
        elif isinstance(node, OutputLayerNode):
            node_name = f"OutputLayerNode_{id(node)}"
            add_node(node_name, f"OutputLayerNode(neurons={node.neurons_node})")
            add_edge(node_name, visit(node.neurons_node))
        elif isinstance(node, NetworkNode):
            node_name = f"NetworkNode_{id(node)}"
            add_node(node_name, f"NetworkNode(input_layer={node.input_layer_node})")
            add_edge(node_name, visit(node.input_layer_node))
            for hidden_layer in node.hidden_layers_node:
                add_edge(node_name, visit(hidden_layer))
            add_edge(node_name, visit(node.output_layer_node))
        elif isinstance(node, VarAccessNode):
            node_name = f"VarAccessNode_{id(node)}"
            add_node(node_name, f"VarAccessNode({node.var_name_tok})")
        elif isinstance(node, VarAssignNode):
            node_name = f"VarAssignNode_{id(node)}"
            add_node(node_name, f"VarAssignNode({node.var_name_tok} = {node.value_node})")
            add_edge(node_name, visit(node.value_node))
        elif isinstance(node, BinOpNode):
            node_name = f"BinOpNode_{id(node)}"
            add_node(node_name, f"BinOpNode({node.left_node}, {node.op_tok}, {node.right_node})")
            add_edge(node_name, visit(node.left_node))
            add_edge(node_name, visit(node.right_node))
        elif isinstance(node, UnaryOpNode):
            node_name = f"UnaryOpNode_{id(node)}"
            add_node(node_name, f"UnaryOpNode({node.op_tok}, {node.node})")
            add_edge(node_name, visit(node.node))
        elif isinstance(node, IfNode):
            node_name = f"IfNode_{id(node)}"
            add_node(node_name, f"IfNode(cases={len(node.cases)}, else_case={node.else_case})")
            for case in node.cases:
                add_edge(node_name, visit(case[0]))
            if node.else_case:
                add_edge(node_name, visit(node.else_case))
        elif isinstance(node, ForNode):
            node_name = f"ForNode_{id(node)}"
            add_node(node_name, f"ForNode({node.var_name_tok}, {node.start_value_node}..{node.end_value_node})")
            add_edge(node_name, visit(node.start_value_node))
            add_edge(node_name, visit(node.end_value_node))
            add_edge(node_name, visit(node.body_node))
        elif isinstance(node, WhileNode):
            node_name = f"WhileNode_{id(node)}"
            add_node(node_name, f"WhileNode(condition={node.condition_node})")
            add_edge(node_name, visit(node.condition_node))
            add_edge(node_name, visit(node.body_node))
        elif isinstance(node, DoWhileNode):
            node_name = f"DoWhileNode_{id(node)}"
            add_node(node_name, f"DoWhileNode(condition={node.condition_node})")
            add_edge(node_name, visit(node.condition_node))
            add_edge(node_name, visit(node.body_node))
        elif isinstance(node, FuncDefNode):
            node_name = f"FuncDefNode_{id(node)}"
            add_node(node_name, f"FuncDefNode({node.var_name_tok})")
            add_edge(node_name, visit(node.body_node))
        elif isinstance(node, CallNode):
            node_name = f"CallNode_{id(node)}"
            add_node(node_name, f"CallNode({node.node_to_call})")
            add_edge(node_name, visit(node.node_to_call))
            for arg_node in node.arg_nodes:
                add_edge(node_name, visit(arg_node))
        elif isinstance(node, ReturnNode):
            node_name = f"ReturnNode_{id(node)}"
            add_node(node_name, f"ReturnNode({node.node_to_return})")
            add_edge(node_name, visit(node.node_to_return))
        elif isinstance(node, ContinueNode):
            node_name = f"ContinueNode_{id(node)}"
            add_node(node_name, f"ContinueNode()")
        elif isinstance(node, BreakNode):
            node_name = f"BreakNode_{id(node)}"
            add_node(node_name, f"BreakNode()")

        return node_name

    visit(node)
    return dot
