import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK,
         arcade.color.FRENCH_ROSE, arcade.color.GOLDEN_POPPY]

class Ball():
   def __init__(self, rayon, centre_x, centre_y, color):
       self.rayon = rayon
       self.centre_x = centre_x
       self.centre_y = centre_y
       self.color = color
       self.cercle_change_x = 3  # Nombre d'unité pour le déplacement sur l'axe des X
       self.cercle_change_y = 3  # Nombre d'unité pour le déplacement sur l'axe des Y
   def draw(self):
       arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.color)

   def on_update(self):

        if self.centre_x < self.rayon:
           self.cercle_change_x *= -1
        if self.centre_x > SCREEN_WIDTH - self.rayon:
           self.cercle_change_x *= -1
        if self.centre_y < self.rayon:
           self.cercle_change_y *= -1
        if self.centre_y > SCREEN_HEIGHT - self.rayon:
           self.cercle_change_y *= -1

        self.centre_x += self.cercle_change_x
        self.centre_y += self.cercle_change_y




class MyGame(arcade.Window):
   def __init__(self):
       super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
       self.liste_cercles = []



   def on_draw(self):
       arcade.start_render()

       for cercle in self.liste_cercles:
           cercle.draw()
           cercle.on_update()

   def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
       for cercle in self.liste_cercles:
           if x > cercle.centre_x - cercle.rayon and x < cercle.centre_x + cercle.rayon and y < cercle.centre_y + cercle.rayon and y > cercle.centre_y - cercle.rayon:

               if button == arcade.MOUSE_BUTTON_LEFT:
                   rayon = random.randint(10, 50)
                   center_x = random.randint(0 + rayon, SCREEN_WIDTH - rayon)
                   center_y = random.randint(0 + rayon, SCREEN_HEIGHT - rayon)
                   color = random.choice(COLORS)
                   self.liste_cercles.append(Ball(rayon, center_x, center_y, color))

           #if button == arcade.MOUSE_BUTTON_RIGHT:
                   #rayon = random.randint(10, 50)
                   #center_x = random.randint(0 + rayon, SCREEN_WIDTH - rayon)
                   #center_y = random.randint(0 + rayon, SCREEN_HEIGHT - rayon)
                   #color = random.choice(COLORS)
                  # self.liste_cercles.append(Cercle(rayon, center_x, center_y, color))

    #def on_update(self):


def main():
    my_game = MyGame()
    arcade.run()

main()