#Primero crear la matriz 9x9
from random import random, randint
import time

GameOver=False
matriz=[[" "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "]
        
]

def Presentacion():
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



def MostrarTablero():
    print("     0   1   2     3   4   5     6   7   8")   
    print("    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
  
    
    for i in range(len(matriz)):
        tab=f""" {i} ▐ {matriz[i][0]} ▐ {matriz[i][1]} ▐ {matriz[i][2]} |▓| {matriz[i][3]} ▐ {matriz[i][4]} ▐ {matriz[i][5]} |▓| {matriz[i][6]} ▐ {matriz[i][7]} ▐ {matriz[i][8]} ▐ """
        print(tab)
        if i==2 or i==5:
            print("    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print("    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")


#Meter numeros aleatorios que no se repitan en indices aleatorios
def numerosIniciales():
      for i in range(20):#Se pone a 300 para probar mas rapidamente
        rellenoAleatorio=randint(0,9)
        filAleatoria=randint(0,8)
        colAleatoria=randint(0,8)
        matriz[filAleatoria][colAleatoria]=rellenoAleatorio


#hacer que el usuario meta numeros en posicion indicada
def rellenarPosiciones():
    global GameOver
    while(GameOver==False):
        jugadaUsuario= int(input("Ingrese el numero para rellenar la posicion " ))
        fila=int(input("En que fila ingresara el numero? " ))
        columna=int(input("En que columna ingresara el numero? " ))
        matriz[fila][columna]=jugadaUsuario
        if all(posiciones != " " for fila in matriz for posiciones in fila):
            GameOver=True
        MostrarTablero()
        

Presentacion()
numerosIniciales()
MostrarTablero()
rellenarPosiciones()

if GameOver== True:
    print("""      
███████╗███████╗     █████╗  ██████╗ █████╗ ██████╗  ██████╗     ███████╗██╗              ██╗██╗   ██╗███████╗ ██████╗  ██████╗ 
██╔════╝██╔════╝    ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗    ██╔════╝██║              ██║██║   ██║██╔════╝██╔════╝ ██╔═══██╗
███████╗█████╗      ███████║██║     ███████║██████╔╝██║   ██║    █████╗  ██║              ██║██║   ██║█████╗  ██║  ███╗██║   ██║
╚════██║██╔══╝      ██╔══██║██║     ██╔══██║██╔══██╗██║   ██║    ██╔══╝  ██║         ██   ██║██║   ██║██╔══╝  ██║   ██║██║   ██║
███████║███████╗    ██║  ██║╚██████╗██║  ██║██████╔╝╚██████╔╝    ███████╗███████╗    ╚█████╔╝╚██████╔╝███████╗╚██████╔╝╚██████╔╝
╚══════╝╚══════╝    ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═════╝     ╚══════╝╚══════╝     ╚════╝  ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ """)
    










