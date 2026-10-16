num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

print(f"La suma es: {num1 + num2}")
print(f"La multiplicación es: {num1 * num2}")

if num2 != 0:
    print(f"El residuo de la división es: {num1 % num2}")
else:
    print("No se puede dividir entre cero")