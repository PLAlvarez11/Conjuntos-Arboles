import math
import re

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

# Función para verificar si el carácter es un operador
def es_operador(c):
    return c in ['+', '-', '*', '/', '=']

# Función para obtener la precedencia de los operadores
def precedencia(c):
    if c == '=':
        return 0
    if c == '+' or c == '-':
        return 1
    if c == '*' or c == '/':
        return 2
    return 0

def infija_a_postfija(expresion):
    stack = []
    salida = []
    
    # Usamos una expresión regular para extraer números con letras juntos como un único token
    tokens = re.findall(r'\d+[a-zA-Z]+|\d+|\w+|[+*/=()-]', expresion)
    
    for token in tokens:
        if re.match(r'\d+[a-zA-Z]+|\d+|\w+', token):  # Si es un número con letra o un operando
            salida.append(token)
        elif es_operador(token):
            while (stack and precedencia(token) <= precedencia(stack[-1])):
                salida.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                salida.append(stack.pop())
            stack.pop()  # Eliminar el '(' de la pila
    
    # Vaciar el resto de la pila
    while stack:
        salida.append(stack.pop())
    
    return ''.join(salida)

# Función para construir el árbol binario desde una expresión
def construir_arbol(postfija):
    stack = []
    
    for c in postfija:
        if not es_operador(c):
            # Crear un nodo para el operando y apilarlo
            nodo = Nodo(c)
            stack.append(nodo)
        else:
            # Crear un nodo para el operador y apilarlo
            nodo = Nodo(c)
            
            # El hijo derecho es el último nodo en la pila
            nodo.derecho = stack.pop()
            
            # El hijo izquierdo es el siguiente en la pila
            nodo.izquierdo = stack.pop()
            
            # Apilar el nuevo subárbol
            stack.append(nodo)
    
    # El árbol completo estará en la parte superior de la pila
    return stack.pop()

# Metodo para validar la altura del nodo 
def altura(nodo):
    if nodo is None:
        return 0
    else:
        izquierda = altura(nodo.izquierdo)
        derecha = altura(nodo.derecho)
        return max(izquierda, derecha) + 1

# Función para calcular el ancho máximo del árbol
def calcular_ancho(nivel):
    return int(math.pow(2, nivel))

# Función para imprimir un nivel específico del árbol
def imprimir_nivel(nodo, nivel_actual, nivel_objetivo, espacio_total):
    if nivel_actual == nivel_objetivo:
        if nodo is not None:
            print(f"{nodo.valor}".center(espacio_total), end="")
        else:
            print(" ".center(espacio_total), end="")
        return

    if nodo is not None:
        imprimir_nivel(nodo.izquierdo, nivel_actual + 1, nivel_objetivo, espacio_total // 2)
        imprimir_nivel(nodo.derecho, nivel_actual + 1, nivel_objetivo, espacio_total // 2)
    else:
        # Imprime espacios en blanco si el nodo es None
        imprimir_nivel(None, nivel_actual + 1, nivel_objetivo, espacio_total // 2)
        imprimir_nivel(None, nivel_actual + 1, nivel_objetivo, espacio_total // 2)

# Función principal para imprimir el árbol de manera estructurada
def imprimir_arbol(nodo):
    h = altura(nodo)
    espacio_total = calcular_ancho(h) * 6  # Espacio entre nodos

    for nivel in range(1, h + 1):
        imprimir_nivel(nodo, 1, nivel, espacio_total)
        print()



def convertir(expresion):
    # Convertir la expresión infija a postfija
    postfija = infija_a_postfija(expresion)

    # Construir el árbol binario
    arbol = construir_arbol(postfija)

    # Imprimir el árbol en formato visual
    imprimir_arbol(arbol)