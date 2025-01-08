# Generated from D:/5th_Semester_Concepts/Compiler_Design/Project/RADENN/Grammar/RADENN.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RADENNParser import RADENNParser
else:
    from RADENNParser import RADENNParser

# This class defines a complete generic visitor for a parse tree produced by RADENNParser.

class RADENNVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RADENNParser#program.
    def visitProgram(self, ctx:RADENNParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#statements.
    def visitStatements(self, ctx:RADENNParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#returnStatement.
    def visitReturnStatement(self, ctx:RADENNParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#continueStatement.
    def visitContinueStatement(self, ctx:RADENNParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#breakStatement.
    def visitBreakStatement(self, ctx:RADENNParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#exprStatement.
    def visitExprStatement(self, ctx:RADENNParser.ExprStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#varAssignment.
    def visitVarAssignment(self, ctx:RADENNParser.VarAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#logicalExpr.
    def visitLogicalExpr(self, ctx:RADENNParser.LogicalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#notExpr.
    def visitNotExpr(self, ctx:RADENNParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#comparisonExpr.
    def visitComparisonExpr(self, ctx:RADENNParser.ComparisonExprContext):
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


    # Visit a parse tree produced by RADENNParser#intAtom.
    def visitIntAtom(self, ctx:RADENNParser.IntAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#floatAtom.
    def visitFloatAtom(self, ctx:RADENNParser.FloatAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#stringAtom.
    def visitStringAtom(self, ctx:RADENNParser.StringAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#identifierAtom.
    def visitIdentifierAtom(self, ctx:RADENNParser.IdentifierAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#parenExpr.
    def visitParenExpr(self, ctx:RADENNParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#listAtom.
    def visitListAtom(self, ctx:RADENNParser.ListAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#matrixAtom.
    def visitMatrixAtom(self, ctx:RADENNParser.MatrixAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#datasetAtom.
    def visitDatasetAtom(self, ctx:RADENNParser.DatasetAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#optimizerAtom.
    def visitOptimizerAtom(self, ctx:RADENNParser.OptimizerAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#inputLayerAtom.
    def visitInputLayerAtom(self, ctx:RADENNParser.InputLayerAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#hiddenLayerAtom.
    def visitHiddenLayerAtom(self, ctx:RADENNParser.HiddenLayerAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#outputLayerAtom.
    def visitOutputLayerAtom(self, ctx:RADENNParser.OutputLayerAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#networkAtom.
    def visitNetworkAtom(self, ctx:RADENNParser.NetworkAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#ifAtom.
    def visitIfAtom(self, ctx:RADENNParser.IfAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#forAtom.
    def visitForAtom(self, ctx:RADENNParser.ForAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#whileAtom.
    def visitWhileAtom(self, ctx:RADENNParser.WhileAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#doWhileAtom.
    def visitDoWhileAtom(self, ctx:RADENNParser.DoWhileAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RADENNParser#funcDefAtom.
    def visitFuncDefAtom(self, ctx:RADENNParser.FuncDefAtomContext):
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