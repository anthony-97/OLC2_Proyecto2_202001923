from interfaces.instruction import Instruction
from environment.execute import StatementExecuter
from environment.environment import Environment
from expressions.continue_statement import Continue
from environment.value import Value

class If(Instruction):
    def __init__(self, line, col, exp, block, listaElseIfs, listaInsElse):
        self.line = line
        self.col = col
        self.exp = exp
        self.block = block
        self.listaElseIfs = listaElseIfs
        self.listaInsElse = listaInsElse

    def ejecutar(self, ast, env, gen):
        gen.comment('Generando un If')
        temp = gen.new_temp()
        
        # Se imprime el "if" en el código de la expresion
        condition = self.exp.ejecutar(ast, env, gen)

        # Etiqueta de salida
        gen.comment("ETIQUETA DE SALIDA")
        newLabel = gen.new_label()

        gen.add_br()
        gen.comment('Agregando etiquetas verdaderas')
        # Se agregan las etiquetas verdaderas
        for lvl in condition.truelvl:
            gen.new_body_label(lvl)

        gen.add_br()
        gen.comment('Instrucciones del if')
        # Instrucciones If
        if_env = Environment(env, "IF")
        StatementExecuter(self.block, ast, if_env, gen)

       # Salto etiqueta de salida
        gen.add_br()
        gen.comment("Agregando etiquetas de salida")
        gen.add_jump(newLabel)
        
        gen.add_br()
        gen.comment("Agregando etiquetas falsas")
        # Se agregan las etiquetas falsas
        for lvl in condition.falselvl:
            
            """gen.add_br()
            gen.add_li('t3', str(self.entrarAlElse)) #Recuperando el valor en la direccion guardada
            gen.add_lw('a0', '0(t3)')
            gen.add_li('t0', '1')
            gen.add_beq('a0', 't0', lvl)"""
            gen.new_body_label(lvl)

            gen.add_br()
            gen.comment("Verificando si vienen elseifs")
            # Viene la lista de elseifs
            if self.listaElseIfs != None:
                for elseif in self.listaElseIfs:
                    elseif.salidaFlujo = newLabel
                    elseif.ejecutar(ast, env, gen) #Ejecuta cada elseif 

        
        gen.add_br()
        gen.comment("Generando un else") 
        #VIene un else
        if self.listaInsElse != None:
            else_env = Environment(env, "ELSE")
            StatementExecuter(self.listaInsElse, ast, else_env, gen)
        
        gen.comment("Generando etiqueta de salida 2")
        # Etiqueta de salida
        gen.new_body_label(newLabel)
        return None