grammar Larisha;

program: line* EOF;

line: statement | ifBlock | whileBlock | break ';'| functionDefinition | functionCall ';' | returnStatement ';' ;

statement: ( assignment ) ';';

assignment: IDENTIFIER '=' expression;

ifBlock: 'if' ('(' expression ')'| expression ) block ('else' elseIfBlock);

elseIfBlock: ifBlock | block;

whileBlock: WHILE ('(' expression ')' | expression ) block;

WHILE: 'while';

functionDefinition: FUNCTION IDENTIFIER '(' parameters? ')' block;

functionCall: IDENTIFIER '(' arguments? ')' ;

arguments: expression (',' expression)*;
FUNCTION: 'fun';
parameters: IDENTIFIER (',' IDENTIFIER)*;

expression
    : constant                      #constantExpression
    | IDENTIFIER                #identifierExpression
    | '(' expression ')'        #parenthesizedExpression
    | '!' expression            #notExpression
    | '-' expression            #negativeExpression
    | expression multOp expression  #multiplicativeExpression
    | expression addOp expression   #additiveExpression
    | expression compreOp expression #comparativeExpression
    | expression boolOp expression #booleanExpression 
    | functionCall              #functionCallExpression
    ;


multOp: '*' | '/' | '%';
addOp: '+' | '-';
compreOp: '<' | '>' | '<=' | '>=' | '==' | '!=';
boolOp: '&&' | '||';


constant: INTEGER | FLOAT | STRING | BOOL | CHAR;

BOOL: 'true' | 'false';
STRING: '"'( ~'"')*'"';
FLOAT: [0-9]+ '.' [0-9]+;
INTEGER: [0-9]+;
CHAR: '\'' (.|'\\'.) '\'';

block: '{' (line)* '}';
break: 'break';
returnStatement: 'return' expression;

WS: [ \t\n\r]+ -> skip;
COMMENT: '/*' .*? '*/' -> skip;

LINE_COMMENT: '//' ~[\r\n]* -> skip;
IDENTIFIER: ([a-zA-Z_][a-zA-Z0-9_]*)+('.'([a-zA-Z_][a-zA-Z0-9_]*))*;
