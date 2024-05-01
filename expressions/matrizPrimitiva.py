from interfaces.instruction import Instruction
from environment.types import ExpressionType
from environment.symbol import Symbol
from expressions.array import Array

#MatrizPrimitiva(linea, columna, arrays)
class MatrizPrimitiva(Instruction):
    def __init__(self, line, col, arrays):
        self.line = line
        self.col = col
        self.arrays = arrays

    def ejecutar(self, ast, env):
        # Array Principal
        arrPrincipal = Symbol(line=self.line, col=self.col, value=[], type=ExpressionType.ARRAY)
        for exp in self.arrays:
            arrayExpresion = exp.ejecutar(ast, env)
            arrPrincipal.value.append(arrayExpresion) #Inserta el arreglo en simbolo
        return Symbol(line=self.line, col=self.col, value=arrPrincipal, type=ExpressionType.MATRIZ)
        