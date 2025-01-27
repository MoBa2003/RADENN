
from antlr4 import *
from Code.RADENNLexer import RADENNLexer
from Code.RADENNParser import RADENNParser
from graphviz import Digraph
from Code.TreeNode import *
from Code.ANTLRtoSimpleTree import *
from Code.ConvertToGraphviz import *
from Code.radenn_nodes import *
from IRBuilder import start
import os, logging
logging.getLogger('tensorflow').disabled = True
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow.keras.optimizers import *
from tensorflow.keras.layers import Dense, Dropout, Activation, BatchNormalization
from tensorflow.keras.models import Sequential, clone_model
from radenn_lexer import TOKENS, lex
from radenn_parser import parse
from radenn_errors import RTError
from radenn_context import Context
from radenn_symbol_table import SymbolTable
import pickle

import numpy as np
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.metrics import confusion_matrix, mean_squared_error, mean_absolute_error, r2_score
from copy import deepcopy

PATH = None
OPTIMIZERS = ["SGD", "RMSprop", "Adagrad", "Adadelta", "Adam", "Adamax", "Nadam"]
KERNEL_INITIALIZERS = ["zeros", "ones", "RandomNormal", "RandomUniform", "TruncatedNormal", "VarianceScaling", "Orthogonal", "Identity", "lecun_uniform", "glorot_normal", "glorot_uniform", "he_normal", "lecun_normal", "he_uniform"]
ACTIVATION_FUNCTIONS = ["elu", "softmax", "selu", "softplus", "softsign", "relu", "tanh", "sigmoid", "hard_sigmoid", "linear"]
LOSS_FUNCTIONS = ["mean_squared_error", "mean_squared_logarithmic_error", "mean_absolute_error", "binary_crossentropy", "hinge", "squared_hinge", "categorical_crossentropy", "sparse_categorical_crossentropy", "kullback_leibler_divergence"]

class Context:
    def __init__(self, display_name, parent=None, parent_entry_pos=None):
        self.display_name = display_name
        self.parent = parent
        self.parent_entry_pos = parent_entry_pos
        self.symbol_table = None
        

class SymbolTable:
    def __init__(self, parent=None):
        self.symbols = {}
        self.parent = parent
        
    def get(self, name):
        value = self.symbols.get(name, None)
        if value == None and self.parent:
            return self.parent.get(name)
        return value 
    def set(self, name, value):
        self.symbols[name] = value
        
    def remove(self, name):
        del self.symbols[name]

class RTResult:
    def __init__(self):
        self.reset()

    def reset(self):
        self.value = None
        self.error = None
        self.func_return_value = None
        self.loop_should_continue = False
        self.loop_should_break = False

    def register(self, res):
        self.error = res.error
        self.func_return_value = res.func_return_value
        self.loop_should_continue = res.loop_should_continue
        self.loop_should_break = res.loop_should_break
        return res.value

    def success(self, value):
        self.reset()
        self.value = value
        return self

    def success_return(self, value):
        self.reset()
        self.func_return_value = value
        return self

    def success_continue(self):
        self.reset()
        self.loop_should_continue = True
        return self

    def success_break(self):
        self.reset()
        self.loop_should_break = True
        return self

    def failure(self, error):
        self.reset()
        self.error = error
        return self

    def should_return(self):
        return (self.error or self.func_return_value or self.loop_should_continue or self.loop_should_break)

class Value:
    def __init__(self):
        self.set_context()
        self.set_should_print()


    def set_context(self, context=None):
        self.context = context
        return self
    
    def set_should_print(self, should_print=True):
        self.should_print = should_print
        return self

    def copy(self):
        raise Exception("No copy method defined")

    def is_true(self):
        return False


    def execute(self, args):
        pass 

    def added_to(self, other):
        pass

    def subbed_by(self, other):
        pass

    def multed_by(self, other):
        pass

    def dived_by(self, other):
        pass

    def moded_by(self, other):
        pass

    def powed_by(self, other):
        pass

    def get_comparison_ee(self, other):
        pass

    def get_comparison_ne(self, other):
        pass

    def get_comparison_lt(self, other):
        pass

    def get_comparison_gt(self, other):
        pass

    def get_comparison_lte(self, other):
        pass

    def get_comparison_gte(self, other):
        pass

    def anded_by(self, other):
        pass

    def ored_by(self, other):
        pass

    def notted(self):
        pass



