# -*- coding: utf-8 -*-f
# Importe módulo sudoku
from sudoku import *
'''Desidi no usar from sodoku import * Por que el interprete me mostrava la
señal de advertencia y para mi era muy molesto y no quiero que mi codigo
se vea defectuoso me advertia que las funciones no existion o que tal vez 
estavan en el archivo sodoku'''
# Importe otros paquetes o modulos que pueda necesitar
import copy
# Imprima en consola el mensaje de bienvenida
printIntro("Python\lb\sodoku\sudoku.txt")
# Seleccione aleatoriamente el tablero inicial desde alguna de las 5 plantillas
txt = 0
text = getRandomSudoku(txt)
# Imprima el tablero inicial	a
printSudoku(text)
# Ciclo principal del juego
# Variables Extras
nue = getRandomSudoku(txt)
copia = copy.deepcopy(text)
ia = ()
_c = ('                              '+'               ')
while True:
        # Implemente la lógica y funcionamiento del juego aquí
    sd = str(text)
    if '0' in sd:
        asu = 0
        print(chr(27)+"[32;1m")
        print('¬ Ingresar comando "ayuda" para leer las instrucciones \n \n')
        cd = input('Por favor ingrese su coordenada = ')
        
        print(chr(27)+"[0m")
        dic = {'a': 0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8}
        if (cd.lower() != 'exit' and len(cd) == 4) == True:
           fil = cd[0]
           #and cd[1].isalnum == True
           fil = fil.lower()
           numero = cd[1]
           rempl = cd[3]
           ol = int(numero)
           col = ol - 1
           lugar = int(rempl)
           col = col  
           checkBloque(fil,col,text,dic,lugar,numero,text,cd,asu,copia)
        elif (cd[:1] == 'm' or cd[:1] == 'M') == True:
            asu = 1
            fil = cd[1]
            numero = cd[2].lower()
            rempl = cd[4] #numero deberia ser lugary visebersa pero ya me envolato
            ol = int(numero)
            col = ol - 1
            dic = {'a': 0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8}
            #rem = chr(27)+"[1;35m"+rempl+chr(27)+"[0m"# NO d apor esto
            lugar = int(rempl)
            col = col
            checkBloque(fil,col,text,dic,lugar,numero,text,cd,asu,copia)
        elif ('clear' in cd.lower() or 'CLEAR' in cd.lower()) == True:
            if 'clear board' in cd.lower():
                asu = 3
                text = copy.deepcopy(copia)
                checkBloque(fil,col,text,dic,lugar,numero,text,cd,asu,copia)
            else:
                asu = 2
                fil = cd[6]
                numero = cd[7]
                ol = int(numero)
                col = ol - 1
                dic = {'a': 0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8}
                #rem = chr(27)+"[1;35m"+rempl+chr(27)+"[0m"# NO d apor esto
                lugar = 0
                col = col
                checkBloque(fil,col,text,dic,lugar,numero,text,cd,asu,copia)
        elif 'new' == cd.lower():
            asu = 4
            fil = 0
            numero = 0
            col = 0
            lugar = 0
            dic = 0
            text = getRandomSudoku(txt)
            checkBloque(fil,col,text,dic,lugar,numero,text,cd,asu,copia)
        elif 'ayuda' == cd.lower():
            print('Bienvenido al Manual de instrucciones sodoku')
            print('Creado por Danis Abadia Bejarano "Industries Abby"')
            print(_c[:20]+chr(27)+"[36;4m"+'Instrucciones'+chr(27)+"[0m")
            printIntro("instrucciones")
        elif 'exit' in cd.lower():
            asu = 5
            printIntro("adios.txt")
            sado = input('Industries Abby')
            break
        elif 'save' in cd.lower(): 
            if cd.lower() != 'savering':
                filenames = cd.replace('save','').replace(' ','')
                registro = filenames
                mtxt(registro)
                creartxt(filenames,text)
            else:
                printIntro("56446gfh5f.txt")
        elif 'load' in cd.lower():
            asu = 6
            filename = cd.replace('load','').replace(' ','')
            lsd = abrirg(filename)
            text = lsd
            asu = 6
            fil = 0
            numero = 0
            col = 0
            lugar = 0
            dic = 0
            cd = 0
            checkFil(fil,text,dic,lugar,col,numero,cd,asu,copia)
            checkCol(col,fil,lugar,numero,dic,text,cd,asu,copia)
            checkBloque(fil,col,text,dic,lugar,numero,text,cd,asu,copia)
        else:
            print('Error comando desconocido')
    else:
        asu = 6
        fil = 0
        numero = 0
        col = 0
        lugar = 0
        dic = 0
        cd = 0
        checkBloque(fil,col,text,dic,lugar,numero,text,cd,asu,copia)
        chr(27)+"[35;4m"
        printIntro("win")
   
