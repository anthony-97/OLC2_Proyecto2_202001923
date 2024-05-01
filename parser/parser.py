# PLY Imports
import parser.ply.yacc as yacc
import parser.ply.lex as Lex


# Expressions imports
from environment.types import ExpressionType
from expressions.primitive import Primitive
from expressions.operation import Operation
from expressions.access import Access
from expressions.array import Array
from expressions.array_access import ArrayAccess
from expressions.break_statement import Break
from expressions.continue_statement import Continue
from expressions.return_statement import Return
from expressions.popjoin import PopJoin
from expressions.indexof import IndexOf
from expressions.arraylength import ArrayLength
from expressions.objectFunction import ObjectFunction

# Instructions imports
from instructions.print import Print
from instructions.declaration import Declaration
from instructions.constante import Constante
from instructions.assignment import Assignment

from instructions.array_declaration import ArrayDeclaration

from instructions.if_instruction import If
from instructions.elseif import ElseIf
from instructions.switchCase import SwitchCase
from instructions.case import Caso
from instructions.whileInstruction import While
from instructions.forRange import For
from instructions.push import Push

from instructions.matriz import Matriz
from expressions.accesoMatriz import AccesoMatriz
from expressions.indiceMatriz import IndiceMatriz
from expressions.matrizPrimitiva import MatrizPrimitiva
from instructions.asignacionIndMatriz import AsignacionIndMatriz

from expressions.call import Call
from expressions.interface_access import InterfaceAccess
from instructions.function import Function
from instructions.interface import Interface
from instructions.interface_declaration import InterfaceDeclaration
from expressions.FuncionEmbebida import FuncionEmbebida

class codeParams:
    def __init__(self, line, column):
        self.line = line
        self.column = column

#LEXICO
reserved_words = {
    'console': 'CONSOLE', 
    'log': 'LOG', 
    'false': 'FALSE',
    'true': 'TRUE',
    'var': 'VAR',
    'const': 'CONST',
    'float': 'FLOAT',
    'number': 'NUMBER',
    'string': 'STRING',
    'boolean': 'BOOL',
    'char': 'CHAR',
    'if' : 'IF',
    'else': 'ELSE',
    'switch': 'SWITCH',
    'case': 'CASE',
    'default': 'DEFAULT',
    'while' : 'WHILE',
    'for': 'FOR',
    'break' : 'BREAK',
    'continue' : 'CONTINUE',
    'return' : 'RETURN',
    'function' : 'FUNC',
    'push': 'PUSH',
    'pop': 'POP',
    'indexof': 'INDEXOF',
    'join': 'JOIN',
    'length': 'LENGTH',
    'interface' : 'INTERFACE',
    'object' : 'OBJECT',
    'keys' : 'KEYS',
    'values' : 'VALUES',
    'parsefloat' : 'PARSEFLOAT',
    'parseint' : 'PARSEINT',
    'tostring' : 'TOSTRING',
    'tolowercase' : 'TOLOWERCASE',
    'touppercase' : 'TOUPPERCASE',
    'typeof' : 'TYPEOF'
}

# Listado de tokens
tokens = [
    'PARIZQ',
    'PARDER',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'MODULO',
    'PUNTO',
    'DOSPTS',
    'COMA',
    'PYC',
    'CADENA',
    'ENTERO',
    'DECIMAL',
    'IG',
    'IGIG',
    'DIF',
    'CORIZQ',
    'CORDER',
    'LLAVEIZQ',
    'LLAVEDER',
    'MAYQUE',
    'MENQUE',
    'MAYIGUAL',
    'MENIGUAL',
    'AND',
    'OR',
    'NOT',
    'TERN',
    'ID'
] + list(reserved_words.values())

