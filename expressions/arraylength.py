from interfaces.expression import Expression
from environment.types import ExpressionType
from expressions.primitive import Primitive

#ArrayLength(linea, columna, idArray)

class ArrayLength(Expression):
    def __init__(self, line, col, idArray):
        self.line = line
        self.col = col
        self.idArray = idArray

    def ejecutar(self, ast, env):
        # Traer el arreglo
        simboloArreglo = env.getVariable(ast, self.idArray)
        # Validar tipo principal
        if simboloArreglo.type != ExpressionType.ARRAY:
            ast.setErrors('La variable no es un arreglo')
            return None
        return Primitive(self.line, self.col, len(simboloArreglo.value), ExpressionType.INTEGER) #Retorna el tamano del arreglo