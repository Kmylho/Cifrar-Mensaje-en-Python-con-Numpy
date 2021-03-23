#importamos numpy para manipular el array
import numpy as np
#libreria para sacar el redondeo
from math import ceil 
#pedimos la variable a cifrar
TextoPreCifrar = input("Ingrese el texto a cifrar: ")
#le eliminamos los espacios y los volvemos -
TextoCifrar = TextoPreCifrar.replace(" ", "-")
#sacamos la longitud del texto
LongitudTextoCifrar = len(TextoCifrar)
#Declaramos un array donde guardaremos temporalmente los caracteres
Array = []
#vamos a pedir un entero
while True:
    try:
        #pedimos el numero y lo volvemos un entero
        numeroCapturado = int(input("Introduce un numero entero menor a "+str(LongitudTextoCifrar)+": "))
        while True:
            try:
                #verificamos que sea menor a la longitud del texto a cifrar
                if numeroCapturado<LongitudTextoCifrar:
                    break
                else:
                    #en caso de no serlo lo volveremos a pedir
                    numeroCapturado = int(input("Introduce un numero entero menor a "+str(LongitudTextoCifrar)+": "))
            #en caso de ingresar un dato erroneo  
            except ValueError:
                print("Ingreso un dato erroneo.  Intente de nuevo")
        break
    #en caso de ingresar un dato erroneo  
    except ValueError:
        print("Ingreso un dato erroneo.  Intente de nuevo")

#sacamos el redondeo
redondeo = ceil(LongitudTextoCifrar/numeroCapturado)

#preparamos para la matriz
while (((len(TextoCifrar))%numeroCapturado)!=0):
    txtTemp = TextoCifrar+"*"
    TextoCifrar = txtTemp

#separamos los caracteres
for i in TextoCifrar:
    Array.append(i)

Array2 = np.array(Array).reshape(redondeo,numeroCapturado)

mensajeCrifrado = ""
for i in np.nditer(Array2, order="F"):
    mensajeCrifrado = mensajeCrifrado+(str(i))

#--------------------------------------
Array = []
for i in mensajeCrifrado:
    Array.append(i)

Array2 = np.array(Array).reshape(numeroCapturado,redondeo)

mensajeDesCrifrado = ""
for i in np.nditer(Array2, order="F"):
    mensajeDesCrifrado = mensajeDesCrifrado+(str(i))


print("--------------------------------")
print("El mensaje cifrado es;  "+(mensajeCrifrado.replace("*","")))
print("--------------------------------")
print("El mensaje descifrado es;  "+(mensajeDesCrifrado.replace("*","")))
print("--------------------------------")