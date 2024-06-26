
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "COMMENT_END COMMENT_START DO DOT DOTSTRING DROP DUP ELSE EMIT FUNC_END FUNC_START ID IF INFEQ LOOP MLOOP MOD NUMBER NUMBERF ONELINE ROT STRING SUPEQ SWAP THEN VARIABLEComandos : Comandos ComandoComandos : Comando : ExpressaoComando : ImprimeComando : CommentComando : StoreComando : VariavelComando : ConditionalComando : LoopComando : FuncComando : FuncPExpressao : Expressao '+'Expressao : Expressao '-'Expressao : Expressao '*'Expressao : Expressao '/'Expressao : Expressao MODExpressao : Expressao '>'Expressao : Expressao SUPEQExpressao : Expressao '<'Expressao : Expressao INFEQExpressao : Expressao '='Expressao : TermoTermo : NUMBERTermo : UnstoreImprime : DOTImprime : DOTSTRINGImprime : EMITComment : COMMENT_START COMMENT_ENDComment : ONELINEStore : ID '!'Unstore : ID '@'Variavel : VARIABLE IDConditional : Expressao IF Comandos THENConditional : Expressao IF Comandos ELSE Comandos THENLoop : Expressao DO Comandos LOOPLoop : Expressao DO Comandos Expressao MLOOPFunc : FUNC_START ID Comandos FUNC_ENDFunc : IDFuncP : ROTFuncP : DROPFuncP : DUPFuncP : SWAP"
    
