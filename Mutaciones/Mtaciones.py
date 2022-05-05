from cmath import exp
from decimal import Decimal
import math
from this import d
import numpy as np
import pandas as pd
from tabulate import tabulate
print("Ingresa Màximo:")
Maximo=input()
print("Ingresa Minimo:")
Minimo=input()
Rango=int(Maximo)-int(Minimo)
print("Rango: ",Rango)
n=math.log(Rango,2)
print("n = ", round(n))
print("exponencial n: ",round(n/2))

Parejas=pow(2,round(n/2))
print("Parejas: ",Parejas)
cont=0
cont2=0
contaa=0
Cadena=""
DecimalDespuesDelPunto=""
DecimalesAEvaluar=[]
d=[]
print("----------------------Poblacion Inicial y Evaluaciòn ----------------------")
for Cal in range(Parejas):
    Poblacion= np.random.randint(2,size=(Parejas,round(n+2)))
    cont+=1
for Bits in Poblacion:
    for Bit in Bits:
        cont2+=1
        if((cont2-1)==round(n)):
            Cadena=Cadena+"."
        Cadena=Cadena+str(Bit)
        Cad=(Cadena)
    Cadena=""
    puntoDeDecimales=Cad.index(".")
    BinarioAntesDelPunto=Cad[0:puntoDeDecimales]
    DecimalAntesDelPunto=int(str(BinarioAntesDelPunto),2)
    BinarioDespuesDelPunto=Cad[(puntoDeDecimales+1):(len(Cad))]
    if(BinarioDespuesDelPunto.count("00")!=0):
        DecimalDespuesDelPunto=".0"
    if(BinarioDespuesDelPunto.count("01")!=0):
        DecimalDespuesDelPunto=".25"
    if(BinarioDespuesDelPunto.count("11")!=0):
        DecimalDespuesDelPunto=".75"
    if(BinarioDespuesDelPunto.count("10")!=0):
        DecimalDespuesDelPunto=".50" 
    x=((int(DecimalAntesDelPunto))+(float(DecimalDespuesDelPunto)))   
    y=((x**2))
    y=(y)-(13*(x))
    y=y+(math.exp(x))
    d.append([contaa,(BinarioAntesDelPunto),".",(BinarioDespuesDelPunto),((int(DecimalAntesDelPunto))+(float(DecimalDespuesDelPunto))),np.format_float_scientific(y, precision = 2, exp_digits=3)])
    DecimalesAEvaluar.append(((int(DecimalAntesDelPunto))+(float(DecimalDespuesDelPunto))))
    cont2=0
    contaa+=1
d2=sorted(d, key=lambda y : y[4])  
print(tabulate(d2, headers=["Num", "BinarioEntero","/","BinarioDecimal", "Decimal","Ev. Y"],tablefmt='fancy_grid',stralign='decimal',
               floatfmt=''))
df =pd.DataFrame(d, columns=["Num", "BinarioEntero","/","BinarioDecimal", "Decimal","Ev. Y"])
df.to_excel ("./Poblacion.xlsx",sheet_name="PoblacionIni", header=True,index=False)
Sus=[0,1,2,3]
d3=[]
for x1 in Sus:
    d3.append(d2[x1])
cont2=0
d4=[]
for pare in d3:
    d4.append(str(d3[cont2][1])+str(d3[cont2][3]))
    cont2+=1 
cont3=0
d5=[]
for mono in d4:
    Random2= np.random.randint(0,((len(d4[cont3]))+1))
    d5.append(str(d4[cont3])[0:Random2]+"|"+str((d4[cont3])[Random2:(len(d4[cont3])+1)]))
    cont3+=1
CadSustituir="" 
cont4=0
d6=[]
index=[]   
for mon2 in d5:
    for mon3 in mon2:  
        CadSustituir+=mon3
    Bandera=CadSustituir.index("|")    
    d6.append(CadSustituir[0:Bandera])
    index.append(Bandera)
    CadSustituir=""    
