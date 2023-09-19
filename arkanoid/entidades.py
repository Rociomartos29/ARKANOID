import os
import random
from typing import Any
import pygame as pg
from . import Ancho, Alto, VEL_MAX, VEL_MIN_Y, VIDAS, ALTO_MARCADOR

margen = 25
velocidad = 5


class Raqueta(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imagenes = []
        margen = 25
        
        for i in range(3):
            ruta_image = os.path.join('resources', 'images', f'electric0{i}.png')
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

    def comprobar_teclas(self):
        velocidad = 10
        teclas = pg.key.get_pressed()
        if teclas[pg.K_LEFT]:
            self.rect.x -= velocidad
        if teclas[pg.K_RIGHT]:
            self.rect.x += velocidad

class Ladrillo(pg.sprite.Sprite):
    verde = 0
    rojo = 1
    rojo_roto = 2
    IMG_LADRILLO = ['greenTile.png', 'redTile.png', 'redTileBreak.png']
    def __init__(self, puntos,color = verde):
        super().__init__()
        self.tipo = color
        self.imagenes = []
        for img in self.IMG_LADRILLO:
            ruta = os.path.join('resources', 'images', img)
            self.imagenes.append(pg.image.load(ruta))
        self.image = pg.image.load(ruta)
        self.image = self.imagenes[color]
        self.rect = self.image.get_rect()
        self.puntos = puntos

    def update(self, muro):
        ruta = os.path.join('resources', 'images', self.IMG_LADRILLO[self.tipo])
        self.image = pg.image.load(ruta)
        if self.tipo == Ladrillo.rojo:
            self.tipo = Ladrillo.rojo_roto
            self.image = self.imagenes[self.tipo]
            return False
        else:
           muro.remove(self)
        return True



        
    
class Pelota(pg.sprite.Sprite):

    vel_x = -10
    vel_y = -13

    def __init__(self, raqueta):
        super().__init__()
        self.image = pg.image.load(os.path.join('resources', 'images', 'ball1.png'))
        self.rect = self.image.get_rect(midbottom=raqueta.rect.midtop)
        self.raqueta = raqueta
        self.vidas = VIDAS
        self.inicializar_velocidades()
        self.he_perdido = False

    def inicializar_velocidades(self):
        self.vel_x = random.randint(-VEL_MAX, VEL_MAX)
        self.vel_y = random.randint(-VEL_MAX, VEL_MIN_Y)
    def update(self, se_mueve_la_pelota):
        if not se_mueve_la_pelota:
            self.rect = self.image.get_rect(midbottom=self.raqueta.rect.midtop)
        else:
            self.rect.x += self.vel_x
            if self.rect.left <= 0 or self.rect.right > Ancho:
                self.vel_x = -self.vel_x

            self.rect.y += self.vel_y
            if self.rect.top <= 0:
                self.vel_y = -self.vel_y

            if self.rect.top >= Alto:
                self.inicializar_velocidades
                self.he_perdido = True

                
            if pg.sprite.collide_mask(self, self.raqueta):
                self.inicializar_velocidades()

        return se_mueve_la_pelota
            

    def pierdes(self):
        self.inicializar_velocidades()

            

class ContadorVidas:
    def __init__(self, vidas_iniciales):
        self.vidas = vidas_iniciales

    def perder_vida(self):
        self.vidas -= 1
        return self.vidas < 0

class Marcador:
    def __init__(self):
        self.valor = 0
        fuente = 'LibreFranklin-VariableFont_wght.ttf'
        ruta = os.path.join('resources', 'fonts', fuente)
        self.tipo_letra = pg.font.Font(ruta, 36)

    def aumentar(self, incremento):
        self.valor += incremento

    def pintar(self, pantalla):
        r = pg.rect.Rect(0,0, Ancho, ALTO_MARCADOR)
        pg.draw.rect(pantalla,(0, 0, 0), r)
        cadena = str(self.valor)
        texto = self.tipo_letra.render(cadena, True, (230, 189, 55))
        pos_x = 20
        pos_y = 10
        pantalla.blit(texto, (pos_x, pos_y)) 




        