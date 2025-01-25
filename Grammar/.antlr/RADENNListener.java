// Generated from c:/Users/ASUS/iman/elmos/fifth semester/Compiler/finalproject/us/RADENN/Grammar/RADENN.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link RADENNParser}.
 */
public interface RADENNListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link RADENNParser#start}.
	 * @param ctx the parse tree
	 */
	void enterStart(RADENNParser.StartContext ctx);
	/**
	 * Exit a parse tree produced by {@link RADENNParser#start}.
	 * @param ctx the parse tree
	 */
	void exitStart(RADENNParser.StartContext ctx);
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
	 * Enter a parse tree produced by {@link RADENNParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(RADENNParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link RADENNParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(RADENNParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link RADENNParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(RADENNParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link RADENNParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(RADENNParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link RADENNParser#compExpr}.
	 * @param ctx the parse tree
	 */
	void enterCompExpr(RADENNParser.CompExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link RADENNParser#compExpr}.
	 * @param ctx the parse tree
	 */
	void exitCompExpr(RADENNParser.CompExprContext ctx);
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
	 * Enter a parse tree produced by {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterAtom(RADENNParser.AtomContext ctx);
	/**
	 * Exit a parse tree produced by {@link RADENNParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitAtom(RADENNParser.AtomContext ctx);
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