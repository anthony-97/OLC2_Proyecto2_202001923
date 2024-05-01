from interfaces.expression import Expression
from environment.types import ExpressionType
from environment.symbol import Symbol
from environment.value import Value

class Operation(Expression):
    def __init__(self, line, col, operador, opL, opR):
        self.line = line
        self.col = col
        self.operador = operador
        self.opL = opL
        self.opR = opR

    def validarTipoDatoCorrectoRel(tp1, tp2, tDom): #Verifica si son tip
        if(tDom == ExpressionType.NULL or tDom == ExpressionType.BOOLEAN):
            return False
        else:
            if(tp1 != tp2): # No se pueden operar relacionalmente dos tipos diferentes
                return False
            else:
                return True

    def anadirCodigoBinarias(self, gen, op1, op2, tipoOp):
        gen.add_br()
        gen.comment('Realizando operacion -->> ' + tipoOp)
        if 't' in str(op1.value):
            gen.add_move('t3', str(op1.value))
        else:
            gen.add_li('t3', str(op1.value))
        gen.add_lw('t1', '0(t3)')
        if 't' in str(op2.value):
            gen.add_move('t3', str(op2.value))
        else:
            gen.add_li('t3', str(op2.value)) 
        gen.add_lw('t2', '0(t3)')

    def anadirCodigoUnarias(self, gen, op1, tipoOp):
        gen.add_br()
        gen.comment('Realizando operacion -->> ' + tipoOp)
        if 't' in str(op1.value):
            gen.add_move('t3', str(op1.value))
        else:
            gen.add_li('t3', str(op1.value))
        gen.add_lw('t1', '0(t3)')
        

    def ejecutar(self, ast, env, gen):
        temp = 0 #Inicializando en 0 
        if self.operador != "-u": #Si no es un -, entonces si generar el corrimiento
            temp = gen.new_temp()
        op1 = op2 = ""
        # Ejecución de operandos
        if self.opL != None and (self.operador != "&&" and self.operador != "||" and self.operador != "!"):
            op1 = self.opL.ejecutar(ast, env, gen)
        if self.opR != None and (self.operador != "&&" and self.operador != "||" and self.operador != "!"):
            op2 = self.opR.ejecutar(ast, env, gen)

        if self.operador == "+": #Suma
            self.anadirCodigoBinarias(gen, op1, op2, "+") #Anade codigo necesario para la suma
            gen.add_operation('add', 't0', 't1', 't2')
            gen.add_li('t3', str(temp))
            gen.add_sw('t0', '0(t3)')
            return  Value(str(temp), True, ExpressionType.INTEGER, [], [], [])
        
        if self.operador == "-": #Resta
            self.anadirCodigoBinarias(gen, op1, op2, "-") #Anade codigo necesario para la resta
            gen.add_operation('sub', 't0', 't1', 't2')
            gen.add_li('t3', str(temp))
            gen.add_sw('t0', '0(t3)')
            return  Value(str(temp), True, ExpressionType.INTEGER, [], [], [])
        
        if self.operador == "*": #Multiplicacion
            self.anadirCodigoBinarias(gen, op1, op2, "*") #Anade codigo necesario para la multiplicacion
            gen.add_operation('mul', 't0', 't1', 't2')
            gen.add_li('t3', str(temp))
            gen.add_sw('t0', '0(t3)')

            return  Value(str(temp), True, ExpressionType.INTEGER, [], [], [])
        
        if self.operador == "/": #Division
            self.anadirCodigoBinarias(gen, op1, op2, "/") #Anade codigo necesario para la division
            gen.add_operation('div', 't0', 't1', 't2')
            gen.add_li('t3', str(temp))
            gen.add_sw('t0', '0(t3)')

            return  Value(str(temp), True, ExpressionType.INTEGER, [], [], [])
        
        #Modulo
        if self.operador == "%": # Módulo
            self.anadirCodigoBinarias(gen, op1, op2, "%") # Añade código necesario para el módulo
            gen.add_operation('rem', 't0', 't1', 't2')
            gen.add_li('t3', str(temp))
            gen.add_sw('t0', '0(t3)')
            return Value(str(temp), True, ExpressionType.INTEGER, [], [], [])
        #Negativo
        if self.operador == "-u": # Negativo
            self.anadirCodigoUnarias(gen, op1, "!") # Añade código necesario para el negativo
            gen.add_operation('neg', 't0', 't1') # Negativo en RISC-V
            gen.add_sw('t0', '0(t3)')
            return Value(str(temp), True, ExpressionType.INTEGER, [], [], [])
        
        #Logicas
        if self.operador == "<":
            self.anadirCodigoBinarias(gen, op1, op2, "<") #Anade codigo necesario para el menor que
            # Generando etiquetas
            trueLvl = gen.new_label()
            falseLvl = gen.new_label()
            # Agregando condición
            gen.add_blt('t1', 't2', trueLvl)
            # Agregando salto
            gen.add_jump(falseLvl)
            # Result
            result = Value("", False, ExpressionType.BOOLEAN, [], [], [])
            result.truelvl.append(trueLvl)
            result.falselvl.append(falseLvl)
            return result
        
        if self.operador == ">":
            self.anadirCodigoBinarias(gen, op1, op2, ">") #Anade codigo necesario para el mayor que
            # Generando etiquetas
            trueLvl = gen.new_label()
            falseLvl = gen.new_label()
            # Agregando condición
            gen.add_bgt('t1', 't2', trueLvl)
            # Agregando salto
            gen.add_jump(falseLvl)
            # Result
            result = Value("", False, ExpressionType.BOOLEAN, [], [], [])
            result.truelvl.append(trueLvl)
            result.falselvl.append(falseLvl)
            return result

        if self.operador == ">=":
            self.anadirCodigoBinarias(gen, op1, op2, ">=") #Anade codigo necesario para el mayigual que
            # Generando etiquetas
            trueLvl = gen.new_label()
            falseLvl = gen.new_label()
            # Agregando condición
            gen.add_bge('t1', 't2', trueLvl)
            # Agregando salto
            gen.add_jump(falseLvl)
            # Result
            result = Value("", False, ExpressionType.BOOLEAN, [], [], [])
            result.truelvl.append(trueLvl)
            result.falselvl.append(falseLvl)
            return result
        
        if self.operador == "<=":
            self.anadirCodigoBinarias(gen, op1, op2, "<=") #Anade codigo necesario para el menigual que
            # Generando etiquetas
            trueLvl = gen.new_label()
            falseLvl = gen.new_label()
            # Agregando condición
            gen.add_blez1('t1', 't2', trueLvl)
            # Agregando salto
            gen.add_jump(falseLvl)
            # Result
            result = Value("", False, ExpressionType.BOOLEAN, [], [], [])
            result.truelvl.append(trueLvl)
            result.falselvl.append(falseLvl)
            return result

        if self.operador == "==":
            self.anadirCodigoBinarias(gen, op1, op2, "==") #Anade codigo necesario para el igual que
            # Generando etiquetas
            trueLvl = gen.new_label()
            falseLvl = gen.new_label()
            # Agregando condición
            gen.add_beq('t1', 't2', trueLvl)
            # Agregando salto
            gen.add_jump(falseLvl)
            # Result
            result = Value("", False, ExpressionType.BOOLEAN, [], [], [])
            result.truelvl.append(trueLvl)
            result.falselvl.append(falseLvl)
            return result
        
        if self.operador == "!=":
            self.anadirCodigoBinarias(gen, op1, op2, "!=") #Anade codigo necesario para el dif que
            # Generando etiquetas
            trueLvl = gen.new_label()
            falseLvl = gen.new_label()
            # Agregando condición
            gen.add_bne('t1', 't2', trueLvl)
            # Agregando salto
            gen.add_jump(falseLvl)
            # Result
            result = Value("", False, ExpressionType.BOOLEAN, [], [], [])
            result.truelvl.append(trueLvl)
            result.falselvl.append(falseLvl)
            return result

        #Logicas
        if self.operador == "&&":
            # Ejecución de operandos
            gen.add_br()
            gen.comment('Realizando operacion and')
            # Ejecución de primer operando
            op1 = self.opL.ejecutar(ast, env, gen)
            # Se agregan las etiquetas verdaderas
            for lvl in op1.truelvl:
                gen.new_body_label(lvl)
            # Ejecución de segundo operando
            op2 = self.opR.ejecutar(ast, env, gen)
            # Result
            result = Value("", False, ExpressionType.BOOLEAN, [], [], [])
            result.truelvl.extend(op2.truelvl)
            result.falselvl.extend(op1.falselvl)
            result.falselvl.extend(op2.falselvl)

            return result
        
        if self.operador == "||":
            # Ejecución de operandos
            gen.add_br()
            gen.comment('Realizando operacion or')
            # Ejecución de primer operando
            op1 = self.opL.ejecutar(ast, env, gen)
            # Se agregan las etiquetas falsas
            for lvl in op1.falselvl:
                gen.new_body_label(lvl)
            # Ejecución de segundo operando
            op2 = self.opR.ejecutar(ast, env, gen)
            # Result
            result = Value("", False, ExpressionType.BOOLEAN, [], [], [])
            result.truelvl.extend(op1.truelvl)
            result.truelvl.extend(op2.truelvl)
            result.falselvl.extend(op2.falselvl)

            return result
        
        if self.operador == "!":
            # Ejecución de operandos
            gen.add_br()
            gen.comment('Realizando operacion not')
            # Ejecución de primer operando
            op1 = self.opL.ejecutar(ast, env, gen)
            # Result
            result = Value("", False, ExpressionType.BOOLEAN, [], [], [])
            result.truelvl.extend(op1.falselvl)
            result.falselvl.extend(op1.truelvl)

            return result
        return None