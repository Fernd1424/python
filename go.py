#EL ´#´ para cometarios etc
#print imprime en consola lo deseados el operador + y - suma y resta 
#la , se usa en print para decir 2 cosas o mas es decir el operador que da numero int y el texto
#el operador * es multiplicacion el ** es potencia el / division en numero float // division en numero int
print (2+2, "suma", "ra" )
print (17/2, "division" )
print (17//2, "division exacta" )
print(2*3, "multiplicacion" )
print (2**3,  "potencia")

#Variables HAY QUE DARLE VALOR CON = O SI NO DA ERROR

hola = 34
re= 2
ñe =  hola * re 
print (ñe)

#el texto es de tipo str
# en caso de usar sifnis espefcficos como # o "" etc se usa / para leerlo como str por python
print("does\"nt")
fer = "sasa\ntoto" #\n para separar lineas cuando se vaya a imprimir en print
print (fer)
print(r"C:\n\s")  #r hace que se omitan caracteres especiales dentro de el str 
print (
    """
    ssssssss
    -a
    -b
    """
)# """ para escribir con espaciados etc
print ("a"+"b")  #con catenar es decir unir str
rah = "sa"
print(rah + "po")

##posicionamiento con [] con la funcion "[]" y ponemos numero busca posicionamiento de una letra en una palabra de 0 a n letras

word = "python"
print (word[0])
print (word [3])
#se puede a la inversa tambien
print (word[-1])
#y concatenar 
print(word[0:3])
print(word[2:])
#len es pa saber la longitud de u UNA STR 
AYMK = "sndhshdsgdhsgd"
print(len(AYMK))

###listas###
print("listas")
ELHP = [2, 3, 4, 5]
print (ELHP) #SON MUTABLES LOS STR no
ELHP[1] = 6 #AJA SE LE CAMBIA CON EL [] que nos permite acceder al carácter  que necesitamos y cambiarlo con =
print (ELHP)
#se pueden sumas cadenas a loco 
homero = ELHP + [23, 90] 
print (homero)
homero.append(200)
print(homero) 


#las variables se unen a lo loco 
rgb = [2, 3, 4]
rgba = rgb
print(rgb == rgba) #se igualan etc
rgb.append(9)
print(rgba)

#rebanados y vaciado 
rgb[0:2] = (5, 6 ) #remplazos 
print (rgb)

rgb[0:2] = [] #borrar partes
print(rgb)

ha = [20, 30 , 90]
ha[:] = [] 
#limpiar todoooooOOOooOOoOoo JAJAJA
print(ha)

letters = ['a', 'b', 'c', 'd', 'e']
print(len(letters))

#anidar lista 
a = [2, 4]
b = [3,9] 
k = [a, b]
print(k)

#Fibonacci series: 
a, b = 0, 1 
while a < 10:  #La función while en programación se utiliza para ejecutar un bloque de código repetidamente mientras una condición sea verdadera. Es una estructura 
    #de control de flujo que revisa la condición antes de cada iteración y se detiene cuando esta deja de cumplirse.
    print(a)
    a, b = b, a+b

    #los signo >< ==  y  != significa diferen 


#Fibonacci series: 
a, b = 0, 1 
while a < 10: 
    print(a, end="," ) #el parametro end hace que la impresion en consola no sea en salto de linea y de ademas se coloque la ,
    a, b = b, a+b 

