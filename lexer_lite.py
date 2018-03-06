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
    "ASIGNACION",
    "ENTERO",
    "CADENA",
    "NUMERAL",
)

t_ignore =' \t'
t_ASIGNACION = r'\:\:'
t_NUMERAL = r'\#'

t_OPERADOR = r'\+|\-|\*|\/|\%|\^|\<\:\:|\>\:\:|\V|\F|\:\:\:|\:\-\:|\<\<|\>\>'

t_DELIMITADOR = r'\"|\'|\\|\(|\)|\{|\}|\[|\]|\,|\;'
t_LITERAL = r"[-+]?\d*\.*\d+"

def t_ENTERO(t):
    r'[+-]?\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFICADOR(t):
    r'\w+(_\d\w)*'
    #r'[a-zA-Z][a-zA-Z0-9_]*'
    if t.value in miLenguaje.getCaracteres():
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

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comments(t):
    r'\*\*\*(.|\n)*?\*\*\*'
    t.lexer.lineno += t.value.count('\n')
    #print("Linea %d inicia comentario de multiples lineas"%(t.lineno))

def t_comments_ONELine(t):
    r'\*\*(.)*\n'
    t.lexer.lineno += 1
    #print("Linea %d comentario"%(t.lineno))

def t_error(t):
    print("Linea %d -> Token %r invalido." % (t.lineno, t.value) )
    print("\n")
    t.lexer.skip(1)    
    
def invalido(t, arg='Error Indefinido'):
    print("Linea %d -> Token %r invalido." % (t.lineno, t.value) )
    if arg : print("Descripcion del error :", arg)
    print("\n")


import sys

def progressbar(valor, total, estado=''):
    longitud_barra = 60
    filled_len = int(round(longitud_barra * valor / float(total)))

    percents = round(100.0 * valor / float(total), 1)
    bar = '#' * filled_len + '-' * (longitud_barra - filled_len)

    sys.stdout.write('[%s] %s%s - Token %s/%s\r' % (bar, percents, '%', estado, total))
    sys.stdout.flush() 


nombreArchivo =  'codigo.blur'
ruta = str(os.getcwd())+"/archivos/"+nombreArchivo
fp = codecs.open(ruta,"r","utf-8")
codigoArchivo = fp.read()
fp.close()

analizadorLexico = lex.lex()
analizadorLexico.input(codigoArchivo)

analizadorLexicoTest = lex.lex()
analizadorLexicoTest.input(codigoArchivo)

if __name__ == '__main__':
    total = 0
    while True:
        tkn0 = analizadorLexicoTest.token()
        if not tkn0 : break
        total = total + 1 
    os.system('clear')
    sys.stdout.flush() 
    
    print("Se iniciara el analizador lexico para el archivo %r"% (nombreArchivo))
    c = 1 
    while True:
        tkn = analizadorLexico.token()
        if not tkn : break
        input("\n\nPresione cualquier tecla para continuar...   ")
        os.system('clear')
        print (tkn, "\n")
        progressbar(c, total, c)
        c = c + 1 
        
    os.system('clear')
    print ("\n\n\n\t\tHa finalizado el analisis lexico")
    input("\n\n\n\n\nPresione cualquier tecla para salir")
    os.system('clear')
    sys.stdout.flush()   
