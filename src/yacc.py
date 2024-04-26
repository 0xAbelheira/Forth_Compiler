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

from lex import tokens
from ply.yacc import yacc
import sys
import math
import readline

def p_Z(t): "Z : Comandos Funcoes"; t[0] = 

def p_Funcoes1(t): "Funcoes : Funcoes Funcao"; t[0] = 
def p_Funcoes2(t): "Funcoes : "; t[0] = 

def p_Comandos1(t): "Comandos : Comandos Comando"; t[0] = 
def p_Comandos2(t): "Comandos : "; t[0] = 

def p_Comando1(t): "Comando : Expressao"; t[0] = 
def p_Comando2(t): "Comando : Variavel"; t[0] = 
def p_Comando3(t): "Comando : Imprime"; t[0] = 
def p_Comando4(t): "Comando : Statement"; t[0] = 
def p_Comando5(t): "Comando : Store"; t[0] = 
def p_Comando6(t): "Comando : UnStore"; t[0] = 
def p_Comando7(t): "Comando : Loop"; t[0] = 
def p_Comando8(t): "Comando : ID"; t[0] = 
def p_Comando9(t): "Comando : Comentario"; t[0] = 

def p_Expressao1(t): "Expressao : Expressao Termo '+'"; t[0] = 
def p_Expressao2(t): "Expressao : Expressao Termo '-'"; t[0] = 
def p_Expressao3(t): "Expressao : Expressao Termo '*'"; t[0] = 
def p_Expressao4(t): "Expressao : Expressao Termo '/'"; t[0] = 
def p_Expressao5(t): "Expressao : Expressao Termo '%'"; t[0] = 
def p_Expressao6(t): "Expressao : Termo"; t[0] = 

def p_Termo1(t): "Termo : NUMBER"; t[0] = 
def p_Termo2(t): "Termo : UnStore"; t[0] = 

def p_Imprime1(t): "Imprime : Expressao DOT"; t[0] = 
def p_Imprime2(t): "Imprime : DOT STRING Comandos"; t[0] = 
def p_Imprime3(t): "Imprime : NUMBER EMIT Comandos"; t[0] = 
def p_Imprime4(t): "Imprime : "; t[0] = 

def p_Statement1(t): "Statement : Expressao IF Comandos ELSE Comandos THEN Comandos"; t[0] = 
def p_Statement2(t): "Statement : Expressao IF Comandos THEN Comandos"; t[0] = 

def p_Variavel(t): "Variavel : VARIABLE ID"; t[0] = 

def p_Store(t): "Store : Termo ID '!'"; t[0] = 

def p_UnStore(t): "UnStore : ID '@'"; t[0] = 

def p_Funcao(t): "Funcao : FUNC_START ID Comandos FUNC_END"; t[0] = 

def p_Loop(t): "Loop : Expressao Expressao DO ID Comandos LOOP"; t[0] = 

def p_Comentario1(t): "Comentario : '(' Comandos ')'"; t[0] = 
def p_Comentario2(t): "Comentario : '\' Comandos"; t[0] = 

def p_error(t):
    print(f"Syntax error: {t.value}")

parser = yacc()

readline.parse_and_bind("tab: complete")

while line := input("> "):
    exp = parser.parse(line)
    
    print(exp)















