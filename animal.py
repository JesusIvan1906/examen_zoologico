import csv

class Animal:
    def __init__(self, datos_dict):
        
        self.datos = datos_dict
        self.nombre = datos_dict.get('Clase_id', 'Desconocido')
        self.clase_id = datos_dict.get('Clase_tipo', '0')

    def __str__(self):
       
        return f"Animal: {self.nombre.capitalize()} | ID Clase: {self.clase_id}"

    def __repr__(self):
        
        return f"Animal(nombre='{self.nombre}', clase='{self.clase_id}')"

def cargar_csv_a_lista(nombre_archivo):
    
    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}")
        return []

def guardar_lista_a_csv(nombre_archivo, lista_diccionarios):

    if not lista_diccionarios:
        return
    
    campos = lista_diccionarios[0].keys()
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(lista_diccionarios)