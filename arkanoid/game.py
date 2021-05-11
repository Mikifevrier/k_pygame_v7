from arkanoid import ANCHO, ALTO, FPS
from arkanoid.escenes import Portada, Game
import pygame as pg

pg.init()

class Arkanoid():
    def __init__(self):
        pantalla = pg.display.set_mode((ANCHO, ALTO))
        self.escenas = [Portada(pantalla), Game(pantalla)]
        self.escena_activa = 0

    def start(self):
        while True:
            la_escena = self.escenas[self.escena_activa]
            la_escena.reset()
            la_escena.bucle_principal()

            self.escena_activa += 1
            if self.escena_activa >= len(self.escenas):
                self.escena_activa = 0

            #self.escena_activa = (self.escena_activa + 1) % len(self.escenas)