_lr_action_items = {'DOT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,],[-2,13,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-22,-25,-26,-27,-29,-38,-39,-40,-41,-42,-23,-24,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-2,-2,-28,-30,-31,-32,-2,13,13,13,-33,-2,-3,-35,-37,13,-36,-34,]),'DOTSTRING':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,],[-2,14,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-22,-25,-26,-27,-29,-38,-39,-40,-41,-42,-23,-24,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-2,-2,-28,-30,-31,-32,-2,14,14,14,-33,-2,-3,-35,-37,14,-36,-34,]),'EMIT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,],[-2,15,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-22,-25,-26,-27,-29,-38,-39,-40,-41,-42,-23,-24,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-2,-2,-28,-30,-31,-32,-2,15,15,15,-33,-2,-3,-35,-37,15,-36,-34,]),'COMMENT_START':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,],[-2,16,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-22,-25,-26,-27,-29,-38,-39,-40,-41,-42,-23,-24,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-2,-2,-28,-30,-31,-32,-2,16,16,16,-33,-2,-3,-35,-37,16,-36,-34,]),'ONELINE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,],[-2,17,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-22,-25,-26,-27,-29,-38,-39,-40,-41,-42,-23,-24,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-2,-2,-28,-30,-31,-32,-2,17,17,17,-33,-2,-3,-35,-37,17,-36,-34,]),'ID':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,],[-2,18,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-22,-25,-26,-27,-29,-38,42,43,-39,-40,-41,-42,-23,-24,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-2,-2,-28,-30,-31,-32,-2,18,18,18,-33,-2,-3,-35,-37,18,-36,-34,]),'VARIABLE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,],[-2,19,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-22,-25,-26,-27,-29,-38,-39,-40,-41,-42,-23,-24,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-2,-2,-28,-30,-31,-32,-2,19,19,19,-33,-2,-3,-35,-37,19,-36,-34,]),'FUNC_START':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,],[-2,20,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-22,-25,-26,-27,-29,-38,-39,-40,-41,-42,-23,-24,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-2,-2,-28,-30,-31,-32,-2,20,20,20,-33,-2,-3,-35,-37,20,-36,-34,]),'ROT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,],[-2,21,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-22,-25,-26,-27,-29,-38,-39,-40,-41,-42,-23,-24,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-2,-2,-28,-30,-31,-32,-2,21,21,21,-33,-2,-3,-35,-37,21,-36,-34,]),'DROP':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,],[-2,22,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-22,-25,-26,-27,-29,-38,-39,-40,-41,-42,-23,-24,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-2,-2,-28,-30,-31,-32,-2,22,22,22,-33,-2,-3,-35,-37,22,-36,-34,]),'DUP':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,],[-2,23,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-22,-25,-26,-27,-29,-38,-39,-40,-41,-42,-23,-24,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-2,-2,-28,-30,-31,-32,-2,23,23,23,-33,-2,-3,-35,-37,23,-36,-34,]),'SWAP':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,],[-2,24,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-22,-25,-26,-27,-29,-38,-39,-40,-41,-42,-23,-24,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-2,-2,-28,-30,-31,-32,-2,24,24,24,-33,-2,-3,-35,-37,24,-36,-34,]),'NUMBER':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,],[-2,25,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-22,-25,-26,-27,-29,-38,-39,-40,-41,-42,-23,-24,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-2,-2,-28,-30,-31,-32,-2,25,25,25,-33,-2,-3,-35,-37,25,-36,-34,]),'$end':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,39,40,41,42,47,50,51,53,54,],[-2,0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-22,-25,-26,-27,-29,-38,-39,-40,-41,-42,-23,-24,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-28,-30,-31,-32,-33,-35,-37,-36,-34,]),'THEN':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,39,40,41,42,44,47,48,50,51,52,53,54,],[-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-22,-25,-26,-27,-29,-38,-39,-40,-41,-42,-23,-24,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-2,-28,-30,-31,-32,47,-33,-2,-35,-37,54,-36,-34,]),'ELSE':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,39,40,41,42,44,47,50,51,53,54,],[-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-22,-25,-26,-27,-29,-38,-39,-40,-41,-42,-23,-24,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-2,-28,-30,-31,-32,48,-33,-35,-37,-36,-34,]),'LOOP':([2,4,5,6,7,8,9,10,11,12,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,39,40,41,42,45,47,49,50,51,53,54,],[-1,-4,-5,-6,-7,-8,-9,-10,-11,-22,-25,-26,-27,-29,-38,-39,-40,-41,-42,-23,-24,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-2,-28,-30,-31,-32,50,-33,-3,-35,-37,-36,-34,]),'FUNC_END':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,39,40,41,42,43,46,47,50,51,53,54,],[-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-22,-25,-26,-27,-29,-38,-39,-40,-41,-42,-23,-24,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-28,-30,-31,-32,-2,51,-33,-35,-37,-36,-34,]),'+':([3,12,25,26,27,28,29,30,31,32,33,34,35,36,41,49,],[27,-22,-23,-24,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-31,27,]),'-':([3,12,25,26,27,28,29,30,31,32,33,34,35,36,41,49,],[28,-22,-23,-24,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-31,28,]),'*':([3,12,25,26,27,28,29,30,31,32,33,34,35,36,41,49,],[29,-22,-23,-24,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-31,29,]),'/':([3,12,25,26,27,28,29,30,31,32,33,34,35,36,41,49,],[30,-22,-23,-24,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-31,30,]),'MOD':([3,12,25,26,27,28,29,30,31,32,33,34,35,36,41,49,],[31,-22,-23,-24,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-31,31,]),'>':([3,12,25,26,27,28,29,30,31,32,33,34,35,36,41,49,],[32,-22,-23,-24,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-31,32,]),'SUPEQ':([3,12,25,26,27,28,29,30,31,32,33,34,35,36,41,49,],[33,-22,-23,-24,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-31,33,]),'<':([3,12,25,26,27,28,29,30,31,32,33,34,35,36,41,49,],[34,-22,-23,-24,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-31,34,]),'INFEQ':([3,12,25,26,27,28,29,30,31,32,33,34,35,36,41,49,],[35,-22,-23,-24,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-31,35,]),'=':([3,12,25,26,27,28,29,30,31,32,33,34,35,36,41,49,],[36,-22,-23,-24,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-31,36,]),'IF':([3,12,25,26,27,28,29,30,31,32,33,34,35,36,41,49,],[37,-22,-23,-24,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-31,37,]),'DO':([3,12,25,26,27,28,29,30,31,32,33,34,35,36,41,49,],[38,-22,-23,-24,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-31,38,]),'MLOOP':([12,25,26,27,28,29,30,31,32,33,34,35,36,41,49,],[-22,-23,-24,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-31,53,]),'COMMENT_END':([16,],[39,]),'!':([18,],[40,]),'@':([18,],[41,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Comandos':([0,37,38,43,48,],[1,44,45,46,52,]),'Comando':([1,44,45,46,52,],[2,2,2,2,2,]),'Expressao':([1,44,45,46,52,],[3,3,49,3,3,]),'Imprime':([1,44,45,46,52,],[4,4,4,4,4,]),'Comment':([1,44,45,46,52,],[5,5,5,5,5,]),'Store':([1,44,45,46,52,],[6,6,6,6,6,]),'Variavel':([1,44,45,46,52,],[7,7,7,7,7,]),'Conditional':([1,44,45,46,52,],[8,8,8,8,8,]),'Loop':([1,44,45,46,52,],[9,9,9,9,9,]),'Func':([1,44,45,46,52,],[10,10,10,10,10,]),'FuncP':([1,44,45,46,52,],[11,11,11,11,11,]),'Termo':([1,44,45,46,52,],[12,12,12,12,12,]),'Unstore':([1,44,45,46,52,],[26,26,26,26,26,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Comandos","S'",1,None,None,None),
  ('Comandos -> Comandos Comando','Comandos',2,'p_Comandos1','yacc.py',36),
  ('Comandos -> <empty>','Comandos',0,'p_Comandos2','yacc.py',40),
  ('Comando -> Expressao','Comando',1,'p_Comando1','yacc.py',44),
  ('Comando -> Imprime','Comando',1,'p_Comando2','yacc.py',48),
  ('Comando -> Comment','Comando',1,'p_Comando3','yacc.py',52),
  ('Comando -> Store','Comando',1,'p_Comando4','yacc.py',56),
  ('Comando -> Variavel','Comando',1,'p_Comando5','yacc.py',60),
  ('Comando -> Conditional','Comando',1,'p_Comando6','yacc.py',64),
  ('Comando -> Loop','Comando',1,'p_Comando7','yacc.py',68),
  ('Comando -> Func','Comando',1,'p_Comando8','yacc.py',72),
  ('Comando -> FuncP','Comando',1,'p_Comando9','yacc.py',76),
  ('Expressao -> Expressao +','Expressao',2,'p_Expressao1','yacc.py',80),
  ('Expressao -> Expressao -','Expressao',2,'p_Expressao2','yacc.py',84),
  ('Expressao -> Expressao *','Expressao',2,'p_Expressao3','yacc.py',88),
  ('Expressao -> Expressao /','Expressao',2,'p_Expressao4','yacc.py',92),
  ('Expressao -> Expressao MOD','Expressao',2,'p_Expressao5','yacc.py',96),
  ('Expressao -> Expressao >','Expressao',2,'p_Expressao6','yacc.py',100),
  ('Expressao -> Expressao SUPEQ','Expressao',2,'p_Expressao7','yacc.py',104),
  ('Expressao -> Expressao <','Expressao',2,'p_Expressao8','yacc.py',108),
  ('Expressao -> Expressao INFEQ','Expressao',2,'p_Expressao9','yacc.py',112),
  ('Expressao -> Expressao =','Expressao',2,'p_Expressao10','yacc.py',116),
  ('Expressao -> Termo','Expressao',1,'p_Expressao11','yacc.py',120),
  ('Termo -> NUMBER','Termo',1,'p_Termo','yacc.py',124),
  ('Termo -> Unstore','Termo',1,'p_Termo2','yacc.py',128),
  ('Imprime -> DOT','Imprime',1,'p_Expressao_Print','yacc.py',132),
  ('Imprime -> DOTSTRING','Imprime',1,'p_Expressao_Print2','yacc.py',136),
  ('Imprime -> EMIT','Imprime',1,'p_Expressao_Print3','yacc.py',140),
  ('Comment -> COMMENT_START COMMENT_END','Comment',2,'p_Comment','yacc.py',144),
  ('Comment -> ONELINE','Comment',1,'p_Comment2','yacc.py',148),
  ('Store -> ID !','Store',2,'p_Store','yacc.py',152),
  ('Unstore -> ID @','Unstore',2,'p_Unstore','yacc.py',156),
  ('Variavel -> VARIABLE ID','Variavel',2,'p_Variavel','yacc.py',161),
  ('Conditional -> Expressao IF Comandos THEN','Conditional',4,'p_Conditional1','yacc.py',168),
  ('Conditional -> Expressao IF Comandos ELSE Comandos THEN','Conditional',6,'p_Conditional2','yacc.py',173),
  ('Loop -> Expressao DO Comandos LOOP','Loop',4,'p_Loop','yacc.py',178),
  ('Loop -> Expressao DO Comandos Expressao MLOOP','Loop',5,'p_Loop2','yacc.py',185),
  ('Func -> FUNC_START ID Comandos FUNC_END','Func',4,'p_Func','yacc.py',192),
  ('Func -> ID','Func',1,'p_Func2','yacc.py',198),
  ('FuncP -> ROT','FuncP',1,'p_FuncP','yacc.py',202),
  ('FuncP -> DROP','FuncP',1,'p_FuncP2','yacc.py',208),
  ('FuncP -> DUP','FuncP',1,'p_FuncP3','yacc.py',214),
  ('FuncP -> SWAP','FuncP',1,'p_FuncP4','yacc.py',218),
]
