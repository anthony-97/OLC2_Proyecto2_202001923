from interfaces.instruction import Instruction
from environment.execute import StatementExecuter
from environment.environment import Environment
from expressions.continue_statement import Continue

class ElseIf(Instruction):
    def __init__(self, line, col, exp, block):
        self.line = line
        self.col = col
        self.exp = exp
        self.block = block
        self.entrarAlElse = 0 #Sera un value, el mismo que el del if que viene
        self.salidaFlujo = ""

    def ejecutar(self, ast, env, gen): 
            gen.comment('Generando un ElseIf')
            # Se imprime el "if" en el código de la expresion
            condition = self.exp.ejecutar(ast, env, gen)
            # Etiqueta de salida
            newLabel = gen.new_label()
            # Se agregan las etiquetas verdaderas
            for lvl in condition.truelvl:
                gen.new_body_label(lvl)
            # Instrucciones If
            elseif_env = Environment(env, "ElseIF")
            StatementExecuter(self.block, ast, elseif_env, gen)
            temp = gen.new_temp()

            gen.add_br()
            gen.comment("SaltoSalidaELSEIF")
            # Salto etiqueta de salida
            gen.add_jump(self.salidaFlujo)

            gen.add_br()
            gen.comment("falsas elseif")
            # Se agregan las etiquetas falsas
            for lvl in condition.falselvl:
                gen.new_body_label(lvl)
            # Etiqueta de salida

            gen.add_br()
            gen.comment("etiquetaSalidaELseif")
            #Generando etiqueta salida
            gen.new_body_label(newLabel)

            gen.comment("Fn elseIf")
            return None
""""
#posibilidades de retorno []
    def ejecutar(self, ast, env):
        # Obtener simbolo
        validate = self.exp.ejecutar(ast, env)
        # Evaluar
        if validate.value:
            # Crear entorno del If
            elseif_env = Environment(env, "ELSEIF")
            returnValue = StatementExecuter(self.block, ast, elseif_env)
            # Entro al else if, retornar True y el retornValue
            return returnValue, True
        return None, None

"""
