// dodawanie, odejmowanie, mnożenie, dzielenie - działa dodawanie stringów - tworzenie tablic z int
// albo REAL - printowanie poszczególnych elementów tablicy - zmiana poszczególnych elementów
// tablicy -

grammar Hello;

start: block EOF;
block: (stat? NEWLINE)*;
// Statement list
stat: printf | scanf | array_assign | assign | if_statement | while_stat;

// Statements
printf: STD_OUT value;
scanf: STD_IN ID;
array_assign: ID '[' expr ']' ASSIGN value;
assign: ID ASSIGN value;

// Key words
STD_OUT: 'print';
STD_IN: 'read';
ASSIGN: '=';

if_statement: IF condition_block (ELSE IF condition_block)* (ELSE stat_block)? ;

condition_block
	: expr jump_block;

jump_block: stat_block;

stat_block:
	'{' block '}'
	| stat
	;

while_stat
	: WHILE '(' expr ')' stat_block
	;

expr
	: expr op = (MUL | DIV) expr		# multiplicationExpr
	| expr op = (ADD | SUB) expr		# additiveExpr
 	| expr op=(LTEQ | GTEQ | LT | GT) expr #relationalExpr
 	| expr op=(EQ | NEQ) expr              #equalityExpr
 	| expr AND expr                        #andExpr
 	| expr OR expr                         #orExpr
	| atom								# atomExpr;

atom:
	INT						# int
	| REAL					# real
	| TOINT atom			# toint
	| TOREAL atom			# toreal
	| TOSTR atom 			# tostr
	| (TRUE | FALSE)		# booleanAtom
	| ID '[' expr ']'		# id_dereference
	| '(' expr ')'			# par
	| ID					# id
	| '{' (value ','?)* '}'	# array
	| STRING				# string;

value: expr;

// variable name
ID: [a-zA-Z][_0-9a-zA-Z]*;

// Math operations
ADD: '+';

MUL: '*';
SUB: '-';
DIV: '/';
TOINT: '(int)';
TOREAL: '(real)';
TOSTR: '(str)';

// data types
INT: '-'? UINT;
UINT: [0-9]+;
REAL: INT '.' UINT;
NEWLINE: '\r'? '\n';
STRING: '"' ( ~('\\' | '"'))* '"';


IF: 'if ';
ELSE: 'else ';
WHILE: 'while ';
TRUE: 'true ';
FALSE: 'false ';

OR: 'or ';
AND: 'and ';
EQ: '==';
NEQ: '!=';
GT: '>';
LT: '<';
GTEQ: '>=';
LTEQ: '<=';
NOT: '!';

// other
WS: [ \t]+ -> skip; // skip white chars
LINE_COMMENT: '#' ~[\r\n]* -> skip;
