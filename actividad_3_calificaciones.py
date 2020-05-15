#Actividad 3 Estructura de Datos Grupo 31 LTI 
#COSS ESCOBEDO MIRIAM			1845198
#RAMOS ORDOÑEZ PEDRO FRANCISCO	1870149
#SALDAÑA RODRÍGUEZ DANIEL ISAI		1604155
#TORRES PASILLAS ROGELIO			1820938

import pandas as pd
import os 
import time 
from sys import exit
import sys
import io
import sqlite3
from sqlite3 import Error
name = "BaseDatosNotas.db"
SEPARADOR = "-"*70+("\n")
def confirmacion():
    go=True
    while True:
        print("Desea guardar los datos? y/n")
        answer = input()
        if answer == "y" or answer == "Y":
            go = True
            return go
        elif answer == "n" or answer == "N":
            go = False
            return go
        else:
            print("Opcion no valida")
            
    
def c_l_Base_de_datos():
    with sqlite3.connect(name) as conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS alumno ( 
                matricula INTEGER PRIMARY KEY, nombre TEXT UNIQUE NOT NULL, estado BOOLEAN
                );''')
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS materia  ( 
                clave INTEGER PRIMARY KEY, nombre TEXT UNIQUE NOT NULL
                );
                ''')
            
            cursor.execute('''            
            CREATE TABLE IF NOT EXISTS calificacion ( 
                matricula INTEGER, 
                clave INTEGER, 
                nota INTEGER NOT NULL,
                FOREIGN KEY (matricula) REFERENCES alumno(matricula),
                FOREIGN KEY (clave) REFERENCES s_materia(clave)
                );
                ''')
            cursor.close()
        except Error as e:
            print(e)
        except:
            print(f"Se produjo el siguiente error : {sys.exc_info()[0]}")
        else:
            print("Base de datos lista.")
def ultimaMatricula():
    with sqlite3.connect(name) as conn:
        try:
            
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM alumno")
            lista_alumnos = cursor.fetchall()
            matricula = len(lista_alumnos)+1
            cursor.close()
            return matricula
        except Error as e:
            print(e)
        except:
            print(f"Se produjo el siguiente error : {sys.exc_info()[0]}")
def ultimaClave():
    with sqlite3.connect(name) as conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM materia")
            lista_materias = cursor.fetchall()
            clave = len(lista_materias)+1
            cursor.close()
            return clave
        except Error as e:
            print(e)
        except:
            print(f"Se produjo el siguiente error : {sys.exc_info()[0]}")
def agregarAlumno(matricula,nombre,estatus):
    alumno = {"matricula": matricula,"nombre": nombre,"estatus":estatus}
    with sqlite3.connect(name) as conn:
        try:

            cursor = conn.cursor()
            cursor.execute("INSERT INTO alumno VALUES ( :matricula, :nombre,:estatus);",alumno)
            cursor.close()  
        except Error as e:
            print(e)
        except:
            print(f"Se produjo el siguiente error : {sys.exc_info()[0]}")
        else:
            print("Registro Insertado Correctamente.")
def agregars_materia(clave,nombre):
    materia = {"clave":clave,"nombre":nombre}
    with sqlite3.connect(name) as conn:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO materia VALUES ( :clave, :nombre);",materia) 
            cursor.close() 
        except Error as e:
            print(e)
        except:
            print(f"Se produjo el siguiente error : {sys.exc_info()[0]}")
        else:
            print("Registro Insertado Correctamente.")
def agregarCalificacion(matricula,clave,nota):
    calificacion = {"matricula":matricula,"clave":clave,"nota":nota}
    with sqlite3.connect(name) as conn:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO calificacion VALUES ( :matricula, :clave, :nota);",calificacion) 
            cursor.close() 
        except Error as e:
            print(e)
        except:
            print(f"Se produjo el siguiente error : {sys.exc_info()[0]}")
        else:
            print("Registro Insertado Correctamente.")
def alumno(matricula):
    
    with sqlite3.connect(name) as conn:
        matricula = {"matricula":matricula}
        cursor = conn.cursor()
        cursor.execute("SELECT nombre FROM alumno WHERE matricula = :matricula",matricula)
        _alumno = cursor.fetchall()
        nombre_alumno = _alumno[0][0]
        cursor.close()
        return nombre_alumno
    