t_PARIZQ        = r'\('
t_PARDER        = r'\)'
t_MAS           = r'\+'
t_MENOS         = r'-'
t_POR           = r'\*'
t_DIVIDIDO      = r'/'
t_MODULO        = r'%'
t_PUNTO         = r'\.'
t_DOSPTS        = r':'
t_COMA          = r','
t_PYC           = r';'
t_IG            = r'='
t_IGIG          = r'=='
t_DIF           = r'!='
t_CORIZQ        = r'\['
t_CORDER        = r'\]'
t_LLAVEIZQ       = r'\{'
t_LLAVEDER       = r'\}'
t_MAYQUE        = r'>'
t_MENQUE        = r'<'
t_MAYIGUAL      = r'>='
t_MENIGUAL      = r'<='
t_AND           = r'&&'
t_OR            = r'\|\|'
t_NOT           = r'!'
t_TERN          = r'\?'

#Función de reconocimiento
#Ver cuando vendran caracteres de escape
def t_CADENA(t):
    #r'\"((.+?))*\"'
    r'\"[^"]*\"'
    try:
        strValue = str(t.value)
        line = t.lexer.lexdata.rfind('\n', 0, t.lexpos) + 1
        column = t.lexpos - line
        t.value = Primitive(line, column, strValue.replace('"', ''), ExpressionType.STRING)
        #print("Reconoci una cadena y su valor es: --" + strValue.replace('"', ''))
    except ValueError:
        print("Error al convertir string %d", t.value)
        t.value = Primitive(0, 0, None, ExpressionType.NULL)
    return t

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        floatValue = float(t.value)
        line = t.lexer.lexdata.rfind('\n', 0, t.lexpos) + 1
        column = t.lexpos - line
        t.value = Primitive(line, column, floatValue, ExpressionType.FLOAT)
    except ValueError:
        print("Error al convertir a decimal %d", t.value)
        t.value = Primitive(0, 0, None, ExpressionType.NULL)
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        intValue = int(t.value)
        line = t.lexer.lexdata.rfind('\n', 0, t.lexpos) + 1
        column = t.lexpos - line
        t.value = Primitive(line, column, intValue, ExpressionType.INTEGER)
    except ValueError:
        print("Error al convertir a entero %d", t.value)
        t.value = Primitive(0, 0, None, ExpressionType.NULL)
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved_words.get(t.value.lower(),'ID')
    return t

t_ignore = " \t"

t_ignore_COMMENTLINE = r'\/\/.*'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_ignore_COMMENTBLOCK(t):
    r'\/\*[^*]*\*+(?:[^/*][^*]*\*+)*\/'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print("Error Léxico '%s'" % t.value[0])
    t.lexer.skip(1)

#SINTACTICO
precedence = (
    ('left', 'OR'),
    ('left','AND'),
    ('left','IGIG','DIF'),
    ('left','MENIGUAL','MAYIGUAL', 'MENQUE', 'MAYQUE'),
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO', 'MODULO'),
    ('left', 'NOT'),
    ('left', 'UMENOS')
)

#precedence left AND;
#precedence right NOT;
#precedence left MAYIGUAL,MENIGUAL, MAYQUE, MENQUE, IGUAL, NOIGUAL;
#precedence left MAS,MENOS,INCREMENTO, DECREMENTO;
#precedence left POR,DIVIDIDO,MODULO;
#precedence left POTENCIA;
#precedence right UMENOS;

#START
def p_start(t):
    '''s : block'''
    t[0] = t[1]

def p_instruction_block(t):
    '''block : block instruccion
            | instruccion '''
    if 2 < len(t):
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]

#Listado de instrucciones
def p_instruction_list(t):
    '''instruccion : print
                | ifinstruction 
                | ifElse
                | ifElseIfs
                | ifElseIfsElse
                | switchCase
                | switchCaseDefault
                | whileInstruction
                | forRange
                | declaration
                | declaracionValor
                | declaracionTipo
                | asignacion
                | asignacionIndMatriz
                | declaracionConstante
                | declConstanteValor
                | arrayDeclaration
                | matrizVariable
                | matrizConstante
                | arrayPush
                | breakstmt
                | continuestmt
                | returnstmt
                | functionstmt
                | interdeclaration
                | interfacecreation
                | interdeclarationConst
                | incrementoIns
                | call'''
    t[0] = t[1]

