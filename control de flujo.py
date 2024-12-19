#sentencia if
x = str(input("Cual es tu nombre:"))   #en str o int aclaramos que tipo de valor pedimos y en imput aja ponemos el coment a mostar y la entarda de texto
# esos datos se almacenan
j = int (input("Cual es tu edad ?"))


print ("tu nombre es", x)
print("tu edad es", j)


#y con if puedo generar respuesta de acuerdo a los datos proporcionados
if j==13 :
 
 print("aqui tienes para que me las beses")

elif j <= 20:

 print("joven a un")

else:
 
 print("la vejes te consume")




#funcnion for hace iteraciones

words = ["girl", "men","father "]

for t in words: #en pocas palabras agarra la viable words pacaya la vuekve t y la desglosa en interlineados la lista y dice cuantas letras 
 #con la funcion len es decir se complementan
 print(t,len(t))
 #en pocas palabras hace un blucle que en la lista de words t va a tomar valor de cada una de los elementos de la lista y por se ven 
 #los resultados de la lista separados

#Condicional RANGEEE

for numeroal5 in range(5):
 print(numeroal5)
#Hace iteraciones en el rango de 5 numeros creando la varible a iterar numeroal5


OLI = list(range(4,6))
print(OLI)

#Para iterar sobre los índices de una secuencia, puedes combinar range() y len() así: 

totuma = ["alverto", "carolina", "nooooMKK"]
for JK in  range(len(totuma)):    #RANGe(len(totuma)) permite que len haga conteo en totuma  ese conteo es sacado como rango en range
 #lo cual permite que range entregue una iteracion a JK de orden de numeros por range y salga en forma de lista
 print(JK, totuma[JK] )   #Cuando escribes TOTUMA[JK], estás diciendo: "Dame el elemento de la lista a que está en la posición JK".
#En el bucle:
#La variable jk toma valores consecutivos desde 0 hasta 4 (por el rango range(len(TOTUMA))).
#y se imprime JK pq es el indice por cada iteracion  y JK totuma[JK] se complementan por la iteracion

#buble con  breAK papa

for  n in range(2,10):   #BUENO ESTA PERRO PERO AJA 
 for x in range(2,n):  #EL FOR LE DICE N SERA EL RANGO DE ITERACION DE 2 A 10 ES DECIR N SERA 2,3,4 HASTA 9
#LUEGO AL FOR EXTERNO ENTRA OTRO INTERNO Y LE DICE AY PAPA X INTERARA SOBRE EL RANGO DE 2 Y EL N QUE ME DES DE TUS INTECACIONES 
#LUEGO IF REVISA SI N AL DIVIDIRSE POR X DA COMO SOBRANTE EN LA DIVISION CERO SE IMPRIME N EL NUMERO PRIMERITO Y X * N/x
# (ESTO SE PONE ASI PQ AL DIVIDIR OBTENEMOS EL VALOR INVERSO DE N AL DIVIDIR AJA COMPRUEBA Y VERAS)
  if n%x==0:
   print(f"{n} ES DIVISIBLE POL {x}*{n//x}  ")
   break
  #EL BREAK PARA EL BUCLE INTERNO AL ENCONTRAR AL PRIMER IF CUMPLIRSE Y VA POR EL PROXIMO N A VER SI CUMPLE EL REQUISITO Y YIA


#continue en la iteraciones es parecido a else pero NOM ES EL MISMO ejem aqui itera de 2 a 10 en ese rango si el numero es divisible 
#por 2 y la division de resto da 0 se impimira un numero par y se ejecutara continue y salta para la proxima itecacion y se salta 
# lo demas esto sirve para ahorrar recursos etc y si el if no se cumple alli si imprime lo otro pero si se usara else antes de 
# el print numero impar daria lo mismo en la impresion pero con el else como condicional es decir el programa lee todo 
 #pero si el if se cumple else se cancela es parecido pero gasta mas recursos

for num in range(2, 10):
    if num % 2 == 0:
        print(f"numero par {num}")
        continue
    print(f"numero impar {num}")



