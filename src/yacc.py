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


# ------------- Gramática --------------- #
# 
#   S -> Prompt $
#
#   Prompt -> Expressoes Prompt
#
#   Expressoes -> Expressao Expressoes
#               | Expressao
#
#   Expressao -> Words Expressao
#              | Exp Expressao 
#              | &
#
#   Exp -> Term opA Exp
#        | Term
#
#   Term -> Factor opM Term
#         | Factor
#
#   Factor -> PA Exp PF
#           | num
