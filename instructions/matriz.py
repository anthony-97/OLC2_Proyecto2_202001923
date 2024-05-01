from interfaces.instruction import Instruction
from environment.types import ExpressionType

#Matriz(line, column, id, tipo, dimensiones, matriz, esConstante)
class Matriz(Instruction):
    def __init__(self, line, col, id, type, dimensiones, matriz, esConstante):
        self.line = line
        self.col = col
        self.id = id
        self.type = type
        self.dimensiones = dimensiones
        self.matriz = matriz
        self.esConstante = esConstante

    def ejecutar(self, ast, env):
        # Obtener simbolo de la matriz primitiva
        result = self.matriz.ejecutar(ast, env) #Retorna el simbolo de la matriz
        # Validar tipo principal
        if result.type != ExpressionType.MATRIZ and result.type != ExpressionType.ARRAY:
            ast.setErrors('La expresión no es una matriz')
            return
        # Validar dimensiones
        env.saveVariable(ast, self.id, result)

        #def validarTipos(array):
        #    for arr in array:
        #        if(arr.type == ExpressionType.ARRAY):
        #            resultado = self.validarTipos(arr.value)
        #            if resultado == False:
        #                return False
        #        else:
        #            if(arr.type != self.type):
        #                ast.setErrors('El arreglo contiene tipos incorrectos')
        #                return False