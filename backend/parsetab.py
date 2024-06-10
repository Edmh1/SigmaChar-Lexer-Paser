
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftLOGICAL_OP_ORleftLOGICAL_OP_ANDrightLOGICAL_OP_NOTleftLESS_OPLESS_EQUAL_OPGREATER_OPGREATER_EQUAL_OPEQUAL_OPDIFFERENT_OPleftPLUS_OPMINUS_OPleftMUL_OPDIV_OPnonassocLPARENRPARENASSIGNMENT_OP BREAK COMMENT CONDITIONAL1 CONDITIONAL2 DIFFERENT_OP DIV_OP END_LINE EQUAL_OP FALSE FUNCTION_DECLARATION GREATER_EQUAL_OP GREATER_OP LESS_EQUAL_OP LESS_OP LOGICAL_OP_AND LOGICAL_OP_NOT LOGICAL_OP_OR LOOP LPAREN MINUS_OP MUL_OP NULL NUMBER_FLOAT NUMBER_INTEGER PLUS_OP PRINT_DECLARATION RETURN RPAREN SEPARATION STRUCTURE_BODY TEXT_CHAR TEXT_STRING TRUE TYPE_BOOLEAN TYPE_CHAR TYPE_FLOAT TYPE_INTEGER TYPE_STRING UNTIL VARIABLEprogram : statement_liststatement_list : statement_list statement\n                      | statementstatement : expression END_LINE\n                 | assignment END_LINE\n                 | declaration END_LINE\n                 | conditional END_LINE\n                 | loop END_LINE\n                 | return_statement END_LINE\n                 | break_statement END_LINE\n                 | function_declaration END_LINE\n                 | function_call END_LINE\n                 | print_statement END_LINE\n                 | comment\n                 function_declaration : type FUNCTION_DECLARATION LPAREN parameter_list RPAREN STRUCTURE_BODY statement_list END_LINE\n                            | FUNCTION_DECLARATION LPAREN parameter_list RPAREN STRUCTURE_BODY statement_list END_LINEparameter_list : parameter_list SEPARATION parameter\n                      | parameter\n                      | emptyparameter : type VARIABLEfunction_call : VARIABLE LPAREN argument_list RPARENargument_list : argument_list SEPARATION expression\n                     | expression\n                     | emptyprint_statement : PRINT_DECLARATION LPAREN expression RPARENexpression : binary_expression\n                  | unitary_expression\n                  | primary_expression\n                  binary_expression : expression PLUS_OP expression\n                         | expression MINUS_OP expression\n                         | expression MUL_OP expression\n                         | expression DIV_OP expression\n                         | expression LESS_OP expression\n                         | expression GREATER_OP expression\n                         | expression LESS_EQUAL_OP expression\n                         | expression GREATER_EQUAL_OP expression\n                         | expression EQUAL_OP expression\n                         | expression DIFFERENT_OP expression\n                         | expression LOGICAL_OP_AND expression\n                         | expression LOGICAL_OP_OR expressionunitary_expression : MINUS_OP expression\n                          | LOGICAL_OP_NOT expressionprimary_expression : VARIABLE\n                          | NUMBER_INTEGER\n                          | NUMBER_FLOAT\n                          | TRUE\n                          | FALSE\n                          | NULL\n                          | TEXT_CHAR\n                          | TEXT_STRING\n                          | function_callassignment : VARIABLE ASSIGNMENT_OP expressiondeclaration : type VARIABLE ASSIGNMENT_OP expression\n                   | type VARIABLEconditional : CONDITIONAL1 LPAREN expression RPAREN STRUCTURE_BODY statement_list CONDITIONAL2 STRUCTURE_BODY statement_list\n                   | CONDITIONAL1 LPAREN expression RPAREN STRUCTURE_BODY statement_listloop : LOOP STRUCTURE_BODY statement_list UNTIL LPAREN expression RPARENreturn_statement : RETURN expressionbreak_statement : BREAKcomment : COMMENTempty : type : TYPE_INTEGER\n            | TYPE_FLOAT\n            | TYPE_BOOLEAN\n            | TYPE_CHAR\n            | TYPE_STRING'
    
