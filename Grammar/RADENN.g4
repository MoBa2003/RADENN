grammar RADENN;

start: program EOF;
program: statements;

statements: (NEWLINE | SEMICOLON)* statement ((NEWLINE | SEMICOLON)+ statement)* (NEWLINE | SEMICOLON)*;

statement
    : 'return' expr?
    | 'continue'
    | 'break'
    | expr
    ;

expr
    : 'var' IDENTIFIER EQ expr
    | compExpr (('and' | 'or') compExpr)*
    ;

compExpr
    : '@' compExpr
    | arithExpr ((EE | NE | LT | GT | LTE | GTE) arithExpr)*
    ;

arithExpr
    : term ((PLUS | MINUS) term)*
    ;

term
    : factor ((MUL | DIV | MOD) factor)*
    ;

factor
    : (PLUS | MINUS) factor
    | power
    ;

power
    : call (POW factor)*
    ;

call
    : atom (LPAREN (expr (COMMA expr)*)? RPAREN)?
    ;

atom
    : INT
    | FLOAT
    | STR
    | IDENTIFIER
    | LPAREN expr RPAREN
    | listExpr
    | matExpr
    | datasetExpr
    | optimizerExpr
    | inputLayerExpr
    | hiddenLayerExpr
    | outputLayerExpr
    | networkExpr
    | ifExpr
    | forExpr
    | whileExpr
    | doWhileExpr
    | funcDef
    ;

listExpr
    : LSQUARE (expr (COMMA expr)*)? RSQUARE
    ;

matExpr
    : LROUND (matRow (COMMA matRow)*)? RROUND
    ;

matRow
    : LROUND expr (COMMA expr)* RROUND
    ;

datasetExpr
    : 'dataset' LPAREN expr COMMA expr RPAREN
    ;

optimizerExpr
    : 'optimizer' LPAREN expr COMMA expr RPAREN
    ;

inputLayerExpr
    : 'inputLayer' LPAREN expr COMMA expr COMMA expr COMMA expr COMMA expr COMMA expr RPAREN
    ;

hiddenLayerExpr
    : 'hiddenLayer' LPAREN expr COMMA expr COMMA expr COMMA expr COMMA expr RPAREN
    ;

outputLayerExpr
    : 'outputLayer' LPAREN expr COMMA expr COMMA expr RPAREN
    ;

networkExpr
    : 'network' LPAREN expr (COMMA expr)* COMMA expr RPAREN
    ;

ifExpr
    : 'if' expr (NEWLINE* (statement | LROUND NEWLINE* statements NEWLINE* RROUND) (elifExpr | elseExpr)?)
    ;

elifExpr
    : 'elif' expr (NEWLINE* (statement |LROUND NEWLINE* statements NEWLINE* RROUND) (elifExpr | elseExpr)?)
    ;

elseExpr
    : 'else' (NEWLINE* (statement | LROUND NEWLINE* statements NEWLINE* RROUND))
    ;


forExpr
    : 'for' LPAREN IDENTIFIER COMMA expr COMMA expr (COMMA expr)? RPAREN (NEWLINE* (statement | LROUND NEWLINE* statements NEWLINE* RROUND))
    ;

whileExpr
    : 'while' expr (NEWLINE* (statement | LROUND NEWLINE* statements NEWLINE* RROUND))
    ;

doWhileExpr
    : 'do' (NEWLINE* (statement | LROUND NEWLINE* statements NEWLINE* RROUND)) 'while' expr
    ;

funcDef
    : 'function' IDENTIFIER? LPAREN (IDENTIFIER (COMMA IDENTIFIER)*)? RPAREN (NEWLINE* (statement | LROUND NEWLINE* statements NEWLINE* RROUND))
    ;

INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STR: '"' .*? '"';
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

NOT: 'not';

EQ: '=';
PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
MOD: '%';
POW: '^';

EE: '==';
NE: '!=';
LT: '<';
GT: '>';
LTE: '<=';
GTE: '>=';

AND: '&&';
OR: '||';

COMMA: ',';
SEMICOLON: ';';
LPAREN: '(';
RPAREN: ')';
LSQUARE: '[';
RSQUARE: ']';
LROUND: '{';
RROUND: '}';

NEWLINE: '\r'? '\n';
WS: [ \r\t]+ -> skip;

// Single-line comments
COMMENT: '#' ~[\r\n]* -> skip;