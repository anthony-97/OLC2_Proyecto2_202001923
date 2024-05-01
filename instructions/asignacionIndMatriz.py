from interfaces.instruction import Instruction
from environment.symbol import Symbol
from environment.types import ExpressionType

#AsignacionIndMatriz(linea, columna, accesoMatriz, expresion)

class AsignacionIndMatriz(Instruction):
    def __init__(self, line, col, accesoMatriz, exp):
        self.line = line
        self.col = col
        self.accesoMatriz = accesoMatriz
        self.exp = exp

    def ejecutar(self, ast, env):
        # Obtener simbolo de la expresion
        result = self.exp.ejecutar(ast, env)
        # Editar simbolo en la matriz
        self.accesoMatriz.asignarValor(ast, env, result)

    def ejecutarIncremento(self, ast, env):
        # Obtener valor inicial
        inicial = env.getVariable(ast, self.id)
        # Obtener simbolo
        result = Symbol(line=self.line, col=self.col, value=inicial.value+self.exp, type=ExpressionType.INTEGER)
        # Editar simbolo
        env.setVariable(ast, self.id, result)
        #ast.setConsole("New = " + str(result.value))