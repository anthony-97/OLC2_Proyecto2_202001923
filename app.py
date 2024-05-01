from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from parser.parser import Parser
from environment.ast import Ast
from environment.environment import Environment
from environment.generator import Generator
from environment.execute import RootExecuter

contenidoReporte = ""
# Se crea una instancia de la aplicación Flask

app = Flask(__name__)
CORS(app)

# Se define una ruta de Test
@app.route('/ping')
def saludo():
    return f'<h1>pong!</h1>'

@app.route('/interpreter', methods=['POST'])
def recibir_datos():
    # Obtención del código
    jsonObj = request.json
    input_data = jsonObj.get("code")
    # Creación del entorno global
    env = Environment(None, 'GLOBAL')
    # Creación del AST
    ast = Ast()
    # Creación del generador
    gen = Generator()
    # Creación del parser
    parser = Parser()
    # [inst1, inst2, inst2]
    instructionsArr = parser.interpretar(input_data)
    # Ejecución
    RootExecuter(instructionsArr, ast, env, gen)
    global contenidoReporte
    contenidoReporte = ast.generarReporteTablaSimbolos()
    # Estructurando respuesta
    res = {"result": True,"console":gen.get_final_code(),"errors":ast.getErrors()}
    return jsonify(res)

@app.route('/reportes', methods=['GET'])
def generar_reportes():
    with open('tablaSimbolos.html', 'w') as file:
        global contenidoReporte
        file.write(contenidoReporte)
    return 'Reportes generados exitosamente'

if __name__ == '__main__':
    app.run(debug=True)