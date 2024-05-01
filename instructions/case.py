from interfaces.instruction import Instruction
from environment.execute import StatementExecuter
from environment.environment import Environment
from expressions.continue_statement import Continue
from expressions.operation import Operation

#Caso(linea,columna,valor,instruccionesCaso)

class Caso(Instruction):
    def __init__(self, line, col, valor, block):
        self.line = line
        self.col = col
        self.valor = valor
        self.block = block
        self.direccionExpresion = 0 #Direccion de la expresion
        self.salidaFlujo = 0
        self.salidaPorBreak = 0


    def ejecutar(self, ast, env, gen): 
        gen.comment('Generando un Caso')
        # Se imprime el "caso" en el código de la expresion
        #                                               Acceso que deriva en Value  Primitivo que deriva en value
        condicion = Operation(self.line, self.col, "==", self.direccionExpresion, self.valor)
        condition = condicion.ejecutar(ast, env, gen)

        # Etiqueta de salida
        newLabel = gen.new_label()
        # Se agregan las etiquetas verdaderas
        for lvl in condition.truelvl:
            gen.new_body_label(lvl)

        # Instrucciones Caso
        caso_env = Environment(env, "Case")
        StatementExecuter(self.block, ast, caso_env, gen)
        temp = gen.new_temp()

        gen.add_br()
        gen.comment("SaltoSalidaCaso")
        # Salto etiqueta de salida
        gen.add_jump(self.salidaFlujo)

        gen.add_br()
        gen.comment("falsas caso")
        # Se agregan las etiquetas falsas
        for lvl in condition.falselvl:
            gen.new_body_label(lvl)
        # Etiqueta de salida

        gen.add_br()
        gen.comment("etiquetaSalidaCaso")
        #Generando etiqueta salida
        gen.new_body_label(newLabel)

        gen.comment("Fn Caso")
        return None

    """def ejecutar(self, ast, env, val):
        # Evaluar
        # print("Valor del caso es>> " + str(self.valor))
        #simbolo de la expresion del caso
        valorCaso = self.valor.ejecutar(ast, env)
        if valorCaso.value == val:
            # Crear entorno del Case
            case_env = Environment(env, "CASE")
            returnValue = StatementExecuter(self.block, ast, case_env)
            if returnValue != None:
                return returnValue
            # Entro al case, retornar True
            return True
        return None"""