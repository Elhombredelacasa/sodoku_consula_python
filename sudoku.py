# -*- coding: utf-8 -*-
# Implemente cada una de las funciones descritas a continuación

def printIntro(filename):
   a = open(filename,"r")
   b = a.read()
   print ('                   '+'"Bienvenidos "Industries AbbyInc."')
   print(chr(27)+"[1;33m"+b+chr(27)+"[0m")
   a.close()
'''
	Imprime el contenido de un archivo en pantalla. El archivo contiene
	un mensaje de bienvenida del juego.		
	Entradas y salidas:
		- inputs: string que contiene el nombre del archivo
		- returns: ninguno, solo imprime el archivo leído en pantalla	
	'''



def getRandomSudoku(n_sud): #agregar mas opciones
    import random
    c = random.randrange(6)
    w = str(c)
    q =('sd')
    t = (".txt")
    texto = q + w + t
    a = open(texto,'r')
    e = []
    for linea in a.readlines():
        partes_linea = linea.split()
        e.append(partes_linea)
    cambio = str(e)
    ptr = cambio.replace('"', '').replace("'", '')
    #itr = ptr + ptr.replace('0',(chr(27)+"[1;32m"+'0'+chr(27)+"[0m"))
    arreglo = ptr
    m = eval(arreglo)
    matriz = m
    # se puede omitir es provicional
    #matriz[1][0] = 18 #mas o menos asi
    n_sud = matriz
    return n_sud
        
  
'''
	Selecciona aleatoriamente uno de los archivos para cargarlo como juego 
	inicial en un arreglo 2D.		
	Entradas y salidas:
		- inputs: int con el número de sudokus disponibles
		- return: list de dos dimensiones (9x9) conteniendo el sudoku	
	'''


def printSudoku(M):
    global text
    q = ('                        '+'   1  2  3  4  5  6  7  8  9')
    a,b=('                      '+'a'+'  '),('                      '+'b'+'  ')
    c,d=('                      '+'c'+'  '),('                      '+'d'+'  ')
    e,f=('    Dani Abbey inc.   '+'e'+'  '),('                      '+'f'+'  ')
    g,h=('                      '+'g'+'  '),('                      '+'h'+'  ')
    i=('                      '+'i'+'  ')
    ce,un,do,tr,cu=str(M[0]),str(M[1]),str(M[2]),str(M[3]),str(M[4])
    ci,se,si,oc=str(M[5]),str(M[6]),str(M[7]),str(M[8])
    #mensaje = mensaje[:14] + "o" + mensaje[15:]
    x = (chr(27)+"[1;37m"+'| '+chr(27)+"[0m")
    rce = ce.replace(']',' ').replace(',',' ').replace('[','')
    rce = rce[:8]+'|'+rce[9:]
    rce = rce[:17]+'|'+rce[18:]
    rce = rce.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
    
    
    run = un.replace(']',' ').replace(',',' ').replace('[','')
    run = run[:8]+'|'+run[9:]
    run = run[:17]+'|'+run[18:]
    run = run.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
    
    rdo = do.replace(']',' ').replace(',',' ').replace('[','')
    rdo = rdo[:8]+'|'+rdo[9:]
    rdo = rdo[:17]+'|'+rdo[18:]
    rdo = rdo.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
    
    rtr = tr.replace(']',' ').replace(',',' ').replace('[','')
    rtr = rtr[:8]+'|'+rtr[9:]
    rtr = rtr[:17]+'|'+rtr[18:]
    rtr = rtr.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
    
    rcu = cu.replace(']',' ').replace(',',' ').replace('[','')
    rcu = rcu[:8]+'|'+rcu[9:]
    rcu = rcu[:17]+'|'+rcu[18:]
    rcu = rcu.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
    
    rci = ci.replace(']',' ').replace(',',' ').replace('[','')
    rci = rci[:8]+'|'+rci[9:]
    rci = rci[:17]+'|'+rci[18:]
    rci = rci.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
    
    rse = se.replace(']',' ').replace(',',' ').replace('[','')
    rse = rse[:8]+'|'+rse[9:]
    rse = rse[:17]+'|'+rse[18:]
    rse = rse.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
    
    rsi = si.replace(']',' ').replace(',',' ').replace('[','')
    rsi = rsi[:8]+'|'+rsi[9:]
    rsi = rsi[:17]+'|'+rsi[18:]
    rsi = rsi.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
    
    roc = oc.replace(']',' ').replace(',',' ').replace('[','')
    roc = roc[:8]+'|'+roc[9:]
    roc = roc[:17]+'|'+roc[18:]
    roc = roc.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
    
    esp = ('                                                                ')
    neg = (chr(27)+"[1;37m"+'|———————————————————————————|'+chr(27)+"[0m")
    print(chr(27)+"[1;36m"+q+chr(27)+"[0m")
    print('')
    print(esp[:25]+neg)
    print(chr(27)+"[1;32m"+a+chr(27)+"[0m"+x+rce+x)
    print(chr(27)+"[1;32m"+b+chr(27)+"[0m"+x+run+x)
    print(chr(27)+"[1;32m"+c+chr(27)+"[0m"+x+rdo+x)
    print(esp[:25]+neg)
    print(chr(27)+"[1;32m"+d+chr(27)+"[0m"+x+rtr+x)
    print(chr(27)+"[1;32m"+e+chr(27)+"[0m"+x+rcu+x)
    print(chr(27)+"[1;32m"+f+chr(27)+"[0m"+x+rci+x)
    print(esp[:25]+neg)
    print(chr(27)+"[1;32m"+g+chr(27)+"[0m"+x+rse+x)
    print(chr(27)+"[1;32m"+h+chr(27)+"[0m"+x+rsi+x)
    print(chr(27)+"[1;32m"+i+chr(27)+"[0m"+x+roc+x)# Esto es lo que are en la funcion 
    print(esp[:25]+neg)
    print('')
    print(chr(27)+"[5;33m"+'¬ Recuerda para jugar debes ingresar la coordenada')
    print('de la celda que deseas modificar seguida del número. Ej: "b7 4"')
    print('Recuerde poner solo un espacio como en el ejemplo anterior')
    print(''+chr(27)+"[0m")
