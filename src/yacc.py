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
from lexer import tokens
from ply.yacc import yacc


def p_Comandos1(t):
    "Comandos : Comandos Comando"
    t[0] = t[1] + t[2]

def p_Comandos2(t):
    "Comandos : "
    t[0] = ""

def p_Comando1(t):
    "Comando : Expressao"
    t[0] = t[1]

def p_Comando2(t):
    "Comando : Imprime"
    t[0] = t[1]

def p_Expressao1(t):
    "Expressao : Expressao Termo '+'"
    t[0] = f'{t[1]} {t[2]} add\n'

def p_Expressao2(t):
    "Expressao : Expressao Termo '-'"
    t[0] = f'{t[1]} {t[2]} sub\n'

def p_Expressao3(t):
    "Expressao : Expressao Termo '*'"
    t[0] = f'{t[1]} {t[2]} mul\n'

def p_Expressao4(t):
    "Expressao : Expressao Termo '/'"
    t[0] = f'{t[1]} {t[2]} div\n'

def p_Expressao5(t):
    "Expressao : Expressao Termo '%'"
    t[0] = f'{t[1]} {t[2]} mod\n'

def p_Expressao6(t):
    "Expressao : Termo"
    t[0] = t[1]

def p_Expressao_Print(t):
    "Imprime : Expressao DOT"
    t[0] = f'{t[1]} writei\n'

def p_Expressao_Print2(t):
    "Imprime : DOTSTRING"
    t[0] = f'pushs "{t[1]}"\n writes\n'

def p_Termo1(t):
    "Termo : NUMBER"
    t[0] = f'pushg {t[1]}\n'

#def p_Termo2(t):
#    "Termo : NUMBER DOT"
#   t[0]=f'pushg {t[1]}\nwritei\n'

#def p_Imprime2(t): "Imprime : DOT STRING Comandos"; t[0] = 
#def p_Imprime3(t): "Imprime : NUMBER EMIT Comandos"; t[0] = 
#def p_Imprime4(t): "Imprime : "; t[0] = ''
#
#def p_Imprime1(t):
#    "Imprime : Expressao DOT"
#    t[0] = f'{t[1]} writei\n'  # Assuming 'writei' prints an integer
#
#def p_Imprime2(t):
#    "Imprime : DOT STRING Comandos"
#    t[0] = f'pushs "{t[2]}"\n writes\n'  # Assuming 'writes' prints a string
#
#def p_Imprime3(t):
#    "Imprime : "
#    t[0] = ''
#
#def p_Statement_if_then_else(t):
#    "Statement : Expressao IF Comandos ELSE Comandos THEN Comandos"
#    label_else = new_label()
#    label_end = new_label()
#    t[0] = (f'{t[1]} jz {label_else}\n'  # Evaluate expression and jump to else if zero
#            f'{t[3]}'                    # Commands to execute if condition is true
#            f'jump {label_end}\n'        # Jump to end after executing true branch
#            f'{label_else}:\n'
#            f'{t[5]}'                    # Commands to execute if condition is false
#            f'{label_end}:\n'
#            f'{t[7]}')                   # Commands after THEN
#
#
#def p_Statement_if_then(t):
#    "Statement : Expressao IF Comandos THEN Comandos"
#    label_end = new_label()
#    t[0] = (f'{t[1]} jz {label_end}\n'  # Evaluate expression and jump to end if zero
#            f'{t[3]}'                    # Commands to execute if condition is true
#            f'{label_end}:\n'
#            f'{t[5]}')                   # Commands after THEN
#
#
#def p_Store(t):
#    "Store : Termo ID '!'"
#    index = get_variable_index(t[2])
#    t[0] = f'{t[1]}storeg {index}\n'
#
#def p_UnStore(t):
#    "UnStore : ID '@'"
#    index = get_variable_index(t[1])
#    t[0] = f'pushg {index}\n'
#
#
#def p_Funcao(t):
#    "Funcao : FUNC_START ID Comandos FUNC_END"
#    start_label = f'func_{t[2]}'
#    end_label = f'end_{t[2]}'
#    t[0] = f'{start_label}:\n{t[3]} jump {end_label}\n{end_label}:\n'
#
#
#def p_Loop(t):
#    "Loop : Expressao Expressao DO ID Comandos LOOP"
#    start_label = new_label()
#    end_label = new_label()
#    t[0] = f'{start_label}:\n{t[1]} jz {end_label}\n{t[5]} jump {start_label}\n{end_label}:\n'
#
#
##def p_Comentario1(t): "Comentario : '(' Comandos ')'"; t[0] = 
#def p_Comentario2(t): "Comentario : '\' Comandos"; t[0] = 

def p_error(t):
    print(f"Syntax error: {t.value}, {t.type}, {t}")

parser = yacc()

while True:
    ewvm = parser.parse(input("> "))
    print(ewvm) 

def parse_program():
    print("Type your code (type 'END' on a new line to finish):")
    lines = []
    while True:
        line = input("> ")
        if line == 'END':
            break
        lines.append(line)
    code = "\n".join(lines)
    result = parser.parse(code)
    print("Generated VM Code:")
    print(result)

if __name__ == "__main__":
    try:
        parse_program()
    except KeyboardInterrupt:
        print("\nProgram terminated!")