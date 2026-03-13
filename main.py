from Animal import Animal, cargar_csv_a_lista, guardar_lista_a_csv

def mostrar_menu():
    print("\n" + "="*30)
    print("      MENÚ ZOOLÓGICO")
    print("="*30)
    print("1. Listar por Clasificación (ID)")
    print("2. Listar por Característica")
    print("3. Agregar nuevo animal")
    print("4. Salir y Guardar")
    return input("Seleccione una opción: ")

def ejecutar_programa():
    
    datos_zoo = cargar_csv_a_lista('zoo.csv')
    datos_clases = cargar_csv_a_lista('clases.csv')
    
    animales_objetos = [Animal(d) for d in datos_zoo]

    dict_nombres_clases = {c['class_type']: c['class_category'] for c in datos_clases}

    