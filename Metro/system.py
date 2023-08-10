# Módulo que contiene las funciones relacionadas con la generación de estadísticas generales del sistema metro

from math import *
 
def stdistance(origen,destino,M):
    def geodistance(P1,P2,h):
        pi = 3.141592
        R = 6371009;
        theta1 =  pi/2 - (P1[0]*pi/180);
        phi1=P1[1]*pi/180;
        rho1=R+h;
        theta2=pi/2 - (P2[0]*pi/180);
        phi2=P2[1]*pi/180;
        rho2=R+h;
        x1=rho1*sin(theta1)*cos(phi1);
        x2=rho2*sin(theta2)*cos(phi2);
        y1=rho1*sin(theta1)*sin(phi1);
        y2=rho2*sin(theta2)*sin(phi2);
        z1=rho1*cos(theta1);
        z2=rho2*cos(theta2);
        D=((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**(1/2);
        return D
    D=0
    if ((origen>'021')or(origen<'001')or(destino>'021')or(destino<'001')):
        D=-1
        return D
    if(origen>destino):
        step=-1
    elif(origen<destino):
        step=1
    else:
        return D
   
    for i in range(int(origen),int(destino),step):
       indx1='0'*(3-len(str(i)))+str(i)
       indx2='0'*(3-len(str(i+step)))+str(i+step)
       D = D + geodistance(M[indx1][1:],M[indx2][1:],1600)

    return D

'''
	   Recibe dos string con los identificadores de las estaciones origen y destino
	   Recibe un diccionario cuya clave es el identificador de la estación y el valor es una tupla con el nombre de la estación
	   y las coordenadas geograficas.
	   Retorna un float con la distancia en metros del recorrido entre las dos estaciones
	'''

# -*- coding: utf-8 -*-
# Módulo que contiene las funciones relacionadas con la generación de estadísticas para una estación específica

def busq(dat,obj):
    for a in (dat):
        print(len(dat))
        if obj in a:
            po = a.index(obj)
            print(po)
        else:
            print(a,'no')
'''Esta funcion resive el id de la estacion y lo busca en la lista'''

def personas(dat,obj):
    m = 0
    l = []
    for a in (dat):
        c = a.count(obj)
        if c > 0:
            p = str(a[1])
            if p in str(l):
                m = m
            else:
                l.append(p)
                m += 1   
        else:
            m = m
    return m
'''Esta funcion ase un conteo de cuantas personas usaron el "Metro" segun el 
registro ademas tiene en cuenta que no cuenta a una misma persona dos veses'''

def veses(dat,obj):
    m = 0
    for a in (dat):
        c = a.count(obj)
        m += c
    m = m
    return m
''' Esta funcion cuenta el numero de de viajes que se realizo segun el registro
del "Metro"'''

def pico(dat,obj):
    l,li = [],[]
    tr = 0
    for a in (dat):
        c = a.count(obj)
        if c > 0 :
            p = str(a[2])
            l.append(p[:2])
            if p[:2] in li:
                pass
            else:
                li.append(p[:2])
    for e in li:
        hor = l.count(e)
        if hor > tr:
            tr = hor
            ti = e
        else:
            tr = tr
    return ti
''' Esta funcion se encarga de extraer de un archivo todos los horarios
transitados en el metro sacando asi los que mas repeticiones tienen'''

def sep(num):
    m = str(num)
    s = int(len(m))
    a = 0
    b = 0
    l = []
    while a < s+1:
        a += 3
        t = m[-a:s-b]
        b += 3
        l.append(t)
    l.reverse()
    if l[0] == "":
        l.remove(l[0])
        l = str(l)
        l = l.replace("'","").replace("[","").replace("]","").replace(",",".")
        l = l.replace(" ","")
        return l
    else:
        l = str(l)
        l = l.replace("'","").replace("[","").replace("]","").replace(",",".")
        l = l.replace(" ","")
        return l
''' Esta funcion es algo extra que decidi implementar para que me separara
los numero con decimales y sus puntos correspondientes'''

def abrirm(nm):
    a = open(nm,'r')
    e = []
    for linea in a.readlines():
        #linea = linea[:5].replace(' ','-')+linea[5:]
        e.append(linea.split(','))
        ca = str(e)
    nm = e
    return nm
''' Esta funcion se encarga de abrir un archivo y lueo extrae la imformacion
necesaria '''

def abrirt(filename):
   a = open(filename,"r")
   return a
''' Esta funcion solo abre un archivo'''

def estac(dat,obj):
    l,li = [],[]
    tr = 0
    for a in (dat):
        c = a.count(obj)
        if c > 0:
            p = str(a[0])
            l.append(p[:3])
            if p[:3] in li:
                pass
            else:
                li.append(p[:3])
    for e in li:
        hor = l.count(e)
        if hor > tr:
            tr = hor
            ti = e
        else:
            tr = tr
    return ti
''' Esta funcion se encarga de extraer de un archivo todos las id de las
estaciones que fueron destino segun el registro en el metro'''
def dis(lata,latb,longa,longb):
    import math
    Xa = float(lata)
    Xb = float(latb)
    Ya = float(longa)
    Yb = float(longb)
    X = math.sqrt (((Xb - Xa)**2) + ((Yb - Ya)**2))
    return X

def tmpo(dat,obj):
    hor = ["001","002","003","004","005","006","007","008","009","010","011","012","013","014","015","016","017","018","019","020,""021"]
    minu = 0
    minutos = []
    horas = []
    IN = []
    l1 = []
    OUT = []
    for i in dat:
        if obj in i:
            if "IN" in i:
                IN.append(i[2])
                
            elif "OUT" in i:
                OUT.append(i[2])            
    print(IN,obj,"IN")
    print(OUT,obj,"OUT")
    
def dicci(ar):
    est = abrirt(ar)
    dic = {}
    li = []
    for i in est.readlines():
        i= i.replace("\n","")
        ln = i.split(',')
        li.append(ln)
    li.pop(0)
    for j in li:
        lat = j[2]       
        long = j[3]
        esta = j[0]
        clave = j[1]
        dic[clave] = esta,eval(lat),eval(long)
    return dic

def dtc():
    est = abrirt("stations.info")
    dic = {}
    li = []
    for i in est.readlines():
        i= i.replace("\n","")
        ln = i.split(',')
        li.append(ln)
    li.pop(0)
    for j in li:      
        n1 = j[0]
        n2 = j[1]
        dic[n1.lower()] = n2
        dic[n2.lower()] = n2
    return dic
    
def d2():
    est = abrirt("stations.info")
    dic = {}
    li = []
    for i in est.readlines():
        i= i.replace("\n","")
        ln = i.split(',')
        li.append(ln)
    li.pop(0)
    for j in li:      
        n1 = j[0]
        n2 = j[1]
        dic[n1.lower()] = n1
        dic[n2.lower()] = n1
    return dic
          
def tray(dat,obj):
    pe = ["001","002","003","004","005","006","007","008","009","010","011","012","013","014","015","016","017","018","019","020,""021"]
    l,li = [],[]
    t = 0
    tr = []
    di = {}
    hor = 0
    lis = []
    cd = {}
    ll = []
    for a in (dat):
        c = a.count(obj)
        if c > 0:
            p = str(a[0])
            l.append(p[:3])
            if p[:3] in li:
                pass
            else:
                li.append(p[:3])
    for e in pe:
        hor = l.count(e)
        di[hor]=e
    for j in di:
        tr.append(j)
    tr.sort()
    tr.reverse()
    while t < 5:
        lis.append(tr[t])
        t += 1
    dic = d2()
    for ñ in lis:
        cl = int(ñ)
        ll.append(di[cl])
    return ll
''' Esta funcion toma como parametros el documento y un str luego crea un diccionario
con el numero de ingresos que tuvo como clave y el id de la estacion como contenido
luego hace una lista con todos las claves y saca las de mayor para luego buscar 
la estacion solo con las claves de mayor valor'''