def s_materia(clave):
    with sqlite3.connect(name) as conn:
        clave = {"clave":clave}
        cursor = conn.cursor()
        cursor.execute("SELECT nombre FROM materia WHERE clave = :clave",clave)
        _materia = cursor.fetchall()
        nombre_materia = _materia[0][0]
        cursor.close()
        return nombre_materia
    
def check_calificacion(matricula,clave):
    go=True
    with sqlite3.connect(name) as conn:
        try:
            
            valores = {"matricula":matricula,"clave":clave}
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM calificacion WHERE matricula = :matricula AND clave = :clave",valores)
            _calificacion = cursor.fetchall()
            lon = len(_calificacion)
            cursor.close()
            return lon
        except Error as e:
            print(e)
        except:
            print(f"Se produjo el siguiente error : {sys.exc_info()[0]}")
        
def check_s_materia(nombre):
    
    go=True
    with sqlite3.connect(name) as conn:
        try:
            
            valores = {"nombre":nombre}
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM materia WHERE nombre=:nombre",valores)
            _materia = cursor.fetchall()
            lon = len(_materia)
            cursor.close()
            return lon
        except Error as e:
            print(e)
        except:
            print(f"Se produjo el siguiente error : {sys.exc_info()[0]}")
        
def seleccionar_todas_materias():
    with sqlite3.connect(name) as conn:
        try:
            
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM materia")
            _materias = cursor.fetchall()
            cursor.close()
            return _materias
        except Error as e:
            print(e)
        except:
            print(f"Se produjo el siguiente error : {sys.exc_info()[0]}")
            
def seleccionar_todos_alumnos(opcion):
    with sqlite3.connect(name) as conn:
        try:
            
            cursor=conn.cursor()
            if opcion == 1:
                cursor.execute("SELECT * FROM alumno WHERE estado = True")
                _alumnos = cursor.fetchall()
                return _alumnos
            if opcion == 2:
                cursor.execute("SELECT * FROM alumno WHERE estado = False")
                _alumnos = cursor.fetchall()
                return _alumnos
            if opcion == 3:
                cursor.execute("SELECT matricula,nombre FROM alumno")
                _alumnos = cursor.fetchall()
                return _alumnos
            if opcion == 4:
                cursor.execute("SELECT * FROM alumno")
                _alumnos = cursor.fetchall()
                return _alumnos
        except Error as e:
            print(e)
        
        finally:
            cursor.close()

            
            
def seleccionar_calificaciones(nombre,opcion):
    
    with sqlite3.connect(name) as conn:
        try:
            
            valores = {"nombre":nombre}
            cursor=conn.cursor()
            if opcion == 1:
            
                cursor.execute("SELECT matricula,nota FROM calificacion WHERE clave = (SELECT clave FROM materia WHERE nombre =:nombre)",valores)
                _calificaciones = cursor.fetchall()
                return _calificaciones
            if opcion == 2:
                cursor.execute("SELECT clave,nota FROM calificacion WHERE matricula = (SELECT matricula FROM alumno WHERE nombre =:nombre)",valores)
                _calificaciones = cursor.fetchall()
                return _calificaciones
        except Error as e:
            print(e)
        except:
            print(f"Se produjo el siguiente error : {sys.exc_info()[0]}")
            
        finally:
            cursor.close()
def corregir_datos(matricula,nombre,estatus):
    try:
        
        with sqlite3.connect(name) as conn:
            valores = {"matricula":matricula,"nombre":nombre,"estatus":estatus}
            cursor=conn.cursor()
            cursor.execute("UPDATE alumno SET nombre = :nombre WHERE matricula = :matricula",valores)
            cursor.execute("UPDATE alumno SET estado = :estatus WHERE matricula = :matricula",valores)
            cursor.close()
    except Error as e:
        print(e)
    
    except:
        print(f"Se produjo el siguiente error : {sys.exc_info()[0]}")
    else:
        print("Datos Actualizados correctamente")
    finally:
        cursor.close()
def corregir_datos_s_materia(clave,nombre):
    try:
        
        with sqlite3.connect(name) as conn:
            valores = {"clave":clave,"nombre":nombre}
            cursor=conn.cursor()
            cursor.execute("UPDATE materia SET nombre = :nombre WHERE clave = :clave",valores)
            cursor.close()
    except Error as e:
        print(e)
    except:
        print(f"Se produjo el siguiente error : {sys.exc_info()[0]}")
    else:
        print("Datos Actualizados correctamente")
    finally:
        cursor.close()

