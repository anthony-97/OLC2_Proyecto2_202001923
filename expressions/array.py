from interfaces.instruction import Instruction
from environment.types import ExpressionType
from environment.value import Value

class Array(Instruction):
    def __init__(self, line, col, list_exp):
        self.line = line
        self.col = col
        self.list_exp = list_exp

    def ejecutar(self, ast, env, gen):
        newArr = [] #Genera un nuevo array
        for var in self.list_exp:
            value = var.ejecutar(ast, env, gen) #Obtiene el valor (posicion) en donde se guarda cada elemento
            newArr.append(value.value) #Inserta el valor (posicion) en el array creado
        return  Value(newArr, False, ExpressionType.ARRAY, [], [], []) #Se basa en el tipo ExpressionType.Array para saber que el valor no es un temporal (pos. en memoria)