# Proyecto calculadora IMC
import time 

print("IMC Monitor")

#Input para el Nombre
nombre = input("Introduzca por favor su nombre: ")
while not nombre.strip() or not all(c.isalpha() or c.isspace() for c in nombre): # Validaciones: Sin espacios vacios, No numeros ni caracteres especiales, Permite espacio entre Palabras 
    if not nombre.strip(): print("El nombre no puede estar vacío. Por favor ingréselo.")
    else: print("Error: El nombre no puede contener números ni caracteres especiales.")
    nombre = input("Introduzca por favor su nombre: ")
    nombre = nombre.strip().title() # Capitalizar las dos primeras letras en caso de dos nombres

#Input para el Apellido Paterno
apellidoPaterno = input("Introduzca por favor su apellido paterno: ")
while not apellidoPaterno.strip() or not all (c.isalpha() or c.isspace() for c in apellidoPaterno): # Validaciones: Sin espacios vacios, No numeros ni caracteres especiales, Permite espacio entre Palabras
    if not apellidoPaterno.strip(): print("El apellido no puede estar vacío. Por favor ingréselo.")
    else: print("Error: El apellido no puede contener números ni caracteres especiales.")
    apellidoPaterno = input("Introduzca por favor su apellido paterno: ")
    apellidoPaterno = apellidoPaterno.strip().title() # Capitalizar las dos primeras letras en caso de dos palabras

#Input para el Apellido Materno
apellidoMaterno = input("Su apellido Materno: ")
while not apellidoMaterno.strip() or not all (c.isalpha() or c.isspace() for c in apellidoMaterno): # Validaciones: Sin espacios vacios, No numeros ni caracteres especiales, Permite espacio entre Palabras
    if not apellidoMaterno.strip(): print("El apellido no puede estar vacío Por favor ingréselo.")
    else: print("Error: El apellido no puede contener números ni caracteres especiales.")
    apellidoMaterno = input("Introduzca por favor su apellido paterno: ")
    apellidoMaterno = apellidoMaterno.strip().capitalize() # Capitalizar las dos primeras letras en caso de dos palabras  

#Imprimir nombre completo
print(f"Hola! {nombre} {apellidoPaterno} {apellidoMaterno}")
time.sleep(1.5) # Tiempo de espera entre prints
print("Calculemos tu Indice de masa corporal")

# Input de edad
while True: # Bucle para validacion correcta
    edad = input("Tu edad: ").strip()  # Elimina espacios en blanco al principio y al final
    if not edad:  # Verifica si la entrada está vacía
        print("Error: No puede dejar el campo vacío.")
        continue
    if edad.isdigit():  # Verifica si la entrada son solo números
        edad = int(edad)  # Convierte a entero
        if edad >= 18: # Limite de edad +18
            break # Bucle para validacion correcta
        else: print("Error: Esta calculadora solo funciona para mayores de 18 años.")
    else: print("Error: Debe ingresar un número válido.")

#Input de estatura
while True:  # Bucle para validación correcta de estatura
    estatura = input("Tu altura (en metros): ").strip()  # Elimina espacios en blanco al principio y al final
    if not estatura:  # Verifica si la entrada está vacía
        print("Error: No puede dejar el campo vacío.")
        continue
    try:
        estatura = float(estatura)  # Intenta convertir la entrada a un número flotante
        if estatura > 1:  # Verifica si la estatura es mayor a 1 metro
            break  # Sale del bucle si todo es válido
        else:
            print("Error: La estatura debe ser mayor a un metro.")
    except ValueError:  # Captura errores de conversión
        print("Error: Debe ingresar un número válido.")

# Input de peso
while True:  # Bucle para validación correcta de peso
    peso = input("Tu peso en Kg: ").strip()  # Elimina espacios en blanco al principio y al final
    if not peso:  # Verifica si la entrada está vacía
        print("Error: No puede dejar el campo vacío.")
        continue
    try:
        peso = float(peso)  # Intenta convertir la entrada a un número flotante
        if peso > 20:  # Verifica si el peso es mayor a 20 kg
            break  # Sale del bucle si todo es válido
        else:
            print("Error: El peso debe ser mayor a 20kg.")
    except ValueError:  # Captura errores de conversión
        print("Error: Debe ingresar un número válido.")

# Print de inputss, con pausas entre prints
print("\nTus datos son los siguientes:")
time.sleep(0.8)
print(f"Nombre: {nombre}")
time.sleep(0.8)
print(f"Apellido paterno: {apellidoPaterno}")
time.sleep(0.8)
print(f"Apellido materno: {apellidoMaterno}")
time.sleep(0.8)
print(f"Edad: {edad}")
time.sleep(0.8)
print(f"Peso: {peso} kg")
time.sleep(0.8)
print(f"Estatura: {estatura} m")

# Print de espera
for _ in range(3): # Repetición de print "Calculando..."
    time.sleep(1)
    print("Calculando...")

# Formulas y prints por rangos
IMC = peso / estatura**2
if IMC >= 0 and IMC <= 15.99 :
        print (f"Tu IMC es {IMC} = a: Delgadez severa")
elif IMC >= 16.00 and IMC <= 16.99 :
        print (f"fTu IMC es {IMC} = a: Delgadez moderada")
elif IMC >= 17.00 and IMC <= 18.49:
        print (f"Tu IMC es {IMC} = a: Delgadez leve")
elif IMC >= 18.50 and IMC <= 24.99 :
        print (f"Tu IMC es {IMC} = a: Normal")
elif IMC >= 25.00 and IMC <= 29.99:
        print (f"Tu IMC es {IMC} = a: Sobrepeso")
elif IMC >= 30.00 and IMC <= 34.99:
        print (f"Tu IMC es {IMC} = a: Obesidad leve")
elif IMC >= 35.00 and IMC <= 39.00:
        print (f"Tu IMC es {IMC} = a: Obesidad media")
elif IMC >= 40.00:
    print (f"Tu IMC es {IMC} = a: Obesidad morbida")