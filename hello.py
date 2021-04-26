import pygame as pg 

pg.init() #inicializar los recursos necesarios (obligatorio)
pantalla = pg.display.set_mode((600, 400)) #para las dimensiones de la pantalla se ponen en tuplas
pg.display.set_caption("Hola") #Pone un display en la pantalla

game_over = False

while not game_over:
    # Gestión de eventos
    for evento in pg.event.get():
        pass
    
    
    
    
    
    # Gestión del estado
    print("Hola mundo")
    
    
    
    # Refrescar pantalla
    pantalla.fill((0, 255, 0)) #colorea la pantalla

    pg.display.flip() #pasa a la memoria gráfica