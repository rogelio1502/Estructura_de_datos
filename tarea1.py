import pandas as pd
import time
import os
cont = 0

class Menu:
    def __init__(self):
        
        while True:
            os.system("cls")
            print(" Elija una opción \n 1)Cargar Lista \n 2)Capturar calificaciones \n 3)Calificaciones de los alumnos \n 4)Salir del Programa")
            answer = input()
            if answer.isdigit():
                answer = int (answer)
                if answer == 1:
                    self.cargarLista()
                elif answer == 2:
                    self.capturarCalificaciones()
                elif answer == 3:
                    self.mostrarCalificaciones()
                elif answer == 4:
                    break
                else:
                    print("Opcion no disponible")
            else:
                print("El valor introducido debe ser un Entero, no un String")
    def cargarLista(self):
        os.system("cls")
        global cont
        if cont==0:
            
            try:
                self.data_alumnos = pd.read_csv("alumnos.csv",index_col=0)
                print("Cargando Archivo con origen en el ordenador.")
                self.calificaciones = list()
                print("Archivo Cargado")
                for i in self.data_alumnos.columns:
                    self.calificaciones.append(i)
                
                cont=cont+1
                print("Volviendo al Menu")
                time.sleep(5)
            
            except:
                alumnos=dict()
                print("No se encontro un archivo de origen, se procedera a crear uno")
                for i in range(3):
                    alumnos[i+1]=[0,0,0,0,0,0]
            
                self.calificaciones = ["Programacion","Contabilidad","Base de Datos","Ingles","Redes","Promedio"]
                _data_alumnos = pd.DataFrame(alumnos)
                _data_alumnos.index = [self.calificaciones]
    
                _data_alumnos.T.to_csv(r"alumnos.csv",index=True,header=True)
                self.data_alumnos = _data_alumnos.T
                _data_alumnos=None
                print("Archivo cargado")
                cont=cont+1
                print("Volviendo al Menu")
                time.sleep(5)
        else:
            print("Ya tiene el archivo cargado, sir")
            print("Volviendo al Menu")
            time.sleep(5)
   
    def capturarCalificaciones(self):
        os.system("cls")
        try:
            for i in self.data_alumnos.index:
                os.system("cls")
                _calificaciones = list()
                for y in range(len(self.calificaciones)-1):
                    while True:
                        print(f"Calificacion del alumno {i} en {self.calificaciones[y]}")
                        cal = input()
                        if cal.isdigit():
                            cal=int(cal)
                            if cal >= 0 and cal<=100:

                                _calificaciones.append(cal)
                                break
                            else:
                                print("La calificacion debe ser mayor igual a 0 o menor igual a 100")
                        else:
                            print("No se permiten valores de tipo String")
                _calificaciones.append(0)
                self.data_alumnos.loc[i]=_calificaciones
                _calificaciones = None
            self.data_alumnos['Promedio'] = self.data_alumnos.mean(axis=1)
            while True:
                answer = input("Desea guardar los cambios? y/n")
                if answer == "y" or answer == "Y":
                    self.data_alumnos.to_csv(r'alumnos.csv',index=True,header=True)
                    del(self.data_alumnos)
                    self.data_alumnos = pd.read_csv('alumnos.csv',index_col=0)
                    print("Cambios guardados con exito")
                    print("Redirigiendose al menu")
                    time.sleep(5)
                    break
                elif answer == "n" or answer == "N":
                    print("No se han guardado los datos")
                    print("Volviendo al Menu Principal")
                    time.sleep(5)
                    break
                else:
                    continue
        except:
            while True:
                print("No se  ha cargado ningun archivo")
                print("Desea cargar uno? y/n")
                answer = input()
                if answer == "y" or answer == "Y":
                    self.cargarLista()
                    break
                elif answer == "n" or answer == "N":
                    print("Volviendo al menu")
                    time.sleep(5)
                    break
                else:
                    print("Opcion no valida")

    def mostrarCalificaciones(self):
        os.system("cls")
        try:
            df = self.data_alumnos
            print("---------------Listado completo de calificaciones------------------")
            print(self.data_alumnos)
            time.sleep(2)
        
            print("------------------Promedio general de las asignaturas------------------")
            self.copy_data_alumnos=self.data_alumnos.to_dict()
            del self.copy_data_alumnos['Promedio']
            self._materias_frame=pd.DataFrame(self.copy_data_alumnos)
            
        
            self.materias_frame=self._materias_frame.T
            self.materias_frame["Promedio General"]=self.materias_frame.mean(axis=1)
            
            
            self.materias_frame=self.materias_frame.sort_values(by="Promedio General")
            print(self.materias_frame['Promedio General'])
            time.sleep(2)
            
            print("------------Alumnos con mas de 2 materias reprobadas---------------")
            lista_conteo = list()
            
            for i in self.data_alumnos.index:
                conteo=0
                for y in range(len(self.calificaciones)-1):
                    if self.data_alumnos.loc[i][self.calificaciones[y]] < 70:
                        conteo=conteo+1
                        
                lista_conteo.append(conteo)
            print("Matricula de alumnos con mas de dos materias reprobadas")
            for i in range(len(lista_conteo)):
                
                if lista_conteo[i] >= 2:
                    
                    print(self.data_alumnos.index[i])
            print(self.data_alumnos)
            while True:
                print("Desea ir al menu? y/n")
                answer = input()
                if answer == "y" or answer == "Y":
                    print("Dirigiendose al menu")
                    time.sleep(5)
                    break
                elif answer == "n" or answer == "N":
                    continue
                else:
                    print("Opcion no valida")
                
                
        except:
            while True:
                
                print("No se  ha cargado ningun archivo")
                print("Desea cargar uno? y/n")
                answer = input()
                if answer == "y" or answer == "Y":
                    self.cargarLista()
                    break
                elif answer == "n" or answer == "N":
                    break
                else:
                    print("Opcion no valida")
        
menu=Menu()
