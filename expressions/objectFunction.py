from interfaces.instruction import Instruction
from environment.environment import Environment
from environment.symbol import Symbol
from environment.types import ExpressionType
from interfaces.expression import Expression

#ObjectFunction(linea, columna, idInterface, tipoFuncion)

class ObjectFunction(Expression):
    def __init__(self, line, col, idInterface, tipoFuncion):
        self.line = line
        self.col = col
        self.idInterface = idInterface
        self.tipoFuncion = tipoFuncion

    def ejecutar(self, ast, env):
        #Obtiene la interfaz es decir, el entorno en donde estan todos sus atributos
        envInterface = self.idInterface.ejecutar(ast, env)

        if(self.tipoFuncion == 0): #El tipo de funcion es values
            arrValores = envInterface.obtenerValores()
            return Symbol(self.line, self.col, arrValores, ExpressionType.ARRAY)
        else: #El tipo de funcion es keys
            arrClaves = envInterface.obtenerClaves()
            return Symbol(self.line, self.col, arrClaves, ExpressionType.ARRAY)
        
