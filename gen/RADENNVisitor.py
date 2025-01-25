# Generated from C:/Users/esikh/term5/compiler/RADENN/Grammar/RADENN.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .RADENNParser import RADENNParser
else:
    from RADENNParser import RADENNParser

# This class defines a complete generic visitor for a parse tree produced by RADENNParser.

class RADENNVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RADENNParser#start.
    def visitStart(self, ctx:RADENNParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#program.
    def visitProgram(self, ctx:RADENNParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#statements.
    def visitStatements(self, ctx:RADENNParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#statement.
    def visitStatement(self, ctx:RADENNParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#expr.
    def visitExpr(self, ctx:RADENNParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#compExpr.
    def visitCompExpr(self, ctx:RADENNParser.CompExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#arithExpr.
    def visitArithExpr(self, ctx:RADENNParser.ArithExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#term.
    def visitTerm(self, ctx:RADENNParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#factor.
    def visitFactor(self, ctx:RADENNParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#power.
    def visitPower(self, ctx:RADENNParser.PowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#call.
    def visitCall(self, ctx:RADENNParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#atom.
    def visitAtom(self, ctx:RADENNParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#listExpr.
    def visitListExpr(self, ctx:RADENNParser.ListExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#matExpr.
    def visitMatExpr(self, ctx:RADENNParser.MatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#matRow.
    def visitMatRow(self, ctx:RADENNParser.MatRowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#datasetExpr.
    def visitDatasetExpr(self, ctx:RADENNParser.DatasetExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#optimizerExpr.
    def visitOptimizerExpr(self, ctx:RADENNParser.OptimizerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#inputLayerExpr.
    def visitInputLayerExpr(self, ctx:RADENNParser.InputLayerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#hiddenLayerExpr.
    def visitHiddenLayerExpr(self, ctx:RADENNParser.HiddenLayerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#outputLayerExpr.
    def visitOutputLayerExpr(self, ctx:RADENNParser.OutputLayerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#networkExpr.
    def visitNetworkExpr(self, ctx:RADENNParser.NetworkExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#ifExpr.
    def visitIfExpr(self, ctx:RADENNParser.IfExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#elifExpr.
    def visitElifExpr(self, ctx:RADENNParser.ElifExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#elseExpr.
    def visitElseExpr(self, ctx:RADENNParser.ElseExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#block.
    def visitBlock(self, ctx:RADENNParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#forExpr.
    def visitForExpr(self, ctx:RADENNParser.ForExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#whileExpr.
    def visitWhileExpr(self, ctx:RADENNParser.WhileExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#doWhileExpr.
    def visitDoWhileExpr(self, ctx:RADENNParser.DoWhileExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#funcDef.
    def visitFuncDef(self, ctx:RADENNParser.FuncDefContext):
        return self.visitChildren(ctx)



del RADENNParser