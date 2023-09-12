import os
from typing import Any
import pygame as pg
from . import Ancho, Alto

margen = 25
velocidad = 5


class Raqueta(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imagenes = []
        margen = 25
        velocidad = 5
        for i in range(3):
            ruta_image = os.path.join(
                'Resorces', 'resources', 'images', f'electric0{i}.png')
            self.imagenes.append(pg.image.load(ruta_image))
        self.contador = 0
        self.image = self.imagenes[self.contador]

        self.rect = self.image.get_rect(
            midbottom=(Ancho/2, Alto - margen))

    def update(self):
        self.contador += 1
        if self.contador > 2:
            self.contador = 0
        self.comprobar_teclas()
        self.image = self.imagenes[self.contador]

    def mover(self):
        pass

    def pintar(self):
        pass

    def reset(self):
        pass

    def comprobar_teclas(self):
        teclas = pg.key.get_pressed()
        if teclas[pg.K_LEFT]:
            self.rect.x -= velocidad
        if teclas[pg.K_RIGHT]:
            self.rect.x += velocidad
