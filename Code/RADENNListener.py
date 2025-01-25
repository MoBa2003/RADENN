# Generated from C:/Users/ASUS/iman/elmos/fifth semester/Compiler/finalproject/us/RADENN/Grammar/RADENN.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .RADENNParser import RADENNParser
else:
    from RADENNParser import RADENNParser

# This class defines a complete listener for a parse tree produced by RADENNParser.
class RADENNListener(ParseTreeListener):

    # Enter a parse tree produced by RADENNParser#start.
    def enterStart(self, ctx:RADENNParser.StartContext):
        pass

    # Exit a parse tree produced by RADENNParser#start.
    def exitStart(self, ctx:RADENNParser.StartContext):
        pass


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


    # Enter a parse tree produced by RADENNParser#statement.
    def enterStatement(self, ctx:RADENNParser.StatementContext):
        pass

    # Exit a parse tree produced by RADENNParser#statement.
    def exitStatement(self, ctx:RADENNParser.StatementContext):
        pass


    # Enter a parse tree produced by RADENNParser#expr.
    def enterExpr(self, ctx:RADENNParser.ExprContext):
        pass

    # Exit a parse tree produced by RADENNParser#expr.
    def exitExpr(self, ctx:RADENNParser.ExprContext):
        pass


    # Enter a parse tree produced by RADENNParser#compExpr.
    def enterCompExpr(self, ctx:RADENNParser.CompExprContext):
        pass

    # Exit a parse tree produced by RADENNParser#compExpr.
    def exitCompExpr(self, ctx:RADENNParser.CompExprContext):
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


    # Enter a parse tree produced by RADENNParser#atom.
    def enterAtom(self, ctx:RADENNParser.AtomContext):
        pass

    # Exit a parse tree produced by RADENNParser#atom.
    def exitAtom(self, ctx:RADENNParser.AtomContext):
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