class Number(Value):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def __repr__(self):
        return f"{self.value}"

    def copy(self):
        copy = Number(self.value)
        copy.set_context(self.context)
        copy.set_should_print(self.should_print)
        return copy

    def is_true(self):
        return self.value != 0

    def added_to(self, other):
        return self.operate(other, "+")

    def subbed_by(self, other):
        return self.operate(other, "-")

    def multed_by(self, other):
        return self.operate(other, "*")

    def dived_by(self, other):
        return self.operate(other, "/")

    def moded_by(self, other):
        return self.operate(other, "%")

    def powed_by(self, other):
        return self.operate(other, "^")

    def get_comparison_ee(self, other):
        return self.compare(other, "==")

    def get_comparison_ne(self, other):
        return self.compare(other, "!=")

    def get_comparison_lt(self, other):
        return self.compare(other, "<")

    def get_comparison_gt(self, other):
        return self.compare(other, ">")

    def get_comparison_lte(self, other):
        return self.compare(other, "<=")

    def get_comparison_gte(self, other):
        return self.compare(other, ">=")

    def anded_by(self, other):
        return self.logic_operate(other, "and")

    def ored_by(self, other):
        return self.logic_operate(other, "or")

    def notted(self):
        return Number(int(self.value == 0)).set_context(self.context)

    def operate(self, other, operand):
        if isinstance(other, Number):
            if operand in "+-*^":
                if operand == "+":
                    return Number(self.value + other.value).set_context(self.context)
                if operand == "-":
                    return Number(self.value - other.value).set_context(self.context)
                if operand == "*":
                    return Number(self.value * other.value).set_context(self.context)
                if operand == "^":
                    return Number(self.value ** other.value).set_context(self.context)
            else:
                if other.value == 0:
                    return None
                if operand == "/":
                    return Number(self.value / other.value).set_context(self.context)
                if operand == "%":
                    return Number(self.value % other.value).set_context(self.context)
        elif isinstance(other, String):
            if operand in "+-*^":
                try:
                    if operand == "+":
                        return Number(self.value + eval(other.value)).set_context(self.context)
                    if operand == "-":
                        return Number(self.value - eval(other.value)).set_context(self.context)
                    if operand == "*":
                        return Number(self.value * eval(other.value)).set_context(self.context)
                    if operand == "^":
                        return Number(self.value ** eval(other.value)).set_context(self.context)
                except Exception as e:
                    if operand == "+":
                        return String(str(self.value) + other.value).set_context(self.context)
                    if operand == "*":
                        return String(self.value * other.value).set_context(self.context)
                    return None
            else:
                try:
                    divisor = eval(other.value)
                except Exception as e:
                    return None
                if divisor == 0:
                    return None
                if operand == "/":
                    return Number(self.value / divisor).set_context(self.context)
                if operand == "%":
                    return Number(self.value % divisor).set_context(self.context)
                
                




Number.null = Number(0).set_should_print(False)
Number.true = Number(1)
Number.false = Number(0)