#Console.log
def p_instruccion_console(t):
    'print : CONSOLE PUNTO LOG PARIZQ expressionList PARDER PYC'
    params = get_params(t)
    t[0] = Print(params.line, params.column, t[5])

#Declaracion de variables
def p_instruccion_declaration(t): #Declaracion
    'declaration : VAR ID DOSPTS type IG expression PYC'
    params = get_params(t)
    #Declaration(linea,columna,id,tipo,expresion)
    t[0] = Declaration(params.line, params.column, t[2], t[4], t[6])

def p_instruccion_declarationValor(t): #Declaracion con valor
    'declaracionValor : VAR ID IG expression PYC'
    params = get_params(t)
    #Declaration(linea,columna,id,tipo,expresion)
    t[0] = Declaration(params.line, params.column, t[2], None, t[4])

def p_instruccion_declarationTipo(t): #Declaracion con tipo y sin valor
    'declaracionTipo : VAR ID DOSPTS type PYC'
    params = get_params(t)
    #Declaration(linea,columna,id,tipo,expresion)
    t[0] = Declaration(params.line, params.column, t[2], t[4], None)

#Asignacion
def p_instruccion_assignment(t):
    'asignacion : ID IG expression PYC'
    params = get_params(t)
    t[0] = Assignment(params.line, params.column, t[1], t[3])

def p_instruccion_asignacionIndMatriz(t):
    'asignacionIndMatriz : accesoMatriz IG expression PYC'
    params = get_params(t)
    #AsignacionIndMatriz(linea, columna, accesoMatriz, expresion)
    t[0] = AsignacionIndMatriz(params.line, params.column, t[1], t[3])

#Declaracion de constantes
def p_instruccion_declarationConstante(t): #Constante con tipo y valor
    'declaracionConstante : CONST ID DOSPTS type IG expression PYC'
    params = get_params(t)
    #Constante(linea,columna,id,tipo,expresion)
    t[0] = Constante(params.line, params.column, t[2], t[4], t[6])

def p_instruccion_declarationConstanteValor(t): #Constante con solo valor
    'declConstanteValor : CONST ID IG expression PYC'
    params = get_params(t)
    #Constante(linea,columna,id,tipo,expresion)
    t[0] = Constante(params.line, params.column, t[2], None, t[4])

#Array-Vectores
#Declaracion de un array
def p_instruccion_array_declaration(t): #Declaracion de un array
    'arrayDeclaration : VAR ID DOSPTS type CORIZQ CORDER IG arrayPrimitivo PYC'
    params = get_params(t)
    t[0] = ArrayDeclaration(params.line, params.column, t[2], t[4], t[8])

#OperacionesArray
#push
def p_instruccion_arrayPush(t):
    'arrayPush : ID PUNTO PUSH PARIZQ expression PARDER PYC'
    params = get_params(t)
    #Push(linea, columna, idArray, elemento)
    t[0] = Push(params.line, params.column, t[1], t[5])

#Declaracion de una matriz
def p_instruccion_matriz_variable(t):
    'matrizVariable : VAR ID DOSPTS type corchetes IG matrizPrimitiva PYC'
    params = get_params(t)
    #Matriz(line, column, id, tipo, dimensiones, matriz, esConstante)
    t[0] = Matriz(params.line, params.column, t[2], t[4], len(t[5]), t[7], False)

#Declaracion de una matriz constante
def p_instruccion_matriz_constante(t):
    '''matrizConstante : CONST ID DOSPTS type corchetes IG matrizPrimitiva PYC
                        | CONST ID DOSPTS type corchetes IG arrayPrimitivo PYC'''
    params = get_params(t)
    #Matriz(line, column, id, tipo, dimensiones, matriz, esConstante)
    t[0] = Matriz(params.line, params.column, t[2], t[4], len(t[5]), t[7], True)

