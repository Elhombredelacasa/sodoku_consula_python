# -*- coding: utf-8 -*-
"""
Created on Fri May  5 16:21:36 2017

@author: dab
"""
#import os
#r_ = str(os.getcwd())
#with open(r_+"/cartas/palabrasclaves.txt","r") as pl:
#    lista = []
#    pl.readline()
#    for a in pl.readlines():
#        fe = a.split()
#        lista.append(fe[0])
#    print(lista)
def main(N="mipagina"):
    '''Esta funcion se encarga crear un archivo html con 
    las etiquetas dentro el archivo
    
    Funcion principal del programa'''
    archivo = open(N+'.html','w+')
    archivo.write('<html></html>')
    archivo.close()
    return 
    
    
def est(T,N="mipagina"):
    '''Esta funcion se encarga de abrir un archvo html y agregarle codigo html 
	para luego ejecutarlo o guardarlo dependiendo de el archivo que se creado
    
    Funcion que agrega un texto dentro de el html'''
    archivo = open(N+'.html','r+')
    ti = archivo.read()
    t = ti[6:]
    archivo.seek(6)
    ñ = '<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>'
    archivo.write('<head>'+ñ+'</head> <body>'+T+'</body>'+t)
    archivo.close()
    #Esto fue algo wxtra que quise agregarle a mi programa
    if "listado" in N.lower():
        import webbrowser
        webbrowser.open_new_tab(N+".html")
    return 
    
def usr(por,tex,np):
    import random
    import os
    r_ = str(os.getcwd())
    i = por
    r_ = str(os.getcwd())
    c = random.randrange(21)
    v = random.randrange(3)
    q_ = 0  
    a0 =("<b>Queremos</b>")
    a1 = ("<u>agradecer</u>")
    a2 = ('<b><mark>fidelidad</b></mark>')
    a3 = ("<i>pronto pago</i>")   
    a4 = ('<mark>oportunamente</mark>')
    a5 = ('<i><b>descuento de '+str(i)+'</i></b>')
    a6 = ('<b><u>fiable</b></u>')
    a7 = ('<b><i><mark>'+str(np)+'</b></i></mark>')
    a8 = ('<mark><i>puntualidad</mark></i>')
    a9 = ('<b><i><u>atrasado</b></i></u>')
    a10 = ('<b><u>acercarce</b></u>')
    a11 = ('<i><b>aportes </i></b>')
    a12 = ('<b>procederá </b>')
    a13 = ('<i>cobro </i>')
    a14 = ('<mark>jurídico </mark>')
    a15 = ('<b><mark>invitarlo </b></mark>')
    a16 = ('<b>conocer </b>')
    a17 = ('<b><u>instalaciones </b></u>')
    a18 = ('<b><u><mark>ofrecemos </b></u></mark>')
    with open(r_+"/cartas/palabrasclaves.txt","r") as pl:
        lista = []
        pl.readline()
        for a in pl.readlines():
            fe = a.split()
            lista.append(fe[0])
        while q_ <= v:
            if np == "as12asq":
                r = random.randrange(9,15)
            else:
                r = random.randrange(19)
            re = str(lista[r])
            if str(lista[r]) == "[nombre":
                re = np
            elif str(lista[r]) == "descuento":
                re ="descuento de "+str(i)
            else:
                re = str(lista[r])
            am = "a"+str(r)
            e = eval(am)
            if re in tex:
                if  q_ == 0:
                    texto = tex.replace(re,e)
                elif q_ == 1:
                    texto = texto.replace(re,e)
                else:
                    texto = texto.replace(re,e)  
                q_ += 1
            else:
                q_ = 0  
    return texto
def pmc(dicc):
    """Esta funcion se encarga de contar el producto con mayor indice de 
    compras por un determindado usuario"""
    cero = 0
    for l in  dicc:
        tdr = dicc.count(l)
        if tdr > cero:
            cero = tdr
            listt=l
        else:
            tdr = tdr
    return listt
    
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

def printIntro(f):
    import os
    r_ = str(os.getcwd())
    with open(r_+"/EXTRA/"+f+".txt","r")as a:
        b = a.read()
        return b

def mejor(l,d):
    """Esta funcion se encarga de contar el producto con mayor indice de 
    compras por un determindado usuario"""
    
    lta = []
    for a in l:
        dcc = d[a]
        cero = 0
        for b in dcc:
            tdr = dcc.count(b)
            if tdr > cero:
                cero = tdr
                listt= b
                dc = dcc
                idn = a
            else:
                tdr = tdr
        z = cero,idn,listt
        lta.append(z)
    return sorted(lta)
