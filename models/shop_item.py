""" This module defines the items available in the shop """

from abc import ABC, abstractmethod

import pygame


class ShopItem(ABC):
    """ Your shop items must define the use method """

    @abstractmethod
    def use(self, hero):
        pass


#item that increase the power point
class Whitestone(ShopItem):
    name = "Whitestone"
    price = 10
    image = pygame.image.load("assets/img/whitestone.jpg")
    image = pygame.transform.scale(image, (50,50))

    def use(self, hero):
        hero.power = int(hero.power * 1.5)

#item cover the medium health point
class Potion(ShopItem):
    name = "Potion"
    price = 5
    image = pygame.image.load("assets/img/potion.png")
    image = pygame.transform.scale(image, (50,50))

    def use(self, hero):
        hero.health = int(hero.health + 50)
        if hero.health > 100:
            hero.health = 100

#item cover the max health point
class MaxPotion(ShopItem):
    name = "Potion G"
    price = 10
    image = pygame.image.load("assets/img/Maxpotion.png")
    image = pygame.transform.scale(image, (60,60))

    def use(self, hero):
        hero.health = 100

#item cover the max energy point
class Dashjuice(ShopItem):
    name = "Dash Juice"
    price = 10
    image = pygame.image.load("assets/img/Dashjuice.png")
    image = pygame.transform.scale(image, (55,55))

    def use(self, hero):
        hero.energy = 100
        
#item cover both health and energy point
class Ancient_Potion(ShopItem):
    name = "Potion G+"
    price = 30
    image = pygame.image.load("assets/img/AncientPotion.png")
    image = pygame.transform.scale(image, (60,60))

    def use(self, hero):
        hero.health = 100
        hero.energy = 100