_lr_action_items = {'VARIABLE':([0,2,3,14,19,22,26,27,28,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,68,69,74,93,96,100,103,114,115,116,118,119,121,122,127,128,],[18,18,-3,-14,66,71,-60,71,71,-62,-63,-64,-65,-66,-2,-4,71,71,71,71,71,71,71,71,71,71,71,71,-5,-6,-7,-8,-9,-10,-11,-12,-13,71,71,71,18,71,71,18,110,71,18,71,18,18,18,18,18,18,18,]),'CONDITIONAL1':([0,2,3,14,26,41,42,55,56,57,58,59,60,61,62,63,69,96,114,116,118,119,121,122,127,128,],[20,20,-3,-14,-60,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,20,20,20,20,20,20,20,20,20,20,]),'LOOP':([0,2,3,14,26,41,42,55,56,57,58,59,60,61,62,63,69,96,114,116,118,119,121,122,127,128,],[21,21,-3,-14,-60,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,21,21,21,21,21,21,21,21,21,21,]),'RETURN':([0,2,3,14,26,41,42,55,56,57,58,59,60,61,62,63,69,96,114,116,118,119,121,122,127,128,],[22,22,-3,-14,-60,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,22,22,22,22,22,22,22,22,22,22,]),'BREAK':([0,2,3,14,26,41,42,55,56,57,58,59,60,61,62,63,69,96,114,116,118,119,121,122,127,128,],[23,23,-3,-14,-60,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,23,23,23,23,23,23,23,23,23,23,]),'FUNCTION_DECLARATION':([0,2,3,14,19,26,36,37,38,39,40,41,42,55,56,57,58,59,60,61,62,63,69,96,114,116,118,119,121,122,127,128,],[24,24,-3,-14,67,-60,-62,-63,-64,-65,-66,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,24,24,24,24,24,24,24,24,24,24,]),'PRINT_DECLARATION':([0,2,3,14,26,41,42,55,56,57,58,59,60,61,62,63,69,96,114,116,118,119,121,122,127,128,],[25,25,-3,-14,-60,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,25,25,25,25,25,25,25,25,25,25,]),'COMMENT':([0,2,3,14,26,41,42,55,56,57,58,59,60,61,62,63,69,96,114,116,118,119,121,122,127,128,],[26,26,-3,-14,-60,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,26,26,26,26,26,26,26,26,26,26,]),'MINUS_OP':([0,2,3,4,12,14,15,16,17,18,22,26,27,28,29,30,31,32,33,34,35,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,68,69,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,93,95,96,101,102,103,104,112,114,115,116,118,119,120,121,122,127,128,],[27,27,-3,44,-51,-14,-26,-27,-28,-43,27,-60,27,27,-44,-45,-46,-47,-48,-49,-50,-2,-4,27,27,27,27,27,27,27,27,27,27,27,27,-5,-6,-7,-8,-9,-10,-11,-12,-13,27,27,27,27,44,-43,-51,27,-41,44,-29,-30,-31,-32,44,44,44,44,44,44,44,44,44,44,27,44,27,44,-21,27,44,44,27,27,27,27,27,44,27,27,27,27,]),'LOGICAL_OP_NOT':([0,2,3,14,22,26,27,28,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,68,69,74,93,96,103,114,115,116,118,119,121,122,127,128,],[28,28,-3,-14,28,-60,28,28,-2,-4,28,28,28,28,28,28,28,28,28,28,28,28,-5,-6,-7,-8,-9,-10,-11,-12,-13,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'NUMBER_INTEGER':([0,2,3,14,22,26,27,28,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,68,69,74,93,96,103,114,115,116,118,119,121,122,127,128,],[29,29,-3,-14,29,-60,29,29,-2,-4,29,29,29,29,29,29,29,29,29,29,29,29,-5,-6,-7,-8,-9,-10,-11,-12,-13,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'NUMBER_FLOAT':([0,2,3,14,22,26,27,28,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,68,69,74,93,96,103,114,115,116,118,119,121,122,127,128,],[30,30,-3,-14,30,-60,30,30,-2,-4,30,30,30,30,30,30,30,30,30,30,30,30,-5,-6,-7,-8,-9,-10,-11,-12,-13,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'TRUE':([0,2,3,14,22,26,27,28,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,68,69,74,93,96,103,114,115,116,118,119,121,122,127,128,],[31,31,-3,-14,31,-60,31,31,-2,-4,31,31,31,31,31,31,31,31,31,31,31,31,-5,-6,-7,-8,-9,-10,-11,-12,-13,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'FALSE':([0,2,3,14,22,26,27,28,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,68,69,74,93,96,103,114,115,116,118,119,121,122,127,128,],[32,32,-3,-14,32,-60,32,32,-2,-4,32,32,32,32,32,32,32,32,32,32,32,32,-5,-6,-7,-8,-9,-10,-11,-12,-13,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'NULL':([0,2,3,14,22,26,27,28,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,68,69,74,93,96,103,114,115,116,118,119,121,122,127,128,],[33,33,-3,-14,33,-60,33,33,-2,-4,33,33,33,33,33,33,33,33,33,33,33,33,-5,-6,-7,-8,-9,-10,-11,-12,-13,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'TEXT_CHAR':([0,2,3,14,22,26,27,28,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,68,69,74,93,96,103,114,115,116,118,119,121,122,127,128,],[34,34,-3,-14,34,-60,34,34,-2,-4,34,34,34,34,34,34,34,34,34,34,34,34,-5,-6,-7,-8,-9,-10,-11,-12,-13,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'TEXT_STRING':([0,2,3,14,22,26,27,28,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,68,69,74,93,96,103,114,115,116,118,119,121,122,127,128,],[35,35,-3,-14,35,-60,35,35,-2,-4,35,35,35,35,35,35,35,35,35,35,35,35,-5,-6,-7,-8,-9,-10,-11,-12,-13,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'TYPE_INTEGER':([0,2,3,14,26,41,42,55,56,57,58,59,60,61,62,63,69,73,94,96,109,114,116,118,119,121,122,127,128,],[36,36,-3,-14,-60,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'TYPE_FLOAT':([0,2,3,14,26,41,42,55,56,57,58,59,60,61,62,63,69,73,94,96,109,114,116,118,119,121,122,127,128,],[37,37,-3,-14,-60,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'TYPE_BOOLEAN':([0,2,3,14,26,41,42,55,56,57,58,59,60,61,62,63,69,73,94,96,109,114,116,118,119,121,122,127,128,],[38,38,-3,-14,-60,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'TYPE_CHAR':([0,2,3,14,26,41,42,55,56,57,58,59,60,61,62,63,69,73,94,96,109,114,116,118,119,121,122,127,128,],[39,39,-3,-14,-60,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'TYPE_STRING':([0,2,3,14,26,41,42,55,56,57,58,59,60,61,62,63,69,73,94,96,109,114,116,118,119,121,122,127,128,],[40,40,-3,-14,-60,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'$end':([1,2,3,14,26,41,42,55,56,57,58,59,60,61,62,63,],[0,-1,-3,-14,-60,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,]),'UNTIL':([3,14,26,41,42,55,56,57,58,59,60,61,62,63,96,],[-3,-14,-60,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,107,]),'CONDITIONAL2':([3,14,26,41,42,55,56,57,58,59,60,61,62,63,119,],[-3,-14,-60,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,123,]),'END_LINE':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,23,26,29,30,31,32,33,34,35,41,42,55,56,57,58,59,60,61,62,63,66,70,71,72,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,102,104,111,119,121,122,124,125,126,128,],[-3,42,55,56,57,58,59,60,61,62,63,-14,-26,-27,-28,-43,-59,-60,-44,-45,-46,-47,-48,-49,-50,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-54,-58,-43,-51,-41,-42,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-52,-21,-53,-25,-56,125,126,-57,-16,-15,-55,]),'PLUS_OP':([4,12,15,16,17,18,29,30,31,32,33,34,35,70,71,72,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,95,101,102,104,112,120,],[43,-51,-26,-27,-28,-43,-44,-45,-46,-47,-48,-49,-50,43,-43,-51,-41,43,-29,-30,-31,-32,43,43,43,43,43,43,43,43,43,43,43,43,-21,43,43,43,]),'MUL_OP':([4,12,15,16,17,18,29,30,31,32,33,34,35,70,71,72,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,95,101,102,104,112,120,],[45,-51,-26,-27,-28,-43,-44,-45,-46,-47,-48,-49,-50,45,-43,-51,45,45,45,45,-31,-32,45,45,45,45,45,45,45,45,45,45,45,45,-21,45,45,45,]),'DIV_OP':([4,12,15,16,17,18,29,30,31,32,33,34,35,70,71,72,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,95,101,102,104,112,120,],[46,-51,-26,-27,-28,-43,-44,-45,-46,-47,-48,-49,-50,46,-43,-51,46,46,46,46,-31,-32,46,46,46,46,46,46,46,46,46,46,46,46,-21,46,46,46,]),'LESS_OP':([4,12,15,16,17,18,29,30,31,32,33,34,35,70,71,72,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,95,101,102,104,112,120,],[47,-51,-26,-27,-28,-43,-44,-45,-46,-47,-48,-49,-50,47,-43,-51,-41,47,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,47,47,47,47,47,47,-21,47,47,47,]),'GREATER_OP':([4,12,15,16,17,18,29,30,31,32,33,34,35,70,71,72,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,95,101,102,104,112,120,],[48,-51,-26,-27,-28,-43,-44,-45,-46,-47,-48,-49,-50,48,-43,-51,-41,48,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,48,48,48,48,48,48,-21,48,48,48,]),'LESS_EQUAL_OP':([4,12,15,16,17,18,29,30,31,32,33,34,35,70,71,72,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,95,101,102,104,112,120,],[49,-51,-26,-27,-28,-43,-44,-45,-46,-47,-48,-49,-50,49,-43,-51,-41,49,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,49,49,49,49,49,49,-21,49,49,49,]),'GREATER_EQUAL_OP':([4,12,15,16,17,18,29,30,31,32,33,34,35,70,71,72,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,95,101,102,104,112,120,],[50,-51,-26,-27,-28,-43,-44,-45,-46,-47,-48,-49,-50,50,-43,-51,-41,50,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,50,50,50,50,50,50,-21,50,50,50,]),'EQUAL_OP':([4,12,15,16,17,18,29,30,31,32,33,34,35,70,71,72,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,95,101,102,104,112,120,],[51,-51,-26,-27,-28,-43,-44,-45,-46,-47,-48,-49,-50,51,-43,-51,-41,51,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,51,51,51,51,51,51,-21,51,51,51,]),'DIFFERENT_OP':([4,12,15,16,17,18,29,30,31,32,33,34,35,70,71,72,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,95,101,102,104,112,120,],[52,-51,-26,-27,-28,-43,-44,-45,-46,-47,-48,-49,-50,52,-43,-51,-41,52,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,52,52,52,52,52,52,-21,52,52,52,]),'LOGICAL_OP_AND':([4,12,15,16,17,18,29,30,31,32,33,34,35,70,71,72,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,95,101,102,104,112,120,],[53,-51,-26,-27,-28,-43,-44,-45,-46,-47,-48,-49,-50,53,-43,-51,-41,-42,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,53,53,53,53,53,-21,53,53,53,]),'LOGICAL_OP_OR':([4,12,15,16,17,18,29,30,31,32,33,34,35,70,71,72,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,95,101,102,104,112,120,],[54,-51,-26,-27,-28,-43,-44,-45,-46,-47,-48,-49,-50,54,-43,-51,-41,-42,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,54,54,54,54,-21,54,54,54,]),'RPAREN':([15,16,17,29,30,31,32,33,34,35,65,71,72,73,75,76,77,78,79,80,81,82,83,84,85,86,87,88,90,91,92,94,95,97,98,99,101,102,105,110,112,117,120,],[-26,-27,-28,-44,-45,-46,-47,-48,-49,-50,-61,-43,-51,-61,-41,-42,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,102,-23,-24,-61,106,108,-18,-19,111,-21,113,-20,-22,-17,124,]),'SEPARATION':([15,16,17,29,30,31,32,33,34,35,65,71,72,73,75,76,77,78,79,80,81,82,83,84,85,86,87,88,90,91,92,94,97,98,99,102,105,110,112,117,],[-26,-27,-28,-44,-45,-46,-47,-48,-49,-50,-61,-43,-51,-61,-41,-42,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,103,-23,-24,-61,109,-18,-19,-21,109,-20,-22,-17,]),'ASSIGNMENT_OP':([18,66,],[64,93,]),'LPAREN':([18,20,24,25,67,71,107,],[65,68,73,74,94,65,115,]),'STRUCTURE_BODY':([21,106,108,113,123,],[69,114,116,118,127,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,69,114,116,118,127,],[2,96,119,121,122,128,]),'statement':([0,2,69,96,114,116,118,119,121,122,127,128,],[3,41,3,41,3,3,3,41,41,41,3,41,]),'expression':([0,2,22,27,28,43,44,45,46,47,48,49,50,51,52,53,54,64,65,68,69,74,93,96,103,114,115,116,118,119,121,122,127,128,],[4,4,70,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,95,4,101,104,4,112,4,120,4,4,4,4,4,4,4,]),'assignment':([0,2,69,96,114,116,118,119,121,122,127,128,],[5,5,5,5,5,5,5,5,5,5,5,5,]),'declaration':([0,2,69,96,114,116,118,119,121,122,127,128,],[6,6,6,6,6,6,6,6,6,6,6,6,]),'conditional':([0,2,69,96,114,116,118,119,121,122,127,128,],[7,7,7,7,7,7,7,7,7,7,7,7,]),'loop':([0,2,69,96,114,116,118,119,121,122,127,128,],[8,8,8,8,8,8,8,8,8,8,8,8,]),'return_statement':([0,2,69,96,114,116,118,119,121,122,127,128,],[9,9,9,9,9,9,9,9,9,9,9,9,]),'break_statement':([0,2,69,96,114,116,118,119,121,122,127,128,],[10,10,10,10,10,10,10,10,10,10,10,10,]),'function_declaration':([0,2,69,96,114,116,118,119,121,122,127,128,],[11,11,11,11,11,11,11,11,11,11,11,11,]),'function_call':([0,2,22,27,28,43,44,45,46,47,48,49,50,51,52,53,54,64,65,68,69,74,93,96,103,114,115,116,118,119,121,122,127,128,],[12,12,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,12,72,72,12,72,12,72,12,12,12,12,12,12,12,]),'print_statement':([0,2,69,96,114,116,118,119,121,122,127,128,],[13,13,13,13,13,13,13,13,13,13,13,13,]),'comment':([0,2,69,96,114,116,118,119,121,122,127,128,],[14,14,14,14,14,14,14,14,14,14,14,14,]),'binary_expression':([0,2,22,27,28,43,44,45,46,47,48,49,50,51,52,53,54,64,65,68,69,74,93,96,103,114,115,116,118,119,121,122,127,128,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'unitary_expression':([0,2,22,27,28,43,44,45,46,47,48,49,50,51,52,53,54,64,65,68,69,74,93,96,103,114,115,116,118,119,121,122,127,128,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'primary_expression':([0,2,22,27,28,43,44,45,46,47,48,49,50,51,52,53,54,64,65,68,69,74,93,96,103,114,115,116,118,119,121,122,127,128,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'type':([0,2,69,73,94,96,109,114,116,118,119,121,122,127,128,],[19,19,19,100,100,19,100,19,19,19,19,19,19,19,19,]),'argument_list':([65,],[90,]),'empty':([65,73,94,],[92,99,99,]),'parameter_list':([73,94,],[97,105,]),'parameter':([73,94,109,],[98,98,117,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','parser.py',28),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','parser.py',32),
  ('statement_list -> statement','statement_list',1,'p_statement_list','parser.py',33),
  ('statement -> expression END_LINE','statement',2,'p_statement','parser.py',43),
  ('statement -> assignment END_LINE','statement',2,'p_statement','parser.py',44),
  ('statement -> declaration END_LINE','statement',2,'p_statement','parser.py',45),
  ('statement -> conditional END_LINE','statement',2,'p_statement','parser.py',46),
  ('statement -> loop END_LINE','statement',2,'p_statement','parser.py',47),
  ('statement -> return_statement END_LINE','statement',2,'p_statement','parser.py',48),
  ('statement -> break_statement END_LINE','statement',2,'p_statement','parser.py',49),
  ('statement -> function_declaration END_LINE','statement',2,'p_statement','parser.py',50),
  ('statement -> function_call END_LINE','statement',2,'p_statement','parser.py',51),
  ('statement -> print_statement END_LINE','statement',2,'p_statement','parser.py',52),
  ('statement -> comment','statement',1,'p_statement','parser.py',53),
  ('function_declaration -> type FUNCTION_DECLARATION LPAREN parameter_list RPAREN STRUCTURE_BODY statement_list END_LINE','function_declaration',8,'p_function_declaration','parser.py',58),
  ('function_declaration -> FUNCTION_DECLARATION LPAREN parameter_list RPAREN STRUCTURE_BODY statement_list END_LINE','function_declaration',7,'p_function_declaration','parser.py',59),
  ('parameter_list -> parameter_list SEPARATION parameter','parameter_list',3,'p_parameter_list','parser.py',75),
  ('parameter_list -> parameter','parameter_list',1,'p_parameter_list','parser.py',76),
  ('parameter_list -> empty','parameter_list',1,'p_parameter_list','parser.py',77),
  ('parameter -> type VARIABLE','parameter',2,'p_parameter','parser.py',86),
  ('function_call -> VARIABLE LPAREN argument_list RPAREN','function_call',4,'p_function_call','parser.py',90),
  ('argument_list -> argument_list SEPARATION expression','argument_list',3,'p_argument_list','parser.py',102),
  ('argument_list -> expression','argument_list',1,'p_argument_list','parser.py',103),
  ('argument_list -> empty','argument_list',1,'p_argument_list','parser.py',104),
  ('print_statement -> PRINT_DECLARATION LPAREN expression RPAREN','print_statement',4,'p_print_statement','parser.py',113),
  ('expression -> binary_expression','expression',1,'p_expression','parser.py',117),
  ('expression -> unitary_expression','expression',1,'p_expression','parser.py',118),
  ('expression -> primary_expression','expression',1,'p_expression','parser.py',119),
  ('binary_expression -> expression PLUS_OP expression','binary_expression',3,'p_binary_expression','parser.py',124),
  ('binary_expression -> expression MINUS_OP expression','binary_expression',3,'p_binary_expression','parser.py',125),
  ('binary_expression -> expression MUL_OP expression','binary_expression',3,'p_binary_expression','parser.py',126),
  ('binary_expression -> expression DIV_OP expression','binary_expression',3,'p_binary_expression','parser.py',127),
  ('binary_expression -> expression LESS_OP expression','binary_expression',3,'p_binary_expression','parser.py',128),
  ('binary_expression -> expression GREATER_OP expression','binary_expression',3,'p_binary_expression','parser.py',129),
  ('binary_expression -> expression LESS_EQUAL_OP expression','binary_expression',3,'p_binary_expression','parser.py',130),
  ('binary_expression -> expression GREATER_EQUAL_OP expression','binary_expression',3,'p_binary_expression','parser.py',131),
  ('binary_expression -> expression EQUAL_OP expression','binary_expression',3,'p_binary_expression','parser.py',132),
  ('binary_expression -> expression DIFFERENT_OP expression','binary_expression',3,'p_binary_expression','parser.py',133),
  ('binary_expression -> expression LOGICAL_OP_AND expression','binary_expression',3,'p_binary_expression','parser.py',134),
  ('binary_expression -> expression LOGICAL_OP_OR expression','binary_expression',3,'p_binary_expression','parser.py',135),
  ('unitary_expression -> MINUS_OP expression','unitary_expression',2,'p_unitary_expression','parser.py',173),
  ('unitary_expression -> LOGICAL_OP_NOT expression','unitary_expression',2,'p_unitary_expression','parser.py',174),
  ('primary_expression -> VARIABLE','primary_expression',1,'p_primary_expression','parser.py',182),
  ('primary_expression -> NUMBER_INTEGER','primary_expression',1,'p_primary_expression','parser.py',183),
  ('primary_expression -> NUMBER_FLOAT','primary_expression',1,'p_primary_expression','parser.py',184),
  ('primary_expression -> TRUE','primary_expression',1,'p_primary_expression','parser.py',185),
  ('primary_expression -> FALSE','primary_expression',1,'p_primary_expression','parser.py',186),
  ('primary_expression -> NULL','primary_expression',1,'p_primary_expression','parser.py',187),
  ('primary_expression -> TEXT_CHAR','primary_expression',1,'p_primary_expression','parser.py',188),
  ('primary_expression -> TEXT_STRING','primary_expression',1,'p_primary_expression','parser.py',189),
  ('primary_expression -> function_call','primary_expression',1,'p_primary_expression','parser.py',190),
  ('assignment -> VARIABLE ASSIGNMENT_OP expression','assignment',3,'p_assignment','parser.py',200),
  ('declaration -> type VARIABLE ASSIGNMENT_OP expression','declaration',4,'p_declaration','parser.py',205),
  ('declaration -> type VARIABLE','declaration',2,'p_declaration','parser.py',206),
  ('conditional -> CONDITIONAL1 LPAREN expression RPAREN STRUCTURE_BODY statement_list CONDITIONAL2 STRUCTURE_BODY statement_list','conditional',9,'p_conditional','parser.py',234),
  ('conditional -> CONDITIONAL1 LPAREN expression RPAREN STRUCTURE_BODY statement_list','conditional',6,'p_conditional','parser.py',235),
  ('loop -> LOOP STRUCTURE_BODY statement_list UNTIL LPAREN expression RPAREN','loop',7,'p_loop','parser.py',242),
  ('return_statement -> RETURN expression','return_statement',2,'p_return_statement','parser.py',246),
  ('break_statement -> BREAK','break_statement',1,'p_break_statement','parser.py',250),
  ('comment -> COMMENT','comment',1,'p_comment','parser.py',254),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',258),
  ('type -> TYPE_INTEGER','type',1,'p_type','parser.py',262),
  ('type -> TYPE_FLOAT','type',1,'p_type','parser.py',263),
  ('type -> TYPE_BOOLEAN','type',1,'p_type','parser.py',264),
  ('type -> TYPE_CHAR','type',1,'p_type','parser.py',265),
  ('type -> TYPE_STRING','type',1,'p_type','parser.py',266),
]
