import pygame as pg
from . import Ancho, Alto, Color_fondo

# Pntalla


class Arkanoid:
    def __init__(self):
        pg.init()
        self.pantalla = pg.display.set_mode((Ancho, Alto))

    def Jugar(self):
        salir = False
        while not salir:
            # Capturar eventos
            for evento in pg.event.get():
                if pg.QUIT == evento.type:
                    salir = True

            # Pintar y calcular el estado de los elementos
            self.pantalla.fill(Color_fondo)

           # Mostrar los cambios y controlar el reloj
            pg.display.flip()
        pg.quit()


if __name__ == 'main':
    print('Arrancamos desde el archivo Arkanoid.py')
    juego = Arkanoid()
    juego.Jugar()