class String(Value):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def __repr__(self):
        return f'"{self.value}"'
    
    def __str__(self):
        return f'{self.value}'

    def copy(self):
        copy = String(self.value)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        copy.set_should_print(self.should_print)
        return copy

    def is_true(self):
        return len(self.value) > 0

    def added_to(self, other):
        return self.operate(other, "+")

    def subbed_by(self, other):
        return self.operate(other, "-")

    def multed_by(self, other):
        return self.operate(other, "*")

    def dived_by(self, other):
        return self.operate(other, "/")

    def moded_by(self, other):
        return self.operate(other, "%")

    def powed_by(self, other):
        return self.operate(other, "^")

    def get_comparison_ee(self, other):
        return self.compare(other, "==")

    def get_comparison_ne(self, other):
        return self.compare(other, "!=")

    def get_comparison_lt(self, other):
        return self.compare(other, "<")

    def get_comparison_gt(self, other):
        return self.compare(other, ">")

    def get_comparison_lte(self, other):
        return self.compare(other, "<=")

    def get_comparison_gte(self, other):
        return self.compare(other, ">=")

    def anded_by(self, other):
        return self.logic_operate(other, "and")

    def ored_by(self, other):
        return self.logic_operate(other, "or")

    def notted(self):
        return Number(int(self.value == 0)).set_context(self.context), None

    def operate(self, other, operand):
        if isinstance(other, Number):
            if operand in "+-*^":
                try:
                    if operand == "+":
                        return Number(eval(self.value) + other.value).set_context(self.context), None
                    if operand == "-":
                        return Number(eval(self.value) - other.value).set_context(self.context), None
                    if operand == "*":
                        return Number(eval(self.value) * other.value).set_context(self.context), None
                    if operand == "^":
                        return Number(eval(self.value) ** other.value).set_context(self.context), None
                except Exception as e:
                    if operand == "+":
                        return String(self.value + str(other.value)).set_context(self.context), None
                    if operand == "*":
                        return String(self.value * other.value).set_context(self.context), None
            else:
                try:
                    dividend = eval(self.value)
                except Exception as e:
                    return None, Value.illegal_operation(self, other)
                if other.value == 0:
                    return None, RTError(other.pos_start, other.pos_end, "Division by zero", self.context)
                if operand == "/":
                    return Number(dividend / other.value).set_context(self.context), None
                if operand == "%":
                    return Number(dividend % other.value).set_context(self.context), None
        elif isinstance(other, String):
            if operand in "+-^":
                try:
                    if operand == "+":
                        return Number(eval(self.value) + eval(other.value)).set_context(self.context), None
                    if operand == "-":
                        return Number(eval(self.value) - eval(other.value)).set_context(self.context), None
                    if operand == "^":
                        return Number(eval(self.value) ** eval(other.value)).set_context(self.context), None
                except Exception as e:
                    if operand == "+":
                        return String(self.value + other.value).set_context(self.context), None
            elif operand == "*":
                op1_is_number = True
                try:
                    n1 = eval(self.value)
                except Exception as e:
                    op1_is_number = False
                op2_is_number = True
                try:
                    n2 = eval(other.value)
                except Exception as e:
                    op2_is_number = False
                if (op1_is_number and op2_is_number):
                    return Number(n1 * n2).set_context(self.context), None
                elif (op1_is_number):
                    return String(n1 * other.value).set_context(self.context), None
                elif (op2_is_number):
                    return String(self.value * n2).set_context(self.context), None
            else:
                try:
                    dividend = eval(self.value)
                    divisor = eval(other.value)
                except Exception as e:
                    return None, Value.illegal_operation(self, other)
                if divisor == 0:
                    return None, RTError(other.pos_start, other.pos_end, "Division by zero", self.context)
                if operand == "/":
                    return Number(dividend / divisor).set_context(self.context), None
                if operand == "%":
                    return Number(dividend % divisor).set_context(self.context), None
        return None, Value.illegal_operation(self, other)

    def compare(self, other, operand):
        if isinstance(other, Number):
            if operand == "==":
                return Number(int(self.value == str(other.value))).set_context(self.context), None
            if operand == "!=":
                return Number(int(self.value != str(other.value))).set_context(self.context), None
            try:
                number = eval(self.value)
            except Exception as e:
                None, Value.illegal_operation(self, other)
            if operand == "<":
                return Number(int(number < other.value)).set_context(self.context), None
            if operand == ">":
                return Number(int(number > other.value)).set_context(self.context), None
            if operand == "<=":
                return Number(int(number <= other.value)).set_context(self.context), None
            if operand == ">=":
                return Number(int(number >= other.value)).set_context(self.context), None
        elif isinstance(other, String):
            if operand == "==":
                return Number(int(self.value == other.value)).set_context(self.context), None
            if operand == "!=":
                return Number(int(self.value != other.value)).set_context(self.context), None
            try:
                n1 = eval(self.value)
                n2 = eval(other.value)
            except Exception as e:
                None, Value.illegal_operation(self, other)
            if operand == "<":
                return Number(int(n1 < n2)).set_context(self.context), None
            if operand == ">":
                return Number(int(n1 > n2)).set_context(self.context), None
            if operand == "<=":
                return Number(int(n1 <= n2)).set_context(self.context), None
            if operand == ">=":
                return Number(int(n1 >= n2)).set_context(self.context), None
        if operand == "==":
            return Number(0).set_context(self.context), None
        if operand == "!=":
            return Number(1).set_context(self.context), None
        return None, Value.illegal_operation(self, other)

    def logic_operate(self, other, operand):
        is_number = True
        try:
            number = eval(self.value)
        except Exception as e:
            is_number = False
        if is_number:
            if isinstance(other, Number):
                if operand == "and":
                    return Number(1 if (number and other.value) else 0).set_context(self.context), None
                if operand == "or":
                    return Number(1 if (number or other.value) else 0).set_context(self.context), None
            elif isinstance(other, String):
                try:
                    if operand == "and":
                        return Number(1 if (number and eval(other.value)) else 0).set_context(self.context), None
                    if operand == "or":
                        return Number(1 if (number or eval(other.value)) else 0).set_context(self.context), None
                except Exception as e:
                    if operand == "and":
                        return Number(1 if (number and other.value) else 0).set_context(self.context), None
                    if operand == "or":
                        return Number(1 if (number or other.value) else 0).set_context(self.context), None
            elif isinstance(other, List):
                if operand == "and":
                    return Number(1 if (number and len(other.elements)) else 0).set_context(self.context), None
                if operand == "or":
                    return Number(1 if (number or len(other.elements)) else 0).set_context(self.context), None
            elif isinstance(other, Matrix):
                if operand == "and":
                    return Number(1 if (number and len(other.rows)) else 0).set_context(self.context), None
                if operand == "or":
                    return Number(1 if (number or len(other.rows)) else 0).set_context(self.context), None

        if isinstance(other, Number):
            if operand == "and":
                return Number(1 if (self.value and other.value) else 0).set_context(self.context), None
            if operand == "or":
                return Number(1 if (self.value or other.value) else 0).set_context(self.context), None
        elif isinstance(other, String):
            try:
                if operand == "and":
                    return Number(1 if (self.value and eval(other.value)) else 0).set_context(self.context), None
                if operand == "or":
                    return Number(1 if (self.value or eval(other.value)) else 0).set_context(self.context), None
            except Exception as e:
                if operand == "and":
                    return Number(1 if (self.value and other.value) else 0).set_context(self.context), None
                if operand == "or":
                    return Number(1 if (self.value or other.value) else 0).set_context(self.context), None
        elif isinstance(other, List):
            if operand == "and":
                return Number(1 if (self.value and len(other.elements)) else 0).set_context(self.context), None
            if operand == "or":
                return Number(1 if (self.value or len(other.elements)) else 0).set_context(self.context), None
        elif isinstance(other, Matrix):
            if operand == "and":
                return Number(1 if (self.value and len(other.rows)) else 0).set_context(self.context), None
            if operand == "or":
                return Number(1 if (self.value or len(other.rows)) else 0).set_context(self.context), None
        return None, Value.illegal_operation(self, other)


input_stream=InputStream("""
var x = "global variable"

function f() print(x)
    
function g(){
    var x = "inner variable"
    f()
}

function h() print(x)
        
f() # global variable
g() # inner variable
h() # global variable
""")

lexer=RADENNLexer(input_stream)
token_stream=CommonTokenStream(lexer)
parser=RADENNParser(token_stream)

tree=parser.start()
custom_tree_root =build_custom_tree(tree)
ast=start(custom_tree_root)