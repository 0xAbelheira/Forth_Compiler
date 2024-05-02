
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "COMMENT_END COMMENT_START DO DOT DOTSTRING ELSE EMIT FUNC_END FUNC_START GEQUAL ID IF LEQUAL LOOP NUMBER STRING THEN VARIABLEComandos : Comandos ComandoComandos : Comando : ExpressaoComando : ImprimeComando : CommentComando : StoreComando : VariavelComando : ConditionalExpressao : Expressao '+'Expressao : Expressao '-'Expressao : Expressao '*'Expressao : Expressao '/'Expressao : Expressao '%'Expressao : TermoTermo : NUMBERTermo : UnstoreImprime : Expressao DOTImprime : DOTSTRINGComment : COMMENT_START Comandos COMMENT_ENDStore : ID '!'Unstore : ID '@'Variavel : VARIABLE IDConditional : '=' IF Comandos THENConditional : '<' IF Comandos THENConditional : '>' IF Comandos THENConditional : LEQUAL IF Comandos THENConditional : GEQUAL IF Comandos THENConditional : '=' IF Comandos ELSE Comandos THENConditional : '<' IF Comandos ELSE Comandos THENConditional : '>' IF Comandos ELSE Comandos THENConditional : LEQUAL IF Comandos ELSE Comandos THENConditional : GEQUAL IF Comandos ELSE Comandos THEN"
    
