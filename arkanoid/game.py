import pygame as pg
from . import Ancho, Alto, Color_fondo
from . escenas import Portada, Partida, Mejore_Jugadores

# Pntalla


class Arkanoid:
    def __init__(self):
        pg.init()
        self.pantalla = pg.display.set_mode((Ancho, Alto))

        portada = Portada(self.pantalla)
        partida = Partida(self.pantalla)
        records = Mejore_Jugadores(self.pantalla)
        self.escenas = [
            portada,
            partida,
            records
        ]

    def Jugar(self):
        for escena in self.escenas:
            escena.bucle_principal()

        pg.quit()


if __name__ == 'main':
    print('Arrancamos desde el archivo Arkanoid.py')
    juego = Arkanoid()
    juego.Jugar()
