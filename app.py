from datetime import datetime

# Estructura de datos para almacenar las tareas con IDs únicos
tareas = {}
proximo_id = 1

# Función para agregar una nueva tarea
def agregar_tarea():
    global proximo_id
    descripcion = input("Ingrese la descripción de la tarea: ")
    while True:
        fecha_limite = input("Ingrese la fecha límite (formato YYYY-MM-DD): ")
        try:
            fecha_limite = datetime.strptime(fecha_limite, "%Y-%m-%d")
            fecha_actual = datetime.now().date()
            if fecha_limite.date() < fecha_actual:
                print("La fecha límite no puede ser anterior a la fecha actual. Intente nuevamente.")
            else:
                break
        except ValueError:
            print("Fecha no válida. Use el formato YYYY-MM-DD.")
            continue

    tarea = {
        "descripcion": descripcion,
        "fecha_limite": fecha_limite,
        "estado": "pendiente",
    }
    tareas[proximo_id] = tarea
    proximo_id += 1
    print("Tarea agregada.")

# Función para listar todas las tareas
def listar_tareas():
    if not tareas:
        print("No hay tareas.")
        return
    for id_tarea, tarea in tareas.items():
        print(f"ID: {id_tarea}")
        print(f"Descripción: {tarea['descripcion']}")
        print(f"Fecha límite: {tarea['fecha_limite'].strftime('%Y-%m-%d')}")
        print(f"Estado: {tarea['estado']}")
        print("---")

# Función para completar una tarea y eliminarla
def completar_tarea():
    try:
        id_tarea = int(input("Ingrese el ID de la tarea a completar: "))
        if id_tarea in tareas:
            tareas[id_tarea]["estado"] = "completada"
            print("Tarea completada.")
            del tareas[id_tarea]
            print("Tarea eliminada.")
        else:
            print("ID de tarea no encontrado.")
    except ValueError:
        print("ID no válido.")

# Función para eliminar una tarea
def eliminar_tarea():
    try:
        id_tarea = int(input("Ingrese el ID de la tarea a eliminar: "))
        if id_tarea in tareas:
            del tareas[id_tarea]
            print("Tarea eliminada.")
        else:
            print("ID de tarea no encontrado.")
    except ValueError:
        print("ID no válido.")

# Menú principal
def mostrar_menu():
    opciones = {
        1: agregar_tarea,
        2: listar_tareas,
        3: completar_tarea,
        4: eliminar_tarea,
        5: salir,
    }
    
    while True:
        print("**Sistema de gestión de tareas**")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion in opciones:
                opciones[opcion]()
            else:
                print("Opción no válida.")
        except ValueError:
            print("Por favor, ingrese un número.")

def salir():
    print("¡Hasta luego!")
    exit()

# Ejecutar el menú
mostrar_menu()
