from interfaces.instruction import Instruction
from environment.types import ExpressionType
from environment.symbol import Symbol

class Declaration(Instruction):
    def __init__(self, line, col, id, type, exp):
        self.line = line
        self.col = col
        self.id = id
        self.type = type
        self.exp = exp

    def asignarDato(tipo, linea, columna):
        datoDefecto = "" #Una cadena vacia, al final tendra el dato por defecto segun el tipoDato
        if(tipo == ExpressionType.INTEGER):
            datoDefecto = 0
        elif(tipo == ExpressionType.FLOAT):
            datoDefecto = 0.0
        elif(tipo == ExpressionType.STRING):
            datoDefecto = ""
        elif(tipo == ExpressionType.CHAR):
            datoDefecto = ''
        elif(tipo == ExpressionType.BOOLEAN):
            datoDefecto = True
        return Symbol(linea, columna, datoDefecto,tipo)

    def ejecutar(self, ast, env, gen):
        # Generar simbolo
        result = self.exp.ejecutar(ast, env, gen)
        sym = Symbol(self.line, self.col, self.id, self.type, result.value)
        # Validar tipo
        if result.type != self.type:
            ast.setErrors("Los tipos de dato son incorrectos")
            return
        # Agregar al entorno
        env.saveVariable(ast, self.id, sym)
        return None
    
"""    
    def ejecutar(self, ast, env):
        if(self.type == None): #El tipo no viene, declaracion con valor
            result = self.exp.ejecutar(ast,env) #Ya vendra con el tipo segun lo interpretado
        elif(self.exp == None): #La expresion no viene, declaracion con tipo y sin valor
            result = self.asignarDato(self.type, self.line, self.col) #Retorna un simbolo con el dato por defecto
        else: # Vienen los 3
            # Obtener simbolo
            result = self.exp.ejecutar(ast, env)
            # Validar tipo
            if result.type != self.type:
                if result.type == ExpressionType.INTEGER and self.type == ExpressionType.FLOAT: # Unica conversion implicita number a float
                    result.value = float(result.value)
                else:
                    print("Los tipos de datos no son correctos")
                    ast.setErrors("Los tipos de dato son incorrectos")
                    return
        # Agregar al entorno
        env.saveVariable(ast, self.id, result)
"""