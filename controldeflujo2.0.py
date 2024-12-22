#aca pq el otro se lleno mucho##

for n in range (2,10):
    for x in range (2,n):
       if n % x == 0:
           print (n, 'equals', x, '*', n//x)
           break
       
    else:
         print(n, "es primo")
    #break hace que si se ejecuto a la primera ya de esa iteracion quieta quita brreak y mira lo q pasa
    #else ya debe estar atras de if ya q si no sucede se cumple el ese si lo ponemos debjo de if se hace un bluce inecesario tmb
    #Una forma de pensar en la cláusula else es imaginarla emparejada con la if dentro del bucle. A medida que se ejecuta el bucle, 
    # ejecutará una secuencia como if/if/if/else. La ifis dentro del bucle, se encuentra varias veces. Si la condición es verdadera 
    # alguna vez,  a breaksucederá. Si la condición nunca es verdadera, elsese ejecutará la cláusula fuera del bucle.

