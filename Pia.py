#librerias usadas
import random
import pandas as pd
import sqlite3 as sq
from sqlite3 import Error as e
import io
import sys
import time
##########
SEPARADOR = "*"*70+"\n"
contador = 0
nombres_alumnos = list()
matriculas = list()
cal_mate=list()
cal_ing=list()
cal_pro=list()
cal_base=list()
cal_est=list()
base = "Base2.db"
nombres = ["Angela","Daniel","Isai","Rodrigo","Maria","Sandra","Juana","Melchor","Estartuino","Jaime","Israel","Liz","Rolando","Adriana","Adrian","Ana","Susana","Rogelio","Eduardo","Francisco","Javier","Axel","Alejandro","Abigail","Miriam","Alejandrino","Marco","Antonio","Luis","Luisa"]

alumnos = {"Alumno":nombres_alumnos,"Matematicas":cal_mate,"Ingles":cal_ing,"Programacion":cal_pro,"Base de Datos":cal_base,"Estadistica":cal_est}
materias = ["Matematicas","Ingles","Programacion","Base de Datos","Estadistica"]
def conexion_base_datos(base):
        with sq.connect(base) as conn:
            cursor= conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS alumno  (matricula INTEGER NOT NULL PRIMARY KEY,nombre TEXT NOT NULL)")
            cursor.execute("CREATE TABLE IF NOT EXISTS materia (clave INTEGER NOT NULL PRIMARY KEY,nombre TEXT NOT NULL)")
            cursor.execute("CREATE TABLE IF NOT EXISTS calificaciones (matricula INTEGER, clave INTEGER, calificacion INTEGER NOT NULL,FOREIGN KEY (matricula) REFERENCES alumno(matricula), FOREIGN KEY (clave) REFERENCES materia(clave))")
        
def insertar_alumno(matricula,nombre,base):
    valores = {"matricula":matricula,"nombre":nombre,"base":base}
    try:
        
    
        with sq.connect(base) as conn:
           
            cursor= conn.cursor()
            cursor.execute("INSERT INTO alumno VALUES (:matricula,:nombre)",valores)
    except e:
        pass
    except:
        print(f"Se produjo el siguiente error : {sys.exc_info()[0]}")
    else:
        print("Alumno Registrado")
def insertar_materia(clave,nombre,base):
    valores = {"clave":clave,"nombre":nombre,"base":base}
    try:
        with sq.connect(base) as conn:   
            cursor= conn.cursor()
            cursor.execute("INSERT INTO materia VALUES (:clave,:nombre)",valores)
    except e:
        pass
    except:
        print(f"Se produjo el siguiente error : {sys.exc_info()[0]}")
    else:
        print("Materia Registrada")
        
    
def insertar_valores(matricula,clave,calificacion,base):
    valores = {"matricula":matricula,"clave":clave,"calificacion":calificacion,"base":base}
    try:
        with sq.connect(base) as conn:   
            cursor= conn.cursor()
            cursor.execute("INSERT INTO calificaciones VALUES (:matricula,:clave,:calificacion)",valores)
    except e:
        print(e)
    except:
        print(f"Se produjo el siguiente error : {sys.exc_info()[0]}")
    else:
        print("Calificacion Registrada")
   
def check(matricula,clave):
    valores = {"matricula":matricula,"clave":clave}
    
    
    try:
        with sq.connect(base) as conn:   
            cursor= conn.cursor()
            cursor.execute("SELECT * FROM calificaciones WHERE matricula=:matricula and clave=:clave",valores)
            check_list=cursor.fetchall()
            if len(check_list) > 0:
                return True
            else:
                return False
    except e:
        print(e)
    except:
        print(f"Se produjo el siguiente error : {sys.exc_info()[0]}")
    else:
        print("Chequeo Realizado")
        
def borrar_registros(base):
    try:
        
        with sq.connect(base) as conn:   
            cursor= conn.cursor()
            cursor.execute("DELETE FROM calificaciones")
    except e:
        print(e)
    except:
        print(f"Se produjo el siguiente error : {sys.exc_info()[0]}")
    else:
        print("Datos Eliminados")
        
    
        
        
    

def menu():
    print("1)Cargar Lista de Alumnos")#listo
    print("2) Capturar las calificaciones de los diferentes alumnos  ")#listo
    print("3) Asignaturas con un desempeño más bajo")#listo
    print("4) Estudiantes que reprobaron dos o más asignaturas en el período ")#listo
    print("5) Guardar en la base de datos las notas")#listo
    print("6) Estadísticas descriptivas por materia y por estudiante")
    print("7) Salir")#listo
