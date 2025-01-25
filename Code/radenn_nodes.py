class ListNode:
    def __init__(self, element_nodes):
        self.element_nodes = element_nodes

    def __repr__(self):
        return f"[{', '.join(map(str, self.element_nodes))}]"


class VarAssignNode:
    def __repr__(self):
        return f"{self.var_name_tok} = {self.value_node}"

    def __init__(self, var_name_tok, value_node):
        self.var_name_tok = var_name_tok
        self.value_node = value_node


    def __repr__(self):
        return f"{self.var_name_tok} = {self.value_node}"


class NumberNode:
    def __init__(self, tok, pos_start, pos_end):
        self.tok = tok
        self.pos_start = pos_start
        self.pos_end = pos_end

    def __repr__(self):
        return f"{self.tok}"
