import random

mano = random.randint(1, 3)

manos = {1: "Piedra", 2: "Papel", 3: "Tijeras"}

intento = int(input("Elige 1 para Piedra, 2 para Papel, 3 para Tijeras:\n "))

print(f"Tu elección: {manos[intento]}")
print(f"Elección de la máquina: {manos[mano]}")

if intento == mano:
    print("Empate")

elif (intento == 1 and mano == 3) or (intento == 2 and mano == 1) or (intento == 3 and mano == 2):
    print("¡Ganaste!")
else:
    print("Perdiste")