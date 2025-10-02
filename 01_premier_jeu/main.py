import pygame
import sys


class Ennemie:
    def __init__(self, x, y, couleur, taille):
        self.x = x
        self.y = y
        self.couleur = couleur
        self.taille = taille

pygame.init()

largeur = 800
hauteur = 600

fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Premier jeu")

NOIR = (0, 0, 0)

JOUEUR = (0, 0, 255)
TAILLE_JOUEUR = 30

vitesse_joueur = 120
direction_joueur = [0, 0]
position_joueur = [largeur // 2, hauteur // 2]

clock = pygame.time.Clock()

while True:
    deltatime = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction_joueur[1] -= vitesse_joueur
            elif event.key == pygame.K_DOWN:
                direction_joueur[1] += vitesse_joueur
            elif event.key == pygame.K_LEFT:
                direction_joueur[0] -= vitesse_joueur
            elif event.key == pygame.K_RIGHT:
                direction_joueur[0] += vitesse_joueur
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                direction_joueur[1] += vitesse_joueur
            elif event.key == pygame.K_DOWN:
                direction_joueur[1] -= vitesse_joueur
            elif event.key == pygame.K_LEFT:
                direction_joueur[0] += vitesse_joueur
            elif event.key == pygame.K_RIGHT:
                direction_joueur[0] -= vitesse_joueur

    #ici
    position_joueur[0] += direction_joueur[0] * deltatime
    position_joueur[1] += direction_joueur[1] * deltatime

    fenetre.fill(NOIR)

    pygame.draw.circle(fenetre, JOUEUR, position_joueur, TAILLE_JOUEUR)

    pygame.display.flip()