#Corchetes
def p_corchetes(t):
    '''corchetes : corchetes corchete
            | corchete '''
    if 2 < len(t): #Si len(t) > 2
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]

def p_corchete(t):
    '''corchete : CORIZQ CORDER'''
    params = get_params(t)
    t[0] = Primitive(params.line, params.column, "[]", ExpressionType.STRING)


# Estructuras de control
#If
def p_instruction_if(t):
    'ifinstruction : IF PARIZQ expression PARDER LLAVEIZQ block LLAVEDER'
    params = get_params(t)
    #If(linea,columna,condicion,bloque,listaElseIfs,listaInsElse)
    t[0] = If(params.line, params.column, t[3], t[6], None, None)

# If-Else
def p_instruction_ifElse(t):
    'ifElse : IF PARIZQ expression PARDER LLAVEIZQ block LLAVEDER ELSE LLAVEIZQ block LLAVEDER'
    params = get_params(t)
    #If(linea,columna,condicion,bloque,listaElseIfs,listaInsElse)
    t[0] = If(params.line, params.column, t[3], t[6], None, t[10])

# If-ElseIfs
def p_instruction_ifElseIfs(t):
    'ifElseIfs : IF PARIZQ expression PARDER LLAVEIZQ block LLAVEDER elseifs'
    params = get_params(t)
    #If(linea,columna,condicion,bloque,listaElseIfs,listaInsElse)
    t[0] = If(params.line, params.column, t[3], t[6], t[8], None)

# If-ElseIfs-Else
def p_instruction_ifElseIfsElse(t):
    'ifElseIfsElse : IF PARIZQ expression PARDER LLAVEIZQ block LLAVEDER elseifs ELSE LLAVEIZQ block LLAVEDER'
    params = get_params(t)
    #If(linea,columna,condicion,bloque,listaElseIfs,listaInsElse)
    t[0] = If(params.line, params.column, t[3], t[6], t[8], t[11])

#ElseIfs
def p_instruction_elseifs(t):
    '''elseifs : elseifs elseif
            | elseif '''
    if 2 < len(t): #Si len(t) > 2
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]

def p_instruction_elseif(t):
    '''elseif : ELSE IF PARIZQ expression PARDER LLAVEIZQ block LLAVEDER'''
    params = get_params(t)
    #ElseIf(linea,columna,condicion,bloque)
    t[0] = ElseIf(params.line, params.column, t[4], t[7])


#SwitchCase
def p_instruction_switchCase(t):
    'switchCase : SWITCH PARIZQ expression PARDER LLAVEIZQ casos LLAVEDER'
    params = get_params(t)
    #SwitchCase(linea,columna,expresion,listaCasos,insDefault)
    t[0] = SwitchCase(params.line, params.column, t[3], t[6], None)

#SwitchCase - default
def p_instruction_switchCaseDefault(t):
    'switchCaseDefault : SWITCH PARIZQ expression PARDER LLAVEIZQ casos DEFAULT DOSPTS block LLAVEDER'
    params = get_params(t)
    #SwitchCase(linea,columna,expresion,listaCasos,insDefault)
    t[0] = SwitchCase(params.line, params.column, t[3], t[6], t[9])

#Casos
def p_instruction_casos(t):
    '''casos : casos caso
            | caso '''
    if 2 < len(t): #Si len(t) > 2
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]

def p_instruction_caso(t):
    '''caso : CASE expression DOSPTS block'''
    params = get_params(t)
    #Caso(linea,columna,expresion,instruccionesCaso)
    t[0] = Caso(params.line, params.column, t[2], t[4])

