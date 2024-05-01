from interfaces.expression import Expression
from environment.types import ExpressionType

class IndiceMatriz(Expression):
    def __init__(self, line, col, indice):
        self.line = line
        self.col = col
        self.indice = indice

    def ejecutar(self, ast, env):
        # Validar indice
        print("El self.indice = " + str(self.indice))
        indexVal = self.indice.ejecutar(ast, env)
        print("El indexVal es = " + str(indexVal))

        if indexVal.type != ExpressionType.INTEGER:
            ast.setErrors('El indice contiene un valor incorrecto')
            return
        # Retornar el indice en simbolo
        return indexVal.indice.value