while True:
    menu()
    desicion = input("Opcion a elegir")
    if desicion in ("1","2","3","4","5","6","7"):
        if desicion == "1":
            if contador == 0:
                contador = contador + 1
            
                for i in range(len(nombres)):
                    nombres_alumnos.append(nombres[i])
                    matriculas.append(i+1)
                    cal_mate.append(0)
                    cal_ing.append(0)
                    cal_pro.append(0)
                    cal_base.append(0)
                    cal_est.append(0)
            
                print("lista cargada")
            elif contador != 0:
                while True:
                    
                    print("La lista ya esta cargada, para borrar los datos que ya estan cargados, presione 0 y vuelva a elegir esta opcion, presione 1 para volver")
                    borrar = input()
                    if borrar in ("1","0"):
                        break
                if borrar == "0":
                    contador = 0
                    nombres_alumnos = list()
                    matriculas = list()
                    cal_mate=list()
                    cal_ing=list()
                    cal_pro=list()
                    cal_base=list()
                    cal_est=list()
                    nombres = ["Angela","Daniel","Isai","Rodrigo","Maria","Sandra","Juana","Melchor","Estartuino","Jaime","Israel","Liz","Rolando","Adriana","Adrian","Ana","Susana","Rogelio","Eduardo","Francisco","Javier","Axel","Alejandro","Abigail","Miriam","Alejandrino","Marco","Antonio","Luis","Luisa"]

                    alumnos = {"Alumno":nombres_alumnos,"Matematicas":cal_mate,"Ingles":cal_ing,"Programacion":cal_pro,"Base de Datos":cal_base,"Estadistica":cal_est}
                    dataFrame=None
                elif borrar == "1":
                     print("Volviendo al menu")
        if desicion == "2":
            calificaciones_todas=list()
            if len(nombres_alumnos)==0:
                print("No se ha cargado la lista de alumnos")
            else:
                
                for i in alumnos:
                    if i != "Alumno":
                        for y in nombres_alumnos:
                             while True:
                                indice = nombres_alumnos.index(y)
                                print(f"Calificacion del alumno {y} en {i}")
                                try:
                                    calificacion = int(input())
                                except ValueError:
                                    print("Valor no admitido intente de nuevo")
                                else:
                                    if i == "Matematicas" and calificacion in range(0,101):
                                        cal_mate[indice]=calificacion
                                        break
                                    elif i == "Ingles" and calificacion in range(0,101):
                                        cal_ing[indice]=calificacion
                                        break
                                    elif i == "Programacion" and calificacion in range(0,101):
                                        cal_pro[indice]=calificacion
                                        break
                                    elif i == "Base de Datos" and calificacion in range(0,101):
                                        cal_base[indice]=calificacion
                                        break
                                        
                                    elif i == "Estadistica" and calificacion in range(0,101):
                                        cal_est[indice]=calificacion
                                        break
                                    else:
                                        print("Calificacion no en el rango permitido")
                                    
                                
                calificaciones_todas.append(cal_mate)
                calificaciones_todas.append(cal_ing)
                calificaciones_todas.append(cal_pro)
                calificaciones_todas.append(cal_base)
                calificaciones_todas.append(cal_est)
                    
                    
                try:
                    
                    dataFrame = pd.DataFrame(alumnos)
                    dataFrame.index=matriculas
                    print(dataFrame)
                except:
                    print("Ha ocurrido un error")
                else:
                    print("Calificaciones de los alumnos capturada correctamente")
        if desicion == "3":
            try:
                
                promedios = list()
                materias_dict = {"Asignatura":materias,"Promedio":promedios}
                for i in materias:
                
                    df = dataFrame[["Alumno",i]].copy()
                    promedio = df[{i}].mean()
                    promedios.append(promedio[0])
                dataFrame_Materias=pd.DataFrame(materias_dict)
            
                print("Materias con promedio general menor a 70")
                promedio_materias=dataFrame_Materias[dataFrame_Materias["Promedio"]<70]
                if len(promedio_materias)==0:
                    print("N/A")
                else:
                    
                    print(promedio_materias.to_string(index=False))
            
                print("Las 3 materias con mas baja calificacion")
                df_mas_baja=dataFrame_Materias.sort_values(by="Promedio")
                print(df_mas_baja.head(3).to_string(index=False))
            except:
                print("Ha ocurrido un error asegure se haber capturado las calificaciones")
            
        if desicion == "4":
            lista_reprobados = list()
            lista_conteo_reprobados = list()
            lista_2_reprobadas = list()
            cantidades = list()
            try:
                reprobados_mate=dataFrame[dataFrame["Matematicas"]<70]
                reprobados_ingles=dataFrame[dataFrame["Ingles"]<70]
                reprobados_progra=dataFrame[dataFrame["Programacion"]<70]
                reprobados_base=dataFrame[dataFrame["Base de Datos"]<70]
                reprobados_estadistica=dataFrame[dataFrame["Estadistica"]<70]
                
                lista_reprobados.append(reprobados_mate)
                lista_reprobados.append(reprobados_ingles)
                lista_reprobados.append(reprobados_progra)
                lista_reprobados.append(reprobados_base)
                lista_reprobados.append(reprobados_estadistica)
                
                
                for i in lista_reprobados:
                    for y in i.index:
                        lista_conteo_reprobados.append(y)
                
                for i in matriculas:
                    conteo=lista_conteo_reprobados.count(i)
                    if conteo >= 2:
                        lista_2_reprobadas.append(i)
                        cantidades.append(conteo)
                print("Alumnos con mas de dos materias reprobadas")
                if len(lista_2_reprobadas)==0:
                    print("Ningun alumno reprobo mas de dos materias")
                print("ID\tNombre\tCantidad")
                for i in lista_2_reprobadas:
                    print(i,end="")
                    print("\t",dataFrame["Alumno"][i],end="")
                    print("\t",cantidades[i-1])
      
                        
            except:
                print("No se han capturado las calificaciones correspondientes al periodo")
        if desicion == "5":
            opcion = ""
            valor = check(1,1)
            if valor == True:
                
                while True:
                    print("Ya se tiene registradas las calificaciones de este periodo, si las desea sobreescribir presione 1, si no es el caso presione 0")
                    opcion = input()
                    if opcion in ("1","0"):
                        if opcion == "1":
                            borrar_registros(base)
                            break
                        elif opcion== "0":
                            print("Volviendo al menu")
                            break
                        else:
                            print("Opcion no correcta, Intente de nuevo")
                    
            if opcion == "1" or valor==False:
                
                if len(nombres_alumnos) == 0:
                    print("Nada que guardar")
                else:
                    
                    conexion_base_datos(base)
                    for i in materias:
                
                        insertar_materia(materias.index(i)+1,i,base)
                   
                    for i in nombres_alumnos:
                        insertar_alumno(nombres_alumnos.index(i)+1,i,base)
                    for i in nombres_alumnos:
                        for y in materias:
                            matricula = nombres_alumnos.index(i)+1
                            materia = materias.index(y)+1
                            calificacion = calificaciones_todas[materias.index(y)][nombres_alumnos.index(i)]
                            insertar_valores(matricula,materia,calificacion,base)
        if desicion == "6":
            
                try:
                    
                    print(SEPARADOR)
                    print("\t\tEstadisticas descriptivas por alumno")
                    print(SEPARADOR)
                    for i in nombres_alumnos:
                        print(SEPARADOR)
                        print(f"\t\tMatricula {nombres_alumnos.index(i)+1} Alumno {i}") 
                        print(dataFrame[dataFrame["Alumno"]==i])
                        print(dataFrame[dataFrame["Alumno"]==i].describe())
                
                    print(SEPARADOR)
                    print("\t\tEstadisticas descriptivas por materia")
                    print(SEPARADOR)
                    for i in materias:
                        print(SEPARADOR)
                        print(f"\t\tNombre de la materia {i}")
                        print(dataFrame[["Alumno",i]].copy())
                        print(dataFrame[["Alumno",i]].copy().describe())
                except:
                    print("No ha capturado las calificaciones")
                else:
                    print("Listo")
                    while True:
                        
                        print("Desea guardar los registros en un archivo de texto? y/n")
                        guardar = input()
                        if guardar in ("y","n","Y","N"):
                            if guardar in ("y","Y"):
                                print("Guardando")
                                print("Nombre que desea dar al archivo")
                                nombre = input()
                                try:
                                    file=open(f"{nombre}.txt","w")
                                    file.write(SEPARADOR)
                                    file.write("\t\tEstadisticas descriptivas por alumno")
                                    file.write("\n")
                                    file.write(SEPARADOR)
                    
                                    for i in nombres_alumnos:
                                        file.write(SEPARADOR)
                                        file.write(f"\t\tMatricula {nombres_alumnos.index(i)+1} Alumno {i}")
                                        file.write("\n")
                                        file.write(dataFrame[dataFrame["Alumno"]==i].to_string())
                                        file.write("\n")
                                        file.write(dataFrame[dataFrame["Alumno"]==i].describe().to_string())
                                        file.write("\n")
                
                                    file.write(SEPARADOR)
                                    file.write("\t\tEstadisticas descriptivas por materia")
                                    file.write("\n")
                                    file.write(SEPARADOR)
                                    
                                    for i in materias:
                                        file.write(SEPARADOR)
                                        file.write(f"\t\tNombre de la materia {i}")
                                        file.write("\n")
                                        file.write(dataFrame[["Alumno",i]].copy().to_string())
                                        file.write("\n")
                                        file.write(dataFrame[["Alumno",i]].copy().describe().to_string())
                                        file.write("\n")
                                    file.close()
                                    
                                except:
                                    print("Ha ocurrido un error al guardar el archivo")
                                    break
                                else:
                                    print("Guardado")
                                    break
                            elif guardar in ("n","N"):
                                print("Volviendo al menu")
                                break
                            else:
                                print("Opcion no valida, intente de nuevo")
        if desicion == "7":
            print("Saliendo del programa")
            time.sleep(5)
            sys.exit()
                
    
    else:
        print("Opcion elegida no valida")
