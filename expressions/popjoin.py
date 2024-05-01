from interfaces.expression import Expression
from environment.types import ExpressionType
from expressions.primitive import Primitive

# PopJoin(linea, columna, idArray, tipoOp)

class PopJoin(Expression):
    def __init__(self, line, col, idArray, tipoOp):
        self.line = line
        self.col = col
        self.idArray = idArray
        self.tipoOp = tipoOp

    def ejecutar(self, ast, env):
        # Traer el arreglo
        simboloArreglo = env.getVariable(ast, self.idArray)
        # Validar tipo principal
        if simboloArreglo.type != ExpressionType.ARRAY:
            ast.setErrors('La variable no es un arreglo')
            return None
        if self.tipoOp == 0 : #Un pop
            if(len(simboloArreglo.value) == 0):
                return None #Arreglo vacio, retornar Nulo
            valorret = simboloArreglo.value.pop()
            print(valorret)
            print(valorret.value)
            return Primitive(self.line, self.col, valorret.value, valorret.type)
        elif self.tipoOp == 1 : #Un join
            arregloJuntado = ""
            contadorElementos = 0
            for elemento in simboloArreglo.value:
                if contadorElementos == len(simboloArreglo.value)-1 :
                    arregloJuntado += str(elemento.value) + " "
                else:
                    arregloJuntado += str(elemento.value) + ", "
                contadorElementos += 1
            return Primitive(self.line, self.col, arregloJuntado, ExpressionType.STRING)