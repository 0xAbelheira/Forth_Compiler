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
# Definição dos tokens

from ply import lex

states = (
    ('comment', 'exclusive'),
    ('function', 'inclusive')
)

tokens = (
    'FUNC_START',
    'FUNC_END',
    'NUMBER',
    'VARIABLE',
    'ID',
    'IF',
    'THEN',
    'ELSE',
    'DO',
    'LOOP',
    'EMIT',
    'DOT',
    'PRINT',
    'STRING',
    'STORE',
    'UNSTORE',
    'COMMENT_START',
    'COMMENT_END',
    'TEXT',
)

literals = '+-*/%'

# ESTADO INITIAL

def t_FUNC_START(t):
    r':'
    t.lexer.begin('function')
    return t

def t_function_FUNC_END(t):
    r';'
    t.lexer.begin('INITIAL')
    return t

def t_EMIT(t): # faz sentido capturar aqui o inteiro antes do EMIT? assim fazemos a conversao direta para ASCII
    r'\d{1,3}\s+EMIT'
    return t

def t_NUMBER(t):
    r'-?\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_VARIABLE(t):
    r'VARIABLE'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_IF(t):
    r'IF'
    return t

def t_THEN(t):
    r'THEN'
    return t

def t_ELSE(t):
    r'ELSE'
    return t

def t_DO(t):
    r'DO'
    return t

def t_LOOP(t):
    r'LOOP'
    return t


def t_DOT(t):
    r'\.'
    return t

def t_PRINT(t):
    r'\."\s*'
    return t

def t_STRING(t): # isto ta straight up errado chatgpt mal ve strings borra-se todo, este token nao tem nada a ver com string é para tratar o comando ." "
    r'"[^"]*"'
    t.value = t.value[1:-1]  # Remover as aspas
    return t

def t_STORE(t):
    r'!'
    return t

def t_UNSTORE(t):
    r'@'
    return t

def t_COMMENT_START(t):
    r'\('
    t.lexer.begin('comment')
    t.lexer.contador = 1
    return t

def t_COMMENT_END(t):
    r'\)'
    return t

# NO ESTADO FUNCTION

def t_function_NUMBER(t):
    r'-?\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_function_VARIABLE(t):
    r'VARIABLE'
    return t

def t_function_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_function_IF(t):
    r'IF'
    return t

def t_function_THEN(t):
    r'THEN'
    return t

def t_function_ELSE(t):
    r'ELSE'
    return t

def t_function_DO(t):
    r'DO'
    return t

def t_function_LOOP(t):
    r'LOOP'
    return t

def t_function_EMIT(t):
    r'\d{1,3}\s+EMIT'
    return t

def t_function_DOT(t):
    r'\.'
    return t

def t_function_PRINT(t):
    r'\."\s*'
    return t

def t_function_STRING(t): # isto ta straight up errado 
    r'"[^"]*"'
    t.value = t.value[1:-1]  # Remover as aspas
    return t

def t_function_STORE(t):
    r'!'
    return t

def t_function_UNSTORE(t):
    r'@'
    return t

def t_function_COMMENT_START(t):
    r'\('
    t.lexer.begin('comment')
    return t

def t_function_COMMENT_END(t):
    r'\)'
    return t

# NO ESTADO COMMENT

def t_comment_COMMENT_START(t):
    r'\('
    t.lexer.contador += 1
    return t

def t_comment_TEXT(t):
    r'\w+'
    return t

def t_comment_COMMENT_END(t):
    r'\)'
    t.lexer.contador -= 1
    if t.lexer.contador == 0:
        t.lexer.begin('INITIAL')
    return t

t_ANY_ignore = ' \n\r\t'

def t_ANY_error(t):
    print(f"Illegal Character: {t.value[0]}")
    t.lexer.skip(1)

def t_ANY_lineno(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

lexer = lex.lex()

lexer.begin('INITIAL')

try:
    while True:
        line = input("> Digite uma linha (Ctrl+C para sair):\n")

        # inserir a linha no lexer
        lexer.input(line)

        for token in lexer:
            print(token)
            
        print() # linha extra para cada comando

except KeyboardInterrupt:
    # Ctrl+c para sair
    print("\nPrograma terminado!")
