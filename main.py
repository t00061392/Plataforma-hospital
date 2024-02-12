credencial = "esternon"
import csv
import os


# Comprobacion
def comprobacion():
    if not os.path.exists("pacientes.csv"):
        with open("pacientes.csv", "w"):
            pass
    else:
        pass


# Limpieza
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# Estampa
def estampa():
    print('------------------------')
    print('|▬Hospital San Vicente▬|')
    print('------------------------')


log = False


# Inicio
def login():
    global log
    pas = input('Ingrese su credencial: ')
    if pas == credencial:
        log = True
        clear()
    else:
        clear()
        estampa()
        print('Credencial incorrecta')
        login()


datos_paciente = []


def ingresar_datos():
    global datos_paciente
    nombre = input("Ingrese el nombre completo del paciente: ")
    sexo = input("Ingrese el sexo del paciente (F/M): ")
    birth = input("Ingrese la fecha de nacimiento del paciente (dd/mm/aaaa): ")
    documento = input("Ingrese el número de documento del paciente: ")
    presion = input("Ingrese la presión del paciente (mm Hg): ")
    temperatura = input("Ingrese la temperatura del paciente (c°): ")
    saturacion = input("Ingrese la saturación de oxígeno del paciente (%): ")
    frec_cardiaca = input("Ingrese la frecuencia cardiaca del paciente (lat/min): ")
    notas = input("Ingrese las notas de evolución del paciente: ")
    cama = input("¿El paciente usará cama? (s/n): ")
    cama_n = "0"
    if cama == "s":
        cama_n = input("Ingrese el número de cama: ")
    else:
        cama_n = "ninguna"
    medicamento = input("Ingrese el medicamento del paciente: ")
    alta=input("El paciente fue dado de alta?(s/n): ")
    datos_paciente = [nombre, sexo, birth, documento, presion, temperatura, saturacion, frec_cardiaca, notas, cama,
                      cama_n, medicamento,alta]


def guardar_csv(nombre_archivo, datos_paciente):
    with open(nombre_archivo, 'a', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(datos_paciente)


def opcion1():
    clear()
    estampa()
    ingresar_datos()
    guardar_csv("pacientes.csv", datos_paciente)


def opcion2():
    tarjet = 0
    clear()
    estampa()
    documento = input("Ingrese el documento del paciente: ")
    with open("pacientes.csv", 'r') as archivo:
        lectura = csv.reader(archivo)
        datos = list(lectura)
        for i in range(len(datos)):
            if datos[i][3] == documento:
                tarjet = i
        print(f"Nombre: {datos[tarjet][0]}\nSexo: {datos[tarjet][1]}\nFecha de nacimiento: {datos[tarjet][2]}"
              f"\nDocumento: {datos[tarjet][3]}\nPresión(mmHg): {datos[tarjet][4]}\nTemperatura(c°): "
              f"{datos[tarjet][5]}\nSaturación(%): {datos[tarjet][6]}\nFrecuencia cardiaca(lat/min): "
              f"{datos[tarjet][7]}\nNotas: {datos[tarjet][8]}\nCamilla: {datos[tarjet][9]}\nNúmero de camilla: "
              f"{datos[tarjet][10]}\nMedicamento: {datos[tarjet][11]}\nEsta en alta: {datos[tarjet][12]}")


def opcion3():
    tarjet = 0
    flag = False
    clear()
    estampa()
    while flag != True:
        documento = input("Ingrese el documento del paciente: ")
        with open("pacientes.csv", 'r') as archivo:
            lectura = csv.reader(archivo)
            datos = list(lectura)
            for i in range(len(datos)):
                if datos[i][3] == documento:
                    flag = True
                    tarjet = i
                    print("Seleccione información a modificar:\n1. Nombre\n2. Sexo\n3. Fecha de nacimiento\n"
                          "4. Documento\n5. Presión(mmHg)\n6. Temperatura(c°)\n7. Saturación(%)\n"
                          "8. Frecuencia cardiaca(lat/min)\n9. Notas\n10. Camilla\n11. Número de camilla\n"
                          "12. Medicamento\n13. Esta en alta(s/n)")
                    opcion = int(input("Ingrese la opción: "))
                    cache = input("Ingrese el nuevo valor: ")
                    datos[tarjet][opcion - 1] = cache
                    deseo = input("¿Desea guardar el cambio? (s/n): ")
                    if deseo == "s":
                        with open('pacientes.csv', 'w', newline='') as archivo:
                            escritor_csv = csv.writer(archivo)
                            escritor_csv.writerows(datos)
                    elif deseo == "n":
                        pass
            if flag is False:
                print("El documento no está registrado")


def opcion4():
    ocupado = 0
    with open("pacientes.csv", 'r') as archivo:
        lectura = csv.reader(archivo)
        datos = list(lectura)
        for i in range(len(datos)):
            if datos[i][9] == "s":
                ocupado += 1
        print(f"Hay {300 - ocupado} camillas disponibles")
def opcion5():
    altas=0
    total_medi=0
    with open("pacientes.csv", 'r') as archivo:
        lectura= csv.reader(archivo)
        datos=list(lectura)
        for i in range(len(datos)):
            if datos[i][12]=="s":
                altas+=1
            if datos[i][11]!="ninguno":
                total_medi+=1
    print(f"Número de pacientes: {len(datos)} ")
    print(f"Número de altas: {altas}\nNúmero de pacientes con medicamento: {total_medi}")

def menu():
    if log is True:
        chose = 0
        estampa()
        print("Bienvenido\nEscriba el número de la opción que desea realizar")
        print("1. Agregar paciente\n2. Consultar pacientes\n3. Editar paciente\n4. Camillas disponibles\n"
              "5. Indicadores del hospital\n6. Salir")
        chose = int(input("Ingrese el número de la opción: "))
        if chose == 1:
            opcion1()
            clear()
            print("↓Guardado↓")
            menu()
        elif chose == 2:
            opcion2()
            contin = "1"
            while contin != "0":
                contin = input("Presione cero para volver al menú: ")
            if contin == "0":
                clear()
                menu()
        elif chose == 3:
            opcion3()
            clear()
            menu()
        elif chose == 4:
            clear()
            opcion4()
            contin = "1"
            while contin != "0":
                contin = input("Presione cero para volver al menú: ")
            if contin == "0":
                clear()
                menu()
        elif chose == 5:
            clear()
            opcion5()
            contin = "1"
            while contin != "0":
                contin = input("Presione cero para volver al menú: ")
            if contin == "0":
                  clear()
                  menu()
        elif chose == 6:
            clear()
            estampa()
            login()
            menu()
        else:
            clear()
            print("No existe esa opción")
            menu()
    else:
      pass
comprobacion()
estampa()
login()
menu()
