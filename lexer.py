import ply.lex as lex
import os
import codecs

resultado_lexer = []

palabrasReservadas = (
    "ver", #print
    "obt", #input
    "es", #if
    "deloc", #else
    "yy", #and
    "oo", #or
    "negar", #not
    "repetir", #whie, for
    "func", #def
    "fin", #break
    "devol" #return
)

literales = (
    "CIERTO",
    "FALSO"
)

tiposDeToken = (
    "IDENTIFICADOR",
    "PALABRA_RESERVADA",
    "LITERAL"
)

tokens = literales + tiposDeToken + (
    "IMPRIMIR",
    "LEER",
    "SI",
    "SINO",
    "Y",
    "O",
    "NEGAR",
    "MIESTRAS",
    "FUNCION",
    "BREAK",
    "RETORNAR",

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

t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_MODULO = r'\%'
t_POTENCIA = r'(\*{2} | \^)'

t_ASIGNACION = r'\:\:'
t_NUMERAL = r'\#'

t_MENOR_QUE = r'\<\<'
t_MAYOR_QUE = r'\>\>'
t_PUNTO_COMA = ';'
t_COMA = r','
t_PARENTESIS_IZQUIERDO = r'\('
t_PARENTESIS_DERECHO = r'\)'
t_CORCHETE_IZQUIERDO = r'\['
t_CORCHETE_DERECHO = r'\]'
t_LLAVE_IZQUIERDA = r'{'
t_LLAVE_DERECHA = r'}'
t_BACKSLASH = r'\\'
t_COMILLA_SIMPLE = r'\''
t_COMILLA_DOBLE = r'\"'

def t_IMPRIMIR(t):
    r'ver'
    return t

def t_LEER(t):
    r'obt'
    return t

def t_SI(t):
    r'es'
    return t

def t_SINO(t):
    r'deloc'
    return t

def t_Y(t):
    r'yy'
    return t

def t_O(t):
    r'oo'
    return t

def t_NEGAR(t):
    r'neg'
    return t

def t_MIESTRAS(t):
    r'repetir'
    return t

def t_FUNCION(t):
    r'func'
    return t

def t_BREAK(t):
    r'fin'
    return t

def t_RETORNAR(t):
    r'devol'
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFICADOR(t):
    r'\w+(_\d\w)*'
    if t.value in literales:
        t.type = 'LITERAL'
    elif t.value.lower() in palabrasReservadas:
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
    #print("Linea %d inicia comentario de multiples lineas"%(t.lineno))

def t_comments_ONELine(t):
    r'\*\*(.)*\n'
    t.lexer.lineno += 1
    #print("Linea %d comentario"%(t.lineno))

t_ignore =' \t'

def t_error(t):
    global resultado_lexer
    mensaje = "Linea %d -> Token %r invalido." % (t.lineno, str(t.value)[0])
    print(mensaje, "\n")
    resultado_lexer.append(mensaje)
    t.lexer.skip(1)

def invalido(t, arg='Error Indefinido'):
    global resultado_lexer
    mensaje = "Linea %d -> Token %r invalido." % (t.lineno, t.value)
    if arg : mensaje.append(". Descripcion del error: "+arg)
    print(mensaje,"\n")
    resultado_lexer.append(mensaje)


nombreArchivo =  'code.slx'
ruta = str(os.getcwd())+"/archivos/"+nombreArchivo
fp = codecs.open(ruta,"r","utf-8")
codigoArchivo = fp.read()
fp.close()

analizadorLexico = lex.lex()
