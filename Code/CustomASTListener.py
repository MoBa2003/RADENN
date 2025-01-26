from Repository.ast import AST
from Repository.make_ast_subtree import make_ast_subtree
from gen.RADENNListener import RADENNListener
from gen.RADENNParser import RADENNParser

class CustomASTListener(RADENNListener):
    def __init__(self, rule_names):
        self.overridden_rules = []  # No overridden rules specific to RADENN
        self.binary_operator_list = ['term', 'expr', 'assign']
        self.rule_names = rule_names
        self.ast = AST()

    def exitEveryRule(self, ctx):
        rule_name = self.rule_names[ctx.getRuleIndex()]
        if rule_name not in self.overridden_rules:
            if rule_name in self.binary_operator_list and ctx.getChildCount() > 1:
                make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText())
            else:
                make_ast_subtree(self.ast, ctx, rule_name)

    def exitProgram(self, ctx:RADENNParser.ProgramContext):
        make_ast_subtree(self.ast, ctx, 'program')

    def exitStatements(self, ctx:RADENNParser.StatementsContext):
        make_ast_subtree(self.ast, ctx, 'statements')

    def exitStatement(self, ctx:RADENNParser.StatementContext):
        make_ast_subtree(self.ast, ctx, 'statement')

    def exitExpr(self, ctx:RADENNParser.ExprContext):
        make_ast_subtree(self.ast, ctx, 'expr')

    def exitCompExpr(self, ctx:RADENNParser.CompExprContext):
        make_ast_subtree(self.ast, ctx, 'compExpr')

    def exitArithExpr(self, ctx:RADENNParser.ArithExprContext):
        make_ast_subtree(self.ast, ctx, 'arithExpr')

    def exitTerm(self, ctx:RADENNParser.TermContext):
        make_ast_subtree(self.ast, ctx, 'term')

    def exitFactor(self, ctx:RADENNParser.FactorContext):
        make_ast_subtree(self.ast, ctx, 'factor')

    def exitPower(self, ctx:RADENNParser.PowerContext):
        make_ast_subtree(self.ast, ctx, 'power')

    def exitCall(self, ctx:RADENNParser.CallContext):
        make_ast_subtree(self.ast, ctx, 'call')

    def exitAtom(self, ctx:RADENNParser.AtomContext):
        make_ast_subtree(self.ast, ctx, 'atom')

    def exitListExpr(self, ctx:RADENNParser.ListExprContext):
        make_ast_subtree(self.ast, ctx, 'listExpr')

    def exitMatExpr(self, ctx:RADENNParser.MatExprContext):
        make_ast_subtree(self.ast, ctx, 'matExpr')

    def exitMatRow(self, ctx:RADENNParser.MatRowContext):
        make_ast_subtree(self.ast, ctx, 'matRow')

    def exitDatasetExpr(self, ctx:RADENNParser.DatasetExprContext):
        make_ast_subtree(self.ast, ctx, 'datasetExpr')

    def exitOptimizerExpr(self, ctx:RADENNParser.OptimizerExprContext):
        make_ast_subtree(self.ast, ctx, 'optimizerExpr')

    def exitInputLayerExpr(self, ctx:RADENNParser.InputLayerExprContext):
        make_ast_subtree(self.ast, ctx, 'inputLayerExpr')

    def exitHiddenLayerExpr(self, ctx:RADENNParser.HiddenLayerExprContext):
        make_ast_subtree(self.ast, ctx, 'hiddenLayerExpr')

    def exitOutputLayerExpr(self, ctx:RADENNParser.OutputLayerExprContext):
        make_ast_subtree(self.ast, ctx, 'outputLayerExpr')

    def exitNetworkExpr(self, ctx:RADENNParser.NetworkExprContext):
        make_ast_subtree(self.ast, ctx, 'networkExpr')

    def exitIfExpr(self, ctx:RADENNParser.IfExprContext):
        make_ast_subtree(self.ast, ctx, 'ifExpr')

    def exitElifExpr(self, ctx:RADENNParser.ElifExprContext):
        make_ast_subtree(self.ast, ctx, 'elifExpr')

    def exitElseExpr(self, ctx:RADENNParser.ElseExprContext):
        make_ast_subtree(self.ast, ctx, 'elseExpr')

    def exitBlock(self, ctx:RADENNParser.BlockContext):
        make_ast_subtree(self.ast, ctx, 'block')

    def exitForExpr(self, ctx:RADENNParser.ForExprContext):
        make_ast_subtree(self.ast, ctx, 'forExpr')

    def exitWhileExpr(self, ctx:RADENNParser.WhileExprContext):
        make_ast_subtree(self.ast, ctx, 'whileExpr')

    def exitDoWhileExpr(self, ctx:RADENNParser.DoWhileExprContext):
        make_ast_subtree(self.ast, ctx, 'doWhileExpr')

    def exitFuncDef(self, ctx:RADENNParser.FuncDefContext):
        make_ast_subtree(self.ast, ctx, 'funcDef')
