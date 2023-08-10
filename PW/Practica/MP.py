# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Created on Fri May  5 15:35:59 2017

@author: dab
"""
from FE import *
def num1():
    '''Esta funcion abre varios archivos los modifica y se los pasa a la
    funcion principal'''
    import os
    import time
    import random
    from subprocess import call
    ko = ""
    A = printIntro("A")
    T = printIntro("T")
    print(chr(27)+"[96m"+T+chr(27)+"[94m"+A)
    print ('                      '+'"DOÑA CARMELITA"')
    chr(27)+"[37m"
    a0 = ('''
    «Por que Tienda de Abarrotes Doña Carmelita sempre "PREMIA"
    A Sus mejores clientes, estaremos ofreciendo grandes descuentos a
    nuestros clientes puntuales en los productos mas significativos para ti»\n''') 
    a1 = ('''
    “Ven y realiza tus Pagos, ponte al dia y no te pierdas los
    grandes veneficios que tiene Tienda de Abarrotes Doña Carmelita para ti”\n''')
    a2 = ('''
    ·Tienda de Abarrotes Doña Carmelita, ventas al por mayor y al detal
    ven y consigue todo lo que necesitas para ti y para tu familia· \n''')
    ab = random.randrange(3)
    ac = "a"+str(ab)
    ad = eval(ac)
    print(chr(27)+"[93m"+ad+chr(27)+"[4;96m"+"\n Por favor espere. Cargando... "+chr(27)+"[0;1m")
    tenda,aple = "",[]
    dgl,lll,licgen,licf,licd,d_0,nol,lsg ={},[],[],[],[],{},[],[]
    r_,lc,lidc,dcc = str(os.getcwd()),[],[],{}#Los de cliente
    lv,lidv = [],[]#Los de ventas
    lp,dcp,dp,lco = [],{},{},500#Los de pagos
    lr,lidr,dcr = [],[],{}#Los de productos
    with open(r_+("/datos/productos.txt")) as producto:
        nor = producto.readline()
        for f in producto.readlines():
            fe = str(f).replace("\n","")
            l0 = fe.split(",")
            idr = l0[0] #id de el producto
            nmr = l0[1]#Nombre de el producto
            mr = [str(l0[2])+"."+str(l0[3])]# Marca de presentacion
            marc = str(l0[2])
            prr = l0[4]#Precio de el producto
            der = l0[5]#Tanto por ciento de descuento
            nypr = [nmr,prr]
            dcr[idr] =[nmr,prr,der]#Dic 0nombre 1precio
            dp[idr] = nmr+" "+marc
            lr.append(nypr)
            lidr.append(idr)
    with open(r_+"/datos/clientes.txt","r") as cliente:
        noc = cliente.readline()
        for a in cliente.readlines():
            l1 = a.split()
            idc = l1[0]
            eval(idc)#Provablemente no necesite ser evaluado
            l1.pop(0)
            txc = str(l1).replace(","," ").replace("[","").replace("]","").replace("'","")
            dc = [idc,txc]
            lidc.append(dc[0])#Lista de solo las ide de los usuarios
            lc.append(dc)#Por si necesito la lista
            dcc[dc[0]]=dc[1]#poe si neceito el diccionario
    with open(r_+"/datos/ventas.txt","r") as ventas:
        nov = ventas.readline()
        for b in ventas:
            l2 = b.split()
            idv = l2[0] #Ide de el cliente
            idvp = l2[1] #ide de el producto
            hrcv = l2[2] #Hora de compra
            fcv = l2[3] #Fecha de compra
            orv = idv,idvp# ide de el cliente y ide de el producto
            lidv.append(idv)
            lv.append(orv)#liesta de ide de el cliente y ide de el producto
    with open(r_+"/datos/pagos.txt","r") as pagos:
        nop = pagos.readline()
        tot_p = 0
        for c in pagos:
            l3 = c.split()
            idp = l3[0] #Id de el cliente
            vp = eval(l3[1])#valor pago 
            #eval(vp)
            hp = l3[2]#hora de pago
            fp = l3[3]#fecha de pagado
            ipg = idp,vp
            lp.append(ipg)
            tot_p += vp
            if idp in dcp:
                dcp[idp] = float(dcp[idp])+float(vp)
            else:
                dcp[idp] =float(vp)#total pagado
        cajac = 0
        invitado = 0
        for d in lidc:
            cmprs = 0
            l_0 = []
            for e in lv:
                if d == e[0]:
                    l_0.append(e[1])
                    valor = eval(dcr[e[1]][1])#ide pro y valor pro 
                    dscnto = eval(dcr[e[1]][2])
                    por = valor * dscnto / 100 
                    #por = dscnto
                    #print(_as)
                    #return
                    vlr = valor - por
                    cmprs += vlr
                    d_0[e[0]] = l_0 #id cli con ids de productos para calcular los max 
            dgl[d]=cmprs#Ids con el total de compra en ventas ya descnrdo
        #v_p = 0
        #v_c = 0
        
        for j in dgl: #dcp: # sumar p y c
            cajac += dgl[j]
            #v_p = tot_p #dcp[j]#suma de pagos y el mas
            #v_c += dgl[j]#suma de compras
        for k in lidc: # este for revisa los clientes que no han echo compras
            sss = str(lidv).replace("[","").replace("]","")
            """ lidc es una lista con todos los id de los clientes y sss es el 
            str de una lista con todos los id de los clientes que han comprado"""
            if str(k) in sss:
                pass
                #print(k,"si")
            else:
                #print(k,"no")
                nol.append(str(k))
                invitado = 10
        pscn = 0
        de = 0
        list_ = []
        dic_= {}
        #v_c = 0
        for l in dgl:
            for m in dcp:
                if l == m:
                    """AQUI ESTA EL PROBLEMA"""
                    ttlc =float(dgl[l]) #"%.*f" % (2,float(dgl[l]))
                    ttlp =float(dcp[m])#"%.*f" % (2,float(dcp[m]))
                    cac = float(ttlc) - float(ttlp)
                    #cac = float("%.*f" % (2,float(c_c)))
                    o_ = float(ttlc)* 10 / 100
                    #o_  = float("%.*f" % (2,float(_o_)))
#                    ttlc =int(dgl[l])
#                    ttlp =int(dcp[m])                    
#                    cac = ttlc - ttlp
#                    o_ = (ttlc*10) / 100
                    if cac <= 0.0:
                        nea = dcc[l],"fiable"
                        dic_[l] = "fiable1",cac
                        nevu = [int(cac),l,"fiable1"]
                        list_.append(nevu)
                        lll.append(nea)
                    elif cac <= o_:
                        nea = dcc[l],"fiable"
                        dic_[l] = "fiable2",cac
                        nevu = [int(cac),l,"fiable2"]
                        list_.append(nevu)
                        lll.append(nea)
                    elif cac <= 15000.9:
                        nea = dcc[l],"fiable"
                        dic_[l] = "fiable3",cac
                        nevu = [int(cac),l,"fiable3"]
                        list_.append(nevu)
                        lll.append(nea)
                    elif invitado == 10:
                        nea = dcc[l],"Este cliente no ha realizado compras"
                        dic_[l] = "invitado",cac
                        nevu = [int(cac),l,"fiable3"]
                        list_.append(nevu)
                        lll.append(dcc[l],"Este cliente no ha realizado compras")
                    else:
                        dic_[l] = "deudor",cac
                        nea = dcc[l],"moroso"
                        nevu = [int(cac),l,"moroso."]
                        list_.append(nevu)
                        lll.append(nea)
        in_1 = 0
        for r in sorted(list_):
            if r[2] != "deudor":
                pscn += 1
                r[0] = pscn
            elif r[2] == "invitado":
                in_1 += 1
                r[0] = in_1
            else:
                de += 1
                r[0] = de           
        todo = ""
        cl_f = 0
        cl_m = 0
        for i in sorted(lll):
            _T_ = str(i[0])#nombre 
            mdd = str(i[1])
            if mdd == "fiable":
                cl_f += 1
                mdd = "<i>– Fiable</i>"
                suma = '<LI>'+'<b>'+_T_+'</b>'' '+mdd
            else:
                cl_m += 1
                mdd = "– <u>Deudor</u>"
                _T_ = '<mark>'+_T_+'</mark>'
                suma = '<LI>'+_T_+' '+mdd
            todo += suma#<br></br>'
        tienda = "<h1>Tienda de Abarrotes Doña Carmelita</h1><i><h2>Lista de Clientes</i></h2>"
        lete = '<br></br><i><b>Clientes Fiables: </b></i>'+str(cl_f)+'<br></br><b>Clientes Deudores: </b>'+str(cl_m)
        valnc = tot_p - cajac
        #valnc =sep(vanc)
        if valnc < 0:
            vi = sep(int(valnc))
            vlr_ = '<mark>'+str(vi)+'</mark>'
        else:
            vi = sep(int(valnc))
            vlr_ = str(vi)
        vl_C = "<br></br><h2><b>Balance de caja: "+vlr_+"</h2></b>"
        resum = tienda+'<OL TYPE="1">'+todo+'</OL>'+lete+vl_C
        N = "listado de clientes"
        aple.append(N)
    dat = "0"
    while dat != "1":
        print('INVENTARIOS Tienda de Abarrotes Doña Carmelita \n \t\t\t → "MENU" ← ')
        print("\nPor Favor ingres “1” Para generar Listado de clientes e Informe de caja")
        dat = input("Intrese aqui 1 : ") 
    if dat == "1":
        main(N)
        est(resum,N)
    lla = r_
    al = lla.split("/")
    ala = len(al)-1
    print("El archivo ",N," fue creado con exito en la carpeta ",al[ala]+ "\n Ruta",r_)
    with open(r_+"/cartas/invitacion.txt","r") as invitar:
        tein = invitar.read()
    with open(r_+"/cartas/cartafibles.txt","r") as cartaf:
        cartaf.readline()
        c_1 =cartaf.read(237)
        cartaf.seek(315)
        c_2 = cartaf.read(231)
        cartaf.seek(584)
        c_3 = cartaf.read()
    with open(r_+"/cartas/morosos.txt","r") as cartaM:
        cM = cartaM.read()
    if invitado == 10:
        fi = ["fiable1","fiable2","fiable3","moroso.","invidado"]
    else:
        fi = ["fiable1","fiable2","fiable3","moroso."]
    for h in fi:
        for g in sorted(list_):#dicgen:
            if h == g[2]:
                if h == "fiable1":
                    N = "fiable"+str(g[0])
                    ok = "Fiable",str(g[0])
                    licgen.append(ok)
                    mayor = pmc(d_0[g[1]])
                    nm = dp[mayor]
                    p_p = str(dcr[mayor][2])
                    FCH = time.strftime("%d/%m/%y")#fehca
                    _t ="<p>Medellín, "+str(FCH)+"</p><br></br>"#fehca html
                    SR = "<br></br><p>Sr (a).</p>"
                    CL = "<b><h2>"+dcc[g[1]]+"</h2></b><br></br>"#Nombre html
                    AS = "<b>Asunto : </b><p>Agradecimiento</p><br></br>"
                    c1 = str(c_1).replace("xx",p_p).replace("[nombre del producto y marca]",nm)
                    GRP = "</p>Gracias por su atención,</p><br></br><b>Abarrotes Doña Carmelita</b>"
                    cfin = usr(p_p,c1,nm)
                    fin =_t+SR+CL+AS+cfin+GRP
                    main(N)
                    aple.append(N)
                    est(str(fin),str(N))
                elif h == "fiable2":
                    N = "fiable"+str(g[0])
                    ok = "Fiable",str(g[0])
                    licgen.append(ok)
                    mayor = pmc(d_0[g[1]])
                    nm = dp[mayor]
                    p_p = str(dcr[mayor][2])
                    FCH = time.strftime("%d/%m/%y")#fehca
                    _t ="<p>Medellín, "+str(FCH)+"</p><br></br>"#fehca html
                    SR = "<br></br><p>Sr (a).</p>"
                    CL = "<b><h2>"+dcc[g[1]]+"</h2></b><br></br>"#Nombre html
                    AS = "<b>Asunto : </b><p>Agradecimiento</p><br></br>"
                    c2 = str(c_2).replace("xx",p_p).replace("[nombre del producto y marca]",nm)
                    GRP = "</p>Gracias por su atención,</p><br></br><b>Abarrotes Doña Carmelita</b>"
                    cfin = usr(p_p,c2,nm)
                    fin =_t+SR+CL+AS+cfin+GRP
                    main(N)
                    aple.append(N)
                    est(str(fin),str(N))
                elif h == "fiable3":
                    N = "fiable"+str(g[0])
                    ok = "Fiable",str(g[0])
                    licgen.append(ok)
                    mayor = pmc(d_0[g[1]])
                    nm = dp[mayor]
                    p_p = str(dcr[mayor][2])
                    FCH = time.strftime("%d/%m/%y")#fehca
                    _t ="<p>Medellín, "+str(FCH)+"</p><br></br>"#fehca html
                    SR = "<br></br><p>Sr (a).</p>"
                    CL = "<b><h2>"+dcc[g[1]]+"</h2></b><br></br>"#Nombre html
                    AS = "<b>Asunto : </b><p>Agradecimiento</p><br></br>"
                    c3 = str(c_3).replace("xx",p_p).replace("[nombre del producto y marca]",nm)
                    GRP = "</p>Gracias por su atención,</p><br></br><b>Abarrotes Doña Carmelita</b>"
                    cfin = usr(p_p,c3,nm)
                    fin =_t+SR+CL+AS+cfin+GRP
                    main(N)
                    aple.append(N)
                    est(str(fin),str(N))
                elif h == "moroso.":
                    N = "moroso"+str(g[0])
                    ok = "moroso",str(g[0])
                    licgen.append(ok) 
                    mayor = "asa2112as"#pmc(d_0[g[1]])
                    nm = "as12asq"
                    p_p = "aja"
                    FCH = time.strftime("%d/%m/%y")#fehca
                    _t ="<p>Medellín, "+str(FCH)+"</p><br></br>"#fehca html
                    SR = "<br></br><p>Sr (a).</p>"
                    CL = "<b><h2>"+dcc[g[1]]+"</h2></b><br></br>"#Nombre html
                    AS = "<b>Asunto : </b><p>Cobro</p><br></br>"
                    cm = str(cM)
                    GRP = "</p>Gracias por su atención,</p><br></br><b>Abarrotes Doña Carmelita</b>"
                    cfin = usr(p_p,cm,nm)
                    fin =_t+SR+CL+AS+cfin+GRP
                    aple.append(N)
                    main(N)
                    est(str(fin),str(N))
                    
                elif h == "invitado" :
                    N = "Invitacion"+str(g[0])
                    ok = "Invitacion",str(g[0])
                    licgen.append(ok)
                    ñ = random.choice(lidr)
                    nm = dp[ñ]
                    p_p = str(dcr[mayor][2])
                    FCH = time.strftime("%d/%m/%y")#fehca
                    _t ="<p>Medellín, "+str(FCH)+"</p><br></br>"#fehca html
                    SR = "<br></br><p>Sr (a).</p>"
                    CL = "<b><h2>"+dcc[g[1]]+"</h2></b><br></br>"#Nombre html
                    AS = "<b>Asunto : </b><p>Invitacion</p><br></br>"
                    iv = str(tein).replace("xx",p_p).replace("[nombre del producto y marca]",nm)
                    GRP = "</p>Gracias por su atención,</p><br></br><b>Abarrotes Doña Carmelita</b>"
                    cfin = usr(p_p,cm,nm)
                    fin =_t+SR+CL+AS+cfin+GRP
                    main(N)
                    aple.append(N)
                    est(str(fin),str(N))   
                else:
                    pass
    for n in licgen:
        s = ".html"
        im = '<td sortable-data='+'"'+n[0].lower()+n[1]+s+'"'+'><table class="ellipsis"><tbody><tr><td><a'+' '
        mii = 'class="file" href="file://'+r_+"/"+n[0].lower()+n[1]+s+'"><img'+' '
        mi = 'alt="'+n[0]+' :"><mark>['+n[1]+']</mark>.html</a></td></tr></tbody></table></td></tr><tr>'+' '
        mio = '<tr>'+im+mii+mi
        ko += mio
    o_e = "<h1>Tienda de Abarrotes Doña Carmelita</h1><i><h2>Lista de Cartas</i></h2>"+" "
    N = "listado de Cartas"
    aple.append(N)
    TEe = o_e+ko
    Dat = "0"
    while Dat != "2":
        print('INVENTARIOS Tienda de Abarrotes Doña Carmelita \n \t\t\t → "MENU" ← ')
        print("Por favor ingrese “2” Para generar Cartas")
        Dat = input("Intrese “2” : ") 
    main(N)
    est(str(TEe),str(N))
    lla = r_
    al = lla.split("/")
    ala = len(al)-1
    print("El archivo ",N," fue creado con exito en la carpeta ",al[ala]+ "\n Ruta",r_)  
    wq = 501
    que = mejor(lidc,d_0)
    for q in que:
        for w in lll:
            if dcc[q[1]] == w[0]:
                if w[1] == "fiable":
                    #wqw = str(w).replace("(","").replace(")","")
                    wq -= 1
                    qw = wq,w[0],w[1],q[0],q[2],q[1]#num,nom,tip,cua,pro,id
                    licf.append(qw)
    yes = sorted(licf)
    ye = yes[0]
    ey = 50,ye[1],dcr[ye[4]][0],'50'
    eye =sorted(licf)
    eye.pop(0)
    licd.append(ey)
    for y in eye:
        eyes = int(dcr[y[4]][2]),y[1],dcr[y[4]][0],dcr[y[4]][2]
        licd.append(eyes)
    for u in sorted(licd):
        lco -= 1
        un = lco,u[1],u[2],u[3]
        lsg.append(un)
    isi = sorted(lsg)
    for o in isi:
        negri = '<b>'+str(o[1])+'</b> '
        ponegri = '<b>'+str(o[3])+'% </b> '
        ese = str(o[2])
        abarro = '<li><p align="left">'+negri+".   "+ese+".   "+ponegri+'</li></p>'
        tenda += abarro 
    epa = "<h1><b>Tienda de Abarrotes Doña Carmelita</b></h1> "
    eple = '<OL TYPE="1">'+tenda+'</OL> '  
    Nsi = "<font size=4><i>Lista de Clientes fiables, productos y descuentos</i></font> "
    formado = epa+Nsi+eple
    nisi = "Listado de Clientes fiables, productos y descuentos"
    main(nisi)
    aple.append(nisi)
    daT = "0"
    while daT != "3":
        print('INVENTARIOS Tienda de Abarrotes Doña Carmelita \n \t\t\t → "MENU" ← ')
        print("Ingrese “3”  Para Generar un Listado de clientes fiables, Productos y descuentos")
        daT = input("Intrese “3” : ") 
    est(formado,nisi)
    print("El archivo ",nisi," fue creado con exito en la carpeta ",al[ala]+ "\n Ruta",r_)
    porfin = input('Desea eliminar los archivos creados ? "Si" "No"')
    if porfin.lower() == "si" :
        for p in aple:
            os.remove(r_+"/"+str(p)+".html")
        print("Los archivos fueron elimidos con exito")
    elif porfin.lower() == "no":
        print("Adios")
        time.sleep(3)
        exit()
    else:
        print("Hasta luego Comando incorrecto")

num1()
    

