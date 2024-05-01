from environment.symbol import Symbol
from environment.types import ExpressionType
from interfaces.expression import Expression
from expressions.access import Access

class FuncionEmbebida(Expression):
    def __init__(self, line, col, idVar, tipoFuncion):
        self.line = line
        self.col = col
        self.idVar = idVar
        self.tipoFuncion = tipoFuncion

    #FuncionEmbebida(linea, columna, idVar, tipoFuncion)
    def ejecutar(self, ast, env):
        #idVar sera una expresion de tipo Access, o un primitivo
        if(isinstance(self.idVar, Access)):
            #Obtiene el simbolo de la variable con el idVar
            symVar = self.idVar.ejecutar(ast, env) #Viene un acceso y obtiene el simbolo asociado
            if(self.tipoFuncion == 'pF'): #parseFloat
                if(symVar.type == ExpressionType.STRING):
                    valorFloat = float(symVar.value)
                    return Symbol(self.line, self.col, valorFloat, ExpressionType.FLOAT)
                return None
            elif(self.tipoFuncion == 'pI'):
                if(symVar.type == ExpressionType.STRING):
                    valorInt = int(symVar.value)
                    return Symbol(self.line, self.col, valorInt, ExpressionType.INTEGER)
                return None
            elif(self.tipoFuncion == 'tS'):
                valorStr = str(symVar.value)
                return Symbol(self.line, self.col, valorStr, ExpressionType.STRING)
            elif(self.tipoFuncion == 'tU'):
                if(symVar.type == ExpressionType.STRING):
                    valorToUpper = symVar.value.upper()
                    return Symbol(self.line, self.col, valorToUpper, ExpressionType.STRING)
                return None
            elif(self.tipoFuncion == 'tL'):
                if(symVar.type == ExpressionType.STRING):
                    valorToLower = symVar.value.lower()
                    return Symbol(self.line, self.col, valorToLower, ExpressionType.STRING)
                return None
            elif(self.tipoFuncion == 'tO'):
                tipoDato = ""
                if(symVar.type == ExpressionType.INTEGER):
                    tipoDato = "number"
                elif(symVar.type == ExpressionType.FLOAT):
                    tipoDato = "float"
                elif(symVar.type == ExpressionType.CHAR):
                    tipoDato = "char"
                elif(symVar.type == ExpressionType.STRING):
                    tipoDato = "string"
                elif(symVar.type == ExpressionType.ARRAY):
                    tipoDato = "array"
                elif(symVar.type == ExpressionType.BOOLEAN):
                    tipoDato = "boolean"
                elif(symVar.type == ExpressionType.MATRIZ):
                    tipoDato = "matriz"
                return Symbol(self.line, self.col, tipoDato, ExpressionType.STRING)
        else: #El self.idVar es un primitivo
            symVar = self.idVar
            if(self.tipoFuncion == 'pF'): #parseFloat
                if(symVar.type == ExpressionType.STRING):
                    valorFloat = float(symVar.value)
                    return Symbol(self.line, self.col, valorFloat, ExpressionType.FLOAT)
                return None
            elif(self.tipoFuncion == 'pI'):
                if(symVar.type == ExpressionType.STRING):
                    valorInt = int(symVar.value)
                    return Symbol(self.line, self.col, valorInt, ExpressionType.INTEGER)
                return None
            elif(self.tipoFuncion == 'tS'):
                valorStr = str(symVar.value)
                return Symbol(self.line, self.col, valorStr, ExpressionType.STRING)
            elif(self.tipoFuncion == 'tU'):
                if(symVar.type == ExpressionType.STRING):
                    valorToUpper = symVar.value.upper()
                    return Symbol(self.line, self.col, valorToUpper, ExpressionType.STRING)
                return None
            elif(self.tipoFuncion == 'tL'):
                if(symVar.type == ExpressionType.STRING):
                    valorToLower = symVar.value.lower()
                    return Symbol(self.line, self.col, valorToLower, ExpressionType.STRING)
                return None
            elif(self.tipoFuncion == 'tO'):
                tipoDato = ""
                if(symVar.type == ExpressionType.INTEGER):
                    tipoDato = "number"
                elif(symVar.type == ExpressionType.FLOAT):
                    tipoDato = "float"
                elif(symVar.type == ExpressionType.CHAR):
                    tipoDato = "char"
                elif(symVar.type == ExpressionType.STRING):
                    tipoDato = "string"
                elif(symVar.type == ExpressionType.ARRAY):
                    tipoDato = "array"
                elif(symVar.type == ExpressionType.BOOLEAN):
                    tipoDato = "boolean"
                elif(symVar.type == ExpressionType.MATRIZ):
                    tipoDato = "matriz"
                return Symbol(self.line, self.col, tipoDato, ExpressionType.STRING)