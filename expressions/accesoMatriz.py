from interfaces.expression import Expression
from environment.types import ExpressionType

 # AccesoMatriz(linea, columna, idMatriz, listaIndices)

class AccesoMatriz(Expression):
    def __init__(self, line, col, idMatriz, listaIndices):
        self.line = line
        self.col = col
        self.idMatriz = idMatriz
        self.listaIndices = listaIndices

    def ejecutar(self, ast, env):
        # Traer la matriz, el idMatriz es un acceso que al interpretar, trae la matriz
        sym = self.idMatriz.ejecutar(ast, env)
        # Validar tipo principal
        if sym.type != ExpressionType.MATRIZ and sym.type != ExpressionType.ARRAY:
            ast.setErrors('La variable no es una matriz')
            return
        listaIndicesInt = []
        for ind in self.listaIndices:
            listaIndicesInt.append(ind.indice.value)
        # Retornar valor
        if sym.type == ExpressionType.ARRAY:
            return sym.value[listaIndicesInt[0]]
        return self.accederMatriz(sym.value, listaIndicesInt)

    def accederMatriz(self, matriz, listaIndices):
        elemento = matriz
        for indice in listaIndices:
            elemento = elemento.value[indice]
        return elemento
    
    def asignarValor(self, ast, env, simbolo):
        # Traer la matriz, el idMatriz es un acceso que al interpretar, trae la matriz
        sym = self.idMatriz.ejecutar(ast, env)
        # Validar tipo principal
        if sym.type != ExpressionType.MATRIZ and sym.type != ExpressionType.ARRAY:
            ast.setErrors('La variable no es una matriz')
            return
        listaIndicesInt = []
        for ind in self.listaIndices:
            listaIndicesInt.append(ind.indice.value)
        # Retornar valor
        if sym.type == ExpressionType.ARRAY:
            sym.value[listaIndicesInt[0]] = simbolo

        elemento = sym.value #Asigna la matriz pura, o sea, el aray de arrays, para poder asignar
        for indice in listaIndicesInt[:-1]:
            elemento = elemento.value[indice]
        elemento.value[listaIndicesInt[-1]] = simbolo