#print(d5[0],"---",str(d5[0]).replace((str(d5[0])[0:index[0]]),d6[1]))
d7=[]
print("--------------------Cruza 1 --------------------------")
d5[0]=str(d5[0]).replace("|","")
d5[1]=str(d5[1]).replace("|","")
d5[2]=str(d5[2]).replace("|","")
d5[3]=str(d5[3]).replace("|","")
print(d5[0],"--",(str(d5[0])[0:index[0]]),"--",d6[1],len(d6[1]))
d7.append(d5[0])
d5[0]=str(d5[0]).replace((str(d5[0])[0:len(d6[1])]),d6[1])
print(d5[0])
print("--------------------Cruza 2--------------------------")
print(d5[1],"--",(str(d5[1])[0:index[1]]),"--",d6[0],len(d6[0]))
d7.append(d5[1])
d5[1]=str(d5[1]).replace((str(d5[1])[0:len(d6[0])]),d6[0])
print(d5[1])


print("--------------------Cruza 3--------------------------")
print(d5[2],"--",(str(d5[2])[0:index[2]]),"--",d6[3],len(d6[3]))
d7.append(d5[2])
d5[2]=str(d5[2]).replace((str(d5[2])[0:len(d6[3])]),d6[3])
print(d5[2])
print("--------------------Cruza 4--------------------------")
print(d5[3],"--",(str(d5[3])[0:index[3]]),"--",d6[2],len(d6[2]))
d7.append(d5[3])
d5[3]=str(d5[3]).replace((str(d5[3])[0:len(d6[2])]),d6[2])
print(d5[3])
print("------------------------------------")
contx=0
conty=0
megaMa=[[],[]]
matriz=[]
print(matriz)
D8=[]
for x in  d5:
    D8.append(d7[contx])
    D8.append(x)
    contx+=1
print(D8)

for fila in range(int(len(D8))):
    matriz.append([])
    for columnas in D8[fila]:
        matriz[fila].append(None)
f=0
c=0
for Bit1 in D8:
    for B2 in Bit1:
        matriz[c][f]=B2
        f+=1
    c+=1
    f=0
tol=0
tol2=0  
print(len(matriz))
muta= np.random.randint((len(matriz)*len(matriz)),size=(1))
t=0  
for matri in  matriz:
    for ma2 in matri:
       
        if(tol==int(muta)):
            if(str(matriz[t][tol2]).count("1")==1):
                print("Cambio ",matriz[t][tol2]," En la mutacion: ",muta," por el valor 0", )
                matriz[t][tol2]=0                
            else:    
                print("Cambio ",matriz[t][tol2]," En la mutacion: ",muta," por el valor 1", )
                matriz[t][tol2]=1
            muta=0
        tol+=1
        tol2+=1
    tol2=0
          
    t+=1
temp=[]
cara=""
for  ma3 in matriz:
    print(ma3)    
for  ma in matriz:
    for m2 in ma:
        cara=cara+str(m2)
    temp.append(cara)
    cara=""
print(temp)
BinarioAntesDelPunto=""
DecimalAntesDelPunto=0
BinarioDespuesDelPunto=""
contaa=0
Original=d
d=[]
d2=[]
print("-------------------------------monogamo---------------------------------")
for bits in temp:
    BinarioAntesDelPunto=bits[0:int(len(bits)-2)]
    DecimalAntesDelPunto=int(str(BinarioAntesDelPunto),2)
    BinarioDespuesDelPunto=bits[int(len(bits)-2):(len(bits))]
    if(BinarioDespuesDelPunto.count("00")!=0):
        DecimalDespuesDelPunto=".0"
    if(BinarioDespuesDelPunto.count("01")!=0):
        DecimalDespuesDelPunto=".25"
    if(BinarioDespuesDelPunto.count("11")!=0):
        DecimalDespuesDelPunto=".75"
    if(BinarioDespuesDelPunto.count("10")!=0):
        DecimalDespuesDelPunto=".50"
    x=((int(DecimalAntesDelPunto))+(float(DecimalDespuesDelPunto)))   
    y=((x**2))
    y=(y)-(13*(x))
    y=y+(math.exp(x))
    d.append([contaa,(BinarioAntesDelPunto),".",(BinarioDespuesDelPunto),((int(DecimalAntesDelPunto))+(float(DecimalDespuesDelPunto))),np.format_float_scientific(y, precision = 2, exp_digits=3)])
    DecimalesAEvaluar.append(((int(DecimalAntesDelPunto))+(float(DecimalDespuesDelPunto))))
    cont2=0
    contaa+=1

