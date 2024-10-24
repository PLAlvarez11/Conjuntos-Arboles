def leer_conjunto(nombre):
    n = input(f"Introduce los Numeros del conjunto {nombre}, separados por espacios: ")
    #convertir elementos a entero
    conjunto = set(map(int, n.split()))
    return conjunto
#Operacion y muestra de cada conjunto
def operaciones_conjuntos(conjunto_A, conjunto_B):
    union = conjunto_A.union(conjunto_B)
    interseccion = conjunto_A.intersection(conjunto_B)
    
    diferencia = conjunto_A.difference(conjunto_B)
#--------------F\N---------------------------------
    print(f"\nUnión (A ∪ B): {union}")
    print(f"Intersección (A ∩ B): {interseccion}")
    print(f"Diferencia (A - B): {diferencia}")
if __name__ == "__main__":
    conjunto_A = leer_conjunto("A")
    conjunto_B = leer_conjunto("B") 
    operaciones_conjuntos(conjunto_A, conjunto_B)
