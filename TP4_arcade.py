import arcade
import random

#la grandeur de l'ecran
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#liste de couleurs qui est appelé pur les formes
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

class Rectangle():
    def __init__(self, center_x, center_y, width, height, color):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.color = color
        self.rectangle_change_x = 3
        self.rectangle_change_y = 3


    def draw(self):
       arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)


    def on_update(self):
        if self.center_x < self.width and self.center_x < self.height:
            self.rectangle_change_x *= -1
        if self.center_x > SCREEN_WIDTH - self.width:
            self.rectangle_change_x *= -1
        if self.center_y < self.width and self.center_y < self.height:
            self.rectangle_change_y *= -1
        if self.center_y > SCREEN_HEIGHT - self.height:
            self.rectangle_change_y *= -1
        self.center_x += self.rectangle_change_x
        self.center_y += self.rectangle_change_y




class MyGame(arcade.Window):
   def __init__(self):
       super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
       self.liste_cercles = []
       self.liste_rectangles = []



   def on_update(self, delta_time: float):
       arcade.start_render()
       for cercle in self.liste_cercles:
           cercle.on_update()
       for rect in self.liste_rectangles:
           rect.on_update()



   def on_draw(self):
       arcade.start_render()

       for cercle in self.liste_cercles:
           cercle.draw()

       for rect in self.liste_rectangles:
           rect.draw()



   def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
           rayon = random.randint(10, 50)
           center_x = x
           center_y = y
           color = random.choice(COLORS)
           self.liste_cercles.append(Ball(rayon, center_x, center_y, color))

        if button == arcade.MOUSE_BUTTON_RIGHT:
            height = random.randint(10,50)
            width = random.randint(1,50)
            center_x = x
            center_y = y
            color = random.choice(COLORS)
            self.liste_rectangles.append(Rectangle(center_x, center_y, width, height, color))



def main():
    my_game = MyGame()
    arcade.run()

main()