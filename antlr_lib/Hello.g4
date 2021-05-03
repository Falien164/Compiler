// dodawanie, odejmowanie, mnożenie, dzielenie - działa dodawanie stringów - tworzenie tablic z int
// albo REAL - printowanie poszczególnych elementów tablicy - zmiana poszczególnych elementów
// tablicy -
// 
//
// 
//
// 
//
// 
//

grammar Hello;

start: (stat? NEWLINE)* EOF;

// Statement list
stat:
	printf
	//	| scanf	
	| assign;

// Statements
printf: STD_OUT value;
//scanf : STD_IN ID;
assign: ID ASSIGN value;

// Key words
STD_OUT: 'print';
//STD_IN : 'read' ;
ASSIGN: '=';

expr0: expr1 # single0 | expr1 ADD expr1 # add;

expr1: expr2 # single1 | expr2 SUB expr2 # sub;

expr2: expr3 # single2 | expr3 MUL expr3 # mul;

expr3: number # single3 | number DIV number # div;
//expr4: '-'? number | number ;

number:
	INT				# int //negative expressions
	| REAL			# real
	| TOINT number	# toint
	| TOREAL number	# toreal
	| '(' expr0 ')'	# par
	| ID			# id_number;

array: '<' value (',' value)* '>';

value: word | array | expr0 | number;

// Possible values
word: ID # id | STRING # string;

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
UINT: [0-9]+;
INT: '-'? UINT;
REAL: INT '.' UINT;
NEWLINE: '\r'? '\n';
STRING: '"' ( ~('\\' | '"'))* '"';

// other
WS: [ \t]+ -> skip; // skip white chars
LINE_COMMENT: '#' ~[\r\n]* -> skip;

//number : INT | TOINT number | TOREAL number | REAL | array | '(' number ')' ; expr: number
// op=('*'|'/') number # MulDiv | number op=('+'|'-') number # AddSub ;
