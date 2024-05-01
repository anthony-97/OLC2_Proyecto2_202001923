from interfaces.instruction import Instruction
from environment.types import ExpressionType

#Push(linea, columna, idArray, elemento)

class Push(Instruction):
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
            ast.setErrors('La variable a la que se le aplico un push no es un arreglo')
            return
        # Pusheando el elemento
        simboloElemento = self.elemento.ejecutar(ast,env)
        simboloArreglo.value.append(simboloElemento)
        return None