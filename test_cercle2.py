import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK,
         arcade.color.FRENCH_ROSE, arcade.color.GOLDEN_POPPY]

class Cercle():
   def __init__(self, rayon, centre_x, centre_y, color):
       self.rayon = rayon
       self.centre_x = centre_x
       self.centre_y = centre_y
       self.color = color

   def draw(self):
       arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.color)


class MyGame(arcade.Window):
   def __init__(self):
       super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
       self.liste_cercles = []

   def setup(self):
       # remplir la liste avec 20 objets de type Cercle
       for _ in range(20):
           rayon = random.randint(10, 50)
           center_x = random.randint(0 + rayon, SCREEN_WIDTH - rayon)
           center_y = random.randint(0 + rayon, SCREEN_HEIGHT - rayon)
           color = random.choice(COLORS)
           self.liste_cercles.append(Cercle(rayon, center_x, center_y, color))

   def on_draw(self):
       arcade.start_render()

       for cercle in self.liste_cercles:
           cercle.draw()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        for cercle in self.liste_cercles:
            if x > cercle.centre_x - cercle.rayon and x < cercle.centre_x + cercle.rayon and y < cercle.centre_y + cercle.rayon and y > cercle.centre_y - cercle.rayon
                self.liste_cercles.remove(cercle)
    if arcade.MOUSE_BUTTON_LEFT

   if button == arcade.MOUSE_BUTTON_RIGHT:

   cercle.color = random.choice(COLORS)



def main():
   my_game = MyGame()
   my_game.setup()

   arcade.run()


main()



