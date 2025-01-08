grammar RADENN;

program
    : statements EOF
    ;

statements
    : NEWLINE* statement (NEWLINE+ statement)* NEWLINE*
    ;

statement
    : 'return' expr?  #returnStatement
    | 'continue'      #continueStatement
    | 'break'         #breakStatement
    | expr           #exprStatement
    ;

expr
    : 'var' IDENTIFIER '=' expr                    #varAssignment
    | compExpr (('and' | 'or') compExpr)*         #logicalExpr
    ;

compExpr
    : 'not' compExpr                              #notExpr
    | arithExpr ((EE|NE|LT|GT|LTE|GTE) arithExpr)* #comparisonExpr
    ;

arithExpr
    : term ((PLUS | MINUS) term)*
    ;

term
    : factor ((MUL | DIV | MOD) factor)*
    ;

factor
    : (PLUS|MINUS) factor
    | power
    ;

power
    : call (POW factor)*
    ;

call
    : atom (LPAREN (expr (COMMA expr)*)? RPAREN)?
    ;

atom
    : INT                                         #intAtom
    | FLOAT                                       #floatAtom
    | STRING                                      #stringAtom
    | IDENTIFIER                                  #identifierAtom
    | LPAREN expr RPAREN                         #parenExpr
    | listExpr                                   #listAtom
    | matExpr                                    #matrixAtom
    | datasetExpr                                #datasetAtom
    | optimizerExpr                              #optimizerAtom
    | inputLayerExpr                             #inputLayerAtom
    | hiddenLayerExpr                            #hiddenLayerAtom
    | outputLayerExpr                            #outputLayerAtom
    | networkExpr                                #networkAtom
    | ifExpr                                     #ifAtom
    | forExpr                                    #forAtom
    | whileExpr                                  #whileAtom
    | doWhileExpr                                #doWhileAtom
    | funcDef                                    #funcDefAtom
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
    : 'inputLayer' LPAREN expr (COMMA expr){5} RPAREN
    ;

hiddenLayerExpr
    : 'hiddenLayer' LPAREN expr (COMMA expr){4} RPAREN
    ;

outputLayerExpr
    : 'outputLayer' LPAREN expr COMMA expr RPAREN
    ;

networkExpr
    : 'network' LPAREN expr (COMMA expr)* COMMA expr RPAREN
    ;

ifExpr
    : 'if' expr (
        (NEWLINE* statement (elifExpr | elseExpr)?) |
        (LROUND NEWLINE statements (RROUND | elifExpr | elseExpr))
    )
    ;

elifExpr
    : 'elif' expr (
        (NEWLINE* statement (elifExpr | elseExpr)?) |
        (LROUND NEWLINE statements (RROUND | elifExpr | elseExpr))
    )
    ;

elseExpr
    : 'else' (
        NEWLINE* statement |
        (LROUND NEWLINE statements RROUND)
    )
    ;

forExpr
    : 'for' LPAREN IDENTIFIER COMMA expr COMMA expr (COMMA expr)? RPAREN 
      (NEWLINE* statement | (LROUND statements RROUND))
    ;

whileExpr
    : 'while' expr (NEWLINE* statement | (LROUND statements RROUND))
    ;

doWhileExpr
    : 'do' (NEWLINE* statement NEWLINE* | (LROUND statements RROUND)) 'while' expr
    ;

funcDef
    : 'function' IDENTIFIER? LPAREN (IDENTIFIER (COMMA IDENTIFIER)*)? RPAREN 
      (NEWLINE* statement | (LROUND statements RROUND))
    ;

// Lexer Rules
PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
MOD: '%';
POW: '^';
EQ: '=';
LPAREN: '(';
RPAREN: ')';
LSQUARE: '[';
RSQUARE: ']';
LROUND: '{';
RROUND: '}';
COMMA: ',';
EE: '==';
NE: '!=';
LT: '<';
GT: '>';
LTE: '<=';
GTE: '>=';

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]*;
STRING: '"' (~["\r\n] | '\\"')* '"';
NEWLINE: [\r\n]+;
WS: [ \t]+ -> skip;

// Skip comments
COMMENT: '//' ~[\r\n]* -> skip;
MULTILINE_COMMENT: '/*' .*? '*/' -> skip;


// by claude
// https://claude.ai/chat/f72f0ea0-3a87-4984-8135-b16ce0154726