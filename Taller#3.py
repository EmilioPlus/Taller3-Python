#Ejercicio #1 y 2 del taller 3
def hash(string):
    return any(char.isdigit() for char in string)

Objetos = []

for a in range(10):
    objeto = input("Ingrese cualquier objeto de la vida cotidiana: ")
    if(hash(objeto)):
        print("Error eso no es un objecto, intentalo de nuevo: ")
    else:
        Objetos.append(objeto)
        print("Eso es un objeto")
        print(Objetos, len(Objetos))

Animales = []

for a in range(7):
    animal = input("Ahora Ingrese in animal que desee: ")
    if(hash(animal)):
        print("Esto no es un animal, por vafor intentalo de nuevo:")
    else:
        Animales.append(animal)
        print("Eso es un animales")
        print(Animales, len(Animales))


opcion = input("Desea terminar? (Si/No):\n").lower()
if(opcion == "si"):
    Objetos += Animales
    print(Objetos)
else:
    del Objetos[:]
    del Animales[:]
    print(Objetos,Animales)

#Ejercico #3 
lista = ["Figeroa", "Marcela",  "Sistema", "Apellido", (7,10,9,7,"Maria"), "Anton", 7881.36]

print("-----longitud-----")
longitud = len(lista)
print(f"La longitud tiene {longitud}")

#Ejercicio #4
import math 

Opcn = int(input("Ingrese el calculo geometrico de la figuras basica "
        "\n1. Circulo "
        "\n2. Rectangulo "
        "\n3. Paralelogramo " 
        "\n4. Paralelepipedo "
        "\n5. Triangulo"
        "\n6. Salir"
        "\nOpcion: "))

if Opcn == 1: 
    print("El area de un Circulo")
    radio = float(input("Ingrese el radio del circulo: "))
    area = math.pi * (radio * radio)
    print("El area del circulo con radio "+radio+" es " + round(area,2))
elif Opcn == 2:
    print("El area de un rectángulo")
    base = float(input("Digite la base del Rectangulo: "))
    altura = float(input("Digite la altura del Rectangulo: "))
    area = base * altura
    print("El area del paralelogramo es igual a: "+ area)
elif Opcn == 3:    
    print("El area de un paralelogramo")
    base = float(input("Digite la base del paralelogramo: "))
    altura = float(input("Digite la altura del paralelogramo: "))
    area = base * altura
    print("El area del paralelogramo es igual a: " + area)
elif Opcn == 4:
    print("El area de un paralelepípedo")
    largo = int(input("Digite la base da largo: "))
    ancho = int(input("Digite la base da ancho: "))
    alto = int(input("Digite la base da alto: "))
    area = ( 2 * (largo*ancho) + (largo*alto) + (ancho*alto) )
    print("El area paralelepipedo " + area)
elif Opcn == 5:    
    print("El area de un Triangulo")
    base = float(input("Escriba la base del triangulo: "))
    altura = float(input("Escriba la Altura del triangulo: "))
    area = (base * altura) / 2
    print("")
    print("El area del triangulo es " + area)
elif Opcn == 6:
    print("Geacias por participar, Adios")
else:
    print("Error del sistema")

#Ejercico #5
Numero = 0
suma = 0
for Numero in [10,11,12,13,14,15,16,17,18,19,20]: 
    if Numero % 2 == 0:
        suma += Numero
        print(Numero)
        
        
print("")
print("La suma total es: ",str(suma))

#Ejercico #6
perro=[]
gato=[]
pez=[]
loro=[]

contdPerro = 1
contdGato = 1
contdPez = 1
contdLoro = 1

while (contdPerro  <= 6 or contdGato <= 6 or contdPez <= 6 or contdLoro <= 6):

	animal = input("Ingresa el nombre del animal: ").lower()

	if (animal == "perro"):
		if(len(perro)<6):
			for i in range(0,6):
				nombre=input("Porfavor Ingresa el nombre del Perro #" + str(contdPerro )+ ": ")
				perro.append(nombre)
				contdPerro  +=1
		else:
			print("Lista completa de perros: ")

	elif (animal == "gato"):
		if(len(gato)<6):
			for i in range(0,6):
				nombre=input("Porfavor Ingresa el nombre del Gato #" + str(contdGato)+ ": ")
				gato.append(nombre)
				contdGato +=1
		else:
			print("Lista completa de gatos: ")

		
	elif (animal == "pez"):
		if(len(pez)<6):
			for i in range(0,6):
				nombre=input("Porfavor Ingrese el nombre del Pez #" + str(contdPez)+ ": ")
				pez.append(nombre)
				contdPez +=1
		else:
			print("Lista completa de peces: ")

	elif (animal == "loro"):
		if(len(loro)<6):
			for i in range(0,6):
				nombre=input("Ingrese el nombre del loro #" + str(contdLoro)+ ": ")
				loro.append(nombre)
				contdLoro +=1
		else:
			print("Lista completa de loros: ")

	animales = {'perro':perro, 'gato':gato, 'pez':pez, 'loro':loro}

	busqAnimal = int(input("Le gustaria buscar algun nombre de animal?\n1: Si\n2: No\n"))

	if (busqAnimal == 1):
		continuar =  True
		while (continuar == True):
			buscar = input("Menu:\nPerro\nLoro\nSalir\nPor favor ingrese"+
				"Nombre del tipo de animal que deseas buscar: ").lower()
			if(buscar != "salir"):
				print("Los nombres del tipo de animal "+ buscar + " son:"+ str(animales.get(buscar)))
			else:
				continuar = False
	else:
		print("")





