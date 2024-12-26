
#ek match y case y return 

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

# Llama a la función y usa print para mostrar el resultado:
print(http_error(401))  # Esto debería imprimir: "Not found"


def http_sf(stato):
    match stato:
        case 400 | 600 | 400:
         return "no sirve hecmano"
        case _ : 
            return "ñe"


print(http_sf(200))



#math case

#match point: 
 #   case (0, 0):
 #       print("Origin")
  #  case (0, y):
 #       print(f"Y={y}")
  #  case (x, 0):
   #     print(f"X={x}")
  #  case (x, y):
  #      print(f"X={x}, Y={y}")
  #  case _:
   #     raise ValueError("Not a point")

#¿Qué hace este código?
#El código asume que hay una variable llamada point, que contiene un par de coordenadas (como (x, y)), y usa match-case para
#  analizar esos valores y responder según el caso.
#Explicación de los casos:
#case (0, 0):
#Si point es (0, 0) (el origen en un plano cartesiano), imprime "Origin".

#case (0, y):
#Si x es 0 pero y puede ser cualquier valor (por ejemplo, (0, 5)), imprime el valor de y como "Y={y}".

#case (x, 0):
#Si y es 0 pero x puede ser cualquier valor (por ejemplo, (4, 0)), imprime el valor de x como "X={x}".

#case (x, y):
#Si tanto x como y son cualquier valor (por ejemplo, (3, 7)), imprime ambos valores como "X={x}, Y={y}".

#case _:
#Esto es un "caso por defecto". Si ninguno de los anteriores coincide, lanza un error con el mensaje "Not a point".
#explicale la analogia en suponiendo que point entrega 2 valores y lo q se debe guardar en cada caso


class Point:
      def __init__(self, x, y):
        self.x = x
        self.y = y

       # ¿Qué hace esto?
#Es una clase que define un punto con dos atributos: x e y.
#Cuando creas un objeto Point, debes pasarle dos valores (uno para x y otro para y), y el constructor (__init__) los asigna.
vx = int(input("valor de x:"))
vy = int(input("valor de y:"))

t = Point(vx,vy)

def where_is(t):
    match t:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

where_is(t)





    #creando class para entender mejol
class Culeo:
    def __init__(self, mario1, mario2):  # self es obligatorio en métodos de instancia
        self.JULIO = mario1 # Aquí, self.x es un atributo del objeto
        self.ROBERTO = mario2

#aqui introducimos valores a JULIO Y ROBERTO
sa = int(input("metelo:"))
re = int(input("mele el otro:"))
# Crear un objeto Point
p = Culeo(sa,re)



if re == 0:
 print("no eres gay felicidades:)")

else:    
 print("JULIO TE LA METIO " , p.JULIO, "VECES"  ) # Esto imprime (el valor asignado a x en el constructor)

 
if sa == 0: 
 print("melo no eres gay")

else:
     print("roberto de la metio", p.ROBERTO, "veces" )  # Esto imprime (el valor asignado a y en el constructor)

     #seguir pratocando self y def con macth