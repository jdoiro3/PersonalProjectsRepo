from graphics import *
from graphics import _root
from math import cos, sin, tan, sqrt, pow, radians
import numpy as np
import time

_gravity = 9.81


class Projectile(Circle):

    def __init__(self, v, theta, x=0.0, y=0.0):
        self.initial_v = v
        self.v = v
        self.v_x = self.v * cos(radians(theta)) # constant
        self.v_y = self.v * sin(radians(theta)) # changes with time
        self.theta = theta
        self.x = x
        self.y = y
        self.max_height = (pow(self.initial_v,2) * pow(sin(radians(theta)),2))/(2*_gravity)
        self.range = (pow(self.initial_v,2) * (sin(radians(2*theta)))) / _gravity
        Circle.__init__(self, Point(self.x, self.y), 20)

    def __str__(self):
        return "Projectile instance located at ({self.x},{self.pos_y})".format(self=self)

    def update_velocity(self, time):
        self.v_y = self.v_y - (_gravity * time)
        self.v = sqrt(pow(self.v_x,2)+pow(self.v_y,2))

    def _update_position(self, time):
        self.x = self.initial_v * time * cos(radians(self.theta))
        self.y = (self.initial_v * time * sin(radians(self.theta))) - (.5 * _gravity * pow(time,2))

    def move(self, time, dt):

        self._update_position(time-dt)
        x_before = self.x
        y_before = self.y
        self._update_position(time)

        dx = self.x - x_before
        dy = self.y - y_before

        canvas = self.canvas
        if canvas and not canvas.isClosed():
            trans = canvas.trans
            if trans:
                x = dx/ trans.xscale 
                y = -dy / trans.yscale
            else:
                x = dx
                y = dy
            self.canvas.move(self.id, x, y)
            if canvas.autoflush:
                _root.update()
                


def main(v, angle):
    p = Projectile(v, angle)
    win = GraphWin('Projectile', 5000, 1000)
    win.setCoords(0, 0, 10000, 10000)

    p.draw(win)
    p.setFill("black")

    time.sleep(3)

    t = 0.0
    dt = .1
    while (p.x <= p.range and p.x <= 10000):
        p.move(t, dt)
        t += dt
        time.sleep(.01)

    win.close()

main(420,75)