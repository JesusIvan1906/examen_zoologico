from animal import Animal, cargar_csv_a_lista, guardar_lista_a_csv

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

    dict_nombres_clases = {c['Clase_id']: c['Clase_tipo'] for c in datos_clases}

    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            print("\nClases disponibles:", dict_nombres_clases)
            id_buscado = input("Ingrese el ID de la clase a filtrar: ")
            print(f"\n--- Animales de la clase {id_buscado} ---")
            for a in animales_objetos:
                if a.clase_id == id_buscado:
                    print(a)

        elif opcion == '2':
            print("\nCaracterísticas: hair, feathers, eggs, milk, airborne, aquatic, predator, etc.")
            feat = input("¿Qué característica desea buscar?: ").lower()
            print(f"\n--- Animales con {feat} ---")
            for a in animales_objetos:
                
                if a.datos.get(feat) == '1':
                    print(a)

        elif opcion == '3':
            nombre = input("Nombre del nuevo animal: ").lower()
            print("Clases:", dict_nombres_clases)
            clase = input("Ingrese el ID de la clase: ")
           
            plantilla = {k: '0' for k in datos_zoo[0].keys()}
            plantilla['Clase_id'] = nombre
            plantilla['Clase_tipo'] = clase
            
            
            tiene_pelo = input("¿Tiene pelo? (s/n): ")
            plantilla['hair'] = '1' if tiene_pelo.lower() == 's' else '0'
            
            
            animales_objetos.append(Animal(plantilla))
            print(f"¡{nombre} agregado exitosamente!")

        elif opcion == '4':
           
            lista_final = [a.datos for a in animales_objetos]
            guardar_lista_a_csv('zoo.csv', lista_final)
            print("Datos guardados en zoo.csv. Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    ejecutar_programa()