"""
Módulo de lógica de negocio
-----------------------------
Responsabilidad única: manipular las tareas (agregar, listar,
completar, eliminar) aplicando las reglas del negocio.

Este módulo NO imprime nada en pantalla ni pide datos por teclado:
solo recibe parámetros, devuelve resultados, y lanza excepciones
cuando algo sale mal. Así puede reutilizarse desde cualquier
interfaz (consola, API, tests) sin cambios.
"""

import datos


def agregar_tarea(descripcion):
    """Agrega una tarea nueva. Lanza ValueError si la descripción es inválida."""
    descripcion = descripcion.strip()
    if not descripcion:
        raise ValueError("La descripción de la tarea no puede estar vacía.")

    tarea = {"descripcion": descripcion, "completada": False}
    datos.tareas.append(tarea)
    return tarea


def obtener_tareas():
    """Devuelve la lista completa de tareas."""
    return datos.tareas


def completar_tarea(numero):
    """Marca como completada la tarea en la posición 'numero' (1-indexado)."""
    _validar_numero_tarea(numero)
    indice = numero - 1
    datos.tareas[indice]["completada"] = True
    return datos.tareas[indice]


def eliminar_tarea(numero):
    """Elimina y devuelve la tarea en la posición 'numero' (1-indexado)."""
    _validar_numero_tarea(numero)
    indice = numero - 1
    return datos.tareas.pop(indice)


def _validar_numero_tarea(numero):
    """Valida que el número de tarea sea un entero dentro del rango válido."""
    if not isinstance(numero, int):
        raise TypeError("El número de tarea debe ser un entero.")
    if not datos.tareas:
        raise IndexError("No hay tareas registradas.")
    if numero < 1 or numero > len(datos.tareas):
        raise IndexError(
            f"No existe una tarea con el número {numero}. "
            f"Elige un valor entre 1 y {len(datos.tareas)}."
        )
