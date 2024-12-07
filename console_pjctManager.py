import csv
from datetime import datetime
#import os



# Funciones para manejar el CSV
def cargar_proyectos():
    try:
        with open('proyectos.csv', mode='r') as archivo:
            reader = csv.DictReader(archivo)
            return list(reader)
    except FileNotFoundError:
        return []


def guardar_proyectos(proyectos_guardar):
    with open('proyectos.csv', mode='w', newline='') as archivo:
        fieldnames = ['Titulo', 'Codigo', 'Alcance', 'Fecha de inicio', 'Fecha de fin']
        writer = csv.DictWriter(archivo, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(proyectos_guardar)


# Funciones del menu
def ingresar_proyecto():
    titulo = input("Titulo: ")
    codigo = input("Codigo: ")
    if not verificar_codigo_unico(codigo):
        return
    alcance = input("Alcance (Nacional, Sectorial, Territorial, Institucional): ")
    if not verificar_alcance(alcance):
        return
    fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
    if not verificar_formato_fechas(fecha_inicio):
        return
    fecha_fin = input("Fecha de fin (YYYY-MM-DD): ")
    if not verificar_formato_fechas(fecha_fin):
        return
    proyectos.append({
        'Titulo': titulo,
        'Codigo': codigo,
        'Alcance': alcance,
        'Fecha de inicio': fecha_inicio,
        'Fecha de fin': fecha_fin
    })
    guardar_proyectos(proyectos)

# Verifica que el alcance sea uno de los permitidos
def verificar_alcance(alcance):
    if alcance not in ['Nacional','Sectorial', 'Territorial', 'Institucional']:
        print("El alcance del proyecto es incorrecto")
        return False
    return True

# Verifica que las fechas sean correctas
def verificar_formato_fechas(fecha):
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        print(f'La fecha ({fecha}) tiene formato incorrecto')
        return False

# Verifica que el codigo sea unico y sea un numero entero
def verificar_codigo_unico(codigo):
    proyectos_guardados = cargar_proyectos()
    if int(codigo) >= 0:
        for proyCargo in proyectos_guardados:
            if proyCargo['Codigo'] == codigo:
                print(f"El codigo {codigo} no es un codigo unico")
                return False
    else:
        print('El codigo debe de ser un numero entero no negativo')
        return False
    return True

def modificar_proyecto():
    codigo = input("Codigo del proyecto a modificar: ")
    for proyecto in proyectos:
        if proyecto['Codigo'] == codigo:
            proyecto['Titulo'] = input("Nuevo Titulo: ") or proyecto['Titulo']
            proyecto['Alcance'] = input("Nuevo Alcance (Nacional, Sectorial, Territorial, Institucional): ") or \
                                  proyecto['Alcance']
            if not verificar_alcance(proyecto['Alcance']):
                return
            proyecto['Fecha de inicio'] = input("Nueva Fecha de inicio (YYYY-MM-DD): ") or proyecto['Fecha de inicio']
            if not verificar_formato_fechas(proyecto['Fecha de inicio']):
                return
            proyecto['Fecha de fin'] = input("Nueva Fecha de fin (YYYY-MM-DD): ") or proyecto['Fecha de fin']
            if not verificar_formato_fechas(proyecto['Fecha de fin']):
                return
            guardar_proyectos(proyectos)
            return
    print("Proyecto no encontrado.")


def eliminar_proyecto():
    codigo = input("Codigo del proyecto a eliminar: ")
    global proyectos
    proyectos = [proyecto for proyecto in proyectos if proyecto['Codigo'] != codigo]
    guardar_proyectos(proyectos)


def listar_proyectos():
    for proyecto in proyectos:
        print(proyecto)
    return


def buscar_proyecto_por_titulo():
    titulo = input("Titulo del proyecto a buscar: ")
    for proyecto in proyectos:
        if proyecto['Titulo'].lower() == titulo.lower():
            print(proyecto)
            return
    print("Proyecto no encontrado.")
    return


def buscar_proyecto_por_codigo():
    codigo = input("Codigo del proyecto a buscar: ")
    for proyecto in proyectos:
        if proyecto['Codigo'] == codigo:
            print(proyecto)
            return
    print("Proyecto no encontrado.")
    return


def filtrar_proyectos_por_fecha():
    fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
    if not verificar_formato_fechas(fecha_inicio):
        return
    fecha_fin = input("Fecha de fin (YYYY-MM-DD): ")
    if not verificar_formato_fechas(fecha_inicio):
        return
    for proyecto in proyectos:
        if proyecto['Fecha de inicio'] >= proyecto['Fecha de fin']:
            print('Las fechas ingresadas son icorrectas')
            return
        if proyecto['Fecha de inicio'] >= fecha_inicio and proyecto['Fecha de fin'] <= fecha_fin:
            print(proyecto)
            return
        else:
            print("No hay proyectos que coincidan con las fechas ingresadas")
            return


# Menu principal
proyectos = cargar_proyectos()
if __name__ == '__main__':

    while True:
        #os.system("cls") no me funciona
        print("\nGestión de Proyectos de Investigación")
        print("1. Ingresar un proyecto")
        print("2. Modificar un proyecto")
        print("3. Eliminar un proyecto")
        print("4. Listar los proyectos registrados")
        print("5. Buscar un proyecto por titulo")
        print("6. Buscar un proyecto por codigo")
        print("7. Filtrar proyectos por rango de fecha")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ingresar_proyecto()
        elif opcion == "2":
            modificar_proyecto()
        elif opcion == "3":
            eliminar_proyecto()
        elif opcion == "4":
            listar_proyectos()
        elif opcion == "5":
            buscar_proyecto_por_titulo()
        elif opcion == "6":
            buscar_proyecto_por_codigo()
        elif opcion == "7":
            filtrar_proyectos_por_fecha()
        elif opcion == "8":
            break
        else:
            print("Opción no valida.")
