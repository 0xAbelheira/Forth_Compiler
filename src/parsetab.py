
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "COMMENT_END COMMENT_START DO DOT DOTSTRING ELSE EMIT FUNC_END FUNC_START ID IF LOOP NUMBER STRING THEN VARIABLEComandos : Comandos ComandoComandos : Comando : ExpressaoComando : ImprimeComando : CommentExpressao : Expressao '+'Expressao : Expressao '-'Expressao : Expressao '*'Expressao : Expressao '/'Expressao : Expressao '%'Expressao : NUMBERImprime : Expressao DOTImprime : DOTSTRINGComment : COMMENT_START Comandos COMMENT_END"
    
_lr_action_items = {'NUMBER':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,],[-2,6,-1,-3,-4,-5,-11,-13,-2,-6,-7,-8,-9,-10,-12,6,-14,]),'DOTSTRING':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,],[-2,7,-1,-3,-4,-5,-11,-13,-2,-6,-7,-8,-9,-10,-12,7,-14,]),'COMMENT_START':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,],[-2,8,-1,-3,-4,-5,-11,-13,-2,-6,-7,-8,-9,-10,-12,8,-14,]),'$end':([0,1,2,3,4,5,6,7,9,10,11,12,13,14,16,],[-2,0,-1,-3,-4,-5,-11,-13,-6,-7,-8,-9,-10,-12,-14,]),'COMMENT_END':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,],[-1,-3,-4,-5,-11,-13,-2,-6,-7,-8,-9,-10,-12,16,-14,]),'+':([3,6,9,10,11,12,13,],[9,-11,-6,-7,-8,-9,-10,]),'-':([3,6,9,10,11,12,13,],[10,-11,-6,-7,-8,-9,-10,]),'*':([3,6,9,10,11,12,13,],[11,-11,-6,-7,-8,-9,-10,]),'/':([3,6,9,10,11,12,13,],[12,-11,-6,-7,-8,-9,-10,]),'%':([3,6,9,10,11,12,13,],[13,-11,-6,-7,-8,-9,-10,]),'DOT':([3,6,9,10,11,12,13,],[14,-11,-6,-7,-8,-9,-10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Comandos':([0,8,],[1,15,]),'Comando':([1,15,],[2,2,]),'Expressao':([1,15,],[3,3,]),'Imprime':([1,15,],[4,4,]),'Comment':([1,15,],[5,5,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Comandos","S'",1,None,None,None),
  ('Comandos -> Comandos Comando','Comandos',2,'p_Comandos1','yacc.py',19),
  ('Comandos -> <empty>','Comandos',0,'p_Comandos2','yacc.py',23),
  ('Comando -> Expressao','Comando',1,'p_Comando1','yacc.py',27),
  ('Comando -> Imprime','Comando',1,'p_Comando2','yacc.py',31),
  ('Comando -> Comment','Comando',1,'p_Comando3','yacc.py',35),
  ('Expressao -> Expressao +','Expressao',2,'p_Expressao1','yacc.py',39),
  ('Expressao -> Expressao -','Expressao',2,'p_Expressao2','yacc.py',43),
  ('Expressao -> Expressao *','Expressao',2,'p_Expressao3','yacc.py',47),
  ('Expressao -> Expressao /','Expressao',2,'p_Expressao4','yacc.py',51),
  ('Expressao -> Expressao %','Expressao',2,'p_Expressao5','yacc.py',55),
  ('Expressao -> NUMBER','Expressao',1,'p_Expressao6','yacc.py',59),
  ('Imprime -> Expressao DOT','Imprime',2,'p_Expressao_Print','yacc.py',63),
  ('Imprime -> DOTSTRING','Imprime',1,'p_Expressao_Print2','yacc.py',67),
  ('Comment -> COMMENT_START Comandos COMMENT_END','Comment',3,'p_Comment','yacc.py',71),
]
