import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = []


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        pass

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()

        pass


def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


main()


class Ball:
    rayon_cercle = random.randint(10, 30)
    cercle_x = random.randint(100,150)
    cercle_y = random.randint(100,150)
    color = random.choice(COLORS)
    cercle = Cercle(rayon, center_x, center_y, color)
    self.liste_cercles.append(cercle)



cercle_x += cercle_change_x
cercle_y += cercle_change_y
def on_update:

    cercle_change_x = 3  # Nombre d'unité pour le déplacement sur l'axe des X
    cercle_change_y = 3  # Nombre d'unité pour le déplacement sur l'axe des Y

    if cercle_x < rayon_cercle:
        cercle_x *= -1
    if cercle_x > SCREEN_WIDTH - rayon_cercle:
	pass
    if cercle_y < rayon_cercle:
	pass
    if cercle_y > SCREEN_HEIGHT - rayon_cercle:
	pass


