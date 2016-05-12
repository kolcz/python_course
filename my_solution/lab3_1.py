#import funkcje as f #importuje biblioteke jako f
#from funkcje import * #importuje wszystkie funkcje z biblioteki

#def funkcja(zmienna, zmienna2):
#    pass #funkcja pusta, nic nie robi

#funkcja("lala")
#print suma_liczb(1,2)

import numpy as np

#metoda 1
#aList=[[i**2 for i in range(10)] for j in range(5)]

#table=np.array(aList, dtype=float)
#table2=np.zeros((3,3))
#print type(table) #drukowanie typu zmiennej
#print table
#print aList
#print table2
#table3=np.ones_like(table2)
#print table3
#print table2.shape[0], table2.shape[1]#wypisanie wymiaru tablicy
#print (aList[2])[4] #wypisanie z listy 2 elementu 4
tab=np.zeros(10)
tab[[1,3,9]]=-1
tab1=np.zeros(10)
tab1[2:7:2]= 1
print tab1
print tab
mask =tab1>0
print mask
#exit() #przerywanie kodu