d2=sorted(d, key=lambda y : y[4])  
print(tabulate(d2, headers=["Num", "BinarioEntero","/","BinarioDecimal", "Decimal","Ev. Y"],tablefmt='fancy_grid',stralign='decimal',
               floatfmt=''))
df1 =pd.DataFrame(d, columns=["Num", "BinarioEntero","/","BinarioDecimal", "Decimal","Ev. Y"])
df1.to_excel ("./Monogamia.xlsx",sheet_name="Monogamia", header=True,index=False)
OriginalMuta=[]
yc=0
print("---------------------------------Poligamo------------------------------")
for o in Original:
    Original=sorted(Original, key=lambda yc : yc[4]) 
    c+=1 
for Bits in Original: 
   OriginalMuta.append(Bits[1]+""+Bits[3])
print(OriginalMuta)
CadenAzar=np.random.randint((len(Bits)+1),size=(1))
CruzePoli=[]
for Biit in OriginalMuta:
    subcadena=((str(OriginalMuta[0]))[0:int(CadenAzar)])
    print(Biit,"----Cruzo--->","--",subcadena)
    print("Cadena 1",subcadena)
    subcadena2=(str(Biit)[int(CadenAzar):len(Biit)])
    print("Cadena 2",subcadena2)
    print(subcadena+subcadena2)
    CruzePoli.append(subcadena+subcadena2)
print(CruzePoli)
megaMa=[[],[]]
mm=0
mm2=0
matriz=[]
for fila in range(int(len(CruzePoli))):
    matriz.append([])
    for columnas in CruzePoli[fila]:
        matriz[fila].append(None)
print()
for x in CruzePoli:
    for y in x:
        matriz[mm2][mm]=y
        mm+=1
    mm=0    
    mm2+=1 
muta2=np.random.randint((len(matriz)*len(matriz)),size=(1))
print(muta2)
contt=0
f=0
c=0
for xMa in matriz:
    for xMa2 in xMa:
        if(contt==muta2):
            if(str(xMa2).count("1")==1):
                print("Cambiar 1 a 0 en la mutacion: ",(muta2+1))
                matriz[f][c]=0
            else:
                print("Cambiar 0 a 1 en la mutacion: ",(muta2+1))
                matriz[f][c]=1
            muta2=0    
        c+=1
        contt+=1
    c=0     
    f+=1
PoliMuta=[]       
for Ma in matriz:
    print(Ma)
    Ma=str(Ma).replace("'","")      
    PoliMuta.append(str(Ma).replace(",",""))
print("--------ReevaluacionPoligona--------")
t=0
AntesPuntoBITS=""
Valorsno=["[","]"," "]
DApunto=0
DDpunto=0
x=0
y=0
d=[]
for  Bits in PoliMuta:
    for bit in Bits:
        if bit not in Valorsno:
         AntesPuntoBITS=AntesPuntoBITS+bit
    Tamaño =len(AntesPuntoBITS)
    SubCa=AntesPuntoBITS[0:(Tamaño-2)]
    SubCad2=AntesPuntoBITS[(Tamaño-2):Tamaño] 
    DApunto=int(str(SubCa),2)
    if(SubCad2.count("00")!=0):
        DDpunto=".0"
    if(SubCad2.count("01")!=0):
        DDpunto=".25"
    if(SubCad2.count("11")!=0):
        DDpunto=".75"
    if(SubCad2.count("10")!=0):
        DDpunto=".50"
    x=((int(DApunto))+(float(DDpunto)))   
    y=((x**2))
    y=(y)-(13*(x))
    y=y+(math.exp(x))
    d.append([t,(SubCa),".",(SubCad2),((int(DApunto))+(float(DDpunto))),np.format_float_scientific(y, precision = 2, exp_digits=3)])
    AntesPuntoBITS=""
    t+=1
d2=[]    
d2=sorted(d, key=lambda y : y[4])  
print(tabulate(d2, headers=["Num", "BinarioEntero","/","BinarioDecimal", "Decimal","Ev. Y"],tablefmt='fancy_grid',stralign='decimal',
               floatfmt=''))
df2 =pd.DataFrame(d, columns=["Num", "BinarioEntero","/","BinarioDecimal", "Decimal","Ev. Y"])
df2.to_excel ("./Poligamia.xlsx",sheet_name="Poligamia", header=True,index=False) 
print(df2)


