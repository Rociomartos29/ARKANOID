import pygame
from . import Ancho, Alto, Color_fondo

# Pntalla


class Arkanoid:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((Ancho, Alto))

    def Jugar(self):
        salir = False
        while not salir:
            # Capturar eventos
            for evento in pygame.event.get():
                if pygame.QUIT == evento.type:
                    salir = True

            # Pintar y calcular el estado de los elementos
            self.pantalla.fill(Color_fondo)

           # Mostrar los cambios y controlar el reloj
            pygame.display.flip()
        pygame.quit()


if __name__ == 'main':
    print('Arrancamos desde el archivo Arkanoid.py')
    juego = Arkanoid()
    juego.Jugar()
