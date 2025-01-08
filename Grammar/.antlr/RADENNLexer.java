// Generated from d:/5th_Semester_Concepts/Compiler_Design/Project/RADENN/Grammar/RADENN.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class RADENNLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, PLUS=21, MINUS=22, MUL=23, DIV=24, MOD=25, 
		POW=26, EQ=27, LPAREN=28, RPAREN=29, LSQUARE=30, RSQUARE=31, LROUND=32, 
		RROUND=33, COMMA=34, EE=35, NE=36, LT=37, GT=38, LTE=39, GTE=40, IDENTIFIER=41, 
		INT=42, FLOAT=43, STRING=44, NEWLINE=45, WS=46, COMMENT=47, MULTILINE_COMMENT=48;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "T__10", "T__11", "T__12", "T__13", "T__14", "T__15", "T__16", 
			"T__17", "T__18", "T__19", "PLUS", "MINUS", "MUL", "DIV", "MOD", "POW", 
			"EQ", "LPAREN", "RPAREN", "LSQUARE", "RSQUARE", "LROUND", "RROUND", "COMMA", 
			"EE", "NE", "LT", "GT", "LTE", "GTE", "IDENTIFIER", "INT", "FLOAT", "STRING", 
			"NEWLINE", "WS", "COMMENT", "MULTILINE_COMMENT"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'return'", "'continue'", "'break'", "'var'", "'and'", "'or'", 
			"'not'", "'dataset'", "'optimizer'", "'inputLayer'", "'hiddenLayer'", 
			"'outputLayer'", "'network'", "'if'", "'elif'", "'else'", "'for'", "'while'", 
			"'do'", "'function'", "'+'", "'-'", "'*'", "'/'", "'%'", "'^'", "'='", 
			"'('", "')'", "'['", "']'", "'{'", "'}'", "','", "'=='", "'!='", "'<'", 
			"'>'", "'<='", "'>='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, "PLUS", "MINUS", 
			"MUL", "DIV", "MOD", "POW", "EQ", "LPAREN", "RPAREN", "LSQUARE", "RSQUARE", 
			"LROUND", "RROUND", "COMMA", "EE", "NE", "LT", "GT", "LTE", "GTE", "IDENTIFIER", 
			"INT", "FLOAT", "STRING", "NEWLINE", "WS", "COMMENT", "MULTILINE_COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public RADENNLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "RADENN.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u00000\u015a\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002"+
		"\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002"+
		"\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002"+
		"\u001b\u0007\u001b\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002"+
		"\u001e\u0007\u001e\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007"+
		"!\u0002\"\u0007\"\u0002#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007"+
		"&\u0002\'\u0007\'\u0002(\u0007(\u0002)\u0007)\u0002*\u0007*\u0002+\u0007"+
		"+\u0002,\u0007,\u0002-\u0007-\u0002.\u0007.\u0002/\u0007/\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001"+
		"\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001"+
		"\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001"+
		"\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0001"+
		"\u0018\u0001\u0018\u0001\u0019\u0001\u0019\u0001\u001a\u0001\u001a\u0001"+
		"\u001b\u0001\u001b\u0001\u001c\u0001\u001c\u0001\u001d\u0001\u001d\u0001"+
		"\u001e\u0001\u001e\u0001\u001f\u0001\u001f\u0001 \u0001 \u0001!\u0001"+
		"!\u0001\"\u0001\"\u0001\"\u0001#\u0001#\u0001#\u0001$\u0001$\u0001%\u0001"+
		"%\u0001&\u0001&\u0001&\u0001\'\u0001\'\u0001\'\u0001(\u0001(\u0005(\u0115"+
		"\b(\n(\f(\u0118\t(\u0001)\u0004)\u011b\b)\u000b)\f)\u011c\u0001*\u0004"+
		"*\u0120\b*\u000b*\f*\u0121\u0001*\u0001*\u0005*\u0126\b*\n*\f*\u0129\t"+
		"*\u0001+\u0001+\u0001+\u0001+\u0005+\u012f\b+\n+\f+\u0132\t+\u0001+\u0001"+
		"+\u0001,\u0004,\u0137\b,\u000b,\f,\u0138\u0001-\u0004-\u013c\b-\u000b"+
		"-\f-\u013d\u0001-\u0001-\u0001.\u0001.\u0001.\u0001.\u0005.\u0146\b.\n"+
		".\f.\u0149\t.\u0001.\u0001.\u0001/\u0001/\u0001/\u0001/\u0005/\u0151\b"+
		"/\n/\f/\u0154\t/\u0001/\u0001/\u0001/\u0001/\u0001/\u0001\u0152\u0000"+
		"0\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006"+
		"\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e"+
		"\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013\'\u0014)\u0015+\u0016-\u0017"+
		"/\u00181\u00193\u001a5\u001b7\u001c9\u001d;\u001e=\u001f? A!C\"E#G$I%"+
		"K&M\'O(Q)S*U+W,Y-[.]/_0\u0001\u0000\u0006\u0003\u0000AZ__az\u0004\u0000"+
		"09AZ__az\u0001\u000009\u0003\u0000\n\n\r\r\"\"\u0002\u0000\n\n\r\r\u0002"+
		"\u0000\t\t  \u0163\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001"+
		"\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001"+
		"\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000"+
		"\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000"+
		"\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000"+
		"\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000"+
		"\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000"+
		"\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000"+
		"\u0000\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000"+
		"%\u0001\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001"+
		"\u0000\u0000\u0000\u0000+\u0001\u0000\u0000\u0000\u0000-\u0001\u0000\u0000"+
		"\u0000\u0000/\u0001\u0000\u0000\u0000\u00001\u0001\u0000\u0000\u0000\u0000"+
		"3\u0001\u0000\u0000\u0000\u00005\u0001\u0000\u0000\u0000\u00007\u0001"+
		"\u0000\u0000\u0000\u00009\u0001\u0000\u0000\u0000\u0000;\u0001\u0000\u0000"+
		"\u0000\u0000=\u0001\u0000\u0000\u0000\u0000?\u0001\u0000\u0000\u0000\u0000"+
		"A\u0001\u0000\u0000\u0000\u0000C\u0001\u0000\u0000\u0000\u0000E\u0001"+
		"\u0000\u0000\u0000\u0000G\u0001\u0000\u0000\u0000\u0000I\u0001\u0000\u0000"+
		"\u0000\u0000K\u0001\u0000\u0000\u0000\u0000M\u0001\u0000\u0000\u0000\u0000"+
		"O\u0001\u0000\u0000\u0000\u0000Q\u0001\u0000\u0000\u0000\u0000S\u0001"+
		"\u0000\u0000\u0000\u0000U\u0001\u0000\u0000\u0000\u0000W\u0001\u0000\u0000"+
		"\u0000\u0000Y\u0001\u0000\u0000\u0000\u0000[\u0001\u0000\u0000\u0000\u0000"+
		"]\u0001\u0000\u0000\u0000\u0000_\u0001\u0000\u0000\u0000\u0001a\u0001"+
		"\u0000\u0000\u0000\u0003h\u0001\u0000\u0000\u0000\u0005q\u0001\u0000\u0000"+
		"\u0000\u0007w\u0001\u0000\u0000\u0000\t{\u0001\u0000\u0000\u0000\u000b"+
		"\u007f\u0001\u0000\u0000\u0000\r\u0082\u0001\u0000\u0000\u0000\u000f\u0086"+
		"\u0001\u0000\u0000\u0000\u0011\u008e\u0001\u0000\u0000\u0000\u0013\u0098"+
		"\u0001\u0000\u0000\u0000\u0015\u00a3\u0001\u0000\u0000\u0000\u0017\u00af"+
		"\u0001\u0000\u0000\u0000\u0019\u00bb\u0001\u0000\u0000\u0000\u001b\u00c3"+
		"\u0001\u0000\u0000\u0000\u001d\u00c6\u0001\u0000\u0000\u0000\u001f\u00cb"+
		"\u0001\u0000\u0000\u0000!\u00d0\u0001\u0000\u0000\u0000#\u00d4\u0001\u0000"+
		"\u0000\u0000%\u00da\u0001\u0000\u0000\u0000\'\u00dd\u0001\u0000\u0000"+
		"\u0000)\u00e6\u0001\u0000\u0000\u0000+\u00e8\u0001\u0000\u0000\u0000-"+
		"\u00ea\u0001\u0000\u0000\u0000/\u00ec\u0001\u0000\u0000\u00001\u00ee\u0001"+
		"\u0000\u0000\u00003\u00f0\u0001\u0000\u0000\u00005\u00f2\u0001\u0000\u0000"+
		"\u00007\u00f4\u0001\u0000\u0000\u00009\u00f6\u0001\u0000\u0000\u0000;"+
		"\u00f8\u0001\u0000\u0000\u0000=\u00fa\u0001\u0000\u0000\u0000?\u00fc\u0001"+
		"\u0000\u0000\u0000A\u00fe\u0001\u0000\u0000\u0000C\u0100\u0001\u0000\u0000"+
		"\u0000E\u0102\u0001\u0000\u0000\u0000G\u0105\u0001\u0000\u0000\u0000I"+
		"\u0108\u0001\u0000\u0000\u0000K\u010a\u0001\u0000\u0000\u0000M\u010c\u0001"+
		"\u0000\u0000\u0000O\u010f\u0001\u0000\u0000\u0000Q\u0112\u0001\u0000\u0000"+
		"\u0000S\u011a\u0001\u0000\u0000\u0000U\u011f\u0001\u0000\u0000\u0000W"+
		"\u012a\u0001\u0000\u0000\u0000Y\u0136\u0001\u0000\u0000\u0000[\u013b\u0001"+
		"\u0000\u0000\u0000]\u0141\u0001\u0000\u0000\u0000_\u014c\u0001\u0000\u0000"+
		"\u0000ab\u0005r\u0000\u0000bc\u0005e\u0000\u0000cd\u0005t\u0000\u0000"+
		"de\u0005u\u0000\u0000ef\u0005r\u0000\u0000fg\u0005n\u0000\u0000g\u0002"+
		"\u0001\u0000\u0000\u0000hi\u0005c\u0000\u0000ij\u0005o\u0000\u0000jk\u0005"+
		"n\u0000\u0000kl\u0005t\u0000\u0000lm\u0005i\u0000\u0000mn\u0005n\u0000"+
		"\u0000no\u0005u\u0000\u0000op\u0005e\u0000\u0000p\u0004\u0001\u0000\u0000"+
		"\u0000qr\u0005b\u0000\u0000rs\u0005r\u0000\u0000st\u0005e\u0000\u0000"+
		"tu\u0005a\u0000\u0000uv\u0005k\u0000\u0000v\u0006\u0001\u0000\u0000\u0000"+
		"wx\u0005v\u0000\u0000xy\u0005a\u0000\u0000yz\u0005r\u0000\u0000z\b\u0001"+
		"\u0000\u0000\u0000{|\u0005a\u0000\u0000|}\u0005n\u0000\u0000}~\u0005d"+
		"\u0000\u0000~\n\u0001\u0000\u0000\u0000\u007f\u0080\u0005o\u0000\u0000"+
		"\u0080\u0081\u0005r\u0000\u0000\u0081\f\u0001\u0000\u0000\u0000\u0082"+
		"\u0083\u0005n\u0000\u0000\u0083\u0084\u0005o\u0000\u0000\u0084\u0085\u0005"+
		"t\u0000\u0000\u0085\u000e\u0001\u0000\u0000\u0000\u0086\u0087\u0005d\u0000"+
		"\u0000\u0087\u0088\u0005a\u0000\u0000\u0088\u0089\u0005t\u0000\u0000\u0089"+
		"\u008a\u0005a\u0000\u0000\u008a\u008b\u0005s\u0000\u0000\u008b\u008c\u0005"+
		"e\u0000\u0000\u008c\u008d\u0005t\u0000\u0000\u008d\u0010\u0001\u0000\u0000"+
		"\u0000\u008e\u008f\u0005o\u0000\u0000\u008f\u0090\u0005p\u0000\u0000\u0090"+
		"\u0091\u0005t\u0000\u0000\u0091\u0092\u0005i\u0000\u0000\u0092\u0093\u0005"+
		"m\u0000\u0000\u0093\u0094\u0005i\u0000\u0000\u0094\u0095\u0005z\u0000"+
		"\u0000\u0095\u0096\u0005e\u0000\u0000\u0096\u0097\u0005r\u0000\u0000\u0097"+
		"\u0012\u0001\u0000\u0000\u0000\u0098\u0099\u0005i\u0000\u0000\u0099\u009a"+
		"\u0005n\u0000\u0000\u009a\u009b\u0005p\u0000\u0000\u009b\u009c\u0005u"+
		"\u0000\u0000\u009c\u009d\u0005t\u0000\u0000\u009d\u009e\u0005L\u0000\u0000"+
		"\u009e\u009f\u0005a\u0000\u0000\u009f\u00a0\u0005y\u0000\u0000\u00a0\u00a1"+
		"\u0005e\u0000\u0000\u00a1\u00a2\u0005r\u0000\u0000\u00a2\u0014\u0001\u0000"+
		"\u0000\u0000\u00a3\u00a4\u0005h\u0000\u0000\u00a4\u00a5\u0005i\u0000\u0000"+
		"\u00a5\u00a6\u0005d\u0000\u0000\u00a6\u00a7\u0005d\u0000\u0000\u00a7\u00a8"+
		"\u0005e\u0000\u0000\u00a8\u00a9\u0005n\u0000\u0000\u00a9\u00aa\u0005L"+
		"\u0000\u0000\u00aa\u00ab\u0005a\u0000\u0000\u00ab\u00ac\u0005y\u0000\u0000"+
		"\u00ac\u00ad\u0005e\u0000\u0000\u00ad\u00ae\u0005r\u0000\u0000\u00ae\u0016"+
		"\u0001\u0000\u0000\u0000\u00af\u00b0\u0005o\u0000\u0000\u00b0\u00b1\u0005"+
		"u\u0000\u0000\u00b1\u00b2\u0005t\u0000\u0000\u00b2\u00b3\u0005p\u0000"+
		"\u0000\u00b3\u00b4\u0005u\u0000\u0000\u00b4\u00b5\u0005t\u0000\u0000\u00b5"+
		"\u00b6\u0005L\u0000\u0000\u00b6\u00b7\u0005a\u0000\u0000\u00b7\u00b8\u0005"+
		"y\u0000\u0000\u00b8\u00b9\u0005e\u0000\u0000\u00b9\u00ba\u0005r\u0000"+
		"\u0000\u00ba\u0018\u0001\u0000\u0000\u0000\u00bb\u00bc\u0005n\u0000\u0000"+
		"\u00bc\u00bd\u0005e\u0000\u0000\u00bd\u00be\u0005t\u0000\u0000\u00be\u00bf"+
		"\u0005w\u0000\u0000\u00bf\u00c0\u0005o\u0000\u0000\u00c0\u00c1\u0005r"+
		"\u0000\u0000\u00c1\u00c2\u0005k\u0000\u0000\u00c2\u001a\u0001\u0000\u0000"+
		"\u0000\u00c3\u00c4\u0005i\u0000\u0000\u00c4\u00c5\u0005f\u0000\u0000\u00c5"+
		"\u001c\u0001\u0000\u0000\u0000\u00c6\u00c7\u0005e\u0000\u0000\u00c7\u00c8"+
		"\u0005l\u0000\u0000\u00c8\u00c9\u0005i\u0000\u0000\u00c9\u00ca\u0005f"+
		"\u0000\u0000\u00ca\u001e\u0001\u0000\u0000\u0000\u00cb\u00cc\u0005e\u0000"+
		"\u0000\u00cc\u00cd\u0005l\u0000\u0000\u00cd\u00ce\u0005s\u0000\u0000\u00ce"+
		"\u00cf\u0005e\u0000\u0000\u00cf \u0001\u0000\u0000\u0000\u00d0\u00d1\u0005"+
		"f\u0000\u0000\u00d1\u00d2\u0005o\u0000\u0000\u00d2\u00d3\u0005r\u0000"+
		"\u0000\u00d3\"\u0001\u0000\u0000\u0000\u00d4\u00d5\u0005w\u0000\u0000"+
		"\u00d5\u00d6\u0005h\u0000\u0000\u00d6\u00d7\u0005i\u0000\u0000\u00d7\u00d8"+
		"\u0005l\u0000\u0000\u00d8\u00d9\u0005e\u0000\u0000\u00d9$\u0001\u0000"+
		"\u0000\u0000\u00da\u00db\u0005d\u0000\u0000\u00db\u00dc\u0005o\u0000\u0000"+
		"\u00dc&\u0001\u0000\u0000\u0000\u00dd\u00de\u0005f\u0000\u0000\u00de\u00df"+
		"\u0005u\u0000\u0000\u00df\u00e0\u0005n\u0000\u0000\u00e0\u00e1\u0005c"+
		"\u0000\u0000\u00e1\u00e2\u0005t\u0000\u0000\u00e2\u00e3\u0005i\u0000\u0000"+
		"\u00e3\u00e4\u0005o\u0000\u0000\u00e4\u00e5\u0005n\u0000\u0000\u00e5("+
		"\u0001\u0000\u0000\u0000\u00e6\u00e7\u0005+\u0000\u0000\u00e7*\u0001\u0000"+
		"\u0000\u0000\u00e8\u00e9\u0005-\u0000\u0000\u00e9,\u0001\u0000\u0000\u0000"+
		"\u00ea\u00eb\u0005*\u0000\u0000\u00eb.\u0001\u0000\u0000\u0000\u00ec\u00ed"+
		"\u0005/\u0000\u0000\u00ed0\u0001\u0000\u0000\u0000\u00ee\u00ef\u0005%"+
		"\u0000\u0000\u00ef2\u0001\u0000\u0000\u0000\u00f0\u00f1\u0005^\u0000\u0000"+
		"\u00f14\u0001\u0000\u0000\u0000\u00f2\u00f3\u0005=\u0000\u0000\u00f36"+
		"\u0001\u0000\u0000\u0000\u00f4\u00f5\u0005(\u0000\u0000\u00f58\u0001\u0000"+
		"\u0000\u0000\u00f6\u00f7\u0005)\u0000\u0000\u00f7:\u0001\u0000\u0000\u0000"+
		"\u00f8\u00f9\u0005[\u0000\u0000\u00f9<\u0001\u0000\u0000\u0000\u00fa\u00fb"+
		"\u0005]\u0000\u0000\u00fb>\u0001\u0000\u0000\u0000\u00fc\u00fd\u0005{"+
		"\u0000\u0000\u00fd@\u0001\u0000\u0000\u0000\u00fe\u00ff\u0005}\u0000\u0000"+
		"\u00ffB\u0001\u0000\u0000\u0000\u0100\u0101\u0005,\u0000\u0000\u0101D"+
		"\u0001\u0000\u0000\u0000\u0102\u0103\u0005=\u0000\u0000\u0103\u0104\u0005"+
		"=\u0000\u0000\u0104F\u0001\u0000\u0000\u0000\u0105\u0106\u0005!\u0000"+
		"\u0000\u0106\u0107\u0005=\u0000\u0000\u0107H\u0001\u0000\u0000\u0000\u0108"+
		"\u0109\u0005<\u0000\u0000\u0109J\u0001\u0000\u0000\u0000\u010a\u010b\u0005"+
		">\u0000\u0000\u010bL\u0001\u0000\u0000\u0000\u010c\u010d\u0005<\u0000"+
		"\u0000\u010d\u010e\u0005=\u0000\u0000\u010eN\u0001\u0000\u0000\u0000\u010f"+
		"\u0110\u0005>\u0000\u0000\u0110\u0111\u0005=\u0000\u0000\u0111P\u0001"+
		"\u0000\u0000\u0000\u0112\u0116\u0007\u0000\u0000\u0000\u0113\u0115\u0007"+
		"\u0001\u0000\u0000\u0114\u0113\u0001\u0000\u0000\u0000\u0115\u0118\u0001"+
		"\u0000\u0000\u0000\u0116\u0114\u0001\u0000\u0000\u0000\u0116\u0117\u0001"+
		"\u0000\u0000\u0000\u0117R\u0001\u0000\u0000\u0000\u0118\u0116\u0001\u0000"+
		"\u0000\u0000\u0119\u011b\u0007\u0002\u0000\u0000\u011a\u0119\u0001\u0000"+
		"\u0000\u0000\u011b\u011c\u0001\u0000\u0000\u0000\u011c\u011a\u0001\u0000"+
		"\u0000\u0000\u011c\u011d\u0001\u0000\u0000\u0000\u011dT\u0001\u0000\u0000"+
		"\u0000\u011e\u0120\u0007\u0002\u0000\u0000\u011f\u011e\u0001\u0000\u0000"+
		"\u0000\u0120\u0121\u0001\u0000\u0000\u0000\u0121\u011f\u0001\u0000\u0000"+
		"\u0000\u0121\u0122\u0001\u0000\u0000\u0000\u0122\u0123\u0001\u0000\u0000"+
		"\u0000\u0123\u0127\u0005.\u0000\u0000\u0124\u0126\u0007\u0002\u0000\u0000"+
		"\u0125\u0124\u0001\u0000\u0000\u0000\u0126\u0129\u0001\u0000\u0000\u0000"+
		"\u0127\u0125\u0001\u0000\u0000\u0000\u0127\u0128\u0001\u0000\u0000\u0000"+
		"\u0128V\u0001\u0000\u0000\u0000\u0129\u0127\u0001\u0000\u0000\u0000\u012a"+
		"\u0130\u0005\"\u0000\u0000\u012b\u012f\b\u0003\u0000\u0000\u012c\u012d"+
		"\u0005\\\u0000\u0000\u012d\u012f\u0005\"\u0000\u0000\u012e\u012b\u0001"+
		"\u0000\u0000\u0000\u012e\u012c\u0001\u0000\u0000\u0000\u012f\u0132\u0001"+
		"\u0000\u0000\u0000\u0130\u012e\u0001\u0000\u0000\u0000\u0130\u0131\u0001"+
		"\u0000\u0000\u0000\u0131\u0133\u0001\u0000\u0000\u0000\u0132\u0130\u0001"+
		"\u0000\u0000\u0000\u0133\u0134\u0005\"\u0000\u0000\u0134X\u0001\u0000"+
		"\u0000\u0000\u0135\u0137\u0007\u0004\u0000\u0000\u0136\u0135\u0001\u0000"+
		"\u0000\u0000\u0137\u0138\u0001\u0000\u0000\u0000\u0138\u0136\u0001\u0000"+
		"\u0000\u0000\u0138\u0139\u0001\u0000\u0000\u0000\u0139Z\u0001\u0000\u0000"+
		"\u0000\u013a\u013c\u0007\u0005\u0000\u0000\u013b\u013a\u0001\u0000\u0000"+
		"\u0000\u013c\u013d\u0001\u0000\u0000\u0000\u013d\u013b\u0001\u0000\u0000"+
		"\u0000\u013d\u013e\u0001\u0000\u0000\u0000\u013e\u013f\u0001\u0000\u0000"+
		"\u0000\u013f\u0140\u0006-\u0000\u0000\u0140\\\u0001\u0000\u0000\u0000"+
		"\u0141\u0142\u0005/\u0000\u0000\u0142\u0143\u0005/\u0000\u0000\u0143\u0147"+
		"\u0001\u0000\u0000\u0000\u0144\u0146\b\u0004\u0000\u0000\u0145\u0144\u0001"+
		"\u0000\u0000\u0000\u0146\u0149\u0001\u0000\u0000\u0000\u0147\u0145\u0001"+
		"\u0000\u0000\u0000\u0147\u0148\u0001\u0000\u0000\u0000\u0148\u014a\u0001"+
		"\u0000\u0000\u0000\u0149\u0147\u0001\u0000\u0000\u0000\u014a\u014b\u0006"+
		".\u0000\u0000\u014b^\u0001\u0000\u0000\u0000\u014c\u014d\u0005/\u0000"+
		"\u0000\u014d\u014e\u0005*\u0000\u0000\u014e\u0152\u0001\u0000\u0000\u0000"+
		"\u014f\u0151\t\u0000\u0000\u0000\u0150\u014f\u0001\u0000\u0000\u0000\u0151"+
		"\u0154\u0001\u0000\u0000\u0000\u0152\u0153\u0001\u0000\u0000\u0000\u0152"+
		"\u0150\u0001\u0000\u0000\u0000\u0153\u0155\u0001\u0000\u0000\u0000\u0154"+
		"\u0152\u0001\u0000\u0000\u0000\u0155\u0156\u0005*\u0000\u0000\u0156\u0157"+
		"\u0005/\u0000\u0000\u0157\u0158\u0001\u0000\u0000\u0000\u0158\u0159\u0006"+
		"/\u0000\u0000\u0159`\u0001\u0000\u0000\u0000\u000b\u0000\u0116\u011c\u0121"+
		"\u0127\u012e\u0130\u0138\u013d\u0147\u0152\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}