from interfaces.instruction import Instruction
from environment.types import ExpressionType

class Print(Instruction):
    def __init__(self, line, col, Exp):
        self.line = line
        self.col = col
        self.Exp = Exp

    def ejecutar(self, ast, env, gen):
        for exp in self.Exp:
            val = exp.ejecutar(ast, env, gen)
            if (val.type == ExpressionType.INTEGER):
                # Imprimiendo expresion
                gen.add_br()
                gen.comment('Imprimiendo')
                if 't' in str(val.value):
                    gen.add_move('t3', str(val.value))
                else:
                    gen.add_li('t3', str(val.value))
                gen.add_lw('a0', '0(t3)')
                gen.add_li('a7', '1')
                gen.add_system_call() #Llama al sistema con un ecall
            elif (val.type == ExpressionType.STRING):
                gen.add_br()
                if 't' in str(val.value) and len(str(val.value)) < 2: #El modo de carga a la memoria, para ver si se usa un li o mv
                    gen.add_move('a0', str(val.value))
                else:
                    gen.add_la('a0', str(val.value))
                gen.add_li('a7', '4')
                gen.add_system_call()
            elif (val.type == ExpressionType.BOOLEAN):
                gen.add_br()
                gen.comment("Imprimiendo")
                # Etiqueta de salida
                newLabel = gen.new_label()
                # Se agregan las etiquetas verdaderas
                for lvl in val.truelvl:
                    gen.new_body_label(lvl)
                # Instrucciones si viene verdadero
                gen.add_li('a0', '1')  # Carga el valor 1 en a0
                gen.add_li('a7', '1')  # Código de la interrupción del sistema para imprimir un carácter
                gen.add_system_call() #Llama al sistema con un ecall

                # Salto etiqueta de salida
                gen.add_jump(newLabel)
                # Se agregan las etiquetas falsas
                for lvl in val.falselvl:
                    gen.new_body_label(lvl)
                # Instrucciones si viene falso
                gen.add_li('a0', '0')  # Carga el valor 1 en a0
                gen.add_li('a7', '1')  # Código de la interrupción del sistema para imprimir un carácter
                gen.add_system_call() #Llama al sistema con un ecall
                # Etiqueta de salida
                gen.new_body_label(newLabel)
        # Imprimiendo salto de linea
        gen.add_br()
        gen.add_li('a0', '10')
        gen.add_li('a7', '11')
        gen.add_system_call()

        return None