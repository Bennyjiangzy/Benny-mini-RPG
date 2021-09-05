""" We can define some custom classes based on our main Monster class.

For brevity reasons, I kept them very simple. Yours would be more complicated.
"""
import pygame
from .monster import Monster


class Giaprey(Monster):
    def __init__(self, level=0):
        super().__init__()
        
        self.health = (50 + level)/2
        self.power = 10 + level
 
        self.update()
        
    image_file = "assets/img/Giaprey.png"


class Ioprey(Monster):
    def __init__(self, level=0):
        super().__init__()
        
        self.health = 50 + level
        self.power = (10 + level)/2

        
        self.update()

    image_file = "assets/img/Ioprey.png"


class Genprey(Monster):
    def __init__(self, level=0):
        super().__init__()
        
        self.health = 20+level
        self.power = 0

        
        self.update()
    image_file = "assets/img/Genprey.png"

class Tignex(Monster):
    def __init__(self, level=0):
        super().__init__()
        
        self.health = 50+2*level
        self.power = 25+2*level

        
        self.update()
    image_file = "assets/img/Tigrex.jpg"

class Rathalos(Monster):
    def __init__(self, level=0):
        super().__init__()
        
        self.health = 50+2*level
        self.power = 20+2*level

        
        self.update()
    image_file = "assets/img/rathalos.png"

class Zinogre(Monster):
    def __init__(self, level=0):
        super().__init__()
        
        self.health = 50+2*level
        self.power = 30+2*level

        
        self.update()
    image_file = "assets/img/zinogre.jpg"