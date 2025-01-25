from graphviz import Digraph

def add_to_graphviz(dot, node, parent_id=None):
    node_id = id(node)

    label = node.val if node.is_rule else f"'{node.val}'"

    dot.node(str(node_id), label=label)

    if parent_id is not None:
        dot.edge(str(parent_id), str(node_id))

    for child in node.children:
        add_to_graphviz(dot, child, node_id)


def draw_tree(custom_tree_root):
    dot = Digraph()

    add_to_graphviz(dot, custom_tree_root)

    dot.render("tree_output", format="png", view=True)
