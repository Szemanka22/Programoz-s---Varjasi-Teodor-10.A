import sys
import os
from time import sleep
lista = []
eredmenyek = []
keddieredmenyek = []


if len(sys.argv)<2:
    print("Nem adtál meg fájlnevet!")
    print("Helyes használat: py {sys.argv[0]} fájlnév")
elif not os.path.exists(sys.argv[1]):
    print("Rossz fájlnevet adtál meg!")
else:
    filename= sys.argv[1]
    f=open(filename, encoding="utf-8")
    sorok=f.readlines()
    f.close()

for i in range(len(sorok)):
    a  = (sorok[i].strip().split(','))
    lista.append(a)


#print(lista)

index = 1
while index < len(lista):
    #szamok = (f'{index}.lista : {lista[index][1:7]}')   
        adatok = {'név': lista[index][0],
                  'Kedd': lista[index][2]
                  }
        Kedd = (adatok["Kedd"])
        keddieredmenyek.append(Kedd)        
        index += 1
        sleep(0.5)

def maximumkiválasztás(szamok=None):
    maximum = szamok[0]
    if szamok == None:
         print("Nem adtál meg értéket")
    for i in szamok:
        if i > maximum:
            maximum = i
    print(maximum)
          
'''
MEGHÍVÁSOK
'''
maximumkiválasztás(keddieredmenyek)    
#print(lista)
#Számok

