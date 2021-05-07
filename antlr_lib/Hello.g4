// dodawanie, odejmowanie, mnożenie, dzielenie - działa dodawanie stringów - tworzenie tablic z int
// albo REAL - printowanie poszczególnych elementów tablicy - zmiana poszczególnych elementów
// tablicy -

grammar Hello;

start: block EOF;
block: (stat? NEWLINE)*;
// Statement list
stat: printf | scanf | array_assign | assign;

// Statements
printf: STD_OUT value;
scanf: STD_IN ID;
array_assign: ID '[' expr ']' ASSIGN value;
assign: ID ASSIGN value;

// Key words
STD_OUT: 'print';
STD_IN: 'read';
ASSIGN: '=';

expr:
	expr op = (MUL | DIV) expr		# multiplicationExpr
	| expr op = (ADD | SUB) expr	# additiveExpr
	| atom							# atomExpr;

atom:
	INT						# int
	| REAL					# real
	| TOINT atom			# toint
	| TOREAL atom			# toreal
	| '(' expr ')'			# par
	| ID '[' expr ']'		# id_dereference
	| ID					# id
	| '{' (value ','?)* '}'	# array
	| STRING				# string;
/*
 a[0] <- expression a = {1,2,3,4,5} {expr}
 */
//array: '<' value (',' value)* '>' ;

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

// data types
INT: '-'? UINT;
UINT: [0-9]+;
REAL: INT '.' UINT;
NEWLINE: '\r'? '\n';
STRING: '"' ( ~('\\' | '"'))* '"';

// other
WS: [ \t]+ -> skip;
// skip white chars
LINE_COMMENT: '#' ~[\r\n]* -> skip;
