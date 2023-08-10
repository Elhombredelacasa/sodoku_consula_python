# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Created on Fri May  5 15:35:59 2017

@author: dab
"""

def main():
    '''El siguiente progrma en python crea el archivo si no existe y escribe
    las etiquetas dentro el archivo
    
    Funcion principal del programa'''
    archivo = open('mipagina.html','w+')
    archivo.write('<html></html>')
    archivo.close()
    return 0
    
if __name__ == '__main__':
   main()
    
def est(T):
    '''1. Haga un función que inserte las etiquetas en head y body dentro de
    las etiquetas html del documento creado (mipagina.html), según la 
    explicación dada. - Pista: utilice el método seek para posicionar el
    puntero dentro del archivo. Abra el documento .html y muestre que aparece.
    
    Funcion que agrega un texto dentro de el html'''
    archivo = open('mipagina.html','r+')
    ti = archivo.read()
    t = ti[6:]
    archivo.seek(6)
    T = T
    archivo.write('<head></head> <body>'+T+'</body>'+t)
    archivo.close()
    #Esto fue algo wxtra que quise agregarle a mi programa
    import webbrowser
    webbrowser.open_new_tab("mipagina.html")
    return 0
    
def color():
    '''Utilice la función creada para insertar la frase HOLA MUNDO! YO SOY 
    [escriba su nombre en mayúscula y cédula], dentro de las etiqueas body, 
    tal y como se muestra a continuación:
    
    Funcion que le da color al texto'''
    t = ("HOLA MUNDO! YO SOY DANIS ABADIA BEJARANO 1045524358")
    m = "<b>"+t[5:11]+"</b>"
    n = "<b>"+t[19:24]+"</b>"
    a = "<b>"+t[33:40]+"</b>"
    t = t.replace('MUNDO',m).replace('DANIS',n).replace('BEJARANO',a)
    T = ('<p style="color:lime;">'+t+'</p>')
    return T
#Si desea activar la funcion color elimiinar "#" Hay abajo
#est(color())
    
def usr():
    """ Un usuario debe ingresar una frase, la frase tiene mínimo 7 palabras
    y debe ser mostrada en una página web como se muestra en el ejemplo 1. 
    Dicho de otra forma, cree un documento html y muestre una lista de 7
    elementos sin orden o numeración. El usuario debe ingresar una frase, y 
    cada elemento de la lista es la misma frase ingresada por el usuario con 
    las etiquetas que se muestran en el ejemplo 1.
    
    Esta funcion basicamente le da la opcion al usuraio de
    ingresar el texto que decea que aparezca en la pagina"""
    clo = ("Por lo menos debes ingresar siete palabras")
    import random
    import copy
    list = []
    while len(list) < 7:
        te = input("Por favor ingrese como minimo 7 palabras = ")
        list = te.split (' ')
        if len(list) < 7 and te.lower() != "exit":
            print(chr(27)+"[31;1m"+clo+chr(27)+"[0m")
        if te.lower() == "exit":
            exit()
    co = copy.deepcopy(list)
    cp = copy.deepcopy(co)
    rmp = te
    re = ""
    lo = len(list)
    con = 0
    ll = int(lo)
    vs = 0
    m = ""
    print(ll)
    while ll > vs:
        rmp = te
        for a in list:
            c = random.randrange(7)
            a0 = ('<mark>'+a+'</mark>')
            a1 =("<b>"+a+"</b>")
            a2 = ("<u>"+a+"</u>")
            a3 = ("<i>"+a+"</i>")
            a4 = ("<h2>"+a+"</h2>")
            a5 = ("<h6>"+a+"</h6>")
            a6 = ('<FONT FACE="courier new">'+a+'</FONT> ')
            am = "a"+str(c)
            e = eval(am)
            rmp = rmp.replace(a,e)
            cp[con]=e
            lm = len(list)
            if con < lm-1:
                con +=1<lm
        re += '<li type="disc">'+rmp+'</li><br></br>'
        vs = vs +1
    m +=re
    ti = '<head><style type="text/css"> h1,h2,h3,h4,h5,h6 {display: inline;}</style></head>'+m
    ti = ti
    return ti
est(usr())
    
    