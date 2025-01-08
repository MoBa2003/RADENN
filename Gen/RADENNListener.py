# Generated from D:/5th_Semester_Concepts/Compiler_Design/Project/RADENN/Grammar/RADENN.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RADENNParser import RADENNParser
else:
    from RADENNParser import RADENNParser

# This class defines a complete listener for a parse tree produced by RADENNParser.
class RADENNListener(ParseTreeListener):

    # Enter a parse tree produced by RADENNParser#program.
    def enterProgram(self, ctx:RADENNParser.ProgramContext):
        pass

    # Exit a parse tree produced by RADENNParser#program.
    def exitProgram(self, ctx:RADENNParser.ProgramContext):
        pass


    # Enter a parse tree produced by RADENNParser#statements.
    def enterStatements(self, ctx:RADENNParser.StatementsContext):
        pass

    # Exit a parse tree produced by RADENNParser#statements.
    def exitStatements(self, ctx:RADENNParser.StatementsContext):
        pass


    # Enter a parse tree produced by RADENNParser#returnStatement.
    def enterReturnStatement(self, ctx:RADENNParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by RADENNParser#returnStatement.
    def exitReturnStatement(self, ctx:RADENNParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by RADENNParser#continueStatement.
    def enterContinueStatement(self, ctx:RADENNParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by RADENNParser#continueStatement.
    def exitContinueStatement(self, ctx:RADENNParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by RADENNParser#breakStatement.
    def enterBreakStatement(self, ctx:RADENNParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by RADENNParser#breakStatement.
    def exitBreakStatement(self, ctx:RADENNParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by RADENNParser#exprStatement.
    def enterExprStatement(self, ctx:RADENNParser.ExprStatementContext):
        pass

    # Exit a parse tree produced by RADENNParser#exprStatement.
    def exitExprStatement(self, ctx:RADENNParser.ExprStatementContext):
        pass


    # Enter a parse tree produced by RADENNParser#varAssignment.
    def enterVarAssignment(self, ctx:RADENNParser.VarAssignmentContext):
        pass

    # Exit a parse tree produced by RADENNParser#varAssignment.
    def exitVarAssignment(self, ctx:RADENNParser.VarAssignmentContext):
        pass


    # Enter a parse tree produced by RADENNParser#logicalExpr.
    def enterLogicalExpr(self, ctx:RADENNParser.LogicalExprContext):
        pass

    # Exit a parse tree produced by RADENNParser#logicalExpr.
    def exitLogicalExpr(self, ctx:RADENNParser.LogicalExprContext):
        pass


    # Enter a parse tree produced by RADENNParser#notExpr.
    def enterNotExpr(self, ctx:RADENNParser.NotExprContext):
        pass

    # Exit a parse tree produced by RADENNParser#notExpr.
    def exitNotExpr(self, ctx:RADENNParser.NotExprContext):
        pass


    # Enter a parse tree produced by RADENNParser#comparisonExpr.
    def enterComparisonExpr(self, ctx:RADENNParser.ComparisonExprContext):
        pass

    # Exit a parse tree produced by RADENNParser#comparisonExpr.
    def exitComparisonExpr(self, ctx:RADENNParser.ComparisonExprContext):
        pass


    # Enter a parse tree produced by RADENNParser#arithExpr.
    def enterArithExpr(self, ctx:RADENNParser.ArithExprContext):
        pass

    # Exit a parse tree produced by RADENNParser#arithExpr.
    def exitArithExpr(self, ctx:RADENNParser.ArithExprContext):
        pass


    # Enter a parse tree produced by RADENNParser#term.
    def enterTerm(self, ctx:RADENNParser.TermContext):
        pass

    # Exit a parse tree produced by RADENNParser#term.
    def exitTerm(self, ctx:RADENNParser.TermContext):
        pass


    # Enter a parse tree produced by RADENNParser#factor.
    def enterFactor(self, ctx:RADENNParser.FactorContext):
        pass

    # Exit a parse tree produced by RADENNParser#factor.
    def exitFactor(self, ctx:RADENNParser.FactorContext):
        pass


    # Enter a parse tree produced by RADENNParser#power.
    def enterPower(self, ctx:RADENNParser.PowerContext):
        pass

    # Exit a parse tree produced by RADENNParser#power.
    def exitPower(self, ctx:RADENNParser.PowerContext):
        pass


    # Enter a parse tree produced by RADENNParser#call.
    def enterCall(self, ctx:RADENNParser.CallContext):
        pass

    # Exit a parse tree produced by RADENNParser#call.
    def exitCall(self, ctx:RADENNParser.CallContext):
        pass


    # Enter a parse tree produced by RADENNParser#intAtom.
    def enterIntAtom(self, ctx:RADENNParser.IntAtomContext):
        pass

    # Exit a parse tree produced by RADENNParser#intAtom.
    def exitIntAtom(self, ctx:RADENNParser.IntAtomContext):
        pass


    # Enter a parse tree produced by RADENNParser#floatAtom.
    def enterFloatAtom(self, ctx:RADENNParser.FloatAtomContext):
        pass

    # Exit a parse tree produced by RADENNParser#floatAtom.
    def exitFloatAtom(self, ctx:RADENNParser.FloatAtomContext):
        pass


    # Enter a parse tree produced by RADENNParser#stringAtom.
    def enterStringAtom(self, ctx:RADENNParser.StringAtomContext):
        pass

    # Exit a parse tree produced by RADENNParser#stringAtom.
    def exitStringAtom(self, ctx:RADENNParser.StringAtomContext):
        pass


    # Enter a parse tree produced by RADENNParser#identifierAtom.
    def enterIdentifierAtom(self, ctx:RADENNParser.IdentifierAtomContext):
        pass

    # Exit a parse tree produced by RADENNParser#identifierAtom.
    def exitIdentifierAtom(self, ctx:RADENNParser.IdentifierAtomContext):
        pass


    # Enter a parse tree produced by RADENNParser#parenExpr.
    def enterParenExpr(self, ctx:RADENNParser.ParenExprContext):
        pass

    # Exit a parse tree produced by RADENNParser#parenExpr.
    def exitParenExpr(self, ctx:RADENNParser.ParenExprContext):
        pass


    # Enter a parse tree produced by RADENNParser#listAtom.
    def enterListAtom(self, ctx:RADENNParser.ListAtomContext):
        pass

    # Exit a parse tree produced by RADENNParser#listAtom.
    def exitListAtom(self, ctx:RADENNParser.ListAtomContext):
        pass


    # Enter a parse tree produced by RADENNParser#matrixAtom.
    def enterMatrixAtom(self, ctx:RADENNParser.MatrixAtomContext):
        pass

    # Exit a parse tree produced by RADENNParser#matrixAtom.
    def exitMatrixAtom(self, ctx:RADENNParser.MatrixAtomContext):
        pass


    # Enter a parse tree produced by RADENNParser#datasetAtom.
    def enterDatasetAtom(self, ctx:RADENNParser.DatasetAtomContext):
        pass

    # Exit a parse tree produced by RADENNParser#datasetAtom.
    def exitDatasetAtom(self, ctx:RADENNParser.DatasetAtomContext):
        pass


    # Enter a parse tree produced by RADENNParser#optimizerAtom.
    def enterOptimizerAtom(self, ctx:RADENNParser.OptimizerAtomContext):
        pass

    # Exit a parse tree produced by RADENNParser#optimizerAtom.
    def exitOptimizerAtom(self, ctx:RADENNParser.OptimizerAtomContext):
        pass


    # Enter a parse tree produced by RADENNParser#inputLayerAtom.
    def enterInputLayerAtom(self, ctx:RADENNParser.InputLayerAtomContext):
        pass

    # Exit a parse tree produced by RADENNParser#inputLayerAtom.
    def exitInputLayerAtom(self, ctx:RADENNParser.InputLayerAtomContext):
        pass


    # Enter a parse tree produced by RADENNParser#hiddenLayerAtom.
    def enterHiddenLayerAtom(self, ctx:RADENNParser.HiddenLayerAtomContext):
        pass

    # Exit a parse tree produced by RADENNParser#hiddenLayerAtom.
    def exitHiddenLayerAtom(self, ctx:RADENNParser.HiddenLayerAtomContext):
        pass


    # Enter a parse tree produced by RADENNParser#outputLayerAtom.
    def enterOutputLayerAtom(self, ctx:RADENNParser.OutputLayerAtomContext):
        pass

    # Exit a parse tree produced by RADENNParser#outputLayerAtom.
    def exitOutputLayerAtom(self, ctx:RADENNParser.OutputLayerAtomContext):
        pass


    # Enter a parse tree produced by RADENNParser#networkAtom.
    def enterNetworkAtom(self, ctx:RADENNParser.NetworkAtomContext):
        pass

    # Exit a parse tree produced by RADENNParser#networkAtom.
    def exitNetworkAtom(self, ctx:RADENNParser.NetworkAtomContext):
        pass


    # Enter a parse tree produced by RADENNParser#ifAtom.
    def enterIfAtom(self, ctx:RADENNParser.IfAtomContext):
        pass

    # Exit a parse tree produced by RADENNParser#ifAtom.
    def exitIfAtom(self, ctx:RADENNParser.IfAtomContext):
        pass


    # Enter a parse tree produced by RADENNParser#forAtom.
    def enterForAtom(self, ctx:RADENNParser.ForAtomContext):
        pass

    # Exit a parse tree produced by RADENNParser#forAtom.
    def exitForAtom(self, ctx:RADENNParser.ForAtomContext):
        pass


    # Enter a parse tree produced by RADENNParser#whileAtom.
    def enterWhileAtom(self, ctx:RADENNParser.WhileAtomContext):
        pass

    # Exit a parse tree produced by RADENNParser#whileAtom.
    def exitWhileAtom(self, ctx:RADENNParser.WhileAtomContext):
        pass


    # Enter a parse tree produced by RADENNParser#doWhileAtom.
    def enterDoWhileAtom(self, ctx:RADENNParser.DoWhileAtomContext):
        pass

    # Exit a parse tree produced by RADENNParser#doWhileAtom.
    def exitDoWhileAtom(self, ctx:RADENNParser.DoWhileAtomContext):
        pass


    # Enter a parse tree produced by RADENNParser#funcDefAtom.
    def enterFuncDefAtom(self, ctx:RADENNParser.FuncDefAtomContext):
        pass

    # Exit a parse tree produced by RADENNParser#funcDefAtom.
    def exitFuncDefAtom(self, ctx:RADENNParser.FuncDefAtomContext):
        pass


    # Enter a parse tree produced by RADENNParser#listExpr.
    def enterListExpr(self, ctx:RADENNParser.ListExprContext):
        pass

    # Exit a parse tree produced by RADENNParser#listExpr.
    def exitListExpr(self, ctx:RADENNParser.ListExprContext):
        pass


    # Enter a parse tree produced by RADENNParser#matExpr.
    def enterMatExpr(self, ctx:RADENNParser.MatExprContext):
        pass

    # Exit a parse tree produced by RADENNParser#matExpr.
    def exitMatExpr(self, ctx:RADENNParser.MatExprContext):
        pass


    # Enter a parse tree produced by RADENNParser#matRow.
    def enterMatRow(self, ctx:RADENNParser.MatRowContext):
        pass

    # Exit a parse tree produced by RADENNParser#matRow.
    def exitMatRow(self, ctx:RADENNParser.MatRowContext):
        pass


    # Enter a parse tree produced by RADENNParser#datasetExpr.
    def enterDatasetExpr(self, ctx:RADENNParser.DatasetExprContext):
        pass

    # Exit a parse tree produced by RADENNParser#datasetExpr.
    def exitDatasetExpr(self, ctx:RADENNParser.DatasetExprContext):
        pass


    # Enter a parse tree produced by RADENNParser#optimizerExpr.
    def enterOptimizerExpr(self, ctx:RADENNParser.OptimizerExprContext):
        pass

    # Exit a parse tree produced by RADENNParser#optimizerExpr.
    def exitOptimizerExpr(self, ctx:RADENNParser.OptimizerExprContext):
        pass


    # Enter a parse tree produced by RADENNParser#inputLayerExpr.
    def enterInputLayerExpr(self, ctx:RADENNParser.InputLayerExprContext):
        pass

    # Exit a parse tree produced by RADENNParser#inputLayerExpr.
    def exitInputLayerExpr(self, ctx:RADENNParser.InputLayerExprContext):
        pass


    # Enter a parse tree produced by RADENNParser#hiddenLayerExpr.
    def enterHiddenLayerExpr(self, ctx:RADENNParser.HiddenLayerExprContext):
        pass

    # Exit a parse tree produced by RADENNParser#hiddenLayerExpr.
    def exitHiddenLayerExpr(self, ctx:RADENNParser.HiddenLayerExprContext):
        pass


    # Enter a parse tree produced by RADENNParser#outputLayerExpr.
    def enterOutputLayerExpr(self, ctx:RADENNParser.OutputLayerExprContext):
        pass

    # Exit a parse tree produced by RADENNParser#outputLayerExpr.
    def exitOutputLayerExpr(self, ctx:RADENNParser.OutputLayerExprContext):
        pass


    # Enter a parse tree produced by RADENNParser#networkExpr.
    def enterNetworkExpr(self, ctx:RADENNParser.NetworkExprContext):
        pass

    # Exit a parse tree produced by RADENNParser#networkExpr.
    def exitNetworkExpr(self, ctx:RADENNParser.NetworkExprContext):
        pass


    # Enter a parse tree produced by RADENNParser#ifExpr.
    def enterIfExpr(self, ctx:RADENNParser.IfExprContext):
        pass

    # Exit a parse tree produced by RADENNParser#ifExpr.
    def exitIfExpr(self, ctx:RADENNParser.IfExprContext):
        pass


    # Enter a parse tree produced by RADENNParser#elifExpr.
    def enterElifExpr(self, ctx:RADENNParser.ElifExprContext):
        pass

    # Exit a parse tree produced by RADENNParser#elifExpr.
    def exitElifExpr(self, ctx:RADENNParser.ElifExprContext):
        pass


    # Enter a parse tree produced by RADENNParser#elseExpr.
    def enterElseExpr(self, ctx:RADENNParser.ElseExprContext):
        pass

    # Exit a parse tree produced by RADENNParser#elseExpr.
    def exitElseExpr(self, ctx:RADENNParser.ElseExprContext):
        pass


    # Enter a parse tree produced by RADENNParser#forExpr.
    def enterForExpr(self, ctx:RADENNParser.ForExprContext):
        pass

    # Exit a parse tree produced by RADENNParser#forExpr.
    def exitForExpr(self, ctx:RADENNParser.ForExprContext):
        pass


    # Enter a parse tree produced by RADENNParser#whileExpr.
    def enterWhileExpr(self, ctx:RADENNParser.WhileExprContext):
        pass

    # Exit a parse tree produced by RADENNParser#whileExpr.
    def exitWhileExpr(self, ctx:RADENNParser.WhileExprContext):
        pass


    # Enter a parse tree produced by RADENNParser#doWhileExpr.
    def enterDoWhileExpr(self, ctx:RADENNParser.DoWhileExprContext):
        pass

    # Exit a parse tree produced by RADENNParser#doWhileExpr.
    def exitDoWhileExpr(self, ctx:RADENNParser.DoWhileExprContext):
        pass


    # Enter a parse tree produced by RADENNParser#funcDef.
    def enterFuncDef(self, ctx:RADENNParser.FuncDefContext):
        pass

    # Exit a parse tree produced by RADENNParser#funcDef.
    def exitFuncDef(self, ctx:RADENNParser.FuncDefContext):
        pass



del RADENNParser