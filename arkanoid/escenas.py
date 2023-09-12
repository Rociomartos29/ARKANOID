import os
import pygame as pg
from . import Alto, Ancho, FPS
from .entidades import Raqueta


class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()

    def bucle_principal(self):
        '''
        Este metodo debe ser implementado por todas y cada una de las escenas, 
        en funcion de lo que esten esperando hasta la condicion de salida.
        '''
        print('Esto es un metodo vacio')


class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        ruta = os.path.join('Resorces', 'resources',
                            'images', 'arkanoid_name.png')
        self.logo = pg.image.load(ruta)

        ruta_font = os.path.join('Resorces', 'resources',
                                 'fonts', 'CabinSketch-Bold.ttf')
        self.tipo = pg.font.Font(ruta_font, 35)

    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    salir = True

            self.pantalla.fill((99, 0, 0))
            self.pintar_logo()
            self.pintar_mensaje()
            # self.comprobar_teclas()
            pg.display.flip()

    '''def comprobar_teclas(self):
        espacio = pg.key.get_pressed()

        if espacio[pg.K_SPACE]:
            salir = True
        print('QUIERES SALIR')'''

    def pintar_logo(self):
        ancho, alto = self.logo.get_size()
        pos_x = (Ancho - ancho) / 2
        pos_y = (Alto - alto)/2
        self.pantalla.blit(self.logo, (pos_x, pos_y))

    def pintar_mensaje(self):
        mensaje = 'Pulsa <Espacio> para comenzar'
        texto = self.tipo.render(mensaje, True, (255, 255, 255))
        pos_x = (Ancho - texto.get_width())/2
        pos_y = Alto / 4 * 3
        self.pantalla.blit(texto, (pos_x, pos_y))


class Partida(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        ruta_fondo = os.path.join(
            'Resorces', 'resources', 'images', 'background.jpg')
        self.fondo = pg.image.load(ruta_fondo)
        self.jugador = Raqueta()

    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            self.reloj.tick(FPS)
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    salir = True
            self.pintar_fondo()
            self.jugador.update()
            self.pantalla.blit(self.jugador.image, self.jugador.rect)
            pg.display.flip()

    def pintar_fondo(self):
        self.pantalla.fill((0, 0, 99))

        self.pantalla.blit(self.fondo, (0, 0))
        self.pantalla.blit(self.fondo, (600, 0))
        self.pantalla.blit(self.fondo, (0, 800))
        self.pantalla.blit(self.fondo, (600, 800))


class Mejore_Jugadores(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)

    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    salir = True
            self.pantalla.fill((0, 0, 99))
            pg.display.flip()
