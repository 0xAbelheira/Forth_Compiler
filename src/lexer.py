#   Copyright 2023  Hugo Abelheira, João Carvalho
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
from ply import lex

states = (
    ('comment', 'exclusive'),
    ('function', 'exclusive')
)

tokens = (
    'FUNC_START',
    'FUNC_END',
    'NUMBER',
    'NUMBERF',
    'VARIABLE',
    'ID',
    'IF',
    'THEN',
    'ELSE',
    'DO',
    'LOOP',
    'EMIT',
    'DOT',
    'SUPEQ',
    'INFEQ',
    'DOTSTRING',
    'STRING',
    'COMMENT_START',
    'COMMENT_END',
    'ONELINE',
    'MLOOP',
    'ROT',
    'DROP',
    'DUP',
    'SWAP',
    'MOD',
)

literals = '+-*/!@><='

def t_ANY_ONELINE(t):
    r'\\\s[^\n]*'
    pass

def t_MLOOP(t):
    r'\+LOOP\b'
    return t

def t_FUNC_START(t):
    r':'
    t.lexer.begin('function')
    return t

def t_function_FUNC_END(t):
    r';'
    t.lexer.begin('INITIAL')
    return t

def t_EMIT(t):
    r'\bEMIT\b'
    return t

def t_NUMBER(t):
    r'-?\d+'
    t.value = int(t.value)
    return t

def t_NUMBERF(t):
    r'-?\d+\.\d+'
    t.value = float(t.value)
    return t

def t_VARIABLE(t):
    r'VARIABLE'
    return t

def t_IF(t):
    r'\bIF\b'
    return t

def t_THEN(t):
    r'\bTHEN\b'
    return t

def t_ELSE(t):
    r'\bELSE\b'
    return t

def t_DO(t):
    r'\bDO\b'
    return t

def t_LOOP(t):
    r'\bLOOP\b'
    return t

def t_ROT(t):
    r'\bROT\b'
    return t

def t_DROP(t):
    r'\bDROP\b'
    return t

def t_DUP(t):
    r'\bDUP\b'
    return t

def t_SWAP(t):
    r'\bSWAP\b'
    return t

def t_MOD(t):
    r'\bMOD\b'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_DOTSTRING(t):
    r'\."\s[^"]*? "'
    t.value = t.value[2:-1]
    return t

def t_DOT(t):
    r'\.'
    return t

def t_SUPEQ(t):
    r'>='
    return t

def t_INFEQ(t):
    r'<='
    return t

def t_STRING(t):
    r'"\s[^"]*? "'
    t.value = t.value[1:-1]
    return t

# NO ESTADO FUNCTION

def t_function_NUMBER(t):
    r'-?\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_function_VARIABLE(t):
    r'\bVARIABLE\b'
    return t

def t_function_IF(t):
    r'\bIF\b'
    return t

def t_function_THEN(t):
    r'\bTHEN\b'
    return t

def t_function_ELSE(t):
    r'\bELSE\b'
    return t

def t_function_DO(t):
    r'\bDO\b'
    return t

def t_function_LOOP(t):
    r'\bLOOP\b'
    return t

def t_function_EMIT(t):
    r'\bEMIT\b'
    return t

def t_function_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_function_DOTSTRING(t):
    r'\."\s[^"]*? "'
    t.value = t.value[2:-1]
    return t

def t_function_DOT(t):
    r'\.'
    return t

def t_function_GEQUAL(t):
    r'>='
    return t

def t_function_LEQUAL(t):
    r'<='
    return t

def t_function_STRING(t):
    r'"\s[^"]*? "'
    t.value = t.value[1:-1]  
    return t

def t_function_COMMENT_START(t):
    r'\('
    t.lexer.begin('comment')
    return t

def t_function_COMMENT_END(t):
    r'\)'
    return t

def t_COMMENT_START(t):
    r'\('
    t.lexer.begin('comment')
    return None

# Comment state functions
def t_comment_TEXT(t):
    r'[^)]+'
    pass

def t_comment_COMMENT_END(t):
    r'\)'
    t.lexer.begin('INITIAL')
    return None

# Common rules
t_ANY_ignore = ' \n\r\t'

def t_ANY_error(t):
    print(f"Illegal Character: {t.value[0]}")
    t.lexer.skip(1)

def t_ANY_lineno(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

lexer = lex.lex()

lexer.begin('INITIAL')

# Testing the lexer

def debug_lexer(exemplo):
    lexer.input(exemplo)
    tokens = [] 

    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok) 

    return tokens

input_file_path = 'input.txt'
output_file_path = 'tokenizer.txt'

tokenizer = "Tokens read:\n"

with open(input_file_path, 'r') as file:
    for line in file:
        parsed_line = debug_lexer(line.strip())
        tokenizer += '\n'.join(str(tok) for tok in parsed_line) + '\n' 

with open(output_file_path, 'w') as file:
    file.write(tokenizer)