_lr_action_items = {'DOTSTRING':([0,1,2,3,4,5,6,7,8,9,10,11,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,],[-2,10,-1,-3,-4,-5,-6,-7,-8,-14,-18,-2,-15,-16,-9,-10,-11,-12,-13,-17,10,-20,-21,-22,-2,-2,-2,-2,-2,-19,10,10,10,10,10,-23,-2,-24,-2,-25,-2,-26,-2,-27,-2,10,10,10,10,10,-28,-29,-30,-31,-32,]),'COMMENT_START':([0,1,2,3,4,5,6,7,8,9,10,11,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,],[-2,11,-1,-3,-4,-5,-6,-7,-8,-14,-18,-2,-15,-16,-9,-10,-11,-12,-13,-17,11,-20,-21,-22,-2,-2,-2,-2,-2,-19,11,11,11,11,11,-23,-2,-24,-2,-25,-2,-26,-2,-27,-2,11,11,11,11,11,-28,-29,-30,-31,-32,]),'ID':([0,1,2,3,4,5,6,7,8,9,10,11,13,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,],[-2,12,-1,-3,-4,-5,-6,-7,-8,-14,-18,-2,30,-15,-16,-9,-10,-11,-12,-13,-17,12,-20,-21,-22,-2,-2,-2,-2,-2,-19,12,12,12,12,12,-23,-2,-24,-2,-25,-2,-26,-2,-27,-2,12,12,12,12,12,-28,-29,-30,-31,-32,]),'VARIABLE':([0,1,2,3,4,5,6,7,8,9,10,11,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,],[-2,13,-1,-3,-4,-5,-6,-7,-8,-14,-18,-2,-15,-16,-9,-10,-11,-12,-13,-17,13,-20,-21,-22,-2,-2,-2,-2,-2,-19,13,13,13,13,13,-23,-2,-24,-2,-25,-2,-26,-2,-27,-2,13,13,13,13,13,-28,-29,-30,-31,-32,]),'=':([0,1,2,3,4,5,6,7,8,9,10,11,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,],[-2,14,-1,-3,-4,-5,-6,-7,-8,-14,-18,-2,-15,-16,-9,-10,-11,-12,-13,-17,14,-20,-21,-22,-2,-2,-2,-2,-2,-19,14,14,14,14,14,-23,-2,-24,-2,-25,-2,-26,-2,-27,-2,14,14,14,14,14,-28,-29,-30,-31,-32,]),'<':([0,1,2,3,4,5,6,7,8,9,10,11,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,],[-2,15,-1,-3,-4,-5,-6,-7,-8,-14,-18,-2,-15,-16,-9,-10,-11,-12,-13,-17,15,-20,-21,-22,-2,-2,-2,-2,-2,-19,15,15,15,15,15,-23,-2,-24,-2,-25,-2,-26,-2,-27,-2,15,15,15,15,15,-28,-29,-30,-31,-32,]),'>':([0,1,2,3,4,5,6,7,8,9,10,11,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,],[-2,16,-1,-3,-4,-5,-6,-7,-8,-14,-18,-2,-15,-16,-9,-10,-11,-12,-13,-17,16,-20,-21,-22,-2,-2,-2,-2,-2,-19,16,16,16,16,16,-23,-2,-24,-2,-25,-2,-26,-2,-27,-2,16,16,16,16,16,-28,-29,-30,-31,-32,]),'LEQUAL':([0,1,2,3,4,5,6,7,8,9,10,11,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,],[-2,17,-1,-3,-4,-5,-6,-7,-8,-14,-18,-2,-15,-16,-9,-10,-11,-12,-13,-17,17,-20,-21,-22,-2,-2,-2,-2,-2,-19,17,17,17,17,17,-23,-2,-24,-2,-25,-2,-26,-2,-27,-2,17,17,17,17,17,-28,-29,-30,-31,-32,]),'GEQUAL':([0,1,2,3,4,5,6,7,8,9,10,11,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,],[-2,18,-1,-3,-4,-5,-6,-7,-8,-14,-18,-2,-15,-16,-9,-10,-11,-12,-13,-17,18,-20,-21,-22,-2,-2,-2,-2,-2,-19,18,18,18,18,18,-23,-2,-24,-2,-25,-2,-26,-2,-27,-2,18,18,18,18,18,-28,-29,-30,-31,-32,]),'NUMBER':([0,1,2,3,4,5,6,7,8,9,10,11,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,],[-2,19,-1,-3,-4,-5,-6,-7,-8,-14,-18,-2,-15,-16,-9,-10,-11,-12,-13,-17,19,-20,-21,-22,-2,-2,-2,-2,-2,-19,19,19,19,19,19,-23,-2,-24,-2,-25,-2,-26,-2,-27,-2,19,19,19,19,19,-28,-29,-30,-31,-32,]),'$end':([0,1,2,3,4,5,6,7,8,9,10,19,20,21,22,23,24,25,26,28,29,30,36,42,44,46,48,50,57,58,59,60,61,],[-2,0,-1,-3,-4,-5,-6,-7,-8,-14,-18,-15,-16,-9,-10,-11,-12,-13,-17,-20,-21,-22,-19,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,]),'COMMENT_END':([2,3,4,5,6,7,8,9,10,11,19,20,21,22,23,24,25,26,27,28,29,30,36,42,44,46,48,50,57,58,59,60,61,],[-1,-3,-4,-5,-6,-7,-8,-14,-18,-2,-15,-16,-9,-10,-11,-12,-13,-17,36,-20,-21,-22,-19,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,]),'THEN':([2,3,4,5,6,7,8,9,10,19,20,21,22,23,24,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,],[-1,-3,-4,-5,-6,-7,-8,-14,-18,-15,-16,-9,-10,-11,-12,-13,-17,-20,-21,-22,-2,-2,-2,-2,-2,-19,42,44,46,48,50,-23,-2,-24,-2,-25,-2,-26,-2,-27,-2,57,58,59,60,61,-28,-29,-30,-31,-32,]),'ELSE':([2,3,4,5,6,7,8,9,10,19,20,21,22,23,24,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,46,48,50,57,58,59,60,61,],[-1,-3,-4,-5,-6,-7,-8,-14,-18,-15,-16,-9,-10,-11,-12,-13,-17,-20,-21,-22,-2,-2,-2,-2,-2,-19,43,45,47,49,51,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,]),'+':([3,9,19,20,21,22,23,24,25,29,],[21,-14,-15,-16,-9,-10,-11,-12,-13,-21,]),'-':([3,9,19,20,21,22,23,24,25,29,],[22,-14,-15,-16,-9,-10,-11,-12,-13,-21,]),'*':([3,9,19,20,21,22,23,24,25,29,],[23,-14,-15,-16,-9,-10,-11,-12,-13,-21,]),'/':([3,9,19,20,21,22,23,24,25,29,],[24,-14,-15,-16,-9,-10,-11,-12,-13,-21,]),'%':([3,9,19,20,21,22,23,24,25,29,],[25,-14,-15,-16,-9,-10,-11,-12,-13,-21,]),'DOT':([3,9,19,20,21,22,23,24,25,29,],[26,-14,-15,-16,-9,-10,-11,-12,-13,-21,]),'!':([12,],[28,]),'@':([12,],[29,]),'IF':([14,15,16,17,18,],[31,32,33,34,35,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Comandos':([0,11,31,32,33,34,35,43,45,47,49,51,],[1,27,37,38,39,40,41,52,53,54,55,56,]),'Comando':([1,27,37,38,39,40,41,52,53,54,55,56,],[2,2,2,2,2,2,2,2,2,2,2,2,]),'Expressao':([1,27,37,38,39,40,41,52,53,54,55,56,],[3,3,3,3,3,3,3,3,3,3,3,3,]),'Imprime':([1,27,37,38,39,40,41,52,53,54,55,56,],[4,4,4,4,4,4,4,4,4,4,4,4,]),'Comment':([1,27,37,38,39,40,41,52,53,54,55,56,],[5,5,5,5,5,5,5,5,5,5,5,5,]),'Store':([1,27,37,38,39,40,41,52,53,54,55,56,],[6,6,6,6,6,6,6,6,6,6,6,6,]),'Variavel':([1,27,37,38,39,40,41,52,53,54,55,56,],[7,7,7,7,7,7,7,7,7,7,7,7,]),'Conditional':([1,27,37,38,39,40,41,52,53,54,55,56,],[8,8,8,8,8,8,8,8,8,8,8,8,]),'Termo':([1,27,37,38,39,40,41,52,53,54,55,56,],[9,9,9,9,9,9,9,9,9,9,9,9,]),'Unstore':([1,27,37,38,39,40,41,52,53,54,55,56,],[20,20,20,20,20,20,20,20,20,20,20,20,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Comandos","S'",1,None,None,None),
  ('Comandos -> Comandos Comando','Comandos',2,'p_Comandos1','yacc.py',27),
  ('Comandos -> <empty>','Comandos',0,'p_Comandos2','yacc.py',31),
  ('Comando -> Expressao','Comando',1,'p_Comando1','yacc.py',35),
  ('Comando -> Imprime','Comando',1,'p_Comando2','yacc.py',39),
  ('Comando -> Comment','Comando',1,'p_Comando3','yacc.py',43),
  ('Comando -> Store','Comando',1,'p_Comando4','yacc.py',47),
  ('Comando -> Variavel','Comando',1,'p_Comando5','yacc.py',51),
  ('Comando -> Conditional','Comando',1,'p_Comando6','yacc.py',55),
  ('Expressao -> Expressao +','Expressao',2,'p_Expressao1','yacc.py',59),
  ('Expressao -> Expressao -','Expressao',2,'p_Expressao2','yacc.py',63),
  ('Expressao -> Expressao *','Expressao',2,'p_Expressao3','yacc.py',67),
  ('Expressao -> Expressao /','Expressao',2,'p_Expressao4','yacc.py',71),
  ('Expressao -> Expressao %','Expressao',2,'p_Expressao5','yacc.py',75),
  ('Expressao -> Termo','Expressao',1,'p_Expressao6','yacc.py',79),
  ('Termo -> NUMBER','Termo',1,'p_Termo','yacc.py',83),
  ('Termo -> Unstore','Termo',1,'p_Termo2','yacc.py',88),
  ('Imprime -> Expressao DOT','Imprime',2,'p_Expressao_Print','yacc.py',92),
  ('Imprime -> DOTSTRING','Imprime',1,'p_Expressao_Print2','yacc.py',96),
  ('Comment -> COMMENT_START Comandos COMMENT_END','Comment',3,'p_Comment','yacc.py',100),
  ('Store -> ID !','Store',2,'p_Store','yacc.py',104),
  ('Unstore -> ID @','Unstore',2,'p_Unstore','yacc.py',116),
  ('Variavel -> VARIABLE ID','Variavel',2,'p_Variavel','yacc.py',124),
  ('Conditional -> = IF Comandos THEN','Conditional',4,'p_Conditional1','yacc.py',129),
  ('Conditional -> < IF Comandos THEN','Conditional',4,'p_Conditional2','yacc.py',133),
  ('Conditional -> > IF Comandos THEN','Conditional',4,'p_Conditional3','yacc.py',137),
  ('Conditional -> LEQUAL IF Comandos THEN','Conditional',4,'p_Conditional4','yacc.py',141),
  ('Conditional -> GEQUAL IF Comandos THEN','Conditional',4,'p_Conditional5','yacc.py',145),
  ('Conditional -> = IF Comandos ELSE Comandos THEN','Conditional',6,'p_Conditional6','yacc.py',149),
  ('Conditional -> < IF Comandos ELSE Comandos THEN','Conditional',6,'p_Conditional7','yacc.py',153),
  ('Conditional -> > IF Comandos ELSE Comandos THEN','Conditional',6,'p_Conditional8','yacc.py',157),
  ('Conditional -> LEQUAL IF Comandos ELSE Comandos THEN','Conditional',6,'p_Conditional9','yacc.py',161),
  ('Conditional -> GEQUAL IF Comandos ELSE Comandos THEN','Conditional',6,'p_Conditional10','yacc.py',165),
]