'''
	Imprime en pantalla el Sudoku de forma amigable para el usuario.		
	Entradas y salidas:
		- inputs: list de 9x9 conteniendo el sudoku
		- return: nada	
	'''

def validCoord(M,col,dic,fil,lugar,numero,cd,asu,copia):
    if asu == 2:
        if copia[dic[fil]][col] == 0:
            M[dic[fil]][col] = 0
            return True        
        else:
            print('NO puedes limpiar esta casilla')
            return False
    elif asu == 5:
        return True
    elif asu == 4:
        return True
    elif asu == 3:
        return True
    elif asu == 1:
        if copia[dic[fil]][col] == 0:
            M = M[dic[fil]][col]
            return True        
        else:
            print('No puedes modificar esta casilla')
            return False
    elif asu == 6:
        return True
    else:        
        if M[dic[fil]][col] == 0:
            #M = M[dic[fil]][col]
            return True        
        else:
            return False
      
'''
		
	Entradas y salidas:
		- inputs: string que contiene la coordenada
		- return: True si la coordenada es válida, False en caso contrario	
	'''
def checkFil(fil,text,dic,lugar,col,numero,cd,asu,copia):
    if asu == 2:
        if validCoord(text,col,dic,fil,lugar,numero,cd,asu,copia) == True:
            return True        
        else:
            print('Esta posicion en fila pertenece al Panel de Juego')
            return False        
    elif asu == 5:
        return True    
    elif asu == 4:
        return True
    elif asu == 3:
        return True
    elif asu == 6:
        return True
    else:
        if validCoord(text,col,dic,fil,lugar,numero,cd,asu,copia) == True:
            if lugar in text[dic[fil]]:
                print('El valor %d ya existe en esta fila'%(lugar))
                return False
            else:
                return True
        else:
            return False
              
                #for i in range(len(text[dic[fil]])):
                    #if (text[dic[fil]])[i] == lugar:
                       # a = 20
                    
                    #else:
                     #   n = 0
                
                #if a == 20:
                  #  print('El valor',lugar,'Ya existe en esta Fila')
                 #   return False
                #else:
                 #   print('todo salio bien y la coordenada no se repite')
                  #  return True
              
'''
	Verifica si en la fila especificada ya existe el número que se quiere ingresar.
	Entradas y salidas:
		- inputs: int fila, int número y list que contiene el sudoku
		- return: True si es posible ingresar el valor, False en caso contrario	
	'''

				
