posicion_x = 0

def adelante(pasos):
    global posicion_x
    posicion_x += pasos
    print(f"Tortuga avanza {pasos} pasos. Posición actual: {posicion_x}")

def abajo():
    print("La tortuga baja una línea")

def reiniciar():
    global posicion_x
    posicion_x = 0
    print("La posición fue reiniciada a 0")
