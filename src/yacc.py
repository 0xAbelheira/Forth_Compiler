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

#ter um contador global para os storegs, e guardar num dicionario tipo o da variable store

variable_store = {}
contador = -1 # para tratar o endereçamento de variáveis
label_counter = -1 # to generate unique labels for conditionals

def print_state():
    print(f"s: {variable_store}")
    print()

def generate_label():
    global label_counter
    label_counter += 1
    return label_counter

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
    
def p_Comando7(t):
    "Comando : Loop"
    t[0] = t[1]
    
def p_Comando8(t):
    "Comando : Func"
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
    "Expressao : Expressao '>'"
    t[0] = f'{t[1]}sup\n'
    
def p_Expressao7(t):
    "Expressao : Expressao SUPEQ"
    t[0] = f'{t[1]}supeq\n'
    
def p_Expressao8(t):
    "Expressao : Expressao '<'"
    t[0] = f'{t[1]}inf\n'
    
def p_Expressao9(t):
    "Expressao : Expressao INFEQ"
    t[0] = f'{t[1]}infeq\n'
    
def p_Expressao10(t):
    "Expressao : Expressao '='"
    t[0] = f'{t[1]}equal\n'

def p_Expressao6(t):
    "Expressao : Termo"
    t[0] = t[1]

def p_Termo(t):
    "Termo : NUMBER"
    t[0] = f'pushi {int(t[1])}\n'

def p_Termo2(t):
    "Termo : Unstore"
    t[0] = t[1]

def p_Expressao_Print(t):
    "Imprime : DOT"
    t[0] = f'writei\n'

def p_Expressao_Print2(t):
    "Imprime : DOTSTRING"
    t[0] = f'pushs "{t[1]}"\nwrites\n'

def p_Expressao_Print3(t):
    "Imprime : EMIT"
    t[0] = f'writechr\n'

def p_Comment(t):
    "Comment : COMMENT_START COMMENT_END"
    t[0] = ""

def p_Comment2(t):
    "Comment : ONELINE"
    t[0] = ""

def p_Store(t): # guarda o ultimo valor na stack na variável 'ID'
    "Store : ID '!'"
    t[0] = f'storeg {variable_store.get(t[1], "Undefined Variable")}\n'

def p_Unstore(t): 
    "Unstore : ID '@'"
    value = variable_store.get(t[1], "Undefined Variable")
    t[0] = f'pushg {value}\n'

def p_Variavel(t):
    "Variavel : VARIABLE ID"
    global contador
    contador += 1
    variable_store[t[2]] = contador
    t[0] = f''

def p_Conditional1(t):
    "Conditional : Expressao IF Comandos THEN"
    label = generate_label()
    t[0] = f'jz ENDIF{label}\n{t[3]}\njump ENDIF{label}\nENDIF{label}:\n'
    
def p_Conditional2(t):
    "Conditional : Expressao IF Comandos ELSE Comandos THEN"
    label = generate_label()
    t[0] = f'{t[1]}jz ELSE{label}\n{t[3]}\njump ENDIF{label}\nELSE{label}:\n{t[5]}\njump ENDIF{label}\nENDIF{label}:\n'

def p_Loop(t):
    "Loop : Expressao DO Comandos LOOP"
    global contador
    label = generate_label()
    t[0] = f'storeg {contador+1}\n{t[1]}storeg {contador+2}\nWHILE{label}:\npushg {contador+1}\npushg {contador+2}\nsup\njz ENDWHILE{label}\n{t[3]}pushi 1\npushg {contador+2}\nadd\nstoreg {contador+2}\njump WHILE{label}\nENDWHILE{label}:\n'
    contador += 2

def p_Func(t):
    "Func : FUNC_START ID Comandos FUNC_END"
    t[0] = ""

# +Loop
#def p_Loop2(t):
#    "Loop : +LOOP"
#    global contador
#    label = generate_label()
#    t[0] = ""
#    contador += 2

def p_error(t):
    print(f"Syntax error: {t.value}, {t.type}, {t}")

parser = yacc()

input_file_path = 'input.txt'
output_file_path = 'output.txt'

ewvm_results = ''

with open(input_file_path, 'r') as file:
    for line in file:
        parsed_line = parser.parse(line.strip())
        ewvm_results += str(parsed_line)


ewvmFinal = f'start\n' + f'pushn {contador +1}\n'+ ewvm_results + f'stop'

with open(output_file_path, 'w') as file:
    file.write(ewvmFinal)



# se calhar no fim da execucao fazer um pushi contador e um popn