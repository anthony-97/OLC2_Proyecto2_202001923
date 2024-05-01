from interfaces.expression import Expression
from environment.types import ExpressionType
from expressions.primitive import Primitive

# IndexOf(linea, columna, idArray, elemento)

class IndexOf(Expression):
    def __init__(self, line, col, idArray, elemento):
        self.line = line
        self.col = col
        self.idArray = idArray
        self.elemento = elemento

    def ejecutar(self, ast, env):
        # Traer el arreglo
        simboloArreglo = env.getVariable(ast, self.idArray)
        # Validar tipo principal
        if simboloArreglo.type != ExpressionType.ARRAY:
            ast.setErrors('La variable no es un arreglo')
            return None
        simboloElemento = self.elemento.ejecutar(ast,env)
        #Recorriendo el array
        indiceArray = 0
        for elemento in simboloArreglo.value:
            if(simboloElemento.value == elemento.value):
                return Primitive(self.line, self.col, indiceArray, ExpressionType.INTEGER) # Retorna el indice del elemento buscado
            indiceArray += 1
        return Primitive(self.line, self.col, -1, ExpressionType.INTEGER) #Retorna -1 si no encontro