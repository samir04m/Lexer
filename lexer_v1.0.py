from clases.lenguaje import Lenguaje

import ply.lex as lex
import os
import codecs

palabrasReservadas = (
    "MOST",
    "OBT",
    "OCUQ", 
    "NOCUQ",
    "_Y_",
    "_O_",
    'NEG',  
    "REPET", 
    "REPETMQ", 
    "FIN", 
    "FUN", 
    "DEVOL"
)

miLenguaje = Lenguaje(palabrasReservadas)

literales = (
    "VER", "FAL"
)

tiposDeToken = (
    "IDENTIFICADOR",
    "PALABRA_RESERVADA",
    "OPERADOR",
    "DELIMITADOR",
    "LITERAL"
)

tokens = tiposDeToken + (
    "ENTERO",
    "CADENA",
    "NUMERAL",
    
    "SUMA",
    "RESTA",
    "MULTIPLICACION",
    "DIVISION",
    "MODULO",
    "POTENCIA",

    "ASIGNACION",
    "IGUAL",
    "DIFERENTE",
    "MENOR_IGUAL",
    "MAYOR_IGUAL",
    "MENOR_QUE",
    "MAYOR_QUE",
    "PUNTO_COMA",
    "COMA",
    "PARENTESIS_IZQUIERDO",
    "PARENTESIS_DERECHO",
    "CORCHETE_IZQUIERDO",
    "CORCHETE_DERECHO",
    "LLAVE_IZQUIERDA",
    "LLAVE_DERECHA",
    "BACKSLASH",
    "COMILLA_DOBLE",
    "COMILLA_SIMPLE"
)

t_ignore =' \t'
t_ASIGNACION = r'\:\:'
t_NUMERAL = r'\#'

t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_MODULO = r'\%'
t_POTENCIA = r'\^'

t_MENOR_QUE = r'\<\<'
t_MAYOR_QUE = r'\>\>'
t_PUNTO_COMA = ';'
t_COMA = r'\,'
t_PARENTESIS_IZQUIERDO = r'\('
t_PARENTESIS_DERECHO = r'\)'
t_CORCHETE_IZQUIERDO = r'\['
t_CORCHETE_DERECHO = r'\]'
t_LLAVE_IZQUIERDA = r'\{'
t_LLAVE_DERECHA = r'\}'
t_BACKSLASH = r'\\'
t_COMILLA_SIMPLE = r'\''
t_COMILLA_DOBLE = r'\"'

t_LITERAL = r"[-+]?\d*\.*\d+"

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFICADOR(t):
    r'\w+(_\d\w)*'
    #r'[a-zA-Z][a-zA-Z0-9_]*'
    if t.value in palabrasReservadas:
        t.type = 'PALABRA_RESERVADA'
    elif t.value in literales:
        t.type = 'LITERAL'
    elif t.value.upper() in palabrasReservadas:
        invalido(t,'Es una palabra reservada')
        return
    
    return t

def t_CADENA(t):
   r'\"?(\w+ \ *\w*\d* \ *)\"?'
   return t

def t_MENOR_IGUAL(t):
    r'<::'
    return t

def t_MAYOR_IGUAL(t):
    r'>::'
    return t

def t_IGUAL(t):
    r':::'
    return t

def t_DIFERENTE(t):
    r':-:'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comments(t):
    r'\*\*\*(.|\n)*?\*\*\*'
    t.lexer.lineno += t.value.count('\n')
    print("Linea %d inicia comentario de multiples lineas"%(t.lineno))

def t_comments_ONELine(t):
     r'\*\*(.)*\n'
     t.lexer.lineno += 1
     print("Linea %d comentario"%(t.lineno))

def t_error(t):
    print("Linea %d -> Token %r invalido." % (t.lineno, t.value) )
    print("-------------------------------------------------------")
    t.lexer.skip(1)    
    
def invalido(t, arg='Error Indefinido'):
    print("Linea %d -> Token %r invalido." % (t.lineno, t.value) )
    if arg : print("Descripcion del error :", arg)
    print("-------------------------------------------------------")


directorio = str(os.getcwd())+"/archivos/"
nombreArchivo =  'codigo.blur'
ruta = directorio+nombreArchivo
print (ruta)
fp = codecs.open(ruta,"r","utf-8")
codigoArchivo = fp.read()
fp.close()

analizadorLexico = lex.lex()
#print(codigoArchivo)
analizadorLexico.input(codigoArchivo)

if __name__ == '__main__':
    while True:
        tkn = analizadorLexico.token()
        if not tkn : break
        print (tkn)
