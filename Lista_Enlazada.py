# Creamos la Clase que manejará el Nodo
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        # Empieza con el puntero en None al principio por ser la cabeza
        self.siguiente = None

class Lista_Enlazada:
    
    # Este es el nodo que se inicia de primero 
    def __init__(self):
        self.cabeza = None
        
    # Método para insertar un valor al final       
    def Insertar_Valor_Final(self, valor):          
        nuevo_Nodo = Nodo(valor)    
        # Si la lista está vacía (si en cabeza no hay nada)
        if not self.cabeza:
           self.cabeza = nuevo_Nodo 
        else:
            # Utilizamos la variable actual para tener el último nodo
            actual = self.cabeza
            # Avanza hasta el último nodo 
            while actual.siguiente: 
                actual = actual.siguiente
            actual.siguiente = nuevo_Nodo
    
    # Método para insertar un valor al inicio
    def Insertar_Valor_Inicio(self, valor):
        nuevo_Nodo = Nodo(valor)
        nuevo_Nodo.siguiente = self.cabeza
        self.cabeza = nuevo_Nodo

    # Método para eliminar el primer valor
    def Eliminar_Primer_Valor(self, valor):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.valor == valor:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True  # Valor eliminado
            anterior = actual
            actual = actual.siguiente

        return False  # Valor no encontrado

    # Método para buscar un valor en la lista
    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False
    
    # Método que imprime los valores de la lista
    def imprimir(self):
        actual = self.cabeza
        if not actual:
            print("La lista está vacía")
            return
        print("Lista enlazada:", end=" ")
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")
    
    # Método para contar los nodos de la lista
    def longitudLista(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador
    
    # Método para determinar si la lista está vacía
    def esta_vacia(self):
        return self.cabeza is None

    # Método para imprimir el último valor de la lista
    def imprimir_ultimo_valor(self):
        if not self.cabeza:
            print("La lista está vacía")
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        print(f"Último valor en la lista: {actual.valor}")

"""Esta línea asegura que el siguiente bloque solo se ejecuta si el archivo se corre directamente, y no cuando es importado como módulo en otro archivo"""
if __name__ == "__main__":
    lista = Lista_Enlazada()  # Creando el objeto lista
    
    # Leer datos y añadirlos a la lista
    datos = [10, 20, 30, 40]
    for dato in datos:
        lista.Insertar_Valor_Final(dato)
    
    # Pruebas
    lista.imprimir()  # Lista: 10 -> 20 -> 30 -> 40 -> None
    lista.Insertar_Valor_Inicio(5)
    lista.imprimir()  # Lista: 5 -> 10 -> 20 -> 30 -> 40 -> None
    print("Longitud de la lista:", lista.longitudLista())  # 5
    print("¿La lista está vacía?", lista.esta_vacia())  # False
    lista.imprimir_ultimo_valor()  # Último valor en la lista: 40