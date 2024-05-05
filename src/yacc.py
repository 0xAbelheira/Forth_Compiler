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
contador = -1 # para tratar o endereçamento de variáveis
label_counter = -1 # to generate unique labels for conditionals
contadorA = 0

def print_state():
    print(f"Variables: {variable_store}")
    print()

def generate_label():
    global label_counter
    label_counter += 1
    return label_counter

def p_Comandos1(t):
    "Comandos : Comandos Comando"
    global contadorA, contador
    t[0] = t[1] + t[2]
    contador+=contadorA
    contadorA = 0

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
    
def p_Expressao1(t):
    "Expressao : Expressao '+'"
    global contadorA
    t[0] = f'{t[1]}add\n'
    contadorA -= 1

def p_Expressao2(t):
    "Expressao : Expressao '-'"
    global contadorA
    t[0] = f'{t[1]}sub\n'
    contadorA -= 1

def p_Expressao3(t):
    "Expressao : Expressao '*'"
    global contadorA
    t[0] = f'{t[1]}mul\n'
    contadorA -= 1

def p_Expressao4(t):
    "Expressao : Expressao '/'"
    global contadorA
    t[0] = f'{t[1]}div\n'
    contadorA -= 1

def p_Expressao5(t):
    "Expressao : Expressao '%'"
    global contadorA
    t[0] = f'{t[1]}mod\n'
    contadorA -= 1

def p_Expressao6(t):
    "Expressao : Termo"
    global contadorA
    t[0] = t[1]
    contadorA += 1

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

def p_Comment(t):
    "Comment : COMMENT_START Comandos COMMENT_END"
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
    t[0] = f'pushi 0\n'
    contador -= 1

def p_Conditional1(t):
    "Conditional : '=' IF Comandos THEN"
    label = generate_label()
    t[0] = f'equal\njz ENDIF{label}\n{t[3]}\njump ENDIF{label}\nENDIF{label}:\n'
    
def p_Conditional2(t):
    "Conditional : '<' IF Comandos THEN"
    label = generate_label()
    t[0] = f'inf\njz ENDIF{label}\n{t[3]}\njump ENDIF{label}\nENDIF{label}:\n'
    
def p_Conditional3(t):
    "Conditional : '>' IF Comandos THEN"
    label = generate_label()
    t[0] = f'sup\njz ENDIF{label}\n{t[3]}\njump ENDIF{label}\nENDIF{label}:\n'
    
def p_Conditional4(t):
    "Conditional : INFEQ IF Comandos THEN" # mudar nome 
    label = generate_label()
    t[0] = f'infeq\njz ENDIF{label}\n{t[3]}\njump ENDIF{label}\nENDIF{label}:\n'
    
def p_Conditional5(t):
    "Conditional : SUPEQ IF Comandos THEN"
    label = generate_label()
    t[0] = f'supeq\njz ENDIF{label}\n{t[3]}\njump ENDIF{label}\nENDIF{label}:\n'
    
def p_Conditional6(t):
    "Conditional : '=' IF Comandos ELSE Comandos THEN"
    label = generate_label()
    t[0] = f'equal\njz ELSE{label}\n{t[3]}\njump ENDIF{label}\nELSE{label}:\n{t[5]}\njump ENDIF{label}\nENDIF{label}:\n'
    
def p_Conditional7(t):
    "Conditional : '<' IF Comandos ELSE Comandos THEN"
    label = generate_label()
    t[0] = f'inf\njz ELSE{label}\n{t[3]}\njump ENDIF{label}\nELSE{label}:\n{t[5]}\njump ENDIF{label}\nENDIF{label}:\n'
    
def p_Conditional8(t):
    "Conditional : '>' IF Comandos ELSE Comandos THEN"
    label = generate_label()
    t[0] = f'sup\njz ELSE{label}\n{t[3]}\njump ENDIF{label}\nELSE{label}:\n{t[5]}\njump ENDIF{label}\nENDIF{label}:\n'
    
def p_Conditional9(t):
    "Conditional : INFEQ IF Comandos ELSE Comandos THEN"
    label = generate_label()
    t[0] = f'infeq\njz ELSE{label}\n{t[3]}\njump ENDIF{label}\nELSE{label}:\n{t[5]}\njump ENDIF{label}\nENDIF{label}:\n'
    
def p_Conditional10(t):
    "Conditional : SUPEQ IF Comandos ELSE Comandos THEN"
    label = generate_label()
    t[0] = f'supeq\njz ELSE{label}\n{t[3]}\njump ENDIF{label}\nELSE{label}:\n{t[5]}\njump ENDIF{label}\nENDIF{label}:\n'

def p_Conditional11(t):
    "Conditional : Expressao IF Comandos THEN"
    global contador
    label = generate_label() 
    t[0] = f'{t[1]}\npushi 1\nequal\njz ENDIF{label}\n{t[3]}\njump ENDIF{label}\nENDIF{label}:\n'
    contador += 1
    
def p_Conditional12(t):
    "Conditional : Expressao IF Comandos ELSE Comandos THEN"
    global contador
    label = generate_label()
    t[0] = f'{t[1]}\npushi 1\nequal\njz ELSE{label}\n{t[3]}\njump ENDIF{label}\nELSE{label}:\n{t[5]}\njump ENDIF{label}\nENDIF{label}:\n'
    contador += 1
    
def p_Loop(t):
    "Loop : Expressao DO Comandos LOOP"
    global contador
    contador += 2
    t[0] = f'pushi 0\nswap\nstoreg {contador-4}\npushi 0\n{t[1]}storeg {contador-2}\n{t[3]}'
    

def p_error(t):
    print(f"Syntax error: {t.value}, {t.type}, {t}")

parser = yacc()

while True:
    ewvm = parser.parse(input("> "))
    print(ewvm)
    print_state()

"""def parse_program():
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
        print("\nProgram terminated!")"""