# Datos del atleta
class Atleta: 
    def __init__(self, nombre, apellido, edad, peso_corporal, salida_arranque, salida_envion):
        self.nombre = nombre 
        self.apellido = apellido 
        self.edad=edad 
        self.peso_corporal = peso_corporal 
        self.salida_arranque = salida_arranque 
        self.salida_envion = salida_envion 

# Cantidad de atletas en competencia
cantidad_de_atletas = int(input("Ingrese la cantidad de atletas Inscriptos: "))
cant_atletas = cantidad_de_atletas
#Loop para ingresar la cantidad total de atletas 
atletas_listado = []

while (cantidad_de_atletas != 0 ):
    cantidad_de_atletas -= 1
    #Solicitar los datos del atleta
    nombre = input("Ingresar nombre del atleta: ")
    apellido = input("Ingresar apellido del atleta: ")
    edad = input("Ingresar edad del atleta: ")
    peso_corporal = input("Ingresar peso_corporal del atleta: ")
    salida_arranque = input("Ingresar salida_arranque del atleta peso_corporal: ")
    salida_envion = input("Ingresar salida_envion del atleta peso_corporal: ")
    
    #Creando al atleta
    atleta = Atleta(nombre,apellido,edad,peso_corporal, salida_arranque, salida_envion)

    #agregando el ateta al listado
    atletas_listado.append(atleta)

    print("El atleta fue agregado con exito")


#Imprimiento el listado de atletas

while (cant_atletas != 0):
    print(atletas_listado[cant_atletas-1].nombre)
    print(atletas_listado[cant_atletas-1].apellido)
    print(atletas_listado[cant_atletas-1].edad)
    print(atletas_listado[cant_atletas-1].peso_corporal)
    print(atletas_listado[cant_atletas-1].salida_arranque)
    print(atletas_listado[cant_atletas-1].salida_envion)
    cant_atletas -= 1

print("Atletas ingresado con exito")


