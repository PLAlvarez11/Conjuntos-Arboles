class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Función para construir un árbol binario basado en una expresión
def build_binary_tree(expression):
    root = TreeNode(expression)
    return root  # Simplificado para el ejemplo

# Funciones de operaciones de conjuntos
def union(set_a, set_b):
    return set_a.union(set_b)

def intersection(set_a, set_b):
    return set_a.intersection(set_b)

def difference(set_a, set_b):
    return set_a.difference(set_b)

def main():
    print("Bienvenido al sistema de Operaciones de Conjuntos y Árbol Binario")
    
    # Solicitar la entrada de conjuntos
    a_input = input("Introduce el conjunto A (ejemplo: 1,2,3): ")
    b_input = input("Introduce el conjunto B (ejemplo: 3,4,5): ")
    
    # Convertir la entrada en sets
    set_a = set(map(int, a_input.split(',')))
    set_b = set(map(int, b_input.split(',')))
    
    # Mostrar las opciones de operaciones
    print("\nElige una operación:")
    print("1. Unión")
    print("2. Intersección")
    print("3. Diferencia")
    
    opcion = input("Introduce el número de la operación: ")

    if opcion == '1':
        resultado = union(set_a, set_b)
        operacion = 'Unión'
    elif opcion == '2':
        resultado = intersection(set_a, set_b)
        operacion = 'Intersección'
    elif opcion == '3':
        resultado = difference(set_a, set_b)
        operacion = 'Diferencia'
    else:
        print("Opción no válida")
        return

    print(f"\nResultado de la {operacion}: {resultado}")
    
    # Construir un árbol binario (representación simple)
    expression = f"{set_a} {operacion} {set_b}"
    tree = build_binary_tree(expression)
    print(f"Árbol Binario generado para la expresión: {tree.value}")

if __name__ == "__main__":
    main()
