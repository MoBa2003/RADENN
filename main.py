import argparse
from antlr4 import *

from Code.CustomASTListener import CustomASTListener
from Repository.ast_to_networkx_graph import show_ast
from Repository.post_order_ast_traverser import PostOrderASTTraverser
from gen.RADENNLexer import RADENNLexer
from gen.RADENNParser import RADENNParser


def main(args):
    stream = FileStream(args.file, encoding='utf8')
    lexer = RADENNLexer(stream)
    token_stream = CommonTokenStream(lexer)
    parser = RADENNParser(token_stream)
    parse_tree = parser.start()
    listener = CustomASTListener(parser.ruleNames)
    walker = ParseTreeWalker()
    walker.walk(listener, parse_tree)
    normal_ast = listener.ast
    show_ast(normal_ast.root)
    post_order_ast_traverser = PostOrderASTTraverser()
    post_order_ast_traverser.node_attributes = ['label']
    traversal_dict = post_order_ast_traverser.traverse_ast(normal_ast.root)
    traversal = [item['label'] for item in traversal_dict]
    print(traversal)


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '-n', '--file',
        help='Input source', default=r'input.txt')
    args = argparser.parse_args()
    main(args)
