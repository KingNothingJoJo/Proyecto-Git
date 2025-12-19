import random

maquina = random.randint(1, 3)

manos = {1: "Piedra", 2: "Papel", 3: "Tijeras"}

humano = int(input("Elige 1 para Piedra, 2 para Papel, 3 para Tijeras:\n "))

print(f"Tu elección: {manos[humano]}")
print(f"Elección de la máquina: {manos[maquina]}")

if humano == maquina:
    print("Empate")

elif (humano == 1 and maquina == 3) or (humano == 2 and maquina == 1) or (humano == 3 and maquina == 2):
    print("¡Ganaste!")
else:
    print("Perdiste")