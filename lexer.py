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