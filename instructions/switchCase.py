from interfaces.instruction import Instruction
from environment.execute import StatementExecuter
from environment.environment import Environment
from expressions.continue_statement import Continue

#SwitchCase(linea,columna,expresion,listaCasos,insDefault)

class SwitchCase(Instruction):
    def __init__(self, line, col, exp, listaCasos, insDefault):
        self.line = line
        self.col = col
        self.exp = exp
        self.listaCasos = listaCasos
        self.insDefault = insDefault

    def ejecutar(self, ast, env, gen):
        gen.comment('Generando un SwitchCase')
        temp = gen.new_temp()
    
        #variable = self.exp.ejecutar(ast, env, gen)
        # Etiqueta de salida
        gen.comment("ETIQUETA DE SALIDA")
        newLabel = gen.new_label()

        #gen.add_br()
        #gen.comment('Agregando etiquetas verdaderas')
        # Se agregan las etiquetas verdaderas
        #for lvl in condition.truelvl:
        #    gen.new_body_label(lvl)

        #gen.add_br()
        #gen.comment('Instrucciones del if')
        # Instrucciones If
        #if_env = Environment(env, "IF")
        #StatementExecuter(self.block, ast, if_env, gen)

       # Salto etiqueta de salida
        #gen.add_br()
        #gen.comment("Agregando etiquetas de salida")
        #gen.add_jump(newLabel)
        
        gen.add_br()
        gen.comment("Agregando etiquetas falsas")
        # Se agregan las etiquetas falsas
        #for lvl in condition.falselvl:

        gen.add_br()
        gen.comment("Verificando si vienen casos")
        # Viene la lista de casos
        if self.listaCasos != None:
            for caso in self.listaCasos:
                caso.salidaFlujo = newLabel
                caso.direccionExpresion = self.exp
                caso.ejecutar(ast, env, gen) #Ejecuta cada case

        gen.add_br()
        gen.comment("Generando un default") 
        #VIene un default
        if self.insDefault != None:
            default = Environment(env, "DEFAULT")
            StatementExecuter(self.insDefault, ast, default, gen)
        
        gen.comment("Generando etiqueta de salida 2")
        # Etiqueta de salida
        gen.new_body_label(newLabel)
        return None