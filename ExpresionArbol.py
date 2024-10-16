import re
import math

# Función para verificar si un operador es válido
def es_operador(c):
    return c in ['+', '-', '*', '/', '=']

# Convertir la expresión infija a postfija (notación polaca inversa)
def infija_a_postfija(expresion):
    stack = []
    salida = []
    
    # Usamos una expresión regular para extraer números con letras juntos y números de varios dígitos como un único token
    tokens = re.findall(r'\d+[a-zA-Z]*|\d+|\w+|[+*/=()-]', expresion)  # captura números, letras y operadores
    
    for token in tokens:
        if re.match(r'\d+[a-zA-Z]*|\d+|\w+', token):  # Si es un número con letra, solo número, o variable
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
    
    return ' '.join(salida)

# Función para verificar la precedencia de operadores
def precedencia(c):
    if c == '=':
        return 0
    if c == '+' or c == '-':
        return 1
    if c == '*' or c == '/':
        return 2
    return 0

# Construir el árbol binario desde la expresión postfija
def construir_arbol(postfija):
    stack = []
    tokens = postfija.split()  # Separar los tokens por espacio
    
    for token in tokens:
        if not es_operador(token):
            # Crear un nodo para el operando y apilarlo
            nodo = Nodo(token)
            stack.append(nodo)
        else:
            # Crear un nodo para el operador y apilarlo
            nodo = Nodo(token)
            
            # El hijo derecho es el último nodo en la pila
            nodo.derecho = stack.pop()
            
            # El hijo izquierdo es el siguiente en la pila
            nodo.izquierdo = stack.pop()
            
            # Apilar el nuevo subárbol
            stack.append(nodo)
    
    # El árbol completo estará en la parte superior de la pila
    return stack.pop()

# Función para imprimir el árbol con conexiones
def imprimir_arbol_con_lineas(nodo, nivel=0, prefijo="Root: "):
    if nodo is not None:
        # Mostrar el valor del nodo con un prefijo que indica el nivel
        print(" " * (nivel * 4) + prefijo + str(nodo.valor))
        
        # Si tiene hijos, imprimir los subárboles
        if nodo.izquierdo is not None or nodo.derecho is not None:
            if nodo.izquierdo is not None:
                imprimir_arbol_con_lineas(nodo.izquierdo, nivel + 1, "L--- ")
            else:
                print(" " * ((nivel + 1) * 4) + "L--- None")
            
            if nodo.derecho is not None:
                imprimir_arbol_con_lineas(nodo.derecho, nivel + 1, "R--- ")
            else:
                print(" " * ((nivel + 1) * 4) + "R--- None")

# Definir la clase Nodo
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

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
        # Imprime espacios en blanco si el nodo es nulo
        imprimir_nivel(None, nivel_actual + 1, nivel_objetivo, espacio_total // 2)
        imprimir_nivel(None, nivel_actual + 1, nivel_objetivo, espacio_total // 2)

# Metodo para impimir el arbl
def imprimir_arbol(nodo):
    h = altura(nodo)
    espacio_total = calcular_ancho(h) * 6  # Espacio entre nodos

    for nivel in range(1, h + 1):
        imprimir_nivel(nodo, 1, nivel, espacio_total)
        print()



def convertir(expresion):
    postfija = infija_a_postfija(expresion)

    # Construir el árbol binario
    arbol = construir_arbol(postfija)

    # Imprimir el árbl
    print("\nÁrbol construido:")
    imprimir_arbol(arbol)
