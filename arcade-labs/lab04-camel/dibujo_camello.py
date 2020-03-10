import arcade

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720


def dibujar_fondo():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.ARYLIDE_YELLOW)


def draw_snow_person(x, y):
    """ Draw a snow person """
    arcade.draw_line(x + 10, 235, x + 30, 215, arcade.color.BLACK, 4)
    arcade.draw_line(x - 10, 235, x - 30, 215, arcade.color.BLACK, 4)
    arcade.draw_ellipse_filled(x, 250, 70, 40, arcade.csscolor.SANDY_BROWN) # cuerpo
    arcade.draw_circle_filled(x + 30, 270, 15, arcade.csscolor.SANDY_BROWN) # cabeza
    arcade.draw_circle_filled(x + 25, 280, 2, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(x + 40, 280, 2, arcade.csscolor.BLACK)




def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()

    dibujar_fondo()
    draw_snow_person(on_draw.snow_person1_x, 140)
   # draw_snow_person(450, 180)


   # on_draw.snow_person1_x += 1


# Create a value that our on_draw.snow_person1_x will start at.
on_draw.snow_person1_x = 175


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.BLUE)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()


# Call the main function to get the program started.
main()