#While
def p_instruction_whileInstruction(t):
    'whileInstruction : WHILE PARIZQ expression PARDER LLAVEIZQ block LLAVEDER'
    params = get_params(t)
    #While(linea,columna,condicion,bloque)
    t[0] = While(params.line, params.column, t[3], t[6])

#For Rango
def p_instruction_forRange(t):
    'forRange : FOR PARIZQ declaration expression PYC incremento PARDER LLAVEIZQ block LLAVEDER'
    params = get_params(t)
    #For(linea,columna,varControl,condicion,incremento,bloque)
    t[0] = For(params.line, params.column, t[3], t[4], t[6], t[9])

def p_instruction_incrementoIns(t):
    'incrementoIns : ID MAS MAS PYC'
    params = get_params(t)
    t[0] = Assignment(params.line, params.column, t[1], Primitive(params.line, params.column, 1, ExpressionType.INTEGER)) #Se le incrementa en 1 a la variable


def p_instruction_incremento(t):
    'incremento : ID MAS MAS'
    params = get_params(t)
    t[0] = Assignment(params.line, params.column, t[1], Primitive(params.line, params.column, 1, ExpressionType.INTEGER)) #Se le incrementa en 1 a la variable

# Funciones
def p_instruction_function(t):
    'functionstmt : FUNC ID funcparams functype LLAVEIZQ block LLAVEDER'
    params = get_params(t)
    t[0] = Function(params.line, params.column, t[2], t[3], t[4], t[6])

def p_instruction_function_params_list(t):
    '''funcparams : PARIZQ paramsList PARDER
                |  PARIZQ PARDER'''
    if len(t) > 3:
        t[0] = t[2]
    else:
        t[0] = []

def p_expression_param_list(t):
    '''paramsList : paramsList COMA ID DOSPTS type
                | ID DOSPTS type'''
    arr = []
    if len(t) > 5:
        param = {t[3] : t[5]}
        arr = t[1] + [param]
    else:
        param = {t[1] : t[3]}
        arr.append(param)
    t[0] = arr

def p_instruction_function_type(t):
    '''functype : DOSPTS type
                | '''
    if len(t) > 2:
        t[0] = t[2]
    else:
        t[0] = ExpressionType.NULL

 ##Llamada a funcion
def p_instruction_call_function(t):
    '''call : ID PARIZQ expressionList PARDER PYC
            | ID PARIZQ PARDER PYC'''
    params = get_params(t)
    if len(t) > 5:
        t[0] = Call(params.line, params.column, t[1], t[3])
    else:
        t[0] = Call(params.line, params.column, t[1], [])

#Return
def p_instruction_return(t):
    '''returnstmt : RETURN expression PYC
                | RETURN PYC'''
    params = get_params(t)
    if len(t) > 3:
        t[0] = Return(params.line, params.column, t[2])
    else:
        t[0] = Return(params.line, params.column, None)

#Break
def p_instruction_break(t):
    'breakstmt : BREAK PYC'
    params = get_params(t)
    t[0] = Break(params.line, params.column)

#Continue
def p_instruction_continue(t):
    'continuestmt : CONTINUE PYC'
    params = get_params(t)
    t[0] = Continue(params.line, params.column)

#Tipos de dato
def p_type_prod(t):
    '''type : NUMBER
            | FLOAT
            | STRING
            | BOOL
            | CHAR
            | ID
            | type corchete'''
    if t[1] == 'number':
        t[0] = ExpressionType.INTEGER
    elif t[1] == 'float': 
        t[0] = ExpressionType.FLOAT
    elif t[1] == 'string':
        t[0] = ExpressionType.STRING
    elif t[1] == 'boolean':
        t[0] = ExpressionType.BOOLEAN
    elif t[1] == 'char':
        t[0] = ExpressionType.CHAR
    elif len(t) > 2: #Es del tipo de dato array, para los param de las funciones
        t[0] = ExpressionType.ARRAY
    else: #Cuando venga en un tipo de dato en una interface, un id de otra interface
        t[0] = str(t[1])
    