def menu():
    print("1)Agregar Alumno \n2)Agregar Materia \n3)Capturar Calificacion \n4)Consultar Materias \n5)Consultar Alumnos")
    print("6)Calificaciones \n7)Coreccion Datos del alumno \n8)Correccion Datos Materia \n0)Salir")
def cantidad_materias_reprobadas_gen(matricula):
    with sqlite3.connect(name) as conn:
        valores = {"matricula":matricula}
        try:
            cursor=conn.cursor()
            
            cursor.execute("SELECT count(*) FROM calificacion WHERE matricula = :matricula and nota < 70",valores)
            cuantas = cursor.fetchall()
            if cuantas[0][0] >= 2:
                cursor.execute("SELECT * FROM calificacion  WHERE matricula = :matricula and nota < 70",valores)
                alumnos_reprobados = cursor.fetchall()
                #print(alumnos_reprobados)
                yield alumnos_reprobados
                yield cuantas[0][0]
        except Error as e:
            print(e)
        except:
            print(f"Se produjo el siguiente error : {sys.exc_info()[0]}")
        
c_l_Base_de_datos()
while True:
    menu()
    while True:
        try:
            opcion = int (input("Ingrese la opcion que desee realizar: "))
        except:
            print("Valor no admitido")
        else:
            break
    
    if opcion == 1:
        print(SEPARADOR)
        print("","Agregar Alumno",sep="\t\t\t")
        print(SEPARADOR)
        while True:
            print("1) Agregar Alumno 0) Volver al menu")
            respuesta = input()
            if respuesta == "1":
                
                print("Asignando Matricula")
                _matricula = ultimaMatricula()
                print("Matricula Asignada")
                print("Nombre del alumno")
                _nombre = input()
                print("Estableciendo estatus")
                _estatus = True
                print("Estatus establecido")
                print(f"Matricula: {_matricula} Nombre: {_nombre}")
                if confirmacion():
                    agregarAlumno(_matricula,_nombre,_estatus)
                    print("Datos guardados con exito")
                else:
                    print("Datos no guardados")
            elif respuesta == "0":
                break
            else:
                continue
            
    elif opcion == 2:
        _salir = ""
        print(SEPARADOR)
        print("","Agregar Materia",sep="\t\t\t")
        print(SEPARADOR)
        print(SEPARADOR)
        while True:
            print("1)Agregar Materia 0) Volver al menu")
            respuesta = input()
            if respuesta == "1":
                
                print("Asignando Clave de la Materia")
                _clave = ultimaClave()
                print("Clave Asignada")
                continuar = True
                while continuar:
            
                    print("Nombre de la materia")
                    _nombre = input()
                    lon = check_s_materia(_nombre)
                    if lon == 0:
                        continuar = False
                    else:
                        while True:
                    
                            print("La materia ya existe. 1) Intentar de nuevo 0) Cancelar")
                            _salir = input()
                            if _salir in ("0","1"):
                                if _salir == "0":
                                    continuar =  False
                                    break
                                elif _salir == "1":
                                    break
                            else:
                                print("Opcion no válida")
                if _salir == "0":
                    pass
                else:
                    print("Estatus establecido")
                    print(f"Clave: {_clave} Nombre: {_nombre}")
                    if confirmacion():
                        agregars_materia(_clave,_nombre)
                        print("Datos guardados con exito")
                    else:
                        print("Datos no guardados")
            elif respuesta == "0":
                break
           
            else:
                continue
    elif opcion == 3:
        print(SEPARADOR)
        print("","Capturar Calificaciones",sep="\t\t\t")
        print(SEPARADOR)
        
        while True:
            continuar=True
            print("1)Continuar \n2)Volver")
            answer = input()
            if answer in ("1","2"):
                if answer == "1":
                    pass
                elif answer == "2":
                    break
            else:
                continue
            
            while continuar:
                try:
                    print("Matricula del Alumno")
                    _matricula = int(input())
                    print(alumno(_matricula))
                    print("Alumno correcto? y/n")
                    answer = input()
                    if answer in ("y","Y"):
                        break
                    elif answer in ("n","N"):
                        continue
                    else:
                        print("Opcion no valida")
                except Error as e:
                    print(e)
                except IndexError:
                    print("No se tiene un registro con esa matricula, asegure de haber dado de alta al alumno")
                    continuar = False
                except:
                    print(f"Se produjo el siguiente error : {sys.exc_info()[0]}")
            while continuar:
                try:
                    print("Clave de la materia")
                    _clave = int(input())
                    print(s_materia(_clave))
                    print("Materia correcta? y/n")
                    answer = input()
                    if answer in ("y","Y"):
                        if (check_calificacion(_matricula,_clave)) == 0:
                        
                            break
                        else:
                            print("No se permiten duplicar registros")
                        
                            continuar = False
                    elif answer in ("n","N"):
                        continue
                    else:
                        print("Opcion no valida")
                except Error as e:
                    print(e)
                except IndexError:
                    print("No se tiene un registro con esa clave, asegure de haber dado de alta la asignatura")
                    continuar = False
                except:
                    print(f"Se produjo el siguiente error : {sys.exc_info()[0]}")
                
            while continuar:
                try:
                    print("Calificacion de la materia")
                    _calificacion = int(input())
            
                    if _calificacion in range(0,101):
                        if confirmacion():
                            agregarCalificacion(_matricula,_clave,_calificacion)
                            break
                        else:
                            print("Datos no guardados")
                            break
                    else:
                        print("El rango aceptado de la calificacion es de 0 a 100")
                except Error as e:
                    print(e)
                except:
                    print(f"Se produjo el siguiente error : {sys.exc_info()[0]}")
                    
        
    elif opcion == 4:
        print(SEPARADOR)
        print("","Asignaturas",sep="\t\t\t")
        print(SEPARADOR)
        materias = seleccionar_todas_materias()
        print("Clave","Asignatura",sep="\t")
        for clave,materia in materias:
            print(clave,materia,sep="\t")
    
    elif opcion == 5:
        print(SEPARADOR)
        print("","Alumnos Activos",sep="\t\t\t")
        print(SEPARADOR)
        
        alumnos = seleccionar_todos_alumnos(1)
        if len(alumnos) == 0:
            print("No se tiene registro de alumnos activos")
        elif len(alumnos) > 0:
            
            print("Matricula","Nombre",sep="\t")
            for matricula,nombre,estatus in alumnos:
                print(matricula,nombre,sep="\t\t")
                
        print(SEPARADOR)
        print("","Alumnos Inactivos",sep="\t\t\t")
        print(SEPARADOR)
        alumnos = seleccionar_todos_alumnos(2)
        if len(alumnos) == 0:
            print("No se tiene registro de alumnos inactivos")
        elif len(alumnos) > 0 :
            print("Matricula","Nombre",sep="\t")
            for matricula,nombre,estatus in alumnos:
                print(matricula,nombre,sep="\t\t")
                

    elif opcion == 6:
        contador = 0
        reporte = ""
        print(SEPARADOR)
        print("","Calificaciones",sep="\t\t\t")
              
        print(SEPARADOR)
        nombres_alumnos = list()
        nombres_materias = list()
        matriculas_alumnos = list()
        dfs_alumnos = list()
        dfs_materias = list()
        materias = seleccionar_todas_materias()
        alumnos = seleccionar_todos_alumnos(3)
        
        _alumnos = list()
        _matriculas = list()
        nombre_materias = list()
        clave_materias = list()
        promedios_alumnos = list()
        calificaciones_generales = dict()
        for clave,nombre in materias:
            nombre_materias.append(nombre)
        for matricula,nombre in alumnos:
            _alumnos.append(nombre)
            _matriculas.append(matricula)
        
        print("","Por Alumno",sep="\t\t\t")
        
        for i in range(len(_alumnos)):
            valores = dict()
            acumulado = list()
            _acumulado = 0
            promedio = 0
            print(SEPARADOR)
            print("\t",_alumnos[i],end="")
            print("\t",_matriculas[i])
            
            calificaciones = seleccionar_calificaciones(_alumnos[i],2)
            for materia,calificacion in calificaciones:
                nombre_materia = nombre_materias[materia-1]
                valores[materia]=[materia,nombre_materia,calificacion]
                acumulado.append(calificacion)
            try:
                df = pd.DataFrame(valores)
                df = df.T
                df.columns=["Clave","Materia","Calificacion"]
                print(df.to_string(index=False))
                dfs_alumnos.append(df.to_string(index=False))
                nombres_alumnos.append(_alumnos[i])
                matriculas_alumnos.append(_matriculas[i])
                
            except ValueError:
                print("No cuenta con calificaciones")
                dfs_alumnos.append("No cuenta con calificaciones")
                nombres_alumnos.append(_alumnos[i])
                matriculas_alumnos.append(_matriculas[i])

            for i in acumulado:
                _acumulado = _acumulado + i
                promedio = _acumulado/len(acumulado)
            promedios_alumnos.append(promedio) 
            print(f"El promedio de el alumno es {promedio}")
        

        promedios_materias = list()
        valores0=dict() 
        print(SEPARADOR)
        print("","Por materia",sep="\t\t\t")
        
        for i in nombre_materias:

            print(SEPARADOR)
            print("\t",i)
            calificaciones = seleccionar_calificaciones(i,1)
            calificaciones.sort()
            
            nombre = ""
            for matricula,calificacion in calificaciones:            
                for y in alumnos:
                    if matricula == y[0]:
                        nombre = y[1]
                valores0[matricula]=[matricula,nombre,calificacion]
                
            try:
                
                df= pd.DataFrame(valores0)
                df_materias_calificaciones = df.T
                df_materias_calificaciones.columns=["Matricula","Nombre","Calificacion"]
                print(df_materias_calificaciones.to_string(index=False))
                dfs_materias.append(df_materias_calificaciones.to_string(index=False))
                nombres_materias.append(i)
            except IndexError:
                print("No se tiene registro de calificacion alguna")
            acumulado = 0
            con = 0
            
            
            for i in df_materias_calificaciones["Calificacion"]:
                con = con + 1
                acumulado = acumulado + i
            
            promedio = acumulado / con
            promedios_materias.append(promedio)
            
            
            print(f"El promedio de la asignatura es {promedio}")
   
        go = False
        print(SEPARADOR)
        print("","Cuadro de Honor",sep="\t\t\t")
        
        for i in _matriculas:
            calificaciones_generales[i] = [i,_alumnos[contador],promedios_alumnos[contador]]
            contador = contador + 1
        try:
            
            df = pd.DataFrame(calificaciones_generales)
            df.index=["Matricula","Nombre","Promedio General"]
            promedios = df.T.sort_values(by="Promedio General",ascending=False)
            print(promedios.head(3).to_string(index=False))
        except:
            print("Sin registros")
            go = True
        
        #seccion mas de 2 materias reprobadas-----------------
        contador = 0
        valores1 = dict()
        print(SEPARADOR)
        print("","Alumnos con 2 o más materias reprobadas",sep="\t\t\t")
        alumnos = seleccionar_todos_alumnos(4)
        tipos = list()
        calificaciones_reprobadas= list()
        for matricula,nombre,estado in alumnos:
            reprobadas= cantidad_materias_reprobadas_gen(matricula)
            for i in reprobadas:
                try:
                    x=(len(i))
                except:
                    cantidad=i
                else:
                    calificaciones_reprobadas.append(i[0][0])
            for i in calificaciones_reprobadas:
                if i == matricula:
                    valores1[matricula]=[matricula,nombre,cantidad]
        try:
            
            df=pd.DataFrame(valores1)
            df_alumnos_reprobados = df.T
            df_alumnos_reprobados.columns =["Matricula","Nombre","Cantidad"]
            print(df_alumnos_reprobados.to_string(index=False))
        except:
            print("Sin registros")
        while True:
            if go:
                break
            else:
                pass
            
            print("Desea exportar el reporte a un archivo txt? y/n")
            respuesta = input()
            if respuesta in("Y","y"):
                try:
                    fn=input("Nombre que desea dar al archivo: ")
                    file = open(f"{fn}.txt","w")
                    file.write(SEPARADOR)
                    file.write("\n")
                    file.write("\t\tCalificaciones")
                    file.write("\n")
                    file.write(SEPARADOR)
                    file.write("\n")
                    file.write("\t\tPor alumno")
                    file.write("\n")
                    for i in range(len(dfs_alumnos)):
                        file.write(SEPARADOR)
                        file.write("\n")
                        file.write("\t\t"+nombres_alumnos[i]+"\t"+str(matriculas_alumnos[i])+"\n")
                        file.write(dfs_alumnos[i])
                        file.write("\n")
                        file.write("El promedio del alumno es : " +str(promedios_alumnos[i]))
                        file.write("\n")
                    file.write(SEPARADOR)
                    file.write("\n")
                    file.write("\t\tPor materia")
                    file.write("\n")
                    for i in range(len(dfs_materias)):
                        file.write(SEPARADOR)
                        file.write("\n")
                        file.write("\t\t"+nombres_materias[i]+"\n")
                        file.write("\n")
                        file.write(dfs_materias[i])
                        file.write("\n")
                        file.write("El promedio de la materia es : " +str(promedios_materias[i]))
                        file.write("\n")
                    file.write(SEPARADOR)
                    file.write("\t\tCuadro de Honor")
                    file.write("\n")
                    file.write(promedios.head(3).to_string(index=False))
                    file.write("\n")
                    file.write(SEPARADOR)
                    file.write("\t\tAlumnos con 2 o mas materias reprobadas")
                    file.write("\n")
                    file.write(df_alumnos_reprobados.to_string(index=False))
        
                    file.close()
                except:
                    print(f"Se produjo el siguiente error : {sys.exc_info()[0]}")
                    print("Redirigiendo al menu")
                    time.sleep(5)
                    
                else:
                    print("Se ha exportado correctamente.")
                    time.sleep(5)
                finally:
                    break
            elif respuesta in ("n","N"):
                print("Redirigiendo al menu")
                time.sleep(5)
                break
            else:
                continue
                
                
        

    elif opcion == 7:
        print(SEPARADOR)
        print("","Correccion de información",sep="\t\t\t")
        print(SEPARADOR)
        
        lista_alumnos = seleccionar_todos_alumnos(4)
        print("Matricula\tNombre\t\tEstatus")
        for matricula,nombre,estatus in lista_alumnos:
            if estatus == 1:
                estatus = "Activo"
            else:
                estatus = "Inactivo"
            if len(nombre) >= 9:
                
                print(f"{matricula}\t\t{nombre}\t{estatus}")
            else:
                print(f"{matricula}\t\t{nombre}\t\t{estatus}")
        while True:
            print("1)Corregir 0)Volver al menu")
            answer = input()
            if answer == "1":
                pass
            elif answer == "0":
                break
            else:
                continue
            print("Matricula del alumno del cual quiere actualizar/corregir datos")
            matricula = input()
            nombre = alumno(matricula)
            
            if nombre != None:
                
                while True:
                    print(f"El nombre del alumno es {nombre}? y/n")
                    correcto = input()
                    if correcto in("y","Y"):
                        print("Nuevo nombre: ")
                        new_nombre = input()
                        while True:
                            print("Estatus 1) Activo 0) Inactivo: ")
                            new_estatus = input()
                            if new_estatus in("1","0"):
                                corregir_datos(matricula,new_nombre,new_estatus)
                                break
                            else:
                                continue
                        
                   
                    elif correcto in ("N","n"):
                        break
                    else:
                        continue
                    break
                
    elif opcion == 8:
        print(SEPARADOR)
        print("","Correccion de Información",sep="\t\t")
        print(SEPARADOR)
        
        lista_materias = seleccionar_todas_materias()
        print("Clave\tNombre")
        for clave,nombre in lista_materias:
            print(clave,nombre,sep="\t")
        while True:
            
            print("1)Corregir 0)Volver al menu")
            answer = input()
            if answer == "1":
                pass
            elif answer == "0":
                break
            else:
                continue
            print("Clave de la materia del cual quiere actualizar/corregir datos")
            clave = input()
            nombre = s_materia(clave)
            if nombre != None:   
                while True:
                    print(f"El nombre de la materia es {nombre}? y/n")
                    correcto = input()
                    if correcto in("y","Y"):
                        while True:
                            print("Nuevo nombre: ")
                            new_nombre = input()
                            if new_nombre:
                                corregir_datos_s_materia(clave,new_nombre)
                                break
                            else:
                                continue
                    elif correcto in ("N","n"):
                        break
                    else:
                        continue
                    break
        
    elif opcion == 0:
        exit()

    
    
    
