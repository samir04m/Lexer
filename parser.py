import ply.yacc as yacc
import os
import codecs
import re

from lexer import tokens, analizadorLexico
from sys import stdin

resultado_parser = []
parser_log = []
nombres = {}

precedence = (
    ('right', 'ASIGNACION'),
    ('left', 'IGUAL', 'DIFERENTE'),
    ('left', 'MAYOR_QUE', 'MAYOR_IGUAL', 'MENOR_QUE', 'MENOR_IGUAL'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULTIPLICACION', 'DIVISION', 'MODULO'),
    ('left', 'NEGAR'),
    ('left', 'POTENCIA'),
    ('left', 'PARENTESIS_IZQUIERDO', 'PARENTESIS_DERECHO'),
)

def p_declaracionAsignacion(t):
    'declaracion : IDENTIFICADOR ASIGNACION expresion'
    nombres[t[1]] = t[3]

def p_declaracionExpresion(t):
    'declaracion : expresion'
    t[0] = t[1]

def p_expresionOperacion(t):
    '''
        expresion :  expresion SUMA expresion
            | expresion RESTA expresion
            | expresion MULTIPLICACION expresion
            | expresion DIVISION expresion
            | expresion POTENCIA expresion
            | expresion MODULO expresion
    '''

    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]
    elif t[2] == '%':
        t[0] = t[1] % t[3]
    elif t[2] == '**':
        i = t[3]
        t[0] = t[1]
        while i > 1:
            t[0] *= t[1]
            i -= 1

def p_grupoExpresiones(t):
    '''
    expresion  : PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO
                | LLAVE_IZQUIERDA expresion LLAVE_DERECHA
                | CORCHETE_IZQUIERDO expresion CORCHETE_DERECHO
    '''
    t[0] = t[2]

def p_expresionLogica(t):
    '''
    expresion : expresion MENOR_QUE expresion
        | expresion MAYOR_QUE expresion
        | expresion MENOR_IGUAL expresion
        | expresion MAYOR_IGUAL expresion
        | expresion IGUAL expresion
        | expresion DIFERENTE expresion
        | PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO MENOR_QUE PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO
        | PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO MAYOR_QUE PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO
        | PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO MENOR_IGUAL PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO
        | PARENTESIS_IZQUIERDO  expresion PARENTESIS_DERECHO MAYOR_IGUAL PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO
        | PARENTESIS_IZQUIERDO  expresion PARENTESIS_DERECHO IGUAL PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO
        | PARENTESIS_IZQUIERDO  expresion PARENTESIS_DERECHO DIFERENTE PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO
    '''
    if t[2] == "<<": t[0] = t[1] < t[3]
    elif t[2] == ">>": t[0] = t[1] > t[3]
    elif t[2] == "<::": t[0] = t[1] <= t[3]
    elif t[2] == ">::": t[0] = t[1] >= t[3]
    elif t[2] == ":::": t[0] = t[1] is t[3]
    elif t[2] == ":-:": t[0] = t[1] != t[3]
    elif t[3] == "<<":
        t[0] = t[2] < t[4]
    elif t[2] == ">>":
        t[0] = t[2] > t[4]
    elif t[3] == "<::":
        t[0] = t[2] <= t[4]
    elif t[3] == ">::":
        t[0] = t[2] >= t[4]
    elif t[3] == ":::":
        t[0] = t[2] is t[4]
    elif t[3] == ":-:":
        t[0] = t[2] != t[4]

def p_expresionBooleana(t):
    '''
    expresion   :   expresion Y expresion
                |   expresion O expresion
                |   expresion NEGAR expresion
                |  PARENTESIS_IZQUIERDO expresion Y expresion PARENTESIS_DERECHO
                |  PARENTESIS_IZQUIERDO expresion O expresion PARENTESIS_DERECHO
                |  PARENTESIS_IZQUIERDO expresion NEGAR expresion PARENTESIS_DERECHO
    '''
    if t[2] == "yy":
        t[0] = t[1] and t[3]
    elif t[2] == "oo":
        t[0] = t[1] or t[3]
    elif t[2] == "negar":
        t[0] =  t[1] is not t[3]
    elif t[3] == "yy":
        t[0] = t[2] and t[4]
    elif t[3] == "oo":
        t[0] = t[2] or t[4]
    elif t[3] == "negar":
        t[0] =  t[2] is not t[4]

def p_expresionEntero(t):
    'expresion : ENTERO'
    t[0] = t[1]

def p_expresionCadena(t):
    'expresion : COMILLA_DOBLE expresion COMILLA_DOBLE'
    t[0] = t[2]

def p_expresionIdentificador(t):
    'expresion : IDENTIFICADOR'
    try:
        t[0] = nombres[t[1]]
    except LookupError:
        global parser_log
        mensaje = "En la linea {} -> \"{}\" no definido.".format(t.lexer.lineno,t[1])
        resultado_parser.append(mensaje)
        # print(mensaje)
        t[0] = 0

def p_error(t):
    global resultado_parser
    if t:
        mensaje = "Error sintactico de tipo {} en el valor {}".format( str(t.type),str(t.value))
        print(mensaje)
    else:
        mensaje = "Error sintactico {}".format(t)
        print(mensaje)
    resultado_parser.append(mensaje)

def prueba_sintactica(codigo):
    global resultado_gramatica
    resultado_parser.clear()

    for lineaCodigo in codigo.splitlines():
        if lineaCodigo:
            resultado = parser.parse(lineaCodigo)
            if resultado:
                resultado_parser.append(str(resultado))
        else: print("codigo vacia")

    # print("result: ", resultado_parser)
    print('\n'.join(resultado_parser))
    return resultado_parser

nombreArchivo =  'operaciones.slx'
ruta = str(os.getcwd())+"/archivos/"+nombreArchivo
fp = codecs.open(ruta,"r","utf-8")
codigoArchivo = fp.read()
fp.close()

parser = yacc.yacc()
# result = parser.parse(codigoArchivo)
prueba_sintactica(codigoArchivo)
# print (result)
