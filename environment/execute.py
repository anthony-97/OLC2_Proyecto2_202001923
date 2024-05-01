from environment.types import ExpressionType

def RootExecuter(instructionList, ast, env, gen):
    for inst in instructionList:
        inst.ejecutar(ast, env, gen)

def StatementExecuter(instructionList, ast, env, gen):
    #print("Entorno en SE es >>> " + env.id + "y el anterior es>> " + env.previous.id)
    for inst in instructionList:
        res = inst.ejecutar(ast, env, gen)
        if res != None:
            if res.type == ExpressionType.RETURN:
                return res.value
            return res
    return None