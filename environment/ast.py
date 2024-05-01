from environment.types import ExpressionType
from environment.symbol import Symbol

class Ast():
    def __init__(self):
        self.instructions = []
        self.console = ""
        self.simbolos = []
        self.errors = []

    def setConsole(self, content):
        self.console += content + "\n"
    
    def getConsole(self):
        return self.console

    def addInstructions(self, instructions):
        self.instructions += instructions
    
    def getInstructions(self):
        return self.instructions
    
    def setErrors(self, errors):
        self.errors.append(errors)
    
    def getErrors(self):
        return self.errors
    
    def guardarSimbolo(self, simboloTabla):
        self.simbolos.append(simboloTabla)

    def generarReporteTablaSimbolos(self):
        contenido = ""
        for sym in self.simbolos: #Recorriendo la tabla
            if(isinstance(sym.simbolo, Symbol)):
                if(sym.simbolo.type == ExpressionType.INTEGER):
                    tipoDato = "number"
                elif(sym.simbolo.type == ExpressionType.FLOAT):
                    tipoDato = "float"
                elif(sym.simbolo.type == ExpressionType.CHAR):
                    tipoDato = "char"
                elif(sym.simbolo.type == ExpressionType.STRING):
                    tipoDato = "string"
                elif(sym.simbolo.type == ExpressionType.ARRAY):
                    tipoDato = "array"
                elif(sym.simbolo.type == ExpressionType.BOOLEAN):
                    tipoDato = "boolean"
                elif(sym.simbolo.type == ExpressionType.MATRIZ):
                    tipoDato = "matriz"
                elif(sym.simbolo.type == ExpressionType.STRUCT):
                    tipoDato = "interfaz"
                elif(sym.simbolo.type == 12):
                    tipoDato = "funcion"
                contenido += f"""<tr>
                                <td>{str(sym.id)}</td>
                                <td>{tipoDato}</td>
                                <td>{str(sym.entorno.id)}</td>
                                <td>{str(sym.simbolo.line)}</td>
                                <td>{str(sym.simbolo.col)}</td>
                            </tr>"""
            
            cuerpoHTML = f"""<!DOCTYPE html>
                            <html lang="es">
                            <head>
                                <meta charset="UTF-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                <title>Reportes</title>
                            </head>
                            <body>
                                <div>
                                    <table>
                                    <thead>
                                        <tr>
                                            <th style="background-color: #ADD8E6;">ID</th>
                                            <th style="background-color: #ADD8E6;">Tipo dato</th>
                                            <th style="background-color: #ADD8E6;">Ámbito</th>
                                            <th style="background-color: #ADD8E6;">Línea</th>
                                            <th style="background-color: #ADD8E6;">Columna</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                    {contenido}
                                    </tbody>
                                    </table>
                                </div>
                            </body>
                            </html>
                        """
            return cuerpoHTML