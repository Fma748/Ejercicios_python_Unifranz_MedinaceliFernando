notas = []

cantidad = int(input("¿Cuántas notas deseas ingresar? "))

for i in range(cantidad):
    while True:
        nota = float(input(f"Ingresa la nota {i + 1} (de 0 a 100): "))
        if 0 <= nota <= 100:
            notas.append(nota)
            break
        else:
            print(f"La nota {nota} no es válida. Debe estar entre 0 y 100.")

promedio = sum(notas) / len(notas)
print(f"\nEl promedio final es: {promedio:.2f}")

if promedio <= 50:
    print(f"REPROBADO con la nota: {promedio:.2f}")
else:
    print(f"APROBADO con la nota: {promedio:.2f}")