import random

# Palabras aleatorias
palabras = ['hola', 'mundo', 'python', 'programación', 'UNIR', 'archivo', 'texto', 'lista', 'clase', 'método',
            'variable', 'función', 'biblioteca', 'programador', 'lenguaje', 'operador', 'condicional', 'iteración',
            'índice', 'cadena', 'grupo', 'entorno', 'booleano', 'verdadero', 'falso', 'lógica', 'if', 'else',
            'while', 'pull', 'github', 'request', 'fork', 'as', 'hola', 'santi']

# Crear words.txt y escribir palabras
with open('words.txt', 'w') as archivo:
    for _ in range(100):
        palabra = random.choice(palabras)
        archivo.write(palabra + '\n')
