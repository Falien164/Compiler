// dodawanie, odejmowanie, mnożenie, dzielenie - działa dodawanie stringów - tworzenie tablic z int
// albo REAL - printowanie poszczególnych elementów tablicy - zmiana poszczególnych elementów
// tablicy -

grammar Hello;

start: (statement? NEWLINE)* EOF;

// Statement list
statement:
	printf # stat
	//	| scanf	 # stat
	| assign # stat;

// Statements
printf: STD_OUT expression;
//scanf : STD_IN ID;
assign: ID ASSIGN expression;

// Key words
STD_OUT: 'print';
//STD_IN : 'read' ;
ASSIGN: '=';

expression: value # primary_expression | expr1 ADD expr1 # add;

expr1: expr2 # single1 | expr2 SUB expr2 # sub;

expr2: expr3 # single2 | expr3 MUL expr3 # mul;

expr3: value # single3 | value DIV value # div;
//expr4: '-'? number | number ;

value:
	INT				# int //negative expressions
	| REAL			# real
	| TOINT value	# toint
	| TOREAL value	# toreal
	| ID			# id_number;

// array: '<' value (',' value)* '>';

// value: expression | word | array | number;

// Possible values
word: ID # id | STRING # string;

// address: '&' existingID;

// existingID: ID; variable name
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
WS: [ \t]+ -> skip; // skip white chars
LINE_COMMENT: '#' ~[\r\n]* -> skip;

//number : INT | TOINT number | TOREAL number | REAL | array | '(' number ')' ; expr: number
// op=('*'|'/') number # MulDiv | number op=('+'|'-') number # AddSub ;
