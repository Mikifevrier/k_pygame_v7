from arkanoid import ANCHO, ALTO, FPS, levels
import pygame as pg
import random
from enum import Enum

class Marcador(pg.sprite.Sprite):
    plantilla = "{}"

    def __init__(self, x, y, justificado = "topleft", fontsize=25, color=(255,255,255)):
        super().__init__()
        self.fuente = pg.font.Font(None, fontsize)
        self.text = "0"
        self.color = color
        self.x = x
        self.y = y
        self.justificado = justificado
        self.image = self.fuente.render(str(self.text), True, self.color)
    
    def update(self, dt):
        self.image = self.fuente.render(self.plantilla.format(self.text), True, self.color)
        d = {self.justificado: (self.x, self.y)}
        self.rect = self.image.get_rect(**d)

class Ladrillo(pg.sprite.Sprite):
    disfraces = ["greenTile.png", "redTile.png", "redTileBreak.png"]

    def __init__(self, x, y, esDuro = False):
        super().__init__()
        self.listaImagenes = self.cargaImagenes()
        self.esDuro = esDuro
        self.imagen_actual = 1 if self.esDuro else 0
        self.image = self.listaImagenes[self.imagen_actual]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.numGolpes = 0

    def cargaImagenes(self):
        listaImagenes = []
        for fichero in self.disfraces:
            listaImagenes.append(pg.image.load("./images/{}".format(fichero)))
        return listaImagenes    

    def update(self, dt):
        if self.esDuro and self.numGolpes == 1:
            self.imagen_actual = 2
            self.image = self.listaImagenes[self.imagen_actual] #recuerda que el draw va a mostrar solo self.image***

    def desaparece(self):
        self.numGolpes += 1
        if self.numGolpes > 0 and not self.esDuro or self.numGolpes > 1 and self.esDuro:
            return True
        else:
            return False

class Raqueta(pg.sprite.Sprite):
    disfraces = ['electric00.png', 'electric01.png', 'electric02.png']

    def __init__(self, x, y):
        super().__init__()
        self.listaImagenes = self.cargaImagenes()
        self.imagen_actual = 0
        self.milisegundos_para_cambiar = 1000 // FPS * 5
        self.milisegundos_acumulados = 0
        self.image = self.listaImagenes[self.imagen_actual]

        self.rect = self.image.get_rect(centerx = x, bottom = y)
        self.vx = 7

    def cargaImagenes(self):
        listaImagenes = []
        for fichero in self.disfraces:
            listaImagenes.append(pg.image.load("./images/{}".format(fichero)))
        return listaImagenes

    def update(self, dt):
        teclas_pulsadas = pg.key.get_pressed()
        if teclas_pulsadas[pg.K_LEFT]:
            self.rect.x -= self.vx
        if teclas_pulsadas[pg.K_RIGHT]:
            self.rect.x += self.vx

        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= ANCHO:
            self.rect.right = ANCHO
        
        self.imagen_actual += 1
        if self.imagen_actual >= len(self.disfraces):
            self.imagen_actual = 0
        self.image = self.listaImagenes[self.imagen_actual]

class Bola(pg.sprite.Sprite):

    disfraces = ["ball1.png", "ball2.png", "ball3.png", "ball4.png", "ball5.png"]

    class Estado(Enum): #podemos enumerar estados para poder concadenar con el objeto bola los diferentes estados que enumeremos
        # Ponerlo en 0 para que sea viva, 1 para agonizando y 2 para muerta
        viva = 0
        agonizando = 1
        muerta = 2
    
    def __init__(self, x, y):
        super().__init__()
        self.listaImagenes = self.cargaImagenes()
        self.imagen_actual = 0
        self.image = self.listaImagenes[self.imagen_actual]
        self.milisegundos_acumulados = 0
        self.milisegundos_para_cambiar = 1000 // FPS * 10
        self.rect = self.image.get_rect(center=(x,y))
        self.xOriginal = x
        self.yOriginal = y
        self.estado = Bola.Estado.viva
        
        self.vx = random.randint(5,10) * random.choice([-1, 1])
        self.vy = random.randint(5,10) * random.choice([-1, 1])

    def cargaImagenes(self):
        listaImagenes = []
        for fichero in self.disfraces:
            listaImagenes.append(pg.image.load("./images/{}".format(fichero)))
        return listaImagenes
    
    def prueba_colision(self, grupo):
        candidatos = pg.sprite.spritecollide(self, grupo, False)
        if len(candidatos) > 0:
            self.vy *= -1
        return candidatos

    def update(self, dt):
        #update de estado viva
        if self.estado == Bola.Estado.viva:
            self.rect.x += self.vx
            self.rect.y += self.vy

            if self.rect.left <= 0 or self.rect.right >= ANCHO:
                self.vx *= -1
            if self.rect.top <= 0:
                self.vy *= -1
        
            if self.rect.bottom >= ALTO:
                self.estado = Bola.Estado.agonizando
                self.rect.bottom = ALTO
        
        #uptade de estado agonizando
        elif self.estado == Bola.Estado.agonizando:
            self.milisegundos_acumulados += dt
            if self.milisegundos_acumulados >= self.milisegundos_para_cambiar:
                self.imagen_actual += 1
                self.milisegundos_acumulados = 0
                if self.imagen_actual >= len(self.disfraces):
                    self.estado = Bola.Estado.muerta
                    self.imagen_actual = 0
                self.image = self.listaImagenes[self.imagen_actual]
        
        else:
            self.rect.center = (self.xOriginal, self.yOriginal)
            self.vx = random.randint(5, 10) * random.choice([-1, 1])
            self.vy = random.randint(5, 10) * random.choice([-1, 1])
            self.estado = Bola.Estado.viva