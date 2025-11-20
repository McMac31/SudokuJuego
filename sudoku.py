#Primero crear la matriz 9x9
from random import random, randint
import time
import json

class Sudoku:
    def __init__(self):
        self.GameOver=False
        self.matriz=[[" "," "," "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "," "," "]
        ]

    def Presentacion(self):
        print(""" 
    ██████╗ ██╗███████╗███╗   ██╗██╗   ██╗███████╗███╗   ██╗██╗██████╗  ██████╗ 
    ██╔══██╗██║██╔════╝████╗  ██║██║   ██║██╔════╝████╗  ██║██║██╔══██╗██╔═══██╗
    ██████╔╝██║█████╗  ██╔██╗ ██║██║   ██║█████╗  ██╔██╗ ██║██║██║  ██║██║   ██║
    ██╔══██╗██║██╔══╝  ██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║██║  ██║██║   ██║
    ██████╔╝██║███████╗██║ ╚████║ ╚████╔╝ ███████╗██║ ╚████║██║██████╔╝╚██████╔╝
    ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═╝╚═════╝  ╚═════╝ """)
        time.sleep(1)
        print("""   
    █████╗ ██╗     
    ██╔══██╗██║     
    ███████║██║     
    ██╔══██║██║     
    ██║  ██║███████╗
    ╚═╝  ╚═╝╚══════╝""")
        time.sleep(1)

        print("""  
    ███████╗██╗   ██╗██████╗  ██████╗ ██╗  ██╗██╗   ██╗██╗██╗
    ██╔════╝██║   ██║██╔══██╗██╔═══██╗██║ ██╔╝██║   ██║██║██║
    ███████╗██║   ██║██║  ██║██║   ██║█████╔╝ ██║   ██║██║██║
    ╚════██║██║   ██║██║  ██║██║   ██║██╔═██╗ ██║   ██║╚═╝╚═╝
    ███████║╚██████╔╝██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██╗██╗
    ╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚═╝
                                                                        """)
        time.sleep(2)
        self.nombre= input("Cual es tu nombre? ")
        self.apellido= input("Cual es tu apellido? ")
    def MostrarTablero(self):
        print("     0   1   2     3   4   5     6   7   8")   
        print("    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    
        
        for i in range(len(self.matriz)):
            tab=f""" {i} ▐ {self.matriz[i][0]} ▐ {self.matriz[i][1]} ▐ {self.matriz[i][2]} |▓| {self.matriz[i][3]} ▐ {self.matriz[i][4]} ▐ {self.matriz[i][5]} |▓| {self.matriz[i][6]} ▐ {self.matriz[i][7]} ▐ {self.matriz[i][8]} ▐ """
            print(tab)
            if i==2 or i==5:
                print("    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")


    #Meter numeros aleatorios que no se repitan en indices aleatorios
    def numerosIniciales(self):
        for i in range(300):#Se pone a 300 para probar mas rapidamente
            rellenoAleatorio=randint(1,9)
            filAleatoria=randint(0,8)
            colAleatoria=randint(0,8)
            self.matriz[filAleatoria][colAleatoria]=rellenoAleatorio
    
    def crearDiccionario(self):
        datos_estudiante={"nombre":self.nombre,
                          "apellido":self.apellido,
                          "api_url":"",
                          "sudoku":self.matriz
                          }
        return datos_estudiante



    #hacer que el usuario meta numeros en posicion indicada
    def rellenarPosiciones(self):
        while(self.GameOver==False):
            jugadaUsuario= int(input("Ingrese el numero para rellenar la posicion " ))
            fila=int(input("En que fila ingresara el numero? " ))
            columna=int(input("En que columna ingresara el numero? " ))
            self.matriz[fila][columna]=jugadaUsuario
            if all(posiciones != " " for fila in self.matriz for posiciones in fila):
                self.GameOver=True
            self.MostrarTablero()
            
    def partida(self):
        self.Presentacion()
        self.numerosIniciales()
        self.MostrarTablero()
        self.rellenarPosiciones()

        if self.GameOver== True:
            print("""      
        ███████╗███████╗     █████╗  ██████╗ █████╗ ██████╗  ██████╗     ███████╗██╗              ██╗██╗   ██╗███████╗ ██████╗  ██████╗ 
        ██╔════╝██╔════╝    ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗    ██╔════╝██║              ██║██║   ██║██╔════╝██╔════╝ ██╔═══██╗
        ███████╗█████╗      ███████║██║     ███████║██████╔╝██║   ██║    █████╗  ██║              ██║██║   ██║█████╗  ██║  ███╗██║   ██║
        ╚════██║██╔══╝      ██╔══██║██║     ██╔══██║██╔══██╗██║   ██║    ██╔══╝  ██║         ██   ██║██║   ██║██╔══╝  ██║   ██║██║   ██║
        ███████║███████╗    ██║  ██║╚██████╗██║  ██║██████╔╝╚██████╔╝    ███████╗███████╗    ╚█████╔╝╚██████╔╝███████╗╚██████╔╝╚██████╔╝
        ╚══════╝╚══════╝    ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═════╝     ╚══════╝╚══════╝     ╚════╝  ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ """)
            datos=self.crearDiccionario()
            with open("Datos.json","w+") as archivo:
                json.dump(datos,archivo,indent=4)

        

Juego=Sudoku()
Juego.partida()


