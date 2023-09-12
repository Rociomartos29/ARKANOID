import os
from typing import Any
import pygame as pg
from . import Ancho, Alto


class Raqueta(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imagenes = []

        for i in range(3):
            ruta_image = os.path.join(
                'Resorces', 'resources', 'images', f'electric0{i}.png')
            self.imagenes.append(pg.image.load(ruta_image))
        self.contador = 0
        self.image = self.imagenes[self.contador]

        margen = 25
        self.rect = self.image.get_rect(
            midbottom=(Ancho/2, Alto - margen))

    def update(self):
        self.contador += 1
        if self.contador > 2:
            self.contador = 0

        self.image = self.imagenes[self.contador]

    def mover(self):
        pass

    def pintar(self):
        pass

    def reset(self):
        pass
