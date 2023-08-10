# -*- coding: utf-8 -*-
from stations import *
from system import *
import time
#Mis variables importantes
e = "IN"
s = "OUT"
t = ('¬ Ingrese el número con la opción deseada "o x para salir" : ')
t = (chr(27)+"[3m"+t+chr(27)+"[0m")
metro = abrirt("metro.log")
mt = [] #Contenedor vacio 
for a in metro.readlines(): #Escriviendo el archivo linea por linea
    lineas = a.split() #Teniendo las lineas libres de espacios
    mt.append(lineas) #Contenedor con el contenido del metro
te = str(mt) #Un str que nesecitare en una condicion
#Algunas condiciones
col = (chr(27)+"[37m")
#d = dio(mt)
print('Para volver a menu inicion ingresar comando "Inicio"\n')
while True:
    dt = "0"
    print(chr(27)+"[1m"+"                   "+'Menu principal')
    print(""+chr(27)+"[0m")
    print('Sistema de consulta de estadísticas de operación del metro.\n')
    print('1. - Estadísticas generales del sistema.') 
    print('2. - Estadísticas por estación.\n')
    dat = input(t)
    if dat in ("1","2"):
        while dt.lower() != "inicio":
            if dat == "1":
                print('\n'+chr(27)+"[1m"+"                   "+'Menú para la opción 1')
                print(""+chr(27)+"[0m")
                print('1. - Cantidad de personas que usaron el metro')
                print('2. - Cantidad de viajes que hubo')
                print('3. - Hora pico de ingreso de usuarios')
                print('4. - Ingresos totales por concepto de tiquetes')
                print('5. - Estaciones en las que más personas ingresan y salen')
                print('6. - Distancia y tiempo promedio de viaje de los usuarios\n')
                dt = input(t)
                if dt == "1":
                    print('Cantidad de personas que usaron el metro\n')
                    per = personas(mt,e)
                    print(' ¬ '+str(per)+col+' Personas usaron el "Metro"\n')
                    chr(27)+"[0m"
                elif dt == "2":
                    print('Cantidad de viajes que hubo\n')
                    ves = veses(mt,e)
                    print(' ¬ '+str(ves)+col+' Viajes\n')
                    chr(27)+"[0m"
                elif dt == "3":
                    print('Hora pico de ingreso de usuarios\n')
                    pic = int(pico(mt,e))
                    if pic > 12:
                        print('Las '+str(pic)+":00 Pm."+col+" Es el horario más congestionado\n")
                    else:
                        print('Las '+str(pic)+col+":00 Am."+col+" Es el horario más congestionado\n")
                    chr(27)+"[0m"
                elif dt == "4":
                    pso = 2300
                    ig = (veses(mt,e) * pso)
                    a = sep(pso)
                    b = sep(ig)
                    print('Ingresos totales por concepto de tiquetes\n')
                    print(col+'Tarifa actual de el tiquete de el metro = $'+chr(27)+"[0m"+str(a)+"\n")
                    print(col+'Total de ingresos por tiquetes = $'+chr(27)+"[0m"+str(b)+"\n")
                elif dt.lower() == "x":
                    print("\n \t \t \t \t \t Adios")
                    time.sleep(3)
                    exit()
                elif dt == "5":
                   ing = estac(mt,e)
                   sal = estac(mt,s)
                   est = abrirm("stations.info")
                   for i in est:
                       if ing == i[1]:
                           a = i[0]
                       if sal == i[1]:
                           b = i[0]
                   print('Estaciones en las que más personas ingresan y salen\n')
                   print(col+'La estacion donde mas personas ingresan es la estacion : "'+chr(27)+"[0m"+str(a)+'"')
                   print(col+'La estacion donde mas personas salen es la estacion : "'+chr(27)+"[0m"+str(b)+'"')
                elif dt == "6":
                    est = abrirt("stations.info")
                    a = 1
                    dic = {}
                    li = []
                    dc = dicci("stations.info")
                    oc = 80
                    km = oc*60 
                    #prom(mt,dc)
                    #print(dc)
                    for i in est.readlines():
                        i= i.replace("\n","")
                        ln = i.split(',')
                        li.append(ln)
                    li.pop(0)
                    e = 1
                    for j in li:
                        lat1 = j[2]       
                        long1 = j[3]
                        est1 = j[1]
                        a1 = j[0]
                        for e in li:
                            lat2 = e[2]       
                            long2 = e[3]
                            est2 = e[1]
                            a2 = e[0]
                            clave = e[1]
                            #print(dic[clave],clave)
                            if est1 == est2 :
                                break
                            aju = stdistance(est1,est2,dc)
                            tem = aju/ km
                            st = str(tem)
                            if st[0] == "0":
                                tem = str(tem/0.0166667)
                                tem = "00:"+tem[:2]+" Segundos"
                                tem.replace(".","")
                            else:
                                tem = st
                                tem = "0"+tem[:2]+":00"+" Minutos"
                                tem = tem.replace(".","")
                            print(col+'Distancia entre',a1, 'y',a2,aju)
                            print(col+"El tiempo prometio entre",a1,"y",a2,'%s'%(tem))
                            #print("La distancia entre %s y %s es de " %(est1,est2)+str(dis(lat2,lat1,long2,long1))+' Kilometros.')
                else:
                    if dt.lower() != "inicio" :
                        rr = ("ERROR El comando ingresado no existe en este menu")
                        print("\n \n \t      \t"+dt,chr(27)+"[31;4m"+rr+chr(27)+"[0m"+"\n") 
            elif dat == "2":
               while dt.lower() != "inicio":
                   dett = str(input('Ingrese el nombre o el código de la estación de interés:'))
                   dett = dett.lower()
                   if dett == "niquia":
                       dett = "001"
                   elif dett == "itagui":
                       dett = "019"
                   print('\n'+chr(27)+"[1m"+"                   "+'Menú para la opción 2')
                   print('1. Cantidad total de viajes')
                   print('2. Horas pico de ingreso y de salida de usuarios')
                   print('3. Estaciones de origen y destino más comunes')
                   print('4. Cantidad de usuarios que ingresaron discriminado por hora')
                   print('5. Cantidad de usuarios que salieron discriminado por hora\n')
                   d2 = d2()
                   dcc =dtc()
                   dt = str(input(t))
                   if dt == "1":
                       print("En la estacion ",d2[dett],"se realizo un total de ",pst(mt,dcc[dett]),"Viajes")
                       print()#No es seguro aun
                   elif dt == "2":
                       print('Hora pico de ingreso de usuarios\n')
                       print('En la estaciono',d2[dett])
                       pic = int(tst(mt,dcc[dett]))
                       if pic > 12:
                           print('Las '+str(pic)+':00 Pm. Es el horario más congestionado\n')
                       else:
                           print('Las 0'+str(pic)+':00 Am. Es el horario más congestionado\n') 
                   elif dt == "3":
                       ori = i_ro(mt,dcc[dett])
                       des = lio(mt,dcc[dett])
                       print("Estaciond de destino Mas comun",d2[ori])
                       print("Estacione de origen Mas comun",d2[des])
                   elif dt == "4":
                       print(hr1(mt,dcc[dett]))
                   elif dt == "5":
                       print(hr2(mt,dcc[dett]))
                   elif dt.lower() == "x":
                       print("\n \t \t \t \t \t Adios")
                       time.sleep(3)
                       exit()
    else:
        if dat.lower() == "x":
            print("\n \t \t \t \t \t Adios")
            print(col+"#Dany_Abby.inc")
            time.sleep(3)
            exit()
        else:
            rr = ("ERROR El comando ingresado no existe en este menu")
            print("\n \n \t      \t"+dat,chr(27)+"[31;4m"+rr+chr(27)+"[0m"+"\n")                    
                                #Aun faltan detalles
