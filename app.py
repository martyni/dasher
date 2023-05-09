from sense_hat import SenseHat
from time import sleep


class MyHome(SenseHat):
    my_colour = (250,0,250)
    back_colour = (0 ,100, 0)
    greeting  = "Hi Lya :)"


    def fade(self, steps = 20, delay = 0.01 ):
        r,g,b = self.back_colour
        r_inc = r/steps
        g_inc = g/steps
        b_inc = b/steps
        for s in range(steps):
           sense.clear((
               int(r - r_inc * s), 
               int(g - g_inc * s),
               int(b - b_inc * s)
               ))
           print(int(g - g_inc * s))
           sleep(delay)

class control(object):
    def __init__(self, sense):
        self.sense = sense()
        self.red   = self.sense.my_colour[0]
        self.green = self.sense.my_colour[1]
        self.blue  = self.sense.my_colour[2]
        self.sense.stick.direction_up     = self.green_menu
        self.sense.stick.direction_down   = self.change
        self.sense.stick.direction_left   = self.red_menu
        self.sense.stick.direction_right  = self.blue_menu
        self.sense.stick.direction_middle = self.sense.clear

    def red_menu(self):
        self.sense.clear((255,0,0))

    def green_menu(self):
        self.sense.clear((0,255,0))

    def blue_menu(self):
        self.sense.clear((0,0,255))

    def change(self):
        self.sense.clear((0,0,0))

sense = control(MyHome)
while True:
    pass
