# se Importan las herramientas de flask y json a usar
from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__) 
CORS(app)

@app.route("https://backend-pruebaipc.herokuapp.com/")
def saludo():
    return "<h1>Hola ya esta corriendo el backend</h1>"

# * Ruta 1


@app.route('https://backend-pruebaipc.herokuapp.com/analisisLexico', methods=['POST'])
def analisis_Lexico():
    contenido = request.json['frase']
    palabras = 0
    vocales = 0
    consonantes = 0

    contenido = contenido.lower()
    letras = list(contenido)
    for texto in letras:
        print(texto)
        if texto == "a" or texto == "e" or texto == "i" or texto == "o" or texto == "u":
            vocales = vocales + 1
        elif ord(texto) >= 33 and ord(texto) <= 126:
            consonantes = consonantes + 1

    palabras = len(contenido.split())

    print(f'palabras: {palabras}')
    print(f'vocales: {vocales}')
    print(f'consonantes: {consonantes}')
    return(jsonify({
        "palabras": palabras,
        "vocales": vocales,
        "consonantes": consonantes
    }))

# * Ruta 2


@app.route('https://backend-pruebaipc.herokuapp.com/numerosPrimos', methods=['POST'])
def numerosPrimos():
    print('Funciona la funcion')
    numeroInicial = int(request.json['numInf'])
    numeroFinal = int(request.json['numSup'])
    print(f'numI:{numeroInicial} y numF: {numeroFinal}')
    # *Solo llega un valor antes del deseado por eso el mas 1

        
    cont = 0
    for numero in range(numeroInicial, (numeroFinal+1)):
        #print(f'\nnumero: {numero}')
        acum = 0
        for c in range(1, (numero+1)):
            #print(f'Segundo for: {c}')
            residuo = (numero % c)
            if residuo == 0:
                acum = acum + 1
        #print(f'acum:{acum}')
        if acum == 2:
            acum = 0
            cont += 1
            #print(f'\ncont: {cont}\n')

    print(f'Hay uh total de: {cont} primos')
    return(jsonify({"primos": cont}))

# * Ruta 3


@app.route('https://backend-pruebaipc.herokuapp.com/calculadora_basica', methods=['POST'])
def calculadoraBasica():
    pass

# * Ruta 4


@app.route('https://backend-pruebaipc.herokuapp.com/ruta4', methods=['POST'])
def ruta4():
    pass

# *Ruta inicial


@app.route('/')
def index():
    return f'<h1>The server is on</h1>'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