#Interfaces
def p_instruction_interface_creation(t):
    'interfacecreation : INTERFACE ID LLAVEIZQ attributeList LLAVEDER'
    params = get_params(t)
    t[0] = Interface(params.line, params.column, t[2], t[4])

def p_instruction_interface_attribute(t):
    '''attributeList : attributeList ID DOSPTS type PYC
                | ID DOSPTS type PYC'''
    arr = []
    if len(t) > 5:
        param = {t[2] : t[4]}
        arr = t[1] + [param]
    else:
        param = {t[1] : t[3]}
        arr.append(param)
    t[0] = arr

def p_instruction_interface_declaration(t):
    'interdeclaration : VAR ID DOSPTS ID IG LLAVEIZQ interfaceContent LLAVEDER PYC'
    params = get_params(t)
    t[0] = InterfaceDeclaration(params.line, params.column, t[2], t[4], t[7])

def p_instruction_interface_declarationConst(t):
    'interdeclarationConst : CONST ID DOSPTS ID IG LLAVEIZQ interfaceContent LLAVEDER PYC'
    params = get_params(t)
    t[0] = InterfaceDeclaration(params.line, params.column, t[2], t[4], t[7])

def p_instruction_interface_content(t):
    '''interfaceContent : interfaceContent COMA ID DOSPTS expression
                | ID DOSPTS expression'''
    arr = []
    if len(t) > 5:
        param = {t[3] : t[5]}
        arr = t[1] + [param]
    else:
        param = {t[1] : t[3]}
        arr.append(param)
    t[0] = arr

# Expressions
def p_expression_list(t):
    '''expressionList : expressionList COMA expression
                    | expression '''
    arr = []
    if len(t) > 2:
        arr = t[1] + [t[3]]
    else:
        arr.append(t[1])
    t[0] = arr

# Expresiones aritmeticas, relacionales y lógicas
#NegacionUnaria
def p_expression_negacionUnaria(t): 
    'expression : MENOS expression %prec UMENOS'
    params = get_params(t)
    #Operation(linea,columna,tipoOp,opiIzq,opDer)
    t[0] = Operation(params.line, params.column, "-u", t[2], None)

#Suma
def p_expression_add(t):
    'expression : expression MAS expression'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, "+", t[1], t[3])

#Resta
def p_expression_sub(t):
    'expression : expression MENOS expression'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, "-", t[1], t[3])

#Multiplicacion
def p_expression_mult(t):
    'expression : expression POR expression'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, "*", t[1], t[3])

#Division
def p_expression_div(t):
    'expression : expression DIVIDIDO expression'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, "/", t[1], t[3])

#Modulo
def p_expression_mod(t):
    'expression : expression MODULO expression'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, "%", t[1], t[3])

#Es igual
def p_expression_esIgual(t):
    'expression : expression IGIG expression'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, "==", t[1], t[3])

#No igual
def p_expression_noIgual(t):
    'expression : expression DIF expression'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, "!=", t[1], t[3])

#Mayor que
def p_expression_mayorQue(t):
    'expression : expression MAYQUE expression'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, ">", t[1], t[3])

#Menor que
def p_expression_menorQue(t):
    'expression : expression MENQUE expression'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, "<", t[1], t[3])

#Mayor o igual
def p_expression_mayorIgual(t):
    'expression : expression MAYIGUAL expression'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, ">=", t[1], t[3])

#Menor o igual
def p_expression_menorIgual(t):
    'expression : expression MENIGUAL expression'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, "<=", t[1], t[3])

#Or
def p_expression_or(t):
    'expression : expression OR expression'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, "||", t[1], t[3])

#And
def p_expression_and(t):
    'expression : expression AND expression'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, "&&", t[1], t[3])

#Not
def p_expression_not(t):
    'expression : NOT expression'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, "!", t[2], None)

