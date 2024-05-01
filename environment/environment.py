from environment.symbol import Symbol
from environment.types import ExpressionType
from environment.simboloTabla import SimboloTabla

class Environment():
    def __init__(self, previous, id):
        self.previous = previous
        self.id = id
        self.tabla = {}
        self.interfaces = {}
        self.functions = {}

    def saveVariable(self, ast, id, symbol):
        if id in self.tabla:
            ast.setErrors(f"La variable {id} ya existe.")
            return
        ast.guardarSimbolo(SimboloTabla(id, self, symbol))
        self.tabla[id] = symbol

    def getVariable(self, ast, id):
        tmpEnv = self
        while True:
            if id in tmpEnv.tabla:
                return tmpEnv.tabla[id]
            if tmpEnv.previous == None:
                break
            else:
                tmpEnv = tmpEnv.previous
        ast.setErrors(f"La variable {id} no existe.")
        return Symbol(0, 0, '', ExpressionType.NULL, '')
    
    def obtenerValores(self):
        tmpEnv = self
        arrValores = []
        #Recorriendo el diccionario, usando la clave
        for clave in tmpEnv.tabla:
            arrValores.append(tmpEnv.tabla[clave])
        #Retornando el array ya lleno de los valores
        return arrValores
    
    def obtenerClaves(self):
        tmpEnv = self
        arrClaves = []
        #Recorriendo el diccionario, usando la clave
        for clave in tmpEnv.tabla:
            #Se crea un nuevo simbolo de tipo string que contendra la clave, es decir la key
            arrClaves.append(Symbol(0,0, "'"+str(clave)+"'", ExpressionType.STRING))
        #Retornando el array ya lleno de los valores
        return arrClaves

    def setVariable(self, ast, id, symbol):
        tmpEnv = self
        while True:
            if id in tmpEnv.tabla:
                tmpEnv.tabla[id] = symbol
                return symbol
            if tmpEnv.previous == None:
                break
            else:
                tmpEnv = tmpEnv.previous
        ast.setErrors(f"La variable {id} no existe.")
        return Symbol(0, 0, None, ExpressionType.NULL)

    def saveFunction(self, ast, id, function, linea, columna):
        if id in self.functions:
            ast.setErrors(f"Ya existe una función con el nombre {id}")
            return
        ast.guardarSimbolo(SimboloTabla(id, self, Symbol(linea, columna, function, 12)))
        self.functions[id] = function

    def getFunction(self, ast, id):
        tmpEnv = self
        while True:
            if id in tmpEnv.functions:
                return tmpEnv.functions[id]
            if tmpEnv.previous == None:
                break
            else:
                tmpEnv = tmpEnv.previous
        ast.setErrors(f"La función {id} no existe.")
        return {}

    def saveStruct(self, ast, id, struct, linea, columna):
        if id in self.interfaces:
            ast.setErrors(f"Ya existe una interface con el nombre {id}")
            return
        simb = Symbol(linea, columna, struct, ExpressionType.STRUCT)
        ast.guardarSimbolo(SimboloTabla(id, self, simb))
        self.interfaces[id] = struct

    def getStruct(self, ast, id):
        tmpEnv = self
        while True:
            if id in tmpEnv.interfaces:
                return tmpEnv.interfaces[id]
            if tmpEnv.previous == None:
                break
            else:
                tmpEnv = tmpEnv.previous
        ast.setErrors(f"La interfaz {id} no existe")
        return None

    def LoopValidation(self):
        tmpEnv = self
        while True:
            if tmpEnv.id == 'WHILE' or tmpEnv.id == 'FOR':
                return True
            if tmpEnv.previous == None:
                break
            else:
                tmpEnv = tmpEnv.previous
        return False
    
    def FunctionValidation(self):
        tmpEnv = self
        while True:
            if 'FUNCTION_' in tmpEnv.id:
                return True
            if tmpEnv.previous == None:
                break
            else:
                tmpEnv = tmpEnv.previous
        return False
    
    def getGlobalEnvironment(self):
        tmpEnv = self
        while True:
            if tmpEnv.previous == None:
                return tmpEnv
            else:
                tmpEnv = tmpEnv.previous