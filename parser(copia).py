import ply.yacc as yacc
import os
import codecs
import re

from lexer import tokens
from sys import stdin

precedence = (
    ('right', 'ASIGNACION'),
    ('left', 'NEG'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULTIPLICACION', 'DIVISION', 'MODULO'),
    ('left', 'POTENCIA'),
    ('left', 'PARENTESIS_IZQUIERDO', 'PARENTESIS_DERECHO'),
)

def p_program(p):
    '''program = block'''
    # p[0] = program(p[1], "program")
    print ("p_program")

def p_constDecl(p):
    '''constDecl = CONST constAsssignmentList ;'''
    # p[0] = constDecl(p[2])
    print ("p_constDecl")

def p_constDeclEmpty(p):
    '''consDecl = empty'''
    # p[0] = Null()
    print ("p_constDeclEmpty")

def p_constAssignmentList1(p):
    '''constAssignmentList : IDENTIFICADOR = NUMBER'''
    print('p_constAssignmentList1')

def p_constAssignmentList2(p):
    '''constAssignmentList : constAssignmentList, IDENTIFICADOR = NUMBER'''
    print('p_constAssignmentList2')

def p_varDecl1(p):
    '''varDecl : VAR IDENTIFICADOR ;'''
    print("varDecl1")

def p_varDeclEmpty(p):
    '''varDecl : empty'''
    print("p_varDeclEmpty")

def p_identList1(p):
    '''identList : IDENTIFICADOR'''
    print("p_identList1")

def p_identList2(p):
    '''identList : IDENTIFICADOR identList, IDENTIFICADOR'''
    print("p_identList2")

def p_procDecl1(p):
    '''procDecl : procDecl PROCEDURE IDENTIFICADOR ; block ;'''
    print("p_procDecl1")

def p_procDeclEmpty(p):
    '''procDecl : empty'''
    print("p_procDeclEmpty")

def p_statement1(p):
    '''statement : IDENTIFICADOR ASIGNACION expression'''
    print("p_statement1")

def p_statement2(p):
    '''statement : CALL IDENTIFICADOR'''
    print("p_statement2")

def p_statement3(p):
    '''statement : BEGIN statementList END'''
    print("p_statement3")

def p_statement4(p):
    '''statement : OCUQ condition CORCHETE_IZQUIERDO statement'''
    print("p_statement4")

def p_statement5(p):
    '''statement : REPETMQ condition CORCHETE_IZQUIERDO statement'''
    print("p_statement5")

def p_statementEmpty(p):
    '''statement : empty'''
    print("p_statementEmpty")

def p_statementList1(p):
    '''statementList : statement'''
    print("p_statementList1")

def p_statementList2(p):
    '''statementList : statementList ; statement'''
    print("p_statementList2")

def p_condition1(p):
    '''condition : NEG expression'''
    print("p_condition1")

def p_condition2(p):
    '''condition : expression relation expression'''
    print("p_condition2")

def p_relation1(p):
    '''relation : ASIGNACION'''
    print("p_relation1")

def p_relation2(p):
    '''relation : NEG'''
    print("p_relation2")

# def p_relation3(p):
#     '''relation : '''
#     print("p_relation3")

def p_expression1(p):
    '''expression : term'''
    print("p_expression1")

def p_expression2(p):
    '''expression : addingOperator term'''
    print("p_expression2")

def p_expression3(p):
    '''expression : expression addingOperator term'''
    print("p_expression3")

def p_term1(p):
    '''term : factor'''
    print("p_term1")

def p_term2(p):
    '''term : term multiplyingOperator factor'''
    print("p_term2")

def p_multiplyingOperator1(p):
    '''multiplyingOperator : MULTIPLICACION'''
    print("p_multiplyingOperator1")

def p_multiplyingOperator2(p):
    '''multiplyingOperator : DIVISION'''
    print("p_multiplyingOperator2")

def p_factor1(p):
    '''factor : IDENTIFICADOR'''
    print("p_factor1")

def p_factor2(p):
    '''factor : ENTERO'''
    print("p_factor2")

def p_factor3(p):
    '''factor : PARENTESIS_IZQUIERDO expression PARENTESIS_DERECHO'''
    print("p_factor3")

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    print ("error de sintaxis",p)
    print ("error en la linea"+str(p.lineno))


nombreArchivo =  'code.slx'
ruta = str(os.getcwd())+"/archivos/"+nombreArchivo
fp = codecs.open(ruta,"r","utf-8")
codigoArchivo = fp.read()
fp.close()

PARENTESIS_DERECHOr = yacc.yacc()
result = parser.parse(codigoArchivo)  

print (result)