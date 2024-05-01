from interfaces.instruction import Instruction
from environment.environment import Environment
from environment.execute import StatementExecuter
from environment.types import ExpressionType
from expressions.continue_statement import Continue

    #For(linea,columna,varControl,condicion,incremento,bloque)
    
class For(Instruction):
    def __init__(self, line, col, exp, condicion, incremento, block):
        self.line = line
        self.col = col
        self.exp = exp
        self.condicion = condicion
        self.incremento = incremento # El incremento es una asignacion de id ++
        self.block = block

    def ejecutar(self, ast, env, gen):
        gen.comment('Generando un ciclo For')
        gen.add_br()
        gen.add_br()
        gen.comment("Declaracion de variable iteradora")
        self.exp.ejecutar(ast, env, gen)
        gen.comment("Agregando etiqueta de retorno")
        # Agregando etiqueta de retorno
        newLabel = gen.new_label()
        gen.new_body_label(newLabel)

        #Generando el primitivo de la variable iteradora
        # Generar declaracion de la variable iterador


        # Se imprime el "if" en el código de la expresion
        gen.add_br()
        gen.comment("Evaluando condicion")
        condition = self.condicion.ejecutar(ast, env, gen)
        # Se agregan las etiquetas verdaderas
        gen.add_br()
        gen.comment("Etiquetas verdaderas")
        for lvl in condition.truelvl:
            gen.new_body_label(lvl)

        gen.add_br()
        gen.comment("Instrucciones del for")
        # Instrucciones For
        for_env = Environment(env, "FOR")
        StatementExecuter(self.block, ast, for_env, gen)

        gen.add_br()
        gen.comment("Incrementando la variable iteradora")
        #Incrementando el contador
        self.incremento.ejecutarIncremento(ast, env, gen)

        gen.add_br()
        gen.comment("Salto etiqueta de retorno")
        # Salto etiqueta de retorno
        gen.add_jump(newLabel)

        gen.add_br()
        gen.comment("Agregando etiquetas falsas")
        # Se agregan las etiquetas falsas
        for lvl in condition.falselvl:
            gen.new_body_label(lvl)

        return None