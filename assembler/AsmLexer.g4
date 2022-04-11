lexer grammar AsmLexer;

Asect : 'asect' ;
Break : 'break' ;
Continue : 'continue' ;
Do : 'do' ;
Else : 'else' ;
End : 'end' ;
Ext : 'ext' ;
Fi : 'fi' ;
Goto : 'goto' ;
If : 'if' ;
Is : 'is' ;
Macro : 'macro' ;
Restore : 'restore' ;
Rsect : 'rsect' ;
Save : 'save' ;
Stays : 'stays' ;
Then : 'then' ;
Tplate : 'tplate' ;
Until : 'until' ;
Wend : 'wend' ;
While : 'while' ;

DOT : '.' ;
COMMA : ',' ;
MINUS : '-' ;
COLON : ':' ;
ASTERISK : '*' ;
ANGLE_BRACKET : '>' ;

REGISTER : 'r'[0-3] ;
WORD : [a-zA-Z_][a-zA-Z_0-9]* ;
DECIMAL_NUMBER : [0-9]+  ;
BINARY_NUMBER : '0b'[01]+ ;
HEX_NUMBER : '0x'[0-9a-fA-F]+ ;
STRING : '"'~["\\\n]*(('\\'.)~["\\\n]*)*'"' ;
CHAR : '\'' ('\\'. | ~[\\'\n]) '\'' ;

NEWLINE : '\r'? '\n' ;
COMMENT : '#'~[\n]* -> skip ;
WS : (' ' | '\t') -> skip ;
