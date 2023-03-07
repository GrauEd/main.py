
class MyGame(arcade.Window):
   def __init__(self, width, height, title):
       # Call the parent class's init function
       super().__init__(width, height, title)


def main():
    window = MyGame(640, 480, "Drawing Example")
    arcade.start_render()
    for i in range(20):
        arcade.draw_circle_filled(random.randint(50,540), random.randint(50, 380), random.randint(10,50), (random.randint(130,540),random.randint(1,380), random.randint(50,540)))
    arcade.run()

main()

COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK,
arcade.color.FRENCH_ROSE, arcade.color.GOLDEN_POPPY]

class Ball:
    rayon = random.randint(10, 30)
    center_x = random.randint(100,150)
    center_y = random.randint(100,150)
    color = random.choice(COLORS)
    cercle = Cercle(rayon, center_x, center_y, color)
    self.liste_cercles.append(cercle)