def checkCol(col,fil,lugar,numero,dic,text,cd,asu,copia):
    if checkFil(fil,text,dic,lugar,col,numero,cd,asu,copia) == True:
        if asu == 2:
            if checkFil(fil,text,dic,lugar,col,numero,cd,asu,copia) == True:
                return True        
            else:
                print('Esta posicion en columna pertenece al Panel de Juego')
                return False
        elif asu == 5:
            return True
        elif asu == 4:
            return True
        elif asu == 3:
            return True
        elif asu == 6:
            return True
        else:
            b = 0
            if b == 0:
                for l in range(len(text[col])):
                    if text[l][col] == lugar:
                        b = 20
                if b == 20:
                    print('El valor %d Ya existe en esta columna'%(lugar))
                    return False
                else:
                    return True
    else:
        return False
        print('El valor %d No puede ser ingresado'%(lugar))
                
              
                
            
                
    '''
	Verifica si en la columna especificada ya existe el número que se quiere ingresar.		
	Entradas y salidas:
		- inputs: int columna, int dato y list que contiene el sudoku
		- return: True si es posible ingresar el valor, False en caso contrario
    '''		
def checkBloque(fil,col,M,dic,lugar,numero,text,cd,asu,copia):
    if checkCol(col,fil,lugar,numero,dic,text,cd,asu,copia) == True:
        if asu == 3:
            asu = 0
            t = text
            q = ('                        '+'   1  2  3  4  5  6  7  8  9')
            a,b=('                      '+'a'+'  '),('                      '+'b'+'  ')
            c,d=('                      '+'c'+'  '),('                      '+'d'+'  ')
            e,f=('    Dani Abbey inc.   '+'e'+'  '),('                      '+'f'+'  ')
            g,h=('                      '+'g'+'  '),('                      '+'h'+'  ')
            i=('                      '+'i'+'  ')
            ce,un,do,tr,cu=str(t[0]),str(t[1]),str(t[2]),str(t[3]),str(t[4])
            ci,se,si,oc=str(t[5]),str(t[6]),str(t[7]),str(t[8])
            #mensaje = mensaje[:14] + "o" + mensaje[15:]
            x = (chr(27)+"[1;37m"+'| '+chr(27)+"[0m")
            rce = ce.replace(']',' ').replace(',',' ').replace('[','')
            rce = rce[:8]+'|'+rce[9:]
            rce = rce[:17]+'|'+rce[18:]
            rce = rce.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
            
            
            run = un.replace(']',' ').replace(',',' ').replace('[','')
            run = run[:8]+'|'+run[9:]
            run = run[:17]+'|'+run[18:]
            run = run.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
            
            rdo = do.replace(']',' ').replace(',',' ').replace('[','')
            rdo = rdo[:8]+'|'+rdo[9:]
            rdo = rdo[:17]+'|'+rdo[18:]
            rdo = rdo.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
            
            rtr = tr.replace(']',' ').replace(',',' ').replace('[','')
            rtr = rtr[:8]+'|'+rtr[9:]
            rtr = rtr[:17]+'|'+rtr[18:]
            rtr = rtr.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
            
            rcu = cu.replace(']',' ').replace(',',' ').replace('[','')
            rcu = rcu[:8]+'|'+rcu[9:]
            rcu = rcu[:17]+'|'+rcu[18:]
            rcu = rcu.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
            
            rci = ci.replace(']',' ').replace(',',' ').replace('[','')
            rci = rci[:8]+'|'+rci[9:]
            rci = rci[:17]+'|'+rci[18:]
            rci = rci.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
            
            rse = se.replace(']',' ').replace(',',' ').replace('[','')
            rse = rse[:8]+'|'+rse[9:]
            rse = rse[:17]+'|'+rse[18:]
            rse = rse.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
            
            rsi = si.replace(']',' ').replace(',',' ').replace('[','')
            rsi = rsi[:8]+'|'+rsi[9:]
            rsi = rsi[:17]+'|'+rsi[18:]
            rsi = rsi.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
            
            roc = oc.replace(']',' ').replace(',',' ').replace('[','')
            roc = roc[:8]+'|'+roc[9:]
            roc = roc[:17]+'|'+roc[18:]
            roc = roc.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
            
            esp = ('                                                                ')
            neg = (chr(27)+"[1;37m"+'|———————————————————————————|'+chr(27)+"[0m")
            
            print(chr(27)+"[1;36m"+q+chr(27)+"[0m")
            print('')
            print(esp[:25]+neg)
            print(chr(27)+"[1;32m"+a+chr(27)+"[0m"+x+rce+x)
            print(chr(27)+"[1;32m"+b+chr(27)+"[0m"+x+run+x)
            print(chr(27)+"[1;32m"+c+chr(27)+"[0m"+x+rdo+x)
            print(esp[:25]+neg)
            print(chr(27)+"[1;32m"+d+chr(27)+"[0m"+x+rtr+x)
            print(chr(27)+"[1;32m"+e+chr(27)+"[0m"+x+rcu+x)
            print(chr(27)+"[1;32m"+f+chr(27)+"[0m"+x+rci+x)
            print(esp[:25]+neg)
            print(chr(27)+"[1;32m"+g+chr(27)+"[0m"+x+rse+x)
            print(chr(27)+"[1;32m"+h+chr(27)+"[0m"+x+rsi+x)
            print(chr(27)+"[1;32m"+i+chr(27)+"[0m"+x+roc+x)# Esto es lo que are en la funcion 
            print(esp[:25]+neg)
            print('')
            print(chr(27)+"[5;33m"+'¬ Recuerda para jugar debes ingresar la coordenada')
            print('de la celda que deseas modificar seguida del número. Ej: "b7 4"')
            print('Recuerde poner solo un espacio como en el ejemplo anterior')
            print(''+chr(27)+"[0m")
        
        elif asu == 5:
            print('SODOKU')
        elif asu == 2:
                q = ('                        '+'   1  2  3  4  5  6  7  8  9')
                a,b=('                      '+'a'+'  '),('                      '+'b'+'  ')
                c,d=('                      '+'c'+'  '),('                      '+'d'+'  ')
                e,f=('    Dani Abbey inc.   '+'e'+'  '),('                      '+'f'+'  ')
                g,h=('                      '+'g'+'  '),('                      '+'h'+'  ')
                i=('                      '+'i'+'  ')
                ce,un,do,tr,cu=str(M[0]),str(M[1]),str(M[2]),str(M[3]),str(M[4])
                ci,se,si,oc=str(M[5]),str(M[6]),str(M[7]),str(M[8])
                #mensaje = mensaje[:14] + "o" + mensaje[15:]
                x = (chr(27)+"[1;37m"+'| '+chr(27)+"[0m")
                rce = ce.replace(']',' ').replace(',',' ').replace('[','')
                rce = rce[:8]+'|'+rce[9:]
                rce = rce[:17]+'|'+rce[18:]
                rce = rce.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
                
                
                run = un.replace(']',' ').replace(',',' ').replace('[','')
                run = run[:8]+'|'+run[9:]
                run = run[:17]+'|'+run[18:]
                run = run.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
                
                rdo = do.replace(']',' ').replace(',',' ').replace('[','')
                rdo = rdo[:8]+'|'+rdo[9:]
                rdo = rdo[:17]+'|'+rdo[18:]
                rdo = rdo.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
                
                rtr = tr.replace(']',' ').replace(',',' ').replace('[','')
                rtr = rtr[:8]+'|'+rtr[9:]
                rtr = rtr[:17]+'|'+rtr[18:]
                rtr = rtr.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
                
                rcu = cu.replace(']',' ').replace(',',' ').replace('[','')
                rcu = rcu[:8]+'|'+rcu[9:]
                rcu = rcu[:17]+'|'+rcu[18:]
                rcu = rcu.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
                
                rci = ci.replace(']',' ').replace(',',' ').replace('[','')
                rci = rci[:8]+'|'+rci[9:]
                rci = rci[:17]+'|'+rci[18:]
                rci = rci.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
                
                rse = se.replace(']',' ').replace(',',' ').replace('[','')
                rse = rse[:8]+'|'+rse[9:]
                rse = rse[:17]+'|'+rse[18:]
                rse = rse.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
                
                rsi = si.replace(']',' ').replace(',',' ').replace('[','')
                rsi = rsi[:8]+'|'+rsi[9:]
                rsi = rsi[:17]+'|'+rsi[18:]
                rsi = rsi.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
                
                roc = oc.replace(']',' ').replace(',',' ').replace('[','')
                roc = roc[:8]+'|'+roc[9:]
                roc = roc[:17]+'|'+roc[18:]
                roc = roc.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
                
                esp = ('                                                                ')
                neg = (chr(27)+"[1;37m"+'|———————————————————————————|'+chr(27)+"[0m")
    
                #rce = rce[:col]+chr(27)+"[1;33m"+str(lugar)+chr(27)+"[0m"+rce[col+1:]
                #run = run[:col]+chr(27)+"[1;33m"+str(lugar)+chr(27)+"[0m"+run[col+1:]
                #rdo = rdo[:col]+chr(27)+"[1;33m"+str(lugar)+chr(27)+"[0m"+rdo[col+1:]
                #rtr = rtr[:col]+chr(27)+"[1;33m"+str(lugar)+chr(27)+"[0m"+rtr[col+1:]
                #rcu = rcu[:col]+chr(27)+"[1;33m"+str(lugar)+chr(27)+"[0m"+rcu[col+1:]
                #rci = rci[:col]+chr(27)+"[1;33m"+str(lugar)+chr(27)+"[0m"+rci[col+1:]
                #rse = rse[:col]+chr(27)+"[1;33m"+str(lugar)+chr(27)+"[0m"+rse[col+1:]
                #rsi = rsi[:col]+chr(27)+"[1;33m"+str(lugar)+chr(27)+"[0m"+rsi[col+1:]
                #roc = roc[:col]+chr(27)+"[1;33m"+str(lugar)+chr(27)+"[0m"+roc[col+1:]               
                
                print(chr(27)+"[1;36m"+q+chr(27)+"[0m")
                print('')
                print(esp[:25]+neg)
                print(chr(27)+"[1;32m"+a+chr(27)+"[0m"+x+rce+x)
                print(chr(27)+"[1;32m"+b+chr(27)+"[0m"+x+run+x)
                print(chr(27)+"[1;32m"+c+chr(27)+"[0m"+x+rdo+x)
                print(esp[:25]+neg)
                print(chr(27)+"[1;32m"+d+chr(27)+"[0m"+x+rtr+x)
                print(chr(27)+"[1;32m"+e+chr(27)+"[0m"+x+rcu+x)
                print(chr(27)+"[1;32m"+f+chr(27)+"[0m"+x+rci+x)
                print(esp[:25]+neg)
                print(chr(27)+"[1;32m"+g+chr(27)+"[0m"+x+rse+x)
                print(chr(27)+"[1;32m"+h+chr(27)+"[0m"+x+rsi+x)
                print(chr(27)+"[1;32m"+i+chr(27)+"[0m"+x+roc+x)# Esto es lo que are en la funcion 
                print(esp[:25]+neg)
                print('')
                print(chr(27)+"[5;33m"+'¬ Recuerda para jugar debes ingresar la coordenada')
                print('de la celda que deseas modificar seguida del número. Ej: "b7 4"')
                print('Recuerde poner solo un espacio como en el ejemplo anterior')
                print(''+chr(27)+"[0m")
        elif asu == 6:
                q = ('                        '+'   1  2  3  4  5  6  7  8  9')
                a,b=('                      '+'a'+'  '),('                      '+'b'+'  ')
                c,d=('                      '+'c'+'  '),('                      '+'d'+'  ')
                e,f=('    Dani Abbey inc.   '+'e'+'  '),('                      '+'f'+'  ')
                g,h=('                      '+'g'+'  '),('                      '+'h'+'  ')
                i=('                      '+'i'+'  ')
                ce,un,do,tr,cu=str(M[0]),str(M[1]),str(M[2]),str(M[3]),str(M[4])
                ci,se,si,oc=str(M[5]),str(M[6]),str(M[7]),str(M[8])
                #mensaje = mensaje[:14] + "o" + mensaje[15:]
                x = (chr(27)+"[1;37m"+'| '+chr(27)+"[0m")
                rce = ce.replace(']',' ').replace(',',' ').replace('[','')
                rce = rce[:8]+'|'+rce[9:]
                rce = rce[:17]+'|'+rce[18:]
                rce = rce.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
                
                
                run = un.replace(']',' ').replace(',',' ').replace('[','')
                run = run[:8]+'|'+run[9:]
                run = run[:17]+'|'+run[18:]
                run = run.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
                
                rdo = do.replace(']',' ').replace(',',' ').replace('[','')
                rdo = rdo[:8]+'|'+rdo[9:]
                rdo = rdo[:17]+'|'+rdo[18:]
                rdo = rdo.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
                
                rtr = tr.replace(']',' ').replace(',',' ').replace('[','')
                rtr = rtr[:8]+'|'+rtr[9:]
                rtr = rtr[:17]+'|'+rtr[18:]
                rtr = rtr.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
                
                rcu = cu.replace(']',' ').replace(',',' ').replace('[','')
                rcu = rcu[:8]+'|'+rcu[9:]
                rcu = rcu[:17]+'|'+rcu[18:]
                rcu = rcu.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
                
                rci = ci.replace(']',' ').replace(',',' ').replace('[','')
                rci = rci[:8]+'|'+rci[9:]
                rci = rci[:17]+'|'+rci[18:]
                rci = rci.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
                
                rse = se.replace(']',' ').replace(',',' ').replace('[','')
                rse = rse[:8]+'|'+rse[9:]
                rse = rse[:17]+'|'+rse[18:]
                rse = rse.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
                
                rsi = si.replace(']',' ').replace(',',' ').replace('[','')
                rsi = rsi[:8]+'|'+rsi[9:]
                rsi = rsi[:17]+'|'+rsi[18:]
                rsi = rsi.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
                
                roc = oc.replace(']',' ').replace(',',' ').replace('[','')
                roc = roc[:8]+'|'+roc[9:]
                roc = roc[:17]+'|'+roc[18:]
                roc = roc.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
                
                esp = ('                                                                ')
                neg = (chr(27)+"[1;37m"+'|———————————————————————————|'+chr(27)+"[0m")
                               
                    
                print(chr(27)+"[1;36m"+q+chr(27)+"[0m")
                print('')
                print(esp[:25]+neg)
                print(chr(27)+"[1;32m"+a+chr(27)+"[0m"+x+rce+x)
                print(chr(27)+"[1;32m"+b+chr(27)+"[0m"+x+run+x)
                print(chr(27)+"[1;32m"+c+chr(27)+"[0m"+x+rdo+x)
                print(esp[:25]+neg)
                print(chr(27)+"[1;32m"+d+chr(27)+"[0m"+x+rtr+x)
                print(chr(27)+"[1;32m"+e+chr(27)+"[0m"+x+rcu+x)
                print(chr(27)+"[1;32m"+f+chr(27)+"[0m"+x+rci+x)
                print(esp[:25]+neg)
                print(chr(27)+"[1;32m"+g+chr(27)+"[0m"+x+rse+x)
                print(chr(27)+"[1;32m"+h+chr(27)+"[0m"+x+rsi+x)
                print(chr(27)+"[1;32m"+i+chr(27)+"[0m"+x+roc+x)# Esto es lo que are en la funcion 
                print(esp[:25]+neg)
                print('')
                print(chr(27)+"[5;33m"+'¬ Recuerda para jugar debes ingresar la coordenada')
                print('de la celda que deseas modificar seguida del número. Ej: "b7 4"')
                print('Recuerde poner solo un espacio como en el ejemplo anterior')
                print(''+chr(27)+"[0m")
        elif asu == 4:
            q = ('                        '+'   1  2  3  4  5  6  7  8  9')
            a,b=('                      '+'a'+'  '),('                      '+'b'+'  ')
            c,d=('                      '+'c'+'  '),('                      '+'d'+'  ')
            e,f=('    Dani Abbey inc.   '+'e'+'  '),('                      '+'f'+'  ')
            g,h=('                      '+'g'+'  '),('                      '+'h'+'  ')
            i=('                      '+'i'+'  ')
            ce,un,do,tr,cu=str(M[0]),str(M[1]),str(M[2]),str(M[3]),str(M[4])
            ci,se,si,oc=str(M[5]),str(M[6]),str(M[7]),str(M[8])
            #mensaje = mensaje[:14] + "o" + mensaje[15:]
            x = (chr(27)+"[1;37m"+'| '+chr(27)+"[0m")
            rce = ce.replace(']',' ').replace(',',' ').replace('[','')
            rce = rce[:8]+'|'+rce[9:]
            rce = rce[:17]+'|'+rce[18:]
            rce = rce.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
            
            
            run = un.replace(']',' ').replace(',',' ').replace('[','')
            run = run[:8]+'|'+run[9:]
            run = run[:17]+'|'+run[18:]
            run = run.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
            
            rdo = do.replace(']',' ').replace(',',' ').replace('[','')
            rdo = rdo[:8]+'|'+rdo[9:]
            rdo = rdo[:17]+'|'+rdo[18:]
            rdo = rdo.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
            
            rtr = tr.replace(']',' ').replace(',',' ').replace('[','')
            rtr = rtr[:8]+'|'+rtr[9:]
            rtr = rtr[:17]+'|'+rtr[18:]
            rtr = rtr.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
            
            rcu = cu.replace(']',' ').replace(',',' ').replace('[','')
            rcu = rcu[:8]+'|'+rcu[9:]
            rcu = rcu[:17]+'|'+rcu[18:]
            rcu = rcu.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
            
            rci = ci.replace(']',' ').replace(',',' ').replace('[','')
            rci = rci[:8]+'|'+rci[9:]
            rci = rci[:17]+'|'+rci[18:]
            rci = rci.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
            
            rse = se.replace(']',' ').replace(',',' ').replace('[','')
            rse = rse[:8]+'|'+rse[9:]
            rse = rse[:17]+'|'+rse[18:]
            rse = rse.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
            
            rsi = si.replace(']',' ').replace(',',' ').replace('[','')
            rsi = rsi[:8]+'|'+rsi[9:]
            rsi = rsi[:17]+'|'+rsi[18:]
            rsi = rsi.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
            
            roc = oc.replace(']',' ').replace(',',' ').replace('[','')
            roc = roc[:8]+'|'+roc[9:]
            roc = roc[:17]+'|'+roc[18:]
            roc = roc.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
            
            esp = ('                                                                ')
            neg = (chr(27)+"[1;37m"+'|———————————————————————————|'+chr(27)+"[0m")
                     
            
            print(chr(27)+"[1;36m"+q+chr(27)+"[0m")
            print('')
            print(esp[:25]+neg)
            print(chr(27)+"[1;32m"+a+chr(27)+"[0m"+x+rce+x)
            print(chr(27)+"[1;32m"+b+chr(27)+"[0m"+x+run+x)
            print(chr(27)+"[1;32m"+c+chr(27)+"[0m"+x+rdo+x)
            print(esp[:25]+neg)
            print(chr(27)+"[1;32m"+d+chr(27)+"[0m"+x+rtr+x)
            print(chr(27)+"[1;32m"+e+chr(27)+"[0m"+x+rcu+x)
            print(chr(27)+"[1;32m"+f+chr(27)+"[0m"+x+rci+x)
            print(esp[:25]+neg)
            print(chr(27)+"[1;32m"+g+chr(27)+"[0m"+x+rse+x)
            print(chr(27)+"[1;32m"+h+chr(27)+"[0m"+x+rsi+x)
            print(chr(27)+"[1;32m"+i+chr(27)+"[0m"+x+roc+x)# Esto es lo que are en la funcion 
            print(esp[:25]+neg)
            print('')
            print(chr(27)+"[5;33m"+'¬ Recuerda para jugar debes ingresar la coordenada')
            print('de la celda que deseas modificar seguida del número. Ej: "b7 4"')
            print('Recuerde poner solo un espacio como en el ejemplo anterior')
            print(''+chr(27)+"[0m")
            
        elif M[dic[fil]][col] == lugar:
            print('No puedes ingresar este valor')
            return False  
        else:
            M[dic[fil]][col] = lugar
            q = ('                        '+'   1  2  3  4  5  6  7  8  9')
            a,b=('                      '+'a'+'  '),('                      '+'b'+'  ')
            c,d=('                      '+'c'+'  '),('                      '+'d'+'  ')
            e,f=('    Dani Abbey inc.   '+'e'+'  '),('                      '+'f'+'  ')
            g,h=('                      '+'g'+'  '),('                      '+'h'+'  ')
            i=('                      '+'i'+'  ')
            ce,un,do,tr,cu=str(M[0]),str(M[1]),str(M[2]),str(M[3]),str(M[4])
            ci,se,si,oc=str(M[5]),str(M[6]),str(M[7]),str(M[8])
                
            #mensaje = mensaje[:14] + "o" + mensaje[15:]
            x = (chr(27)+"[1;37m"+'| '+chr(27)+"[0m")
            rce = ce.replace(']',' ').replace(',',' ').replace('[','')
            rce = rce[:8]+'|'+rce[9:]
            rce = rce[:17]+'|'+rce[18:]
            rce = rce.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
            
            
            run = un.replace(']',' ').replace(',',' ').replace('[','')
            run = run[:8]+'|'+run[9:]
            run = run[:17]+'|'+run[18:]
            run = run.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
            
            rdo = do.replace(']',' ').replace(',',' ').replace('[','')
            rdo = rdo[:8]+'|'+rdo[9:]
            rdo = rdo[:17]+'|'+rdo[18:]
            rdo = rdo.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
            
            rtr = tr.replace(']',' ').replace(',',' ').replace('[','')
            rtr = rtr[:8]+'|'+rtr[9:]
            rtr = rtr[:17]+'|'+rtr[18:]
            rtr = rtr.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
            
            rcu = cu.replace(']',' ').replace(',',' ').replace('[','')
            rcu = rcu[:8]+'|'+rcu[9:]
            rcu = rcu[:17]+'|'+rcu[18:]
            rcu = rcu.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
            
            rci = ci.replace(']',' ').replace(',',' ').replace('[','')
            rci = rci[:8]+'|'+rci[9:]
            rci = rci[:17]+'|'+rci[18:]
            rci = rci.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
            
            rse = se.replace(']',' ').replace(',',' ').replace('[','')
            rse = rse[:8]+'|'+rse[9:]
            rse = rse[:17]+'|'+rse[18:]
            rse = rse.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
            
            rsi = si.replace(']',' ').replace(',',' ').replace('[','')
            rsi = rsi[:8]+'|'+rsi[9:]
            rsi = rsi[:17]+'|'+rsi[18:]
            rsi = rsi.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))
            
            roc = oc.replace(']',' ').replace(',',' ').replace('[','')
            roc = roc[:8]+'|'+roc[9:]
            roc = roc[:17]+'|'+roc[18:]
            roc = roc.replace('0',(chr(27)+"[6;37;47m"+'0'+chr(27)+"[0m"))  
            

            esp = ('                                                                ')
            neg = (chr(27)+"[1;37m"+'|———————————————————————————|'+chr(27)+"[0m")
            
            print(chr(27)+"[1;36m"+q+chr(27)+"[0m")
            print('')
            print(esp[:25]+neg)
            print(chr(27)+"[1;32m"+a+chr(27)+"[0m"+x+rce+x)
            print(chr(27)+"[1;32m"+b+chr(27)+"[0m"+x+run+x)
            print(chr(27)+"[1;32m"+c+chr(27)+"[0m"+x+rdo+x)
            print(esp[:25]+neg)
            print(chr(27)+"[1;32m"+d+chr(27)+"[0m"+x+rtr+x)
            print(chr(27)+"[1;32m"+e+chr(27)+"[0m"+x+rcu+x)
            print(chr(27)+"[1;32m"+f+chr(27)+"[0m"+x+rci+x)
            print(esp[:25]+neg)
            print(chr(27)+"[1;32m"+g+chr(27)+"[0m"+x+rse+x)
            print(chr(27)+"[1;32m"+h+chr(27)+"[0m"+x+rsi+x)
            print(chr(27)+"[1;32m"+i+chr(27)+"[0m"+x+roc+x)# Esto es lo que are en la funcion 
            print(esp[:25]+neg)
            print('')
            print(chr(27)+"[5;33m"+'¬ Recuerda para jugar debes ingresar la coordenada')
            print('de la celda que deseas modificar seguida del número. Ej: "b7 4"')
            print('Recuerde poner solo un espacio como en el ejemplo anterior')
            print(''+chr(27)+"[0m")
    else:
        print(chr(27)+"[6;91m"+'ERROR Valor incorrecto'+chr(27)+"[0m")

'''
	Verifica si en el bloque al que pertenece la coordena [fil,col] ya existe el número 
	que se quiere ingresar.
		- inputs: int fila, int columna, int dato y list que contiene el sudoku
		- return: True si es posible ingresar el valor, False en caso contrario	
	'''
 
        
def creartxt(nombre,dato):
    archi=open(nombre,'w')
    i = 0
    while i < 9:
        archi.write((str(dato[i]).replace('[','').replace(']','').replace(' ','')) +'\n')
        i += 1
    archi.close()

def abrirg(nm):
    a = open(nm,'r')
    e = []
    for linea in a.readlines():
        partes_linea = linea.split()
        e.append(partes_linea)
    cambio = str(e)
    ptr = cambio.replace('"', '').replace("'", '')
    arreglo = ptr
    m = eval(arreglo)
    matriz = m
    nm = matriz
    return nm
    
def mtxt(dato):
    archi=open('56446gfh5f.txt','a')
    archi.write(' * '+dato+'\n')
    archi.close()

# Si lo considera necesario, incluya funciones adicionales utilies para el desarrollo del juego en main.py
	
