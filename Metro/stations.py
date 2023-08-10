# -*- coding: utf-8 -*-

def dio(dat):
    q = []
    dic = {}
    for a in dat:
      ide = a[1]
      est = a[0]
      hor = a[2]
      if est in q:
          pass
      else:
          q.append(est)
      if ide in a and "IN" in a:
        for i in dat:
            if ide in i and "OUT" in i:
              ra = est,hor,i[0],i[2]
              ra = str(ra).replace('"','').replace("'","")
              #print(est,i,a,ra)
              dic[a[1]] = ra 
    return dic
    
def pt(dat,est):
    m = 0
    dc = {}
    for a in dat:
        if est in a and "IN" in a :
            m += 1
            dc[est]= m
    m = dc
    return m
'''Esta funcion cuenta el determinado numero de viaje que hubo en una estacion'''


def pst(dat,est):
    m = 0
    for a in (dat):
        if est in a and "IN" in a :
            c = a.count("IN")
            m += c
    m = m
    return m
''' Esta funcion cuenta el numero de de viajes que se realizo segun el registro
del "Metro ademas con determinada estacion'''
    
def tst(dat,est):
    l,li = [],[]
    tr = 0
    for a in (dat):
        c = a.count("IN")
        if c > 0 and est in a:
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

def hr(dat):
    m = 0
    t = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    y = 0
    dic = {}
    l = []
    for a in (dat):
        s = str(a[2])
        print(s[:2])
        if "IN" in a :
            l.append(s[:2])
    for j in t:
        if j < 10:
            st = "0"+str(j)
        else:
            st = str(j)
        cl = l.count(st)
        dic[st]=cl
    m = dic
    return m
    
'''Esta funcion guarda la cantidad de viajes por hora'''
    
    
def cvi(dat,est):
    m = 0
    t = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    y = 0
    dic = {}
    l = []
    for a in (dat):
        s = str(a[2])
        print(s[:2])
        if est in a and "IN" in a :
            l.append(s[:2])
    for j in t:
        if j < 10:
            st = "0"+str(j)
        else:
            st = str(j)
        cl = l.count(st)
        dic[est]=cl
    m = dic
    return m
    
    
def cvei(dat,est):
    m = 0
    t = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    y = 0
    dic = {}
    l = []
    for a in (dat):
        if est in a and "IN" in a :
            l.append(s[:2])
    for j in t:
        if j < 10:
            st = "0"+str(j)
        else:
            st = str(j)
        cl = l.count(st)
        dic[est]=cl
    m = dic
    return m
    
def lio(dat,est):
    q = []
    dic = {}
    li = []
    v = 0
    c = 0
    la = 0
    l = ["001","002","003","004","005","006","007","008","009","010","011","012","013","014","015","016","017","018","019","020,""021"]
    for a in dat:
      ide = a[1]
      hor = a[2]
      if est in q:
          pass
      else:
          q.append(est)
      if ide in a and "IN" in a and est in a:
        for i in dat:
            if ide in i and "OUT" in i and est in a:
              ra = i[0]
              ra = str(ra).replace('"','').replace("'","")
              #print(est,i,a,ra)
              li.append(ra)
    for ñ in l:
        c = li.count(ñ)
        if v > c:
            pass
        else:
          v = c
          la = i[0]
    return la
"""Esta funcion se encarga de sacar la estacion de origen mas usada para la estacion
nombrada"""


def i_ro(dat,est):
    q = []
    dic = {}
    li = []
    v = 0
    c = 0
    la = 0
    l = ["001","002","003","004","005","006","007","008","009","010","011","012","013","014","015","016","017","018","019","020,""021"]
    for a in dat:
      ide = a[1]
      hor = a[2]
      if est in q:
          pass
      else:
          q.append(est)
      if ide in a and "OUT" in a and est in a :
        for i in dat:
            if ide in i and "IN" in i and est in a  :
              ra = i[0]
              ra = str(ra).replace('"','').replace("'","")
              #print(est,i,a,ra)
              li.append(ra)
    for ñ in l:
        c = li.count(ñ)
        if v > c:
            pass
        else:
          v = c
          la = ñ
    return la
    
def hr1(dat,obj):
    m = 0
    t = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    y = 0
    dic = {}
    l = []
    for a in (dat):
        s = str(a[2])
        if "IN" in a and obj in a:
            l.append(s[:2])
    for j in t:
        if j < 10 > 0:
            st = "0"+str(j)
        else:
            st = str(j)
        cl = l.count(st)
        dic[st]=cl
    m = dic
    for ñ in dic:
        print("A la", ñ,"Horas ingresaron",dic[ñ],"Usuarios")
        
def hr2(dat,obj):
    m = 0
    t = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    y = 0
    dic = {}
    l = []
    for a in (dat):
        s = str(a[2])
        if "IN" in a and obj in a:
            l.append(s[:2])
    for j in t:
        if j < 10 > 0:
            st = "0"+str(j)
        else:
            st = str(j)
        cl = l.count(st)
        dic[st]=cl
    m = dic
    for ñ in dic:
        if ñ == 0:
            pass
        print("A la", ñ,"Horas Salieron",dic[ñ],"Usuarios")