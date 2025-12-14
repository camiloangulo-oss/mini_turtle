class Tortuga:
    def __init__(self):
        self.posicion_x = 0

    def adelante(self, pasos):
        self.posicion_x += pasos
        print(f"Tortuga en posición: {self.posicion_x}")

    def abajo(self):
        print("La tortuga bajó")

    def reiniciar(self):
        self.posicion_x = 0
        print("Posición reiniciada")
