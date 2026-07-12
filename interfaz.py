"""
Módulo de interfaz de usuario
-------------------------------
Responsabilidad única: mostrar menús, pedir datos por teclado (input)
y mostrar resultados (print).

Aquí es donde se capturan los errores lanzados por el módulo de
lógica y se traducen en mensajes claros para el usuario. La lógica
de negocio y los datos no se tocan directamente desde aquí, solo
a través de las funciones que expone 'logica'.
"""

import logica


def mostrar_menu():
    print("\n===== SISTEMA DE TAREAS =====")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")


def _pedir_numero(mensaje):
    """Pide un número por teclado y lanza ValueError si no es válido."""
    valor = input(mensaje)
    try:
        return int(valor)
    except ValueError:
        raise ValueError(f"'{valor}' no es un número válido.")


def agregar_tarea():
    descripcion = input("Escribe la descripción de la tarea: ")
    try:
        tarea = logica.agregar_tarea(descripcion)
        print(f"Tarea '{tarea['descripcion']}' agregada correctamente.")
    except ValueError as error:
        print(f"Error: {error}")


def ver_tareas():
    tareas = logica.obtener_tareas()
    if not tareas:
        print("No hay tareas registradas.")
        return

    print("\n--- Lista de tareas ---")
    for indice, tarea in enumerate(tareas, start=1):
        estado = "✔ Completada" if tarea["completada"] else "✘ Pendiente"
        print(f"{indice}. {tarea['descripcion']} - {estado}")


def completar_tarea():
    ver_tareas()
    try:
        numero = _pedir_numero("\nIngresa el número de la tarea a completar: ")
        tarea = logica.completar_tarea(numero)
        print(f"Tarea '{tarea['descripcion']}' marcada como completada.")
    except (ValueError, IndexError, TypeError) as error:
        print(f"Error: {error}")


def eliminar_tarea():
    ver_tareas()
    try:
        numero = _pedir_numero("\nIngresa el número de la tarea a eliminar: ")
        tarea = logica.eliminar_tarea(numero)
        print(f"Tarea '{tarea['descripcion']}' eliminada.")
    except (ValueError, IndexError, TypeError) as error:
        print(f"Error: {error}")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            ver_tareas()
        elif opcion == "3":
            completar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
