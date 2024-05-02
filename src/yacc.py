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

variable_store = {}
number_stack = []

def print_state():
    print(f"Stack: {number_stack}")
    print(f"Variables: {variable_store}")
    print()

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

def p_Comando3(t):
    "Comando : Comment"
    t[0] = t[1]

def p_Comando4(t):
    "Comando : Store"
    t[0] = t[1]

def p_Comando5(t):
    "Comando : Variavel"
    t[0] = t[1]

def p_Comando6(t):
    "Comando : Conditional"
    t[0] = t[1]
    
def p_Expressao1(t):
    "Expressao : Expressao '+'"
    t[0] = f'{t[1]}add\n'

def p_Expressao2(t):
    "Expressao : Expressao '-'"
    t[0] = f'{t[1]}sub\n'

def p_Expressao3(t):
    "Expressao : Expressao '*'"
    t[0] = f'{t[1]}mul\n'

def p_Expressao4(t):
    "Expressao : Expressao '/'"
    t[0] = f'{t[1]}div\n'

def p_Expressao5(t):
    "Expressao : Expressao '%'"
    t[0] = f'{t[1]}mod\n'

def p_Expressao6(t):
    "Expressao : Termo"
    t[0] = t[1]

def p_Termo(t):
    "Termo : NUMBER"
    number_stack.append(t[1])
    t[0] = f'pushg {t[1]}\n'

def p_Termo2(t):
    "Termo : Unstore"
    t[0] = t[1]

def p_Expressao_Print(t):
    "Imprime : Expressao DOT"
    t[0] = f'{t[1]}writei\n'

def p_Expressao_Print2(t):
    "Imprime : DOTSTRING"
    t[0] = f'pushs "{t[1]}"\nwrites\n'

def p_Comment(t):
    "Comment : COMMENT_START Comandos COMMENT_END"
    t[0] = ""

def p_Store(t): # guarda o ultimo valor na stack na variável 'ID'
    "Store : ID '!'"
    if t[1] in variable_store:
        if number_stack:
            last_number = number_stack.pop()
            variable_store[t[1]] = last_number
            t[0] = f'storeg {t[1]}\n'
        else:
            t[0] = 'Error: No number to store.\n'
    else:
        t[0] = f'Error: Variable {t[1]} does not exist.\n'

def p_Unstore(t): #
    "Unstore : ID '@'"
    value = variable_store.get(t[1], "Undefined Variable")
    if value == "Undefined Variable":
        t[0] = f'Error: {value}.\n'
    else:
        t[0] = f'pushg {value}\n'

def p_Variavel(t):
    "Variavel : VARIABLE ID"
    variable_store[t[2]] = 0
    t[0] = f'pushg 0\n'

def p_Conditional1(t):
    "Conditional : '=' IF Comandos THEN"
    t[0] = t[3]
    
def p_Conditional2(t):
    "Conditional : '<' IF Comandos THEN"
    t[0] = t[3]
    
def p_Conditional3(t):
    "Conditional : '>' IF Comandos THEN"
    t[0] = t[3]
    
def p_Conditional4(t):
    "Conditional : LEQUAL IF Comandos THEN"
    t[0] = t[3]
    
def p_Conditional5(t):
    "Conditional : GEQUAL IF Comandos THEN"
    t[0] = t[3]
    
def p_Conditional6(t):
    "Conditional : '=' IF Comandos ELSE Comandos THEN"
    t[0] = t[3]
    
def p_Conditional7(t):
    "Conditional : '<' IF Comandos ELSE Comandos THEN"
    t[0] = t[3]
    
def p_Conditional8(t):
    "Conditional : '>' IF Comandos ELSE Comandos THEN"
    t[0] = t[3]
    
def p_Conditional9(t):
    "Conditional : LEQUAL IF Comandos ELSE Comandos THEN"
    t[0] = t[3]
    
def p_Conditional10(t):
    "Conditional : GEQUAL IF Comandos ELSE Comandos THEN"
    t[0] = t[3]

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
    print_state()

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