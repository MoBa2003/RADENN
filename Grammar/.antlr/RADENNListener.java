// Generated from d:/5th_Semester_Concepts/Compiler_Design/Project/RADENN/Grammar/RADENN.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link RADENNParser}.
 */
public interface RADENNListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link RADENNParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(RADENNParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link RADENNParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(RADENNParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link RADENNParser#statements}.
	 * @param ctx the parse tree
	 */
	void enterStatements(RADENNParser.StatementsContext ctx);
	/**
	 * Exit a parse tree produced by {@link RADENNParser#statements}.
	 * @param ctx the parse tree
	 */
	void exitStatements(RADENNParser.StatementsContext ctx);
	/**
	 * Enter a parse tree produced by the {@code returnStatement}
	 * labeled alternative in {@link RADENNParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterReturnStatement(RADENNParser.ReturnStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code returnStatement}
	 * labeled alternative in {@link RADENNParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitReturnStatement(RADENNParser.ReturnStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code continueStatement}
	 * labeled alternative in {@link RADENNParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterContinueStatement(RADENNParser.ContinueStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code continueStatement}
	 * labeled alternative in {@link RADENNParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitContinueStatement(RADENNParser.ContinueStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code breakStatement}
	 * labeled alternative in {@link RADENNParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterBreakStatement(RADENNParser.BreakStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code breakStatement}
	 * labeled alternative in {@link RADENNParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitBreakStatement(RADENNParser.BreakStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code exprStatement}
	 * labeled alternative in {@link RADENNParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterExprStatement(RADENNParser.ExprStatementContext ctx);
	/**
	 * Exit a parse tree produced by the {@code exprStatement}
	 * labeled alternative in {@link RADENNParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitExprStatement(RADENNParser.ExprStatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code varAssignment}
	 * labeled alternative in {@link RADENNParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterVarAssignment(RADENNParser.VarAssignmentContext ctx);
	/**
	 * Exit a parse tree produced by the {@code varAssignment}
	 * labeled alternative in {@link RADENNParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitVarAssignment(RADENNParser.VarAssignmentContext ctx);
	/**
	 * Enter a parse tree produced by the {@code logicalExpr}
	 * labeled alternative in {@link RADENNParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterLogicalExpr(RADENNParser.LogicalExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code logicalExpr}
	 * labeled alternative in {@link RADENNParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitLogicalExpr(RADENNParser.LogicalExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code notExpr}
	 * labeled alternative in {@link RADENNParser#compExpr}.
	 * @param ctx the parse tree
	 */
	void enterNotExpr(RADENNParser.NotExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code notExpr}
	 * labeled alternative in {@link RADENNParser#compExpr}.
	 * @param ctx the parse tree
	 */
	void exitNotExpr(RADENNParser.NotExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code comparisonExpr}
	 * labeled alternative in {@link RADENNParser#compExpr}.
	 * @param ctx the parse tree
	 */
	void enterComparisonExpr(RADENNParser.ComparisonExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code comparisonExpr}
	 * labeled alternative in {@link RADENNParser#compExpr}.
	 * @param ctx the parse tree
	 */
	void exitComparisonExpr(RADENNParser.ComparisonExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link RADENNParser#arithExpr}.
	 * @param ctx the parse tree
	 */
	void enterArithExpr(RADENNParser.ArithExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link RADENNParser#arithExpr}.
	 * @param ctx the parse tree
	 */
	void exitArithExpr(RADENNParser.ArithExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link RADENNParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(RADENNParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link RADENNParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(RADENNParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link RADENNParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(RADENNParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link RADENNParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(RADENNParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link RADENNParser#power}.
	 * @param ctx the parse tree
	 */
	void enterPower(RADENNParser.PowerContext ctx);
	/**
	 * Exit a parse tree produced by {@link RADENNParser#power}.
	 * @param ctx the parse tree
	 */
	void exitPower(RADENNParser.PowerContext ctx);
	/**
	 * Enter a parse tree produced by {@link RADENNParser#call}.
	 * @param ctx the parse tree
	 */
	void enterCall(RADENNParser.CallContext ctx);
	/**
	 * Exit a parse tree produced by {@link RADENNParser#call}.
	 * @param ctx the parse tree
	 */
	void exitCall(RADENNParser.CallContext ctx);
	/**
	 * Enter a parse tree produced by the {@code intAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterIntAtom(RADENNParser.IntAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code intAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitIntAtom(RADENNParser.IntAtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code floatAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterFloatAtom(RADENNParser.FloatAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code floatAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitFloatAtom(RADENNParser.FloatAtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code stringAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterStringAtom(RADENNParser.StringAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code stringAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitStringAtom(RADENNParser.StringAtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code identifierAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterIdentifierAtom(RADENNParser.IdentifierAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code identifierAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitIdentifierAtom(RADENNParser.IdentifierAtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code parenExpr}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterParenExpr(RADENNParser.ParenExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code parenExpr}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitParenExpr(RADENNParser.ParenExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code listAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterListAtom(RADENNParser.ListAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code listAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitListAtom(RADENNParser.ListAtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code matrixAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterMatrixAtom(RADENNParser.MatrixAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code matrixAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitMatrixAtom(RADENNParser.MatrixAtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code datasetAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterDatasetAtom(RADENNParser.DatasetAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code datasetAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitDatasetAtom(RADENNParser.DatasetAtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code optimizerAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterOptimizerAtom(RADENNParser.OptimizerAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code optimizerAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitOptimizerAtom(RADENNParser.OptimizerAtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code inputLayerAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterInputLayerAtom(RADENNParser.InputLayerAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code inputLayerAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitInputLayerAtom(RADENNParser.InputLayerAtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code hiddenLayerAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterHiddenLayerAtom(RADENNParser.HiddenLayerAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code hiddenLayerAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitHiddenLayerAtom(RADENNParser.HiddenLayerAtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code outputLayerAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterOutputLayerAtom(RADENNParser.OutputLayerAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code outputLayerAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitOutputLayerAtom(RADENNParser.OutputLayerAtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code networkAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterNetworkAtom(RADENNParser.NetworkAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code networkAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitNetworkAtom(RADENNParser.NetworkAtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ifAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterIfAtom(RADENNParser.IfAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ifAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitIfAtom(RADENNParser.IfAtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code forAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterForAtom(RADENNParser.ForAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code forAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitForAtom(RADENNParser.ForAtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code whileAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterWhileAtom(RADENNParser.WhileAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code whileAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitWhileAtom(RADENNParser.WhileAtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code doWhileAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterDoWhileAtom(RADENNParser.DoWhileAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code doWhileAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitDoWhileAtom(RADENNParser.DoWhileAtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code funcDefAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterFuncDefAtom(RADENNParser.FuncDefAtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code funcDefAtom}
	 * labeled alternative in {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitFuncDefAtom(RADENNParser.FuncDefAtomContext ctx);
	/**
	 * Enter a parse tree produced by {@link RADENNParser#listExpr}.
	 * @param ctx the parse tree
	 */
	void enterListExpr(RADENNParser.ListExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link RADENNParser#listExpr}.
	 * @param ctx the parse tree
	 */
	void exitListExpr(RADENNParser.ListExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link RADENNParser#matExpr}.
	 * @param ctx the parse tree
	 */
	void enterMatExpr(RADENNParser.MatExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link RADENNParser#matExpr}.
	 * @param ctx the parse tree
	 */
	void exitMatExpr(RADENNParser.MatExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link RADENNParser#matRow}.
	 * @param ctx the parse tree
	 */
	void enterMatRow(RADENNParser.MatRowContext ctx);
	/**
	 * Exit a parse tree produced by {@link RADENNParser#matRow}.
	 * @param ctx the parse tree
	 */
	void exitMatRow(RADENNParser.MatRowContext ctx);
	/**
	 * Enter a parse tree produced by {@link RADENNParser#datasetExpr}.
	 * @param ctx the parse tree
	 */
	void enterDatasetExpr(RADENNParser.DatasetExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link RADENNParser#datasetExpr}.
	 * @param ctx the parse tree
	 */
	void exitDatasetExpr(RADENNParser.DatasetExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link RADENNParser#optimizerExpr}.
	 * @param ctx the parse tree
	 */
	void enterOptimizerExpr(RADENNParser.OptimizerExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link RADENNParser#optimizerExpr}.
	 * @param ctx the parse tree
	 */
	void exitOptimizerExpr(RADENNParser.OptimizerExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link RADENNParser#inputLayerExpr}.
	 * @param ctx the parse tree
	 */
	void enterInputLayerExpr(RADENNParser.InputLayerExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link RADENNParser#inputLayerExpr}.
	 * @param ctx the parse tree
	 */
	void exitInputLayerExpr(RADENNParser.InputLayerExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link RADENNParser#hiddenLayerExpr}.
	 * @param ctx the parse tree
	 */
	void enterHiddenLayerExpr(RADENNParser.HiddenLayerExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link RADENNParser#hiddenLayerExpr}.
	 * @param ctx the parse tree
	 */
	void exitHiddenLayerExpr(RADENNParser.HiddenLayerExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link RADENNParser#outputLayerExpr}.
	 * @param ctx the parse tree
	 */
	void enterOutputLayerExpr(RADENNParser.OutputLayerExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link RADENNParser#outputLayerExpr}.
	 * @param ctx the parse tree
	 */
	void exitOutputLayerExpr(RADENNParser.OutputLayerExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link RADENNParser#networkExpr}.
	 * @param ctx the parse tree
	 */
	void enterNetworkExpr(RADENNParser.NetworkExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link RADENNParser#networkExpr}.
	 * @param ctx the parse tree
	 */
	void exitNetworkExpr(RADENNParser.NetworkExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link RADENNParser#ifExpr}.
	 * @param ctx the parse tree
	 */
	void enterIfExpr(RADENNParser.IfExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link RADENNParser#ifExpr}.
	 * @param ctx the parse tree
	 */
	void exitIfExpr(RADENNParser.IfExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link RADENNParser#elifExpr}.
	 * @param ctx the parse tree
	 */
	void enterElifExpr(RADENNParser.ElifExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link RADENNParser#elifExpr}.
	 * @param ctx the parse tree
	 */
	void exitElifExpr(RADENNParser.ElifExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link RADENNParser#elseExpr}.
	 * @param ctx the parse tree
	 */
	void enterElseExpr(RADENNParser.ElseExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link RADENNParser#elseExpr}.
	 * @param ctx the parse tree
	 */
	void exitElseExpr(RADENNParser.ElseExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link RADENNParser#forExpr}.
	 * @param ctx the parse tree
	 */
	void enterForExpr(RADENNParser.ForExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link RADENNParser#forExpr}.
	 * @param ctx the parse tree
	 */
	void exitForExpr(RADENNParser.ForExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link RADENNParser#whileExpr}.
	 * @param ctx the parse tree
	 */
	void enterWhileExpr(RADENNParser.WhileExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link RADENNParser#whileExpr}.
	 * @param ctx the parse tree
	 */
	void exitWhileExpr(RADENNParser.WhileExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link RADENNParser#doWhileExpr}.
	 * @param ctx the parse tree
	 */
	void enterDoWhileExpr(RADENNParser.DoWhileExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link RADENNParser#doWhileExpr}.
	 * @param ctx the parse tree
	 */
	void exitDoWhileExpr(RADENNParser.DoWhileExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link RADENNParser#funcDef}.
	 * @param ctx the parse tree
	 */
	void enterFuncDef(RADENNParser.FuncDefContext ctx);
	/**
	 * Exit a parse tree produced by {@link RADENNParser#funcDef}.
	 * @param ctx the parse tree
	 */
	void exitFuncDef(RADENNParser.FuncDefContext ctx);
}