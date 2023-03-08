import arcade
import random

class MyGame(arcade.Window):
   def __init__(self, width, height, title):
       # Call the parent class's init function
       super().__init__(width, height, title)


def mygame():
    window = MyGame(640, 480, "Drawing Example")
    arcade.start_render()
    for i in range(20):
        arcade.draw_circle_filled(random.randint(50,540), random.randint(50, 380), random.randint(10,50), (random.randint(130,540),random.randint(1,380), random.randint(50,540)))
    arcade.finish_render()
    arcade.run()


mygame()

class Circle:
    arcade.draw_circle_filled(random.randint(50, 540), random.randint(50, 380), random.randint(10, 50),(random.randint(130, 540), random.randint(1, 380), random.randint(50, 540)))


def on_mouse_press(self, x, y, button, modifiers):


