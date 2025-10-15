# Paso 1: Solicitar al usuario que ingrese su edad

edad = int(input("Ingrese su edad: "))

# Paso 2: Verificar si la edad cumple con el requisito de ingreso del bar 

permitido = True if edad >= 18 else False

# Paso 3: Mostrar al usuario si es apto o no para el ingreso

if permitido:
    print("Tienes la edad suficiente para ingresar al bar")
else:
    print("No tienes la edad suficiente para ingresar al bar")