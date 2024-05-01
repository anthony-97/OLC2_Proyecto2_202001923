from interfaces.instruction import Instruction
from environment.symbol import Symbol

class Assignment(Instruction):
    def __init__(self, line, col, id, exp):
        self.line = line
        self.col = col
        self.id = id
        self.exp = exp

    def ejecutar(self, ast, env, gen):
        # Obtener valor
        result = self.exp.ejecutar(ast, env, gen)
        # Obteniendo la posicion
        sym = env.getVariable(ast, self.id)
        # Sustituyendo valor
        if 't' in str(result.value):
            gen.add_move('t0', str(result.value))
        else:
            gen.add_li('t0', str(result.value)) #carga a t0 el valor de la posicion de la expresion
        gen.add_lw('t1', '0(t0)')
        gen.add_li('t3', str(sym.position))
        gen.add_sw('t1', '0(t3)')
        gen.comment('Fin asignacion')
        return None
    
    #Metodo del anterior
    def ejecutarIncremento(self, ast, env, gen):
        # Obteniendo la posicion
        sym = env.getVariable(ast, self.id)
        # Sustituyendo valor
        """gen.comment('Agregando un primitivo numerico')
        gen.add_li('t0', str(self.value)) #Valor, el 1
        gen.add_li('t3', str(temp)) #La posicion del t3
        gen.add_sw('t0', '0(t3)') #Carga en la direccion de t3, el valor de t0
        """

        gen.add_li('a0', 1) #carga a a0 el valor de la posicion de la expresion, es decir, recupera el 1

        gen.add_li('a3', str(sym.position))
        gen.add_lw('a2', '0(a3)')
    
        gen.add_operation('add', 't1', 'a0', 'a2') #Ejecuta la suma 

        gen.add_li('t3', str(sym.position))
        gen.add_sw('t1', '0(t3)')
        gen.comment('Fin asignacion')
        return None