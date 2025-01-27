
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
    def compare(self, other, operand):
        if isinstance(other, Number):
            if operand == "==":
                return Number(int(self.value == other.value)).set_context(self.context)
            if operand == "!=":
                return Number(int(self.value != other.value)).set_context(self.context)
            if operand == "<":
                return Number(int(self.value < other.value)).set_context(self.context)
            if operand == ">":
                return Number(int(self.value > other.value)).set_context(self.context)
            if operand == "<=":
                return Number(int(self.value <= other.value)).set_context(self.context)
            if operand == ">=":
                return Number(int(self.value >= other.value)).set_context(self.context)
        elif isinstance(other, String):
            if operand == "==":
                return Number(int(str(self.value) == other.value)).set_context(self.context)
            if operand == "!=":
                return Number(int(str(self.value) != other.value)).set_context(self.context)
            try:
                if operand == "<":
                    return Number(int(self.value < eval(other.value))).set_context(self.context)
                if operand == ">":
                    return Number(int(self.value > eval(other.value))).set_context(self.context)
                if operand == "<=":
                    return Number(int(self.value <= eval(other.value))).set_context(self.context)
                if operand == ">=":
                    return Number(int(self.value >= eval(other.value))).set_context(self.context)
            except Exception as e:
                None
        if operand == "==":
            return Number(0).set_context(self.context)
        if operand == "!=":
            return Number(1).set_context(self.context)
        return None

    def logic_operate(self, other, operand):
        if isinstance(other, Number):
            if operand == "and":
                return Number(1 if (self.value and other.value) else 0).set_context(self.context)
            if operand == "or":
                return Number(1 if (self.value or other.value) else 0).set_context(self.context)
        elif isinstance(other, String):
            try:
                if operand == "and":
                    return Number(1 if (self.value and eval(other.value)) else 0).set_context(self.context)
                if operand == "or":
                    return Number(1 if (self.value or eval(other.value)) else 0).set_context(self.context)
            except Exception as e:
                if operand == "and":
                    return Number(1 if (self.value and other.value) else 0).set_context(self.context)
                if operand == "or":
                    return Number(1 if (self.value or other.value) else 0).set_context(self.context)
        elif isinstance(other, List):
            if operand == "and":
                return Number(1 if (self.value and len(other.elements)) else 0).set_context(self.context)
            if operand == "or":
                return Number(1 if (self.value or len(other.elements)) else 0).set_context(self.context)
        elif isinstance(other, Matrix):
            if operand == "and":
                return Number(1 if (self.value and len(other.rows)) else 0).set_context(self.context)
            if operand == "or":
                return Number(1 if (self.value or len(other.rows)) else 0).set_context(self.context)
        return None    
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
        return Number(int(self.value == 0)).set_context(self.context)

    def operate(self, other, operand):
        if isinstance(other, Number):
            if operand in "+-*^":
                try:
                    if operand == "+":
                        return Number(eval(self.value) + other.value).set_context(self.context)
                    if operand == "-":
                        return Number(eval(self.value) - other.value).set_context(self.context)
                    if operand == "*":
                        return Number(eval(self.value) * other.value).set_context(self.context)
                    if operand == "^":
                        return Number(eval(self.value) ** other.value).set_context(self.context)
                except Exception as e:
                    if operand == "+":
                        return String(self.value + str(other.value)).set_context(self.context)
                    if operand == "*":
                        return String(self.value * other.value).set_context(self.context)
            else:
                try:
                    dividend = eval(self.value)
                except Exception as e:
                    return None
                if other.value == 0:
                    return None
                if operand == "/":
                    return Number(dividend / other.value).set_context(self.context)
                if operand == "%":
                    return Number(dividend % other.value).set_context(self.context)
        elif isinstance(other, String):
            if operand in "+-^":
                try:
                    if operand == "+":
                        return Number(eval(self.value) + eval(other.value)).set_context(self.context)
                    if operand == "-":
                        return Number(eval(self.value) - eval(other.value)).set_context(self.context)
                    if operand == "^":
                        return Number(eval(self.value) ** eval(other.value)).set_context(self.context)
                except Exception as e:
                    if operand == "+":
                        return String(self.value + other.value).set_context(self.context)
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
                    return Number(n1 * n2).set_context(self.context)
                elif (op1_is_number):
                    return String(n1 * other.value).set_context(self.context)
                elif (op2_is_number):
                    return String(self.value * n2).set_context(self.context)
            else:
                try:
                    dividend = eval(self.value)
                    divisor = eval(other.value)
                except Exception as e:
                    return None
                if divisor == 0:
                    return None
                if operand == "/":
                    return Number(dividend / divisor).set_context(self.context)
                if operand == "%":
                    return Number(dividend % divisor).set_context(self.context)
        return None

    def compare(self, other, operand):
        if isinstance(other, Number):
            if operand == "==":
                return Number(int(self.value == str(other.value))).set_context(self.context)
            if operand == "!=":
                return Number(int(self.value != str(other.value))).set_context(self.context)
            try:
                number = eval(self.value)
            except Exception as e:
                None
            if operand == "<":
                return Number(int(number < other.value)).set_context(self.context)
            if operand == ">":
                return Number(int(number > other.value)).set_context(self.context)
            if operand == "<=":
                return Number(int(number <= other.value)).set_context(self.context)
            if operand == ">=":
                return Number(int(number >= other.value)).set_context(self.context)
        elif isinstance(other, String):
            if operand == "==":
                return Number(int(self.value == other.value)).set_context(self.context)
            if operand == "!=":
                return Number(int(self.value != other.value)).set_context(self.context)
            try:
                n1 = eval(self.value)
                n2 = eval(other.value)
            except Exception as e:
                None
            if operand == "<":
                return Number(int(n1 < n2)).set_context(self.context)
            if operand == ">":
                return Number(int(n1 > n2)).set_context(self.context)
            if operand == "<=":
                return Number(int(n1 <= n2)).set_context(self.context)
            if operand == ">=":
                return Number(int(n1 >= n2)).set_context(self.context)
        if operand == "==":
            return Number(0).set_context(self.context)
        if operand == "!=":
            return Number(1).set_context(self.context)
        return None

    def logic_operate(self, other, operand):
        is_number = True
        try:
            number = eval(self.value)
        except Exception as e:
            is_number = False
        if is_number:
            if isinstance(other, Number):
                if operand == "and":
                    return Number(1 if (number and other.value) else 0).set_context(self.context)
                if operand == "or":
                    return Number(1 if (number or other.value) else 0).set_context(self.context)
            elif isinstance(other, String):
                try:
                    if operand == "and":
                        return Number(1 if (number and eval(other.value)) else 0).set_context(self.context)
                    if operand == "or":
                        return Number(1 if (number or eval(other.value)) else 0).set_context(self.context)
                except Exception as e:
                    if operand == "and":
                        return Number(1 if (number and other.value) else 0).set_context(self.context)
                    if operand == "or":
                        return Number(1 if (number or other.value) else 0).set_context(self.context)
            elif isinstance(other, List):
                if operand == "and":
                    return Number(1 if (number and len(other.elements)) else 0).set_context(self.context)
                if operand == "or":
                    return Number(1 if (number or len(other.elements)) else 0).set_context(self.context)
            elif isinstance(other, Matrix):
                if operand == "and":
                    return Number(1 if (number and len(other.rows)) else 0).set_context(self.context)
                if operand == "or":
                    return Number(1 if (number or len(other.rows)) else 0).set_context(self.context)

        if isinstance(other, Number):
            if operand == "and":
                return Number(1 if (self.value and other.value) else 0).set_context(self.context)
            if operand == "or":
                return Number(1 if (self.value or other.value) else 0).set_context(self.context)
        elif isinstance(other, String):
            try:
                if operand == "and":
                    return Number(1 if (self.value and eval(other.value)) else 0).set_context(self.context)
                if operand == "or":
                    return Number(1 if (self.value or eval(other.value)) else 0).set_context(self.context)
            except Exception as e:
                if operand == "and":
                    return Number(1 if (self.value and other.value) else 0).set_context(self.context)
                if operand == "or":
                    return Number(1 if (self.value or other.value) else 0).set_context(self.context)
        elif isinstance(other, List):
            if operand == "and":
                return Number(1 if (self.value and len(other.elements)) else 0).set_context(self.context)
            if operand == "or":
                return Number(1 if (self.value or len(other.elements)) else 0).set_context(self.context)
        elif isinstance(other, Matrix):
            if operand == "and":
                return Number(1 if (self.value and len(other.rows)) else 0).set_context(self.context)
            if operand == "or":
                return Number(1 if (self.value or len(other.rows)) else 0).set_context(self.context)
        return None
    
    
    
    
class List(Value):
    def __init__(self, elements):
        super().__init__()
        self.elements = elements

    def __repr__(self):
        return f'[{", ".join([str(x) for x in self.elements])}]'

    def copy(self):
        copy = List(self.elements)
        copy.set_context(self.context)
        copy.set_should_print(self.should_print)
        return copy

    def is_true(self):
        return len(self.elements) > 0

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

    def operate(self, other, operand):
        if isinstance(other, Number):
            new_list = self.copy()
            for i in range(len(new_list.elements)):
                if not isinstance(new_list.elements[i], Number):
                    return None
                if operand == "+":
                    new_list.elements[i].value += other.value
                elif operand == "-":
                    new_list.elements[i].value -= other.value
                elif operand == "*":
                    new_list.elements[i].value *= other.value
                elif operand == "/":
                    new_list.elements[i].value /= other.value
                elif operand == "%":
                    new_list.elements[i].value %= other.value
                elif operand == "^":
                    new_list.elements[i].value = new_list.elements[i].value**other.value
            return new_list
        if isinstance(other, List):
            if len(self.elements) != len(other.elements):
                return None
            new_list = self.copy()
            for i in range(len(other.elements)):
                if not isinstance(new_list.elements[i], Number):
                    return None
                if not isinstance(other.elements[i], Number):
                    return None
                if operand == "+":
                    new_list.elements[i].value += other.elements[i].value
                elif operand == "-":
                    new_list.elements[i].value -= other.elements[i].value
                elif operand == "*":
                    new_list.elements[i].value *= other.elements[i].value
                elif operand == "/":
                    new_list.elements[i].value /= other.elements[i].value
                elif operand == "%":
                    new_list.elements[i].value %= other.elements[i].value
                elif operand == "^":
                    new_list.elements[i].value = new_list.elements[i].value**other.elements[i].value
            return new_list
        return None

    def compare(self, other, operand):
        if isinstance(other, List):
            if operand == "==":
                return Number(1 if self.get_value(self) == self.get_value(other) else 0)
            if operand == "!=":
                return Number(1 if self.get_value(self) != self.get_value(other) else 0)
        if operand == "==":
            return Number(0).set_context(self.context)
        if operand == "!=":
            return Number(1).set_context(self.context)

    def get_value(self, variable):
        if isinstance(variable, Number) or isinstance(variable, String):
            return variable.value
        elif isinstance(variable, List):
            new_list = []
            for element in variable.elements:
                new_list.append(self.get_value(element))
            return new_list
        elif isinstance(variable, Matrix):
            new_list = []
            for element in variable.rows:
                new_list.append(self.get_value(element))
            return new_list
        elif type(variable) == list:
            new_list = []
            for element in variable:
                new_list.append(self.get_value(element))
            return new_list
    
    
    
class Matrix(Value):
    def __init__(self, rows):
        super().__init__()
        self.rows = rows

    def __repr__(self):
        rep = ", ".join(
            "{" + ", ".join([str(x) for x in row]) + "}" for row in self.rows)
        return "{" + rep + "}"

    def copy(self):
        copy = Matrix(self.rows)
        copy.set_context(self.context)
        copy.set_should_print(self.should_print)
        return copy

    def is_true(self):
        return len(self.rows) > 0

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

    def operate(self, other, operand):
        if isinstance(other, Number) or isinstance(other, Matrix):
            self_value = self.get_value(self)
            if isinstance(other, Number):
                other_value = other.value
            else:
                other_value = self.get_value(other)
            if operand == "+":
                result = self.create_matrix(np.array(self_value)+np.array(other_value))
            elif operand == "-":
                result = self.create_matrix(np.array(self_value)-np.array(other_value))
            elif operand == "*":
                result = self.create_matrix(np.array(self_value)*np.array(other_value))
            elif operand == "/":
                result = self.create_matrix(np.array(self_value)/np.array(other_value))
            elif operand == "%":
                result = self.create_matrix(np.array(self_value)%np.array(other_value))
            elif operand == "^":
                result = self.create_matrix(np.array(self_value)**np.array(other_value))
            return result              
        return None

    def create_matrix(self, mat):
        matrix = self.copy()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                matrix.rows[i][j].value = mat[i][j]
        return matrix

    def compare(self, other, operand):
        if isinstance(other, Matrix):
            if operand == "==":
                return Number(1 if self.get_value(self) == self.get_value(other) else 0)
            if operand == "!=":
                return Number(1 if self.get_value(self) != self.get_value(other) else 0)
        if operand == "==":
            return Number(0).set_context(self.context)
        if operand == "!=":
            return Number(1).set_context(self.context)            
            
    def get_value(self, variable):
        if isinstance(variable, Number) or isinstance(variable, String):
            return variable.value
        elif isinstance(variable, List):
            new_list = []
            for element in variable.elements:
                new_list.append(self.get_value(element))
            return new_list
        elif isinstance(variable, Matrix):
            new_list = []
            for element in variable.rows:
                new_list.append(self.get_value(element))
            return new_list
        elif type(variable) == list:
            new_list = []
            for element in variable:
                new_list.append(self.get_value(element))
            return new_list  
        
class Dataset(Value):
    def __init__(self, data, labels):
        super().__init__()
        self.data = data
        self.labels = labels

    def __repr__(self):
        rep = f"dataset(data: {len(self.data.rows)}x{len(self.data.rows[0])}, labels: {len(set(self.get_value(self.labels)))})"
        return rep

    def copy(self):
        copy = Dataset(self.data, self.labels)
        copy.set_context(self.context)
        copy.set_should_print(self.should_print)
        return copy

    def get_value(self, variable):
        if isinstance(variable, Number) or isinstance(variable, String):
            return variable.value
        elif isinstance(variable, List):
            new_list = []
            for element in variable.elements:
                new_list.append(self.get_value(element))
            return new_list
        elif isinstance(variable, Matrix):
            new_list = []
            for element in variable.rows:
                new_list.append(self.get_value(element))
            return new_list
        elif type(variable) == list:
            new_list = []
            for element in variable:
                new_list.append(self.get_value(element))
            return new_list

class Optimizer(Value):
    def __init__(self, type_, learning_rate):
        super().__init__()
        self.type = type_
        self.learning_rate = learning_rate

    def __repr__(self):
        rep = f"{self.type.value}(learning rate: {self.learning_rate.value})"
        return rep

    def copy(self):
        copy = Optimizer(self.type, self.learning_rate)
        copy.set_context(self.context)
        copy.set_should_print(self.should_print)
        return copy

class InputLayer(Value):
    def __init__(self, input_neurons, hidden_neurons, kernel_initializer, batch_normalization, dropout_percentage, activation_function):
        super().__init__()
        self.input_neurons = input_neurons
        self.hidden_neurons = hidden_neurons
        self.kernel_initializer = kernel_initializer
        self.batch_normalization = batch_normalization
        self.dropout_percentage = dropout_percentage
        self.activation_function = activation_function

    def __repr__(self):
        rep = f"Input Layer ({self.input_neurons.value}, {self.hidden_neurons.value})"
        return rep

    def copy(self):
        copy = InputLayer(self.input_neurons, self.hidden_neurons, self.kernel_initializer, self.batch_normalization, 
                          self.dropout_percentage, self.activation_function)
        copy.set_context(self.context)
        copy.set_should_print(self.should_print)
        return copy

    def added_to(self, other):
        if isinstance(other, HiddenLayer):
            return Network(self, [other], None)
        elif isinstance(other, OutputLayer):
            return Network(self, [], other)
        elif isinstance(other, Network):
            if other.input_layer:
                return None
            other.input_layer = self
            return other
        return None

class HiddenLayer(Value):
    def __init__(self, neurons, kernel_initializer, batch_normalization, dropout_percentage, activation_function):
        super().__init__()
        self.neurons = neurons
        self.kernel_initializer = kernel_initializer
        self.batch_normalization = batch_normalization
        self.dropout_percentage = dropout_percentage
        self.activation_function = activation_function

    def __repr__(self):
        rep = f"Hidden Layer ({self.neurons.value})"
        return rep

    def copy(self):
        copy = HiddenLayer(self.neurons, self.kernel_initializer, self.batch_normalization, self.dropout_percentage, 
                           self.activation_function)
        copy.set_context(self.context)
        copy.set_should_print(self.should_print)
        return copy

    def added_to(self, other):
        if isinstance(other, InputLayer):
            return Network(other, [self], None)
        elif isinstance(other, HiddenLayer):
            return Network(None, [self, other], None)
        elif isinstance(other, OutputLayer):
            return Network(None, [self], other)
        elif isinstance(other, Network):
            other.hidden_layers.insert(0, self)
            return other
        return None

class OutputLayer(Value):
    def __init__(self, neurons, kernel_initializer, activation_function):
        super().__init__()
        self.neurons = neurons
        self.kernel_initializer = kernel_initializer
        self.activation_function = activation_function

    def __repr__(self):
        rep = f"Output Layer ({self.neurons.value})"
        return rep

    def copy(self):
        copy = OutputLayer(self.neurons, self.kernel_initializer, self.activation_function)
        copy.set_context(self.context)
        copy.set_should_print(self.should_print)
        return copy

    def added_to(self, other):
        if isinstance(other, InputLayer):
            return Network(other, [], self)
        elif isinstance(other, HiddenLayer):
            return Network(None, [other], self)
        elif isinstance(other, Network):
            if other.output_layer:
                return None
            other.output_layer = self
            return other, None
        return None

class Network(Value):
    def __init__(self, input_layer, hidden_layers, output_layer, compiled=False,  model_without_output_layer=None, model=None, compile_parameters=None, labels=None, trained=False, training_data=None, type_=None, batch_size=None, epochs=None):
        super().__init__()
        self.input_layer = input_layer
        self.hidden_layers = hidden_layers
        self.output_layer = output_layer
        self.compiled = compiled
        self.model_without_output_layer = model_without_output_layer
        self.model = model
        self.compile_parameters = compile_parameters 
        self.labels = labels
        self.trained = trained
        self.training_data = training_data
        self.type = type_
        self.batch_size = batch_size
        self.epochs = epochs

    def __repr__(self):
        if self.input_layer:
            rep = f"Network ({self.input_layer.input_neurons}, {self.input_layer.hidden_neurons}"
        else:
            rep = f"Network (null"
        for layer in self.hidden_layers:
            rep += f", {layer.neurons}"
        if self.output_layer:
            rep += f", {self.output_layer.neurons})"
        else:
            rep += f", null)"
        return rep

    def copy(self):
        copy = Network(self.input_layer, self.hidden_layers, self.output_layer, self.compiled,
                       self.model_without_output_layer, self.model, self.compile_parameters,
                       self.labels, self.trained, self.training_data, self.type, self.batch_size,
                       self.epochs)
        copy.set_context(self.context)
        copy.set_should_print(self.should_print)
        return copy

    def added_to(self, other):
        if isinstance(other, InputLayer):
            if self.input_layer:
                return None
            self.input_layer = other
            return self
        elif isinstance(other, HiddenLayer):
            self.hidden_layers.append(other)
            return self
        elif isinstance(other, OutputLayer):
            if self.output_layer:
                return None
            self.output_layer = other
            return self
        return None

class BaseFunction(Value):
    def __init__(self, name="<anonymus>"):
        super().__init__()
        self.name = name

    def generate_new_context(self):
        new_context = Context(self.name, self.context)
        new_context.symbol_table = SymbolTable(new_context.parent.symbol_table)
        return new_context

    def check_args(self, arg_names, args):
        res = RTResult()
        
        return res.success(None)

    def populate_args(self, arg_names, args, exec_ctx):
        for i in range(len(args)):
            arg_value = args[i]
            arg_value.set_context(exec_ctx)
            exec_ctx.symbol_table.set(arg_names[i], arg_value)

    def check_and_populate_args(self, arg_names, args, exec_ctx):
        res = RTResult()
        res.register(self.check_args(arg_names, args))
        if res.should_return():
            return res
        self.populate_args(arg_names, args, exec_ctx)
        return res.success(None)
       
class Function(BaseFunction):
    def __init__(self, name, body_node, arg_names, should_auto_return):
        super().__init__(name)
        self.body_node = body_node
        self.arg_names = arg_names
        self.should_auto_return = should_auto_return

    def __repr__(self):
        return f"<function {self.name}>"

    def copy(self):
        copy = Function(self.name, self.body_node, self.arg_names, self.should_auto_return)
        copy.set_context(self.context)
        copy.set_should_print(self.should_print)
        return copy

    def execute(self, args):
        res = RTResult()
        exec_ctx = self.generate_new_context()
        res.register(self.check_and_populate_args(self.arg_names, args, exec_ctx))
        if res.should_return():
            return res
        
        interpreter = Interpreter()
        value = res.register(interpreter.visit(self.body_node, exec_ctx))
        if res.should_return() and res.func_return_value == None:
            return res

        return_value = (value if self.should_auto_return else None) or res.func_return_value
        if return_value != None:
            return res.success(return_value)
        return res.success(Number.null.set_should_print(False))
    

class BuiltInFunction(BaseFunction):
    def __init__(self, name):
        super().__init__(name)

    def __repr__(self):
        return f"<built-in function {self.name}>"

    def copy(self):
        copy = BuiltInFunction(self.name)
        copy.set_context(self.context)
        copy.set_should_print(self.should_print)
        return copy

    def execute(self, args):
        res = RTResult()
        method_name = f"execute_{self.name}"
        method = getattr(self, method_name, self.no_visit_method)
        exec_ctx = self.generate_new_context()
        res.register(self.check_and_populate_args(method.arg_names, args, exec_ctx))
        if res.should_return():
            return res
        return_value = res.register(method(exec_ctx))
        if res.should_return():
            return res
        return res.success(return_value)

    def no_visit_method(self, node, context):
        raise Exception(f"The execute_{self.name} method is not defined")

    def execute_print(self, exec_ctx):
        print(str(exec_ctx.symbol_table.get("value")))
        return RTResult().success(Number.null)
    execute_print.arg_names = ["value"]
    
    def execute_print_optimizers(self, exec_ctx):
        global OPTIMIZERS
        print("The available optimizers are:")
        for optimizer in OPTIMIZERS:
            print(f"* {optimizer}")
        return RTResult().success(Number.null)
    execute_print_optimizers.arg_names = []
    
    def execute_print_kernel_initializers(self, exec_ctx):
        global KERNEL_INITIALIZERS
        print("The available kernel initializers are:")
        for kernel_initializer in KERNEL_INITIALIZERS:
            print(f"* {kernel_initializer}")
        return RTResult().success(Number.null)
    execute_print_kernel_initializers.arg_names = []
    
    def execute_print_activation_functions(self, exec_ctx):
        global ACTIVATION_FUNCTIONS
        print("The available activation functions are:")
        for activation_function in ACTIVATION_FUNCTIONS:
            print(f"* {activation_function}")
        return RTResult().success(Number.null)
    execute_print_activation_functions.arg_names = []
    
    def execute_print_loss_functions(self, exec_ctx):
        global LOSS_FUNCTIONS
        print("The available loss functions are:")
        for loss_function in LOSS_FUNCTIONS:
            print(f"* {loss_function}")
        return RTResult().success(Number.null)
    execute_print_loss_functions.arg_names = []

    def execute_input(self, exec_ctx):
        message = exec_ctx.symbol_table.get("value")
        if not isinstance(message, String):
            return 
        text = input(message.value)
        try:
            result = eval(text)
            if type(result) == int or type(result) == float:
                return RTResult().success(Number(result))
            return RTResult().success(String(text))
        except Exception as e:
            return RTResult().success(String(text))
    execute_input.arg_names = ["value"]

    def execute_type(self, exec_ctx):
        value = exec_ctx.symbol_table.get("value")
        if isinstance(value, Number):
            if type(value.value) == int:
                return RTResult().success(String("int"))
            return RTResult().success(String("float"))
        elif isinstance(value, String):
            return RTResult().success(String("str"))
        elif isinstance(value, List):
            return RTResult().success(String("list"))
        elif isinstance(value, Matrix):
            return RTResult().success(String("matrix"))
        elif isinstance(value, Dataset):
            return RTResult().success(String("dataset"))
        elif isinstance(value, Optimizer):
            return RTResult().success(String("optimizer"))
        elif isinstance(value, InputLayer):
            return RTResult().success(String("inputLayer"))
        elif isinstance(value, HiddenLayer):
            return RTResult().success(String("hiddenLayer"))
        elif isinstance(value, OutputLayer):
            return RTResult().success(String("outputLayer"))
        elif isinstance(value, Network):
            return RTResult().success(String("network"))
        elif isinstance(value, Function):
            return RTResult().success(String("function"))
        elif isinstance(value, BuiltInFunction):
            return RTResult().success(String("built-in-function"))
        return RTResult().failure()
    execute_type.arg_names = ["value"]

    def execute_int(self, exec_ctx):
        value = exec_ctx.symbol_table.get("value")
        if not isinstance(value, String) and not isinstance(value, Number):
            return RTResult().failure()
        try:
            int_value = int(value.value)
            return RTResult().success(Number(int_value))
        except Exception as e:
            return RTResult().failure()
    execute_int.arg_names = ["value"]

    def execute_float(self, exec_ctx):
        value = exec_ctx.symbol_table.get("value")
        if not isinstance(value, String) and not isinstance(value, Number):
            return RTResult().failure()
        try:
            float_value = float(value.value)
            return RTResult().success(Number(float_value))
        except Exception as e:
            return RTResult().failure()
    execute_float.arg_names = ["value"]

    def execute_str(self, exec_ctx):
        value = exec_ctx.symbol_table.get("value")
        try:
            if isinstance(value, Number) or isinstance(value, String):
                return RTResult().success(String(str(value.value)))
            elif isinstance(value, List):
                return RTResult().success(String(str(value.elements)))
            elif isinstance(value, Matrix):
                return RTResult().success(String(str(value.rows).replace("[", "{").replace("]", "}")))
            return RTResult().failure()
        except Exception as e:
            return RTResult().failure()
    execute_str.arg_names = ["value"]

    def execute_list(self, exec_ctx):
        value = exec_ctx.symbol_table.get("value")
        if not isinstance(value, String) and not isinstance(value, Matrix):
            return RTResult().failure()
        if isinstance(value, String):
            return RTResult().success(List([String(char) for char in value.value]))
        return RTResult().success(List([List(row) for row in value.rows]))
    execute_list.arg_names = ["value"]

    def execute_append(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get("list")
        value = exec_ctx.symbol_table.get("value")
        if not isinstance(list_, List) and not isinstance(list_, Matrix) and not isinstance(list_, Network):
            return RTResult().failure()
        if isinstance(list_, List):
            list_.elements.append(value)
        elif isinstance(list_, Matrix):
            if not isinstance(value, List):
                return RTResult().failure()
            for element in value.elements:
                if not isinstance(element, Number):
                    return RTResult().failure()
            rows = len(list_.rows)
            if rows == 0:
                list_.rows.append(value.elements)
            else:
                if len(list_.rows[0]) != len(value.elements):
                    return RTResult().failure()
                list_.rows.append(value.elements)
        else:
            if not isinstance(value, HiddenLayer):
                return RTResult().failure()
            list_.hidden_layers.append(value)
        return RTResult().success(Number.null)
    execute_append.arg_names = ["list", "value"]

    def execute_insert(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get("list")
        index = exec_ctx.symbol_table.get("index")
        value = exec_ctx.symbol_table.get("value")
        if not isinstance(list_, List) and not isinstance(list_, Matrix) and not isinstance(list_, Network):
            return RTResult().failure()
        if not isinstance(index, Number):
            return RTResult().failure()
        if type(index.value) == float:
            return RTResult().failure()
        if isinstance(list_, List):
            list_.elements.insert(index.value, value)
        elif isinstance(list_, Matrix):
            if not isinstance(value, List):
                return RTResult().failure()
            for element in value.elements:
                if not isinstance(element, Number):
                    return RTResult().failure()
            rows = len(list_.rows)
            if rows == 0:
                list_.rows.append(value.elements)
            else:
                if len(list_.rows[0]) != len(value.elements):
                    return RTResult().failure()
                list_.rows.insert(index.value, value.elements)
        else:
            if not isinstance(value, HiddenLayer):
                return RTResult().failure()
            list_.hidden_layers.insert(index.value, value)
        return RTResult().success(Number.null)
    execute_insert.arg_names = ["list", "index", "value"]

    def execute_pop(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get("list")
        index = exec_ctx.symbol_table.get("index")
        if not isinstance(list_, List) and not isinstance(list_, Matrix) and not isinstance(list_, Network):
            return RTResult().failure()
        if not isinstance(index, Number):
            return RTResult().failure()
        if type(index.value) == float:
            return RTResult().failure()
        try:
            if isinstance(list_, List):
                element = list_.elements.pop(index.value)
            elif isinstance(list_, Matrix):
                element = List(list_.rows.pop(index.value))
            else:
                element = list_.hidden_layers.pop(index.value)
        except Exception as e:
            return RTResult().failure()
        return RTResult().success(element)
    execute_pop.arg_names = ["list", "index"]

    def execute_remove(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get("list")
        value = exec_ctx.symbol_table.get("value")
        if not isinstance(list_, List) and not isinstance(list_, Matrix):
            return RTResult().failure()
        value_to_look = self.get_value(value)
        if not value_to_look:
            return RTResult().failure()
        if isinstance(list_, List):
            found = False
            for i in range(len(list_.elements)):
                if self.get_value(list_.elements[i]) == value_to_look:
                    list_.elements.pop(i)
                    found = True
                    break
            if not found:
                return RTResult().failure()
        else:
            rows = len(list_.rows)
            if (rows == 0) or (not isinstance(value, List)) or (len(list_.rows[0]) != len(value.elements)):
                return RTResult().failure()
            for element in value.elements:
                if not isinstance(element, Number):
                    return RTResult().failure()
            found = False
            for i in range(rows):
                if self.get_value(list_.rows[i]) == value_to_look:
                    list_.rows.pop(i)
                    found = True
                    break
            if not found:
                return RTResult().failure()
        return RTResult().success(Number.null)
    execute_remove.arg_names = ["list", "value"]

    def execute_extend(self, exec_ctx):
        list1 = exec_ctx.symbol_table.get("list1")
        list2 = exec_ctx.symbol_table.get("list2")
        if not isinstance(list1, List):
            return RTResult().failure()
        if not isinstance(list2, List):
            return RTResult().failure()
        list1.elements.extend(list2.elements)
        return RTResult().success(Number.null)
    execute_extend.arg_names = ["list1", "list2"]

    def execute_len(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get("list")
        if not isinstance(list_, String) and not isinstance(list_, List) and not isinstance(list_, Matrix):
            return RTResult().failure()
        return RTResult().success(Number(len(self.get_value(list_))))
    execute_len.arg_names = ["list"]

    def execute_slice(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get("list")
        start = exec_ctx.symbol_table.get("start")
        end = exec_ctx.symbol_table.get("end")
        if not isinstance(list_, String) and not isinstance(list_, List) and not isinstance(list_, Matrix):
            return RTResult().failure()
        if not isinstance(start, Number):
            return RTResult().failure()
        if not isinstance(end, Number):
            return RTResult().failure()
        if type(start.value) == float:
            return RTResult().failure()
        if type(end.value) == float:
            return RTResult().failure()
        if isinstance(list_, String):
            return RTResult().success(String(list_.value[start.value: end.value+1]))
        elif isinstance(list_, List):
            return RTResult().success(List(list_.elements[start.value: end.value+1]))
        return RTResult().success(Matrix(list_.rows[start.value: end.value+1]))
    execute_slice.arg_names = ["list", "start", "end"]

    def execute_get(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get("list")
        indexes = exec_ctx.symbol_table.get("indexes")
        if not isinstance(list_, String) and not isinstance(list_, List) and not isinstance(list_, Matrix):
            return RTResult().failure()
        if not isinstance(indexes, Number) and not isinstance(indexes, List):
            return RTResult().failure()
        if isinstance(indexes, Number):
            if type(indexes.value) == float:
                return RTResult().failure()
        else:
            for index in indexes.elements:
                if not isinstance(index, Number):
                    return RTResult().failure()
                if type(index.value) == float:
                    return RTResult().failure()
        try:
            if isinstance(indexes, Number):
                if isinstance(list_, String):
                    return RTResult().success(String(list_.value[indexes.value]))
                elif isinstance(list_, List):
                    return RTResult().success(list_.elements[indexes.value])
                return RTResult().success(List(list_.rows[indexes.value]))

            resulting_value = None
            for index in self.get_value(indexes.elements):
                if resulting_value == None:
                    if isinstance(list_, String):
                        resulting_value = String(list_.value[index])
                    elif isinstance(list_, List):
                        resulting_value = list_.elements[index]
                    else:
                        resulting_value = List(list_.rows[index])
                else:
                    if isinstance(resulting_value, String):
                        resulting_value = String(resulting_value.value[index])
                    elif isinstance(resulting_value, List):
                        resulting_value = resulting_value.elements[index]
                    elif isinstance(resulting_value, Matrix):
                        resulting_value = List(resulting_value.rows[index])
                    else:
                        return RTResult().failure()
            return RTResult().success(resulting_value)
        except Exception as e:
            return RTResult().failure()
    execute_get.arg_names = ["list", "indexes"]

    def execute_update(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get("list")
        indexes = exec_ctx.symbol_table.get("indexes")
        value = exec_ctx.symbol_table.get("value")
        if not isinstance(list_, String) and not isinstance(list_, List) and not isinstance(list_, Matrix):
            return RTResult().failure()
        if not isinstance(indexes, Number) and not isinstance(indexes, List):
            return RTResult().failure()
        if isinstance(indexes, Number):
            if type(indexes.value) == float:
                return RTResult().failure()
        else:
            for index in indexes.elements:
                if not isinstance(index, Number):
                    return RTResult().failure()
                if type(index.value) == float:
                    return RTResult().failure()
        try:
            if isinstance(indexes, Number):
                if isinstance(list_, String):
                    if not isinstance(value, String):
                        return RTResult().failure()
                    list_str = list(list_.value)
                    list_str[indexes.value] = value.value
                    return RTResult().success(String("".join(list_str)))

                elif isinstance(list_, List):
                    if len(list_.elements) == 0:
                        return RTResult().failure()
                    new_list = list_.copy()
                    new_list.elements[indexes.value] = value
                    return RTResult().success(new_list)

                if len(list_.rows) == 0:
                    return RTResult().failure()
                if not isinstance(value, List):
                    return RTResult().failure()
                if len(list_.rows[0]) != len(value.elements):
                    return RTResult().failure()
                for element in value.elements:
                    if not isinstance(element, Number):
                        return RTResult().failure()
                new_mat = list_.copy()
                new_mat.rows[indexes.value] = value.elements
                return RTResult().success(new_mat)

            if len(indexes.elements) == 0:
                return RTResult().failure()

            if isinstance(list_, String):
                if len(indexes.elements) > 1:
                    return RTResult().failure()
                if not isinstance(value, String):
                    return RTResult().failure()
                list_str = list(list_.value)
                list_str[indexes.elements[0].value] = value.value
                return RTResult().success(String("".join(list_str)))
            
            elif isinstance(list_, List):
                if len(indexes.elements) == 1:
                    new_list = list_.copy()
                    new_list.elements[indexes.elements[0].value] = value
                    return RTResult().success(new_list)

                indexes_values = self.get_value(indexes.elements)
                intermediate_elements = []
                for i in range(len(indexes_values)):
                    if i == 0:
                        current_value = list_.elements[indexes_values[i]]
                        if type(current_value) == str:
                            current_value = String(current_value)
                        elif type(current_value) == list:
                            current_value = List(current_value)
                        intermediate_elements.append(current_value)

                    else:
                        if isinstance(intermediate_elements[-1], String):
                            current_value = intermediate_elements[-1].value[indexes_values[i]]
                        elif isinstance(intermediate_elements[-1], List):
                            current_value = intermediate_elements[-1].elements[indexes_values[i]]
                        elif isinstance(intermediate_elements[-1], Matrix):
                            current_value = intermediate_elements[-1].rows[indexes_values[i]]
                        else:
                            return RTResult().failure()

                        if type(current_value) == str:
                            current_value = String(current_value)
                        elif type(current_value) == list:
                            current_value = List(current_value)
                        intermediate_elements.append(current_value)
                updated_value = value
                current_index = -1
                for i in range(len(intermediate_elements)-2, -1, -1):
                    if isinstance(intermediate_elements[i], String):
                        if not isinstance(updated_value, String):
                            return RTResult().failure()
                        intermediate_elements[i] = String(intermediate_elements[i].value[:indexes_values[current_index]] + updated_value.value + intermediate_elements[i].value[indexes_values[current_index]+1:])
                    elif isinstance(intermediate_elements[i], List):
                        intermediate_elements[i].elements[indexes_values[current_index]] = updated_value
                    elif isinstance(intermediate_elements[i], Matrix):
                        if not isinstance(updated_value, List):
                            return RTResult().failure()
                        for element in updated_value.elements:
                            if not isinstance(element, Number):
                                return RTResult().failure()
                        intermediate_elements[i].rows[indexes_values[current_index]] = updated_value.elements
                    updated_value = intermediate_elements[i]
                    current_index -= 1
                
                list_.elements[indexes_values[current_index]] = updated_value
                return RTResult().success(list_)
            
            if len(list_.rows) == 0 or len(indexes.elements) > 2:
                return RTResult().failure()
            if len(indexes.elements) == 1:
                if not isinstance(value, List):
                    return RTResult().failure()
                if len(list_.rows[0]) != len(value.elements):
                    return RTResult().failure()
                for element in value.elements:
                    if not isinstance(element, Number):
                        return RTResult().failure()
                new_mat = list_.copy()
                new_mat.rows[indexes.elements[0].value] = value.elements
                return RTResult().success(new_mat)
            if not isinstance(value, Number):
                return RTResult().failure()
            new_mat = list_.copy()
            new_mat.rows[indexes.elements[0].value][indexes.elements[1].value] = value
            return RTResult().success(new_mat)
        except Exception as e:
            return RTResult().failure()
    execute_update.arg_names = ["list", "indexes", "value"]

    def execute_get_data(self, exec_ctx):
        dataset = exec_ctx.symbol_table.get("dataset")
        if not isinstance(dataset, Dataset):
            return RTResult().failure()
        return RTResult().success(dataset.data)
    execute_get_data.arg_names = ["dataset"]

    def execute_get_labels(self, exec_ctx):
        dataset = exec_ctx.symbol_table.get("dataset")
        if not isinstance(dataset, Dataset):
            return RTResult().failure()
        return RTResult().success(dataset.labels)
    execute_get_labels.arg_names = ["dataset"]

    def execute_save(self, exec_ctx):
        global PATH
        value = exec_ctx.symbol_table.get("value")
        name = exec_ctx.symbol_table.get("name")
        if not isinstance(name, String):
            return RTResult().failure()
        try:
            if isinstance(value, List):
                value_to_save = []
                for element in value.elements:
                    if isinstance(element, InputLayer) or isinstance(element, HiddenLayer) or isinstance(element, OutputLayer) or isinstance(element, Optimizer) or isinstance(element, Network):
                        value_to_save.append(self.decompose_variable(element))
                    else:
                        value_to_save.append(element)
                value.elements = value_to_save
                value_to_save = value
            elif isinstance(value, InputLayer) or isinstance(value, HiddenLayer) or isinstance(value, OutputLayer) or isinstance(value, Optimizer) or isinstance(value, Network):
                value_to_save = self.decompose_variable(value)
            else:
                value_to_save = value

            file_name = f"{PATH or ''}{name.value}" if name.value.endswith(".sav") else f"{PATH or ''}{name.value}.sav"

            with open(file_name, "wb") as f:
                pickle.dump(value_to_save, f)

            return RTResult().success(Number.null)
        except Exception as e:
            return RTResult().failure()

    execute_save.arg_names = ["value", "name"]

    def execute_load(self, exec_ctx):
        global PATH
        name = exec_ctx.symbol_table.get("name")
        if not isinstance(name, String):
            return RTResult().failure()
        try:
            file_name = f"{PATH or ''}{name.value}" if name.value.endswith(".sav") else f"{PATH or ''}{name.value}.sav"

            with open(file_name, "rb") as f:
                loaded_variable = pickle.load(f)

            if not isinstance(loaded_variable, List):
                return RTResult().success(self.compose_variable(loaded_variable))
            return RTResult().success(self.compose_list_variable(loaded_variable))
        except Exception as e:
            return RTResult().failure()

    execute_load.arg_names = ["name"]

    def execute_save_dataset(self, exec_ctx):
        global PATH
        dataset = exec_ctx.symbol_table.get("dataset")
        name = exec_ctx.symbol_table.get("name")
        if not isinstance(dataset, Dataset):
            return RTResult().failure()
        if not isinstance(name, String):
            return RTResult().failure()
        data = dataset.data.rows
        labels = dataset.labels.elements
        try:
            if ".csv" == name.value[-4:]:
                if PATH:
                    file = open(f"{PATH}{name.value}", "w")
                else:
                    file = open(name.value, "w")
            else:
                if PATH:
                    file = open(f"{PATH}{name.value}.csv", "w")
                else:
                    file = open(f"{name.value}.csv", "w")
            for i in range(len(data)):
                label = self.get_value(labels[i])
                label = f'"{label}"' if type(label) == str else f"{label}"
                row = ','.join(list(map(str, self.get_value(data[i]))))
                line = f"{row},{label}\n"
                file.write(line)
            file.close()
            return RTResult().success(Number.null)
        except Exception as e:
            return RTResult().failure()
    execute_save_dataset.arg_names = ["dataset", "name"]

    def execute_load_dataset(self, exec_ctx):
        global PATH
        name = exec_ctx.symbol_table.get("name")
        if not isinstance(name, String):
            return RTResult().failure()
        if ".csv" == name.value[-4:]:
            if PATH:
                file_name = f"{PATH}{name.value}"
            else:
                file_name = name.value
        else:
            if PATH:
                file_name = f"{PATH}{name.value}.csv"
            else:
                file_name = f"{name.value}.csv"
        try:
            file = open(file_name, "r")
        except Exception as e:
            return RTResult().failure()
        data = []
        labels = []
        for line in file:
            line = line.strip()
            if line:
                line = line.split(",")
                if len(line) < 2:
                    return RTResult().failure()
                row = line[:-1]
                try:
                    row = list(map(Number, list(map(eval, row))))
                except Exception as e:
                    RTResult().failure()
                data.append(row)
                label = line[-1]
                if '"' in label:
                    labels.append(String(eval(label)))
                else:
                    try:
                        labels.append(Number(eval(label)))
                    except Exception as e:
                        labels.append(String(label))
        file.close()
        if len(data) < 2:
            return RTResult().failure()
        return RTResult().success(Dataset(Matrix(data), List(labels)))
    execute_load_dataset.arg_names = ["name"]

    def execute_split(self, exec_ctx):
        dataset = exec_ctx.symbol_table.get("dataset")
        percentage = exec_ctx.symbol_table.get("percentage")
        type_ = exec_ctx.symbol_table.get("type")
        balanced = exec_ctx.symbol_table.get("balanced")
        if not isinstance(dataset, Dataset):
            return RTResult().failure()
        if not isinstance(percentage, Number):
            return RTResult().failure()
        if type(percentage.value) == int:
            if not(0 < percentage.value < 100):
                return RTResult().failure()
            final_percentage = percentage.value/100
        else:
            if not(0 < percentage.value < 1):
                return RTResult().failure()
            final_percentage = percentage.value
        if not isinstance(type_, String):
            return RTResult().failure()
        if type_.value != "clf" and type_.value != "reg":
            return RTResult().failure()
        if type_.value == "clf":
            if not isinstance(balanced, Number):
                return RTResult().failure()
            if balanced.value != 0 and balanced.value != 1:
                return RTResult().failure()
        
        X = dataset.data.rows
        y = np.array(self.get_value(dataset.labels.elements))
        
        train_indexes = []
        test_indexes = []
        if type_.value == "reg" or not(balanced.value):
            total_data_for_training = int(len(y)*final_percentage)
            if total_data_for_training == 0:
                total_data_for_training += 1
            elif total_data_for_training == len(y):
                total_data_for_training -= 1
            indexes = list(range(len(y)))
            np.random.shuffle(indexes)
            train_indexes = indexes[:total_data_for_training]
            test_indexes = indexes[total_data_for_training:]
        else:
            labels = list(set(y))
            for label in labels:
                label_indexes = []
                indexes_for_label = y == label
                for i in range(len(indexes_for_label)):
                    if indexes_for_label[i] == True:
                        label_indexes.append(i)
                if len(label_indexes) == 1:
                    train_indexes.append(label_indexes[0])
                else:
                    total_data_for_training = int(len(label_indexes)*final_percentage)
                    if total_data_for_training == 0:
                        total_data_for_training += 1
                    elif total_data_for_training == len(label_indexes):
                        total_data_for_training -= 1
                    np.random.shuffle(label_indexes)
                    train = label_indexes[:total_data_for_training]
                    test = label_indexes[total_data_for_training:]
                    train_indexes.extend(train)
                    test_indexes.extend(test)

        X_train = []
        y_train = []
        for index in train_indexes:
            X_train.append(X[index])
            y_train.append(dataset.labels.elements[index])
        X_train = Matrix(X_train)
        y_train = List(y_train)
        X_test = []
        y_test = []
        for index in test_indexes:
            X_test.append(X[index])
            y_test.append(dataset.labels.elements[index])
        X_test = Matrix(X_test)
        y_test = List(y_test)

        return RTResult().success(List([X_train, y_train, X_test, y_test]))
    execute_split.arg_names = ["dataset", "percentage", "type", "balanced"]

    def execute_compile(self, exec_ctx):
        network = exec_ctx.symbol_table.get("network")
        optimizer = exec_ctx.symbol_table.get("optimizer")
        loss_function = exec_ctx.symbol_table.get("loss_function")
        type_ = exec_ctx.symbol_table.get("type")
        if not isinstance(network, Network):
            return RTResult().failure()
        if network.compiled:
            return RTResult().success(network)
        if not(network.input_layer):
            return RTResult().failure()
        if not(network.output_layer):
            return RTResult().failure()
        if not isinstance(optimizer, Optimizer):
            return RTResult().failure()
        if not isinstance(loss_function, String):
            return RTResult().failure()
        if loss_function.value not in LOSS_FUNCTIONS:
            return RTResult().failure()
        if not isinstance(type_, String):
            return RTResult().failure()
        if type_.value != "clf" and type_.value != "reg":
            return RTResult().failure()

        input_layer = network.input_layer
        hidden_layers = network.hidden_layers
        output_layer = network.output_layer
        model = Sequential()
        model.add(Dense(units=input_layer.hidden_neurons.value, input_dim=input_layer.input_neurons.value, kernel_initializer=input_layer.kernel_initializer.value))
        if input_layer.batch_normalization.value:
            model.add(BatchNormalization())
        model.add(Dropout(input_layer.dropout_percentage.value))
        model.add(Activation(input_layer.activation_function.value))

        for hidden_layer in hidden_layers:
            model.add(Dense(units=hidden_layer.neurons.value, kernel_initializer=hidden_layer.kernel_initializer.value))
            if hidden_layer.batch_normalization.value:
                model.add(BatchNormalization())
            model.add(Dropout(hidden_layer.dropout_percentage.value))
            model.add(Activation(hidden_layer.activation_function.value))
        
        network.model_without_output_layer = clone_model(model)
        model.add(Dense(units=output_layer.neurons.value, kernel_initializer=output_layer.kernel_initializer.value, activation=output_layer.activation_function.value))

        if optimizer.type.value == "SGD":
            opt = SGD(learning_rate=optimizer.learning_rate.value)
        elif optimizer.type.value == "RMSprop":
            opt = RMSprop(learning_rate=optimizer.learning_rate.value)
        elif optimizer.type.value == "Adagrad":
            opt = Adagrad(learning_rate=optimizer.learning_rate.value)
        elif optimizer.type.value == "Adadelta":
            opt = Adadelta(learning_rate=optimizer.learning_rate.value)
        elif optimizer.type.value == "Adam":
            opt = Adam(learning_rate=optimizer.learning_rate.value)
        elif optimizer.type.value == "Adamax":
            opt = Adamax(learning_rate=optimizer.learning_rate.value)
        elif optimizer.type.value == "Nadam":
            opt = Nadam(learning_rate=optimizer.learning_rate.value)

        model.compile(loss=loss_function.value, optimizer=opt, metrics=['accuracy' if type_.value == "clf" else 'mae'])
        network.compiled = True
        network.model = model
        network.compile_parameters = [deepcopy(opt), loss_function.value]
        network.type = type_
        return RTResult().success(network)
    execute_compile.arg_names = ["network", "optimizer", "loss_function", "type"]

    def execute_train(self, exec_ctx):
        network = exec_ctx.symbol_table.get("network")
        data = exec_ctx.symbol_table.get("data")
        labels = exec_ctx.symbol_table.get("labels")
        batch_size = exec_ctx.symbol_table.get("batch_size")
        epochs = exec_ctx.symbol_table.get("epochs")
        verbose = exec_ctx.symbol_table.get("verbose")
        if not isinstance(network, Network):
            return RTResult().failure()
        if not network.compiled:
            return RTResult().failure()
        if not isinstance(data, Matrix):
            return RTResult().failure()
        if not isinstance(labels, List):
            return RTResult().failure()
        final_labels = []
        for element in labels.elements:
            if not isinstance(element, String) and not isinstance(element, Number):
                return RTResult().failure()
            if isinstance(element, String):
                final_labels.append(String(element.value))
            else:
                final_labels.append(Number(element.value))
        labels = labels.copy()
        labels.elements = final_labels
        if not isinstance(batch_size, Number):
            return RTResult().failure()
        if type(batch_size.value) == float:
            return RTResult().failure()
        if batch_size.value <= 0:
            return RTResult().failure()
        if not isinstance(epochs, Number):
            return RTResult().failure()
        if type(epochs.value) == float:
            return RTResult().failure()
        if epochs.value <= 0:
            return RTResult().failure()
        if not isinstance(verbose, Number):
            return RTResult().failure()
        if verbose.value != 0 and verbose.value != 1:
            return RTResult().failure()
        
        if not network.trained:
            X_train = np.array(self.get_value(data.rows))
            y_train = self.get_value(labels.elements)
            if len(X_train[0]) != self.get_value(network.input_layer.input_neurons):
                return RTResult().failure()
            network_labels = None
            sc = MinMaxScaler()
            if network.type.value == "clf":
                network_labels = [None for label in set(y_train)] 
                enc = OneHotEncoder(categories="auto")
                original_y_train = deepcopy(y_train)
                y_train = np.array(y_train).reshape(len(y_train), 1)
                y_train = enc.fit_transform(y_train).toarray()
                network.training_data = [X_train, y_train, original_y_train, labels, enc]
                for i in range(len(y_train)):
                    if None in network_labels:
                        if None == network_labels[np.argmax(y_train[i])]:
                            network_labels[np.argmax(y_train[i])] = labels.elements[i]
                    else:
                        break
            else:
                network.training_data = [X_train, y_train, None, None, None]
                y_train = np.array(y_train)
            X_train = sc.fit_transform(X_train)
            network.training_data.append(sc)
            try:
                network.model.fit(X_train, y_train, batch_size=batch_size.value, epochs=epochs.value, verbose=verbose.value)
            except Exception as e:
                network.training_data = None
                return RTResult().failure()
            network.labels = network_labels
            network.trained = True

        else:  
            prev_X_train, prev_y_train, prev_original_y_train, prev_labels, prev_enc, prev_sc = network.training_data
            prev_model = clone_model(network.model)
            prev_model_without_output_layer = clone_model(network.model_without_output_layer)
            prev_output_layer_neurons = network.output_layer.neurons.value
            if network.labels:
                prev_network_labels = list(network.labels) 
            else:
                prev_network_labels = None
            
            new_X_train = np.array(self.get_value(data.rows))
            new_y_train = self.get_value(labels.elements)
            if len(prev_X_train[0]) != len(new_X_train[0]):
                return RTResult().failure()
            
            sc = MinMaxScaler()
            X_train = np.concatenate((prev_X_train, new_X_train), axis=0)
            
            opt, loss_function = network.compile_parameters
            model = clone_model(network.model_without_output_layer)
            model.add(Dense(units=network.output_layer.neurons.value, kernel_initializer=network.output_layer.kernel_initializer.value, activation=network.output_layer.activation_function.value))
            model.compile(loss=loss_function, optimizer=opt, metrics=['accuracy'])
            network.model = model
                
            if network.type.value == "clf":  
                current_labels = self.get_value(network.labels)
                incoming_labels = list(set(new_y_train))
                new_classes = False
                for label in incoming_labels:
                    if label not in current_labels:
                        new_classes = True
                        break
                
                y_train = deepcopy(prev_original_y_train)
                y_train.extend(new_y_train)
                original_y_train = deepcopy(y_train)
                new_labels = deepcopy(prev_labels.elements)
                new_labels.extend(labels.elements)
                new_labels = List(new_labels)
                       
                if new_classes:
                    total_classes = len(set(current_labels + incoming_labels))
                    network.output_layer.neurons.value = total_classes
                    opt, loss_function = network.compile_parameters
                    model = clone_model(network.model_without_output_layer)
                    model.add(Dense(units=total_classes, kernel_initializer=network.output_layer.kernel_initializer.value, activation=network.output_layer.activation_function.value))
                    model.compile(loss=loss_function, optimizer=opt, metrics=['accuracy'])
                    network.model = model
                    network_labels = [None for label in set(y_train)] 
                    enc = OneHotEncoder(categories="auto")
                    y_train = np.array(y_train).reshape(len(y_train), 1)
                    y_train = enc.fit_transform(y_train).toarray()
                    network.training_data = [X_train, y_train, original_y_train, new_labels, enc]
                    for i in range(len(y_train)):
                        if None in network_labels:
                            if None == network_labels[np.argmax(y_train[i])]:
                                network_labels[np.argmax(y_train[i])] = new_labels.elements[i]
                        else:
                            break
                    network.labels = network_labels
                else:          
                    new_y_train = np.array(new_y_train).reshape(len(labels.elements), 1)
                    new_y_train = prev_enc.transform(new_y_train).toarray()
                    y_train = np.concatenate((prev_y_train, new_y_train), axis=0)
                    network.training_data = [X_train, y_train, original_y_train, new_labels, prev_enc]
            
            else:
                y_train = deepcopy(prev_y_train)
                y_train.extend(new_y_train)
                network.training_data = [X_train, y_train, None, None, None]
                y_train = np.array(y_train)
            X_train = sc.fit_transform(X_train)
            network.training_data.append(sc)
            try:
                network.model.fit(X_train, y_train, batch_size=batch_size.value, epochs=epochs.value, verbose=verbose.value)
            except Exception as e:
                network.training_data = [prev_X_train, prev_y_train, prev_original_y_train, prev_labels, prev_enc, prev_sc]
                network.model = clone_model(prev_model)
                network.model_without_output_layer = clone_model(prev_model_without_output_layer)
                network.output_layer.neurons.value = prev_output_layer_neurons
                network.labels = prev_network_labels
                return RTResult().failure()
        network.batch_size = batch_size.value 
        network.epochs = epochs.value
        return RTResult().success(network)
    execute_train.arg_names = ["network", "data", "labels", "batch_size", "epochs", "verbose"]

    def execute_predict(self, exec_ctx):
        network = exec_ctx.symbol_table.get("network")
        data = exec_ctx.symbol_table.get("data")
        if not isinstance(network, Network):
            return RTResult().failure()
        if not network.compiled:
            return RTResult().failure()
        if not network.trained:
            return RTResult().failure()
        if not isinstance(data, List) and not isinstance(data, Matrix):
            return RTResult().failure()
        if isinstance(data, List):
            for element in data.elements:
                if not isinstance(element, Number):
                    return RTResult().failure()
        sc = network.training_data[-1]
        X_test = np.array(self.get_value(data))
        if isinstance(data, List):
            number_of_features = len(X_test)
            X_test = X_test.reshape(1, -1)
        else:
            number_of_features = len(X_test[0])
        if number_of_features != self.get_value(network.input_layer.input_neurons):
            return RTResult().failure()
        try:
            X_test = sc.transform(X_test)
        except Exception as e:
            return RTResult().failure()
        try:
            y_pred = network.model.predict(X_test)
        except Exception as e:
            return RTResult().failure()
        if network.type.value == "clf":
            y_pred_final = []
            for pred in y_pred:
                y_pred_final.append(network.labels[np.argmax(pred)])
        else:
            y_pred_final = []
            for i in y_pred.flatten():
                y_pred_final.append(Number(i))
        return RTResult().success(List(y_pred_final))
    execute_predict.arg_names = ["network", "data"]

    def execute_evaluate(self, exec_ctx):
        y_test = exec_ctx.symbol_table.get("y_test")
        y_pred = exec_ctx.symbol_table.get("y_pred")
        type_ = exec_ctx.symbol_table.get("type")
        if not isinstance(y_test, List):
            return RTResult().failure()
        for element in y_test.elements:
            if not isinstance(element, String) and not isinstance(element, Number):
                return RTResult().failure()
        if not isinstance(y_pred, List):
            return RTResult().failure()
        for element in y_pred.elements:
            if not isinstance(element, String) and not isinstance(element, Number):
                return RTResult().failure()
        if len(y_test.elements) != len(y_pred.elements):
            return RTResult().failure()
        if not isinstance(type_, String):
            return RTResult().failure()
        if type_.value != "clf" and type_.value != "reg":
            return RTResult().failure()

        y_test_val = self.get_value(y_test)
        y_pred_val = self.get_value(y_pred)
        if type_.value == "clf":
            try:
                cm = confusion_matrix(y_test_val, y_pred_val)
            except Exception as e:
                return RTResult().failure()
            accuracy, sensitivity, specificity = self.calculate_classification_metrics(cm)
            print(f"Accuracy: {accuracy}%")
            print(f"Sensitivity: {sensitivity}%")
            print(f"Specificity: {specificity}%")
            return RTResult().success(List([Number(accuracy), Number(sensitivity), Number(specificity)]))
        try:
            mse = round(mean_squared_error(y_test_val, y_pred_val), 3)
            mae = round(mean_absolute_error(y_test_val, y_pred_val), 3)
            r2 = round(r2_score(y_test_val, y_pred_val), 3)
        except Exception as e:
            return RTResult().failure()
        print(f"MSE: {mse}")
        print(f"MAE: {mae}")
        print(f"R2: {r2}")
        return RTResult().success(List([Number(mse), Number(mae), Number(r2)]))
    execute_evaluate.arg_names = ["y_test", "y_pred", "type"]

    def execute_run(self, exec_ctx):
        global PATH
        fn = exec_ctx.symbol_table.get("fn")
        if not isinstance(fn, String):
            return RTResult().failure()
        fn = fn.value
        if ".rdn" != fn[-4:]:
            return RTResult().failure()
        try:
            with open(fn, "r") as f:
                script = f.read()
        except Exception as e:
            return RTResult().failure()
        if "/" in fn:
            PATH = "/".join(fn.split("/")[:-1])+"/"
        _, error = run(fn, script)
        if error:
            PATH = None
            return RTResult().failure()
        PATH = None
        return RTResult().success(Number.null)
    execute_run.arg_names = ["fn"]

    def get_value(self, variable):
        if isinstance(variable, Number) or isinstance(variable, String):
            return variable.value
        elif isinstance(variable, List):
            new_list = []
            for element in variable.elements:
                new_list.append(self.get_value(element))
            return new_list
        elif isinstance(variable, Matrix):
            new_list = []
            for element in variable.rows:
                new_list.append(self.get_value(element))
            return new_list
        elif type(variable) == list:
            new_list = []
            for element in variable:
                new_list.append(self.get_value(element))
            return new_list

    def calculate_classification_metrics(self, matrix):
        if len(matrix[0]) != 2:
            tp = []
            tn = []
            fp = []
            fn = []
            total = np.sum(matrix)
            l = len(matrix)
            for i in range(l):
                tp.append(matrix[i, i])
                col = np.sum(matrix[:, i])
                row = np.sum(matrix[i])
                tn.append(total - col - row + tp[i])
                fp.append(col - tp[i])
                fn.append(row - tp[i])
            accuracy = 0
            sensitivity = 0
            specificity = 0
            for i in range(l):
                accuracy += (tp[i]+tn[i])/(tp[i]+fn[i]+fp[i]+tn[i])
                sensitivity += tp[i]/(tp[i]+fn[i])
                specificity += tn[i]/(fp[i]+tn[i])
            return round(accuracy/l*100, 3), round(sensitivity/l*100, 3), round(specificity/l*100, 3)
        accuracy = round(np.sum(np.diag(matrix))/np.sum(matrix)*100, 3)
        sensitivity = round(matrix[0, 0]/np.sum(matrix[0, :])*100, 3)
        specificity = round(matrix[1, 1]/np.sum(matrix[1])*100, 3)
        return accuracy, sensitivity, specificity

    def decompose_variable(self, value):
        information = {}
        if isinstance(value, InputLayer):
            information["variable_type"] = "InputLayer"
            information["input_neurons"] = value.input_neurons
            information["hidden_neurons"] = value.hidden_neurons
            information["kernel_initializer"] = value.kernel_initializer
            information["batch_normalization"] = value.batch_normalization
            information["dropout_percentage"] = value.dropout_percentage
            information["activation_function"] = value.activation_function
        elif isinstance(value, HiddenLayer):
            information["variable_type"] = "HiddenLayer"
            information["neurons"] = value.neurons
            information["kernel_initializer"] = value.kernel_initializer
            information["batch_normalization"] = value.batch_normalization
            information["dropout_percentage"] = value.dropout_percentage
            information["activation_function"] = value.activation_function
        elif isinstance(value, OutputLayer):
            information["variable_type"] = "OutputLayer"
            information["neurons"] = value.neurons
            information["kernel_initializer"] = value.kernel_initializer
            information["activation_function"] = value.activation_function
        elif isinstance(value, Optimizer):
            information["variable_type"] = "Optimizer"
            information["type"] = value.type
            information["learning_rate"] = value.learning_rate
        elif isinstance(value, Network):
            information["variable_type"] = "Network"
            information["compiled"] = value.compiled
            information["hidden_layers"] = []
            if value.input_layer:
                information["input_layer"] = {}
                information["input_layer"]["input_neurons"] = Number(self.get_value(value.input_layer.input_neurons))
                information["input_layer"]["hidden_neurons"] = Number(self.get_value(value.input_layer.hidden_neurons))
                information["input_layer"]["kernel_initializer"] = String(self.get_value(value.input_layer.kernel_initializer))
                information["input_layer"]["batch_normalization"] = Number(self.get_value(value.input_layer.batch_normalization))
                information["input_layer"]["dropout_percentage"] = Number(self.get_value(value.input_layer.dropout_percentage))
                information["input_layer"]["activation_function"] = String(self.get_value(value.input_layer.activation_function))
            for hidden_layer in value.hidden_layers:
                current_layer = {}
                current_layer["neurons"] = Number(self.get_value(hidden_layer.neurons))
                current_layer["kernel_initializer"] = String(self.get_value(hidden_layer.kernel_initializer))
                current_layer["batch_normalization"] = Number(self.get_value(hidden_layer.batch_normalization))
                current_layer["dropout_percentage"] = Number(self.get_value(hidden_layer.dropout_percentage))
                current_layer["activation_function"] = String(self.get_value(hidden_layer.activation_function))
                information["hidden_layers"].append(current_layer)
            if value.output_layer:
                information["output_layer"] = {}
                information["output_layer"]["neurons"] =  Number(self.get_value(value.output_layer.neurons))
                information["output_layer"]["kernel_initializer"] =  String(self.get_value(value.output_layer.kernel_initializer))
                information["output_layer"]["activation_function"] =  String(self.get_value(value.output_layer.activation_function))
            if value.compiled:
                information["loss_function"] = value.compile_parameters[1]
                opt = value.compile_parameters[0]
                information["optimizer_type"] = type(opt).__name__
                information["learning_rate"] = opt.lr.numpy()
                information["type"] = String(self.get_value(value.type))
                information["trained"] = value.trained
                if value.trained:
                    information["training_data"] = list(value.training_data)
                    information["labels"] = value.labels
                    information["batch_size"] = value.batch_size
                    information["epochs"] = value.epochs
                    if value.type.value == "clf":
                        labels = information["training_data"].pop(3)
                        labels.context = None
                        labels.pos_start = None
                        labels.pos_end = None
                        information["training_data"].insert(3, labels)
            
        return information
    
    def compose_variable(self, value):
        if type(value).__name__ != "dict":
            return value
        if value["variable_type"] == "InputLayer":
            return InputLayer(value["input_neurons"], value["hidden_neurons"], value["kernel_initializer"], value["batch_normalization"], value["dropout_percentage"], value["activation_function"])
        if value["variable_type"] == "HiddenLayer":   
            return HiddenLayer(value["neurons"], value["kernel_initializer"], value["batch_normalization"], value["dropout_percentage"], value["activation_function"])
        if value["variable_type"] == "OutputLayer": 
            return OutputLayer(value["neurons"], value["kernel_initializer"], value["activation_function"])
        if value["variable_type"] == "Optimizer": 
            return Optimizer(value["type"], value["learning_rate"])
        if value["variable_type"] == "Network": 
            input_layer = None
            if "input_layer" in value:
                input_layer = InputLayer(value["input_layer"]["input_neurons"], value["input_layer"]["hidden_neurons"], value["input_layer"]["kernel_initializer"], value["input_layer"]["batch_normalization"], value["input_layer"]["dropout_percentage"], value["input_layer"]["activation_function"])
            hidden_layers = []
            for hiddenLayer in value["hidden_layers"]:
                hidden_layers.append(HiddenLayer(hiddenLayer["neurons"], hiddenLayer["kernel_initializer"], hiddenLayer["batch_normalization"], hiddenLayer["dropout_percentage"], hiddenLayer["activation_function"]))
            output_layer = None
            if "output_layer" in value:
                output_layer = OutputLayer(value["output_layer"]["neurons"], value["output_layer"]["kernel_initializer"], value["output_layer"]["activation_function"])
            network = Network(input_layer, hidden_layers, output_layer)
            if value["compiled"]:
                model = Sequential()
                model.add(Dense(units=input_layer.hidden_neurons.value, input_dim=input_layer.input_neurons.value, kernel_initializer=input_layer.kernel_initializer.value))
                if input_layer.batch_normalization.value:
                    model.add(BatchNormalization())
                model.add(Dropout(input_layer.dropout_percentage.value))
                model.add(Activation(input_layer.activation_function.value))

                for hidden_layer in hidden_layers:
                    model.add(Dense(units=hidden_layer.neurons.value, kernel_initializer=hidden_layer.kernel_initializer.value))
                    if hidden_layer.batch_normalization.value:
                        model.add(BatchNormalization())
                    model.add(Dropout(hidden_layer.dropout_percentage.value))
                    model.add(Activation(hidden_layer.activation_function.value))
                
                network.model_without_output_layer = clone_model(model)
                model.add(Dense(units=output_layer.neurons.value, kernel_initializer=output_layer.kernel_initializer.value, activation=output_layer.activation_function.value))

                if value["optimizer_type"] == "SGD":
                    opt = SGD(learning_rate=value["learning_rate"])
                elif value["optimizer_type"] == "RMSprop":
                    opt = RMSprop(learning_rate=value["learning_rate"])
                elif value["optimizer_type"] == "Adagrad":
                    opt = Adagrad(learning_rate=value["learning_rate"])
                elif value["optimizer_type"] == "Adadelta":
                    opt = Adadelta(learning_rate=value["learning_rate"])
                elif value["optimizer_type"] == "Adam":
                    opt = Adam(learning_rate=value["learning_rate"])
                elif value["optimizer_type"] == "Adamax":
                    opt = Adamax(learning_rate=value["learning_rate"])
                elif value["optimizer_type"] == "Nadam":
                    opt = Nadam(learning_rate=value["learning_rate"])

                model.compile(loss=value["loss_function"], optimizer=opt, metrics=['accuracy' if value["type"] == "clf" else 'mae'])
                network.compiled = True
                network.model = model
                network.compile_parameters = [deepcopy(opt), value["loss_function"]]
                network.type = value["type"]                
                if value["trained"]:
                    network.trained = True
                    network.batch_size = value["batch_size"]
                    network.epochs = value["epochs"]
                    network.labels = value["labels"]
                    network.training_data = value["training_data"]
                    sc = value["training_data"][-1]
                    X_train = sc.transform(value["training_data"][0])
                    y_train = np.array(value["training_data"][1])
                    network.model.fit(X_train, y_train, batch_size=value["batch_size"], epochs=value["epochs"], verbose=0)
                    
            return network 

    def compose_list_variable(self, value):
        final_value = []
        for element in value.elements:
            if isinstance(element, List):
                final_value.append(self.compose_list_variable(element))
            else:
                final_value.append(self.compose_variable(element))
        value.elements = final_value
        return value     
    
    
    
    
BuiltInFunction.print = BuiltInFunction("print")
BuiltInFunction.print_optimizers = BuiltInFunction("print_optimizers")
BuiltInFunction.print_kernel_initializers = BuiltInFunction("print_kernel_initializers")
BuiltInFunction.print_activation_functions = BuiltInFunction("print_activation_functions")
BuiltInFunction.print_loss_functions = BuiltInFunction("print_loss_functions")
BuiltInFunction.input = BuiltInFunction("input")
BuiltInFunction.type = BuiltInFunction("type")
BuiltInFunction.int = BuiltInFunction("int")
BuiltInFunction.float = BuiltInFunction("float")
BuiltInFunction.str = BuiltInFunction("str")
BuiltInFunction.list = BuiltInFunction("list")
BuiltInFunction.append = BuiltInFunction("append")
BuiltInFunction.insert = BuiltInFunction("insert")
BuiltInFunction.pop = BuiltInFunction("pop")
BuiltInFunction.remove = BuiltInFunction("remove")
BuiltInFunction.extend = BuiltInFunction("extend")
BuiltInFunction.len = BuiltInFunction("len")
BuiltInFunction.slice = BuiltInFunction("slice")
BuiltInFunction.get = BuiltInFunction("get")
BuiltInFunction.update = BuiltInFunction("update")
BuiltInFunction.get_data = BuiltInFunction("get_data")
BuiltInFunction.get_labels = BuiltInFunction("get_labels")
BuiltInFunction.save = BuiltInFunction("save")
BuiltInFunction.load = BuiltInFunction("load")
BuiltInFunction.save_dataset = BuiltInFunction("save_dataset")
BuiltInFunction.load_dataset = BuiltInFunction("load_dataset")
BuiltInFunction.split = BuiltInFunction("split")
BuiltInFunction.compile = BuiltInFunction("compile")
BuiltInFunction.train = BuiltInFunction("train")
BuiltInFunction.predict = BuiltInFunction("predict")
BuiltInFunction.evaluate = BuiltInFunction("evaluate")
BuiltInFunction.run = BuiltInFunction("run")




class Interpreter:
    def visit(self, node, context):
        method_name = f"visit_{type(node).__name__}"
        method = getattr(self, method_name, self.no_visit_method)
        return method(node, context)

    def no_visit_method(self, node, context):
        raise Exception(f"No visit_{type(node).__name__} method define")
    
    def visit_NumberNode(self, node, context):
        return RTResult().success(Number(int(node.tok)).set_context(context))
    
    def visit_StringNode(self, node, context):
        return RTResult().success(String(node.tok).set_context(context))
    
    def visit_ListNode(self, node, context):
        res = RTResult()
        elements = []
        for element_node in node.element_nodes:
            elements.append(res.register(self.visit(element_node, context)))
            if res.should_return():
                return res
        return res.success(List(elements).set_context(context))
    def visit_BinOpNode(self, node, context):
        res = RTResult()
        left = res.register(self.visit(node.left_node, context))
        if res.should_return():
            return res
        right = res.register(self.visit(node.right_node, context))
        if res.should_return():
            return res
        if node.op_tok == '+':
            result = left.added_to(right)
        elif node.op_tok == '-':
            result = left.subbed_by(right)
        elif node.op_tok == '*':
            result = left.multed_by(right)
        elif node.op_tok == '/':
            result = left.dived_by(right)
        elif node.op_tok == '%':
            result = left.moded_by(right)
        elif node.op_tok == '^':
            result = left.powed_by(right)
        elif node.op_tok == '==':
            result = left.get_comparison_ee(right)
        elif node.op_tok == '!=':
            result = left.get_comparison_ne(right)
        elif node.op_tok == "<":
            result = left.get_comparison_lt(right)
        elif node.op_tok == ">":
            result = left.get_comparison_gt(right)
        elif node.op_tok == "<=":
            result = left.get_comparison_lte(right)
        elif node.op_tok == ">=":
            result = left.get_comparison_gte(right)
        elif node.op_tok== "and":
            result = left.anded_by(right)
        elif node.op_tok=="or":
            result = left.ored_by(right)

        
        return res.success(result)
    def visit_VarAccessNode(self, node, context):
        res = RTResult()
        var_name = node.var_name_tok
        value = context.symbol_table.get(var_name)
       
        value = value.copy().set_context(context)
        if var_name == "null":
            return res.success(value.set_should_print(False))
        return res.success(value)
    
    def visit_CallNode(self, node, context):
        res = RTResult()
        args = []
        value_to_call = res.register(self.visit(node.node_to_call, context))
        if res.should_return():
            return res
        value_to_call = value_to_call.copy()
        for arg_node in node.arg_nodes:
            args.append(res.register(self.visit(arg_node, context)))
            if res.should_return():
                return res
        return_value = res.register(value_to_call.execute(args))
        if res.should_return():
            return res
        return_value = return_value.copy().set_context(context)
        return res.success(return_value) 
    def visit_VarAssignNode(self, node, context):
        res = RTResult()
        var_name = node.var_name_tok
        value = res.register(self.visit(node.value_node, context))
        if res.should_return():
            return res
        context.symbol_table.set(var_name, value)
        return_value = value.copy().set_context(context).set_should_print(False)
        return res.success(return_value)
    def visit_UnaryOpNode(self, node, context):
        res = RTResult()
        number = res.register(self.visit(node.node, context))
        if res.should_return():
            return res

        if node.op_tok== '-':
            number= number.multed_by(Number(-1))
        elif node.op_tok==( "not"):
            number= number.notted()
        return res.success(number)
    def visit_IfNode(self, node, context):
        res = RTResult()

        for condition, expr in node.cases:
            condition_value = res.register(self.visit(condition, context))
            if res.should_return():
                return res
            if condition_value.is_true():
                expr_value = res.register(self.visit(expr, context))
                if res.should_return():
                    return res
                return res.success(Number.null)
        if node.else_case:
            expr = node.else_case
            else_value = res.register(self.visit(expr, context))
            if res.should_return():
                return res
            return res.success(Number.null)
        return res.success(Number.null)
    def visit_ForNode(self, node, context):
        res = RTResult()
        elements = []

        start_value = res.register(self.visit(node.start_value_node, context))
        if res.should_return():
            return res

        end_value = res.register(self.visit(node.end_value_node, context))
        if res.should_return():
            return res

        if node.step_value_node:
            step_value = res.register(
                self.visit(node.step_value_node, context))
            if res.should_return():
                return res
        else:
            step_value = Number(1)

        i = start_value.value
        if step_value.value >= 0:
            def condition(): return i <= end_value.value
        else:
            def condition(): return i >= end_value.value

        while condition():
            context.symbol_table.set(node.var_name_tok, Number(i))
            i += step_value.value
            value = res.register(self.visit(node.body_node, context))
            if res.should_return() and res.loop_should_continue == False and res.loop_should_break == False:
                return res
            if res.loop_should_continue:
                continue
            if res.loop_should_break:
                break
            elements.append(value)

        return res.success(Number.null)
    
    
global_symbol_table = SymbolTable()
global_symbol_table.set("null", Number.null)
global_symbol_table.set("true", Number.true)
global_symbol_table.set("false", Number.false)
global_symbol_table.set("print", BuiltInFunction.print)
global_symbol_table.set("print_optimizers", BuiltInFunction.print_optimizers)
global_symbol_table.set("print_kernel_initializers", BuiltInFunction.print_kernel_initializers)
global_symbol_table.set("print_activation_functions", BuiltInFunction.print_activation_functions)
global_symbol_table.set("print_loss_functions", BuiltInFunction.print_loss_functions)
global_symbol_table.set("input", BuiltInFunction.input)
global_symbol_table.set("type", BuiltInFunction.type)
global_symbol_table.set("int", BuiltInFunction.int)
global_symbol_table.set("float", BuiltInFunction.float)
global_symbol_table.set("str", BuiltInFunction.str)
global_symbol_table.set("list", BuiltInFunction.list)
global_symbol_table.set("append", BuiltInFunction.append)
global_symbol_table.set("insert", BuiltInFunction.insert)
global_symbol_table.set("pop", BuiltInFunction.pop)
global_symbol_table.set("remove", BuiltInFunction.remove)
global_symbol_table.set("extend", BuiltInFunction.extend)
global_symbol_table.set("len", BuiltInFunction.len)
global_symbol_table.set("slice", BuiltInFunction.slice)
global_symbol_table.set("get", BuiltInFunction.get)
global_symbol_table.set("update", BuiltInFunction.update)
global_symbol_table.set("get_data", BuiltInFunction.get_data)
global_symbol_table.set("get_labels", BuiltInFunction.get_labels)
global_symbol_table.set("save", BuiltInFunction.save)
global_symbol_table.set("load", BuiltInFunction.load)
global_symbol_table.set("save_dataset", BuiltInFunction.save_dataset)
global_symbol_table.set("load_dataset", BuiltInFunction.load_dataset)
global_symbol_table.set("split", BuiltInFunction.split)
global_symbol_table.set("compile", BuiltInFunction.compile)
global_symbol_table.set("train", BuiltInFunction.train)
global_symbol_table.set("predict", BuiltInFunction.predict)
global_symbol_table.set("evaluate", BuiltInFunction.evaluate)
global_symbol_table.set("run", BuiltInFunction.run)


input_stream=InputStream("""
for (i,0,9,2){
    print(i)
}
""")


lexer=RADENNLexer(input_stream)
token_stream=CommonTokenStream(lexer)
parser=RADENNParser(token_stream)

tree=parser.start()
custom_tree_root =build_custom_tree(tree)
ast=start(custom_tree_root)

context = Context("<program>")
context.symbol_table = global_symbol_table

interpreter=Interpreter()
res=interpreter.visit(ast,context)
# print(res.value)