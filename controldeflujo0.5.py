## ijnteraciones en diccionario 

users = {"fer":"true","milo":"false" }

for user, status in users.copy().items():  #lo que hace for es crear user como iteracion, status esta en la variables users y crea una 
    #copia y accede a los items de el dicionario en tonces con if si se cumple la condicion que el item de alguna represtenacion en el diccionario
    #se borra con la funcion del  en la iteracion user creada
    if status == "false" :
        del users[user]
    else: 
      print (user, status )


print(user, status) 

print(8//2)