#Agrupacion
def p_expression_agrupacion(t):
    'expression : PARIZQ expression PARDER'
    t[0] = t[2]

# Expresion llamada a funcion
def p_expression_call_function(t):
    '''expression : ID PARIZQ expressionList PARDER
            | ID PARIZQ PARDER'''
    params = get_params(t)
    if len(t) > 4:
        t[0] = Call(params.line, params.column, t[1], t[3])
    else:
        t[0] = Call(params.line, params.column, t[1], [])

def p_booleano(t):
    '''booleano : TRUE 
                | FALSE'''
    params = get_params(t)
    if(t[1] == "true"):
        t[0] = Primitive(params.line, params.column, 1, ExpressionType.BOOLEAN)
    else:
        t[0] = Primitive(params.line, params.column, 0, ExpressionType.BOOLEAN)

def p_expression_primitiva(t):
    '''expression    : ENTERO
                    | DECIMAL
                    | CADENA
                    | booleano
                    | listArray
                    | accesoInterface
                    | accesoMatriz
                    | funcEspecialObject
                    | funcionEmbebida'''
    t[0] = t[1]

#pop y join
def p_expresion_arrayPopJoin(t):
    'expression : ID PUNTO popjoin PARIZQ PARDER'
    params = get_params(t)
    # PopJoin(linea, columna, idArray, tipoOp)
    t[0] = PopJoin(params.line, params.column, t[1], t[3])

# popjoin
def p_popjoin(t):
    '''popjoin : POP 
            | JOIN'''
    if t[1] == 'pop':
        t[0] = 0
    if t[1] == 'join': 
        t[0] = 1

def p_expresion_arrayIndexOf(t):
    'expression : ID PUNTO INDEXOF PARIZQ expression PARDER'
    params = get_params(t)
    # IndexOf(linea, columna, idArray, elemento)
    t[0] = IndexOf(params.line, params.column, t[1], t[5])

def p_expresion_arrayLength(t):
    'expression : ID PUNTO LENGTH'
    params = get_params(t)
    # ArrayLength(linea, columna, idArray)
    t[0] = ArrayLength(params.line, params.column, t[1])

#Array
def p_expression_array_primitiva(t):
    '''arrayPrimitivo : CORIZQ expressionList CORDER'''
    params = get_params(t)
    t[0] = Array(params.line, params.column, t[2])

#Matriz
def p_expression_matriz_primitiva(t):
    '''matrizPrimitiva : CORIZQ listaArrays CORDER'''
    params = get_params(t)
    #MatrizPrimitiva(linea, columna, arrays)
    t[0] = MatrizPrimitiva(params.line, params.column, t[2])
    
def p_expression_array_matricial(t):
    '''arrayMatricial : CORIZQ expressionList CORDER
                    | CORIZQ listaArrays CORDER'''
    params = get_params(t)
    t[0] = Array(params.line, params.column, t[2])

def p_expression_listaArrays(t):
    '''listaArrays : listaArrays COMA arrayMatricial
                    | arrayMatricial '''
    arr = []
    if len(t) > 2:
        arr = t[1] + [t[3]]
    else:
        arr.append(t[1])
    t[0] = arr

#Acceso a variables y acceso a Arrays
def p_expression_list_array(t):
    '''listArray : ID CORIZQ expression CORDER
                | ID'''
    params = get_params(t)
    if len(t) > 4: #El aux tiene > 3
        t[0] = ArrayAccess(params.line, params.column, t[1], t[3])
    else:
        print("Encontre un acceso")
        t[0] = Access(params.line, params.column, t[1])


def p_expresion_accesoInterface(t):
    '''accesoInterface : ID PUNTO ID'''
    params = get_params(t)
    t[0] = InterfaceAccess(params.line, params.column, Access(params.line, params.column, t[1]), t[3])
    print("Encontre un acceso a interfaz")

def p_expression_funcEspecialObject(t):
    '''funcEspecialObject : OBJECT PUNTO VALUES PARIZQ expression PARDER
                        | OBJECT PUNTO KEYS PARIZQ expression PARDER'''
    params = get_params(t)
    if(t[3] == 'values'): #0 para values
        #ObjectFunction(linea, columna, idInterface, tipoFuncion)
        t[0] = ObjectFunction(params.line, params.column, t[5], 0)
    else: #1 para keys
        t[0] = ObjectFunction(params.line, params.column, t[5], 1)

def p_expression_funcionEmbebida(t):
    '''funcionEmbebida : PARSEFLOAT PARIZQ expression PARDER
                        | PARSEINT PARIZQ expression PARDER
                        | ID PUNTO TOSTRING PARIZQ PARDER
                        | expression PUNTO TOSTRING PARIZQ PARDER
                        | ID PUNTO TOLOWERCASE PARIZQ PARDER
                        | ID PUNTO TOUPPERCASE PARIZQ PARDER
                        | TYPEOF ID'''
    params = get_params(t)
    #FuncionEmbebida(linea, columna, idVar, tipoFuncion)
    if str(t[1]) == 'parseFloat': #para parseFloat
        print(str(t[1]))
        t[0] = FuncionEmbebida(params.line, params.column, t[3], "pF")
    elif str(t[1]) == 'parseInt': #para parseInt
        t[0] = FuncionEmbebida(params.line, params.column, t[3], "pI")
    elif len(t) > 3:
        if str(t[3]) == 'toString': #para toString
            idVar = t[1]
            if not(isinstance(t[1], Primitive)): #Si no es un primitivo, es decir, es un acceso
                idVar = Access(params.line, params.column, str(t[1]))
                print(idVar.id)
            t[0] = FuncionEmbebida(params.line, params.column, idVar, "tS")
            print(t[0].idVar)
        elif str(t[3]) == 'toLowerCase':
            t[0] = FuncionEmbebida(params.line, params.column, Access(params.line, params.column, str(t[1])), "tL")
        elif str(t[3]) == 'toUpperCase':
            t[0] = FuncionEmbebida(params.line, params.column, Access(params.line, params.column, str(t[1])), "tU")
    elif str(t[1]) == 'typeof':
        t[0] = FuncionEmbebida(params.line, params.column, Access(params.line, params.column, str(t[2])), "tO")


#Acceso a una matriz
def p_expression_accesoMatriz(t):
    '''accesoMatriz : ID accesosMatriz'''
    params = get_params(t)
    # AccesoMatriz(linea, columna, idMatriz, listaIndices)
    t[0] = AccesoMatriz(params.line, params.column, Access(params.line, params.column, t[1]), t[2])

def p_accesosMatriz(t):
    '''accesosMatriz : accesosMatriz acceso 
            | acceso '''
    if 2 < len(t): #Si len(t) > 2
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]

def p_acceso(t):
    '''acceso : CORIZQ expression CORDER'''
    params = get_params(t)
    #IndiceMatriz(linea,columna,expresion)
    t[0] = IndiceMatriz(params.line, params.column, t[2])

#Errores
def p_error(p):
    if p:
        print(f"Error de sintaxis en línea {p.lineno}, columna {p.lexpos}: Token inesperado '{p.value}'")
    else:
        print("Error de sintaxis")

def get_params(t):
    line = t.lexer.lineno  # Obtener la línea actual desde el lexer
    lexpos = t.lexpos if isinstance(t.lexpos, int) else 0  # Verificar si lexpos es un entero
    column = lexpos - t.lexer.lexdata.rfind('\n', 0, lexpos) 
    return codeParams(line, column)

class Parser:
    def __init__(self):
        pass

    def interpretar(self, input):
        lexer = Lex.lex()
        parser = yacc.yacc()
        result = parser.parse(input)
        return result