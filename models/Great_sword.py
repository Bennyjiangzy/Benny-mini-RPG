import pygame
from pygame.sprite import Sprite
from constants import (HERO_AREA_SIZE, HERO_IMG_OFFSET, HERO_INITIAL_HEALTH,
                       HERO_TXT_OFFSET, WHITE,BLACK_TEXT_COLOR,HERO_CHARGED_ATTACK_BUTTON_COLOR,HERO_CHARGED_ATTACK_BUTTON_OFFSET,HERO_INITIAL_ENERGY)

from .monster_custom import Giaprey,Genprey,Ioprey,Tignex,Zinogre,Rathalos
from .hero import Hero

class Hero_GS(Hero):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.SysFont("arial", 24, bold=True)

        # The left side of the main window is for the hero
        self.image = pygame.Surface(HERO_AREA_SIZE)
        self.image.fill(WHITE)

        hero_img = pygame.image.load("assets/img/greatsword.jpg").convert_alpha()
        hero_img = pygame.transform.scale(hero_img, (200,250))
        self.image.blit(hero_img, HERO_IMG_OFFSET)
        self._charged=False
    
    def attack(self, monster):
        """This is a very simple method that attacks a monster.

        You should improve it - ain't nobody got time for that?
        """

        # if the charged is true, no damage caused by monster in this attack
        # then turn charged attributes to false. 
        if self._charged:
            monster.health -=self._power
            self._power=int(self._power/3)
            self.charged=False
        else:
            monster.health -=self._power
            self.health -= monster.power
    
    @property
    def charged_Attacks(self):
        """Three times power to monster and no damage to the hero """
        self.power = self.power*3
        self.energy -= 20
    
    #create the charged button
    @staticmethod
    def get_button_Charged_Attacks_image(window):

        font = pygame.font.SysFont("arial", 24, bold=True)
        text = font.render("Charged", True, WHITE)
        button_shape= pygame.draw.rect(window, HERO_CHARGED_ATTACK_BUTTON_COLOR, (HERO_CHARGED_ATTACK_BUTTON_OFFSET[0],HERO_CHARGED_ATTACK_BUTTON_OFFSET[1],80,35))
        window.blit(text, (HERO_CHARGED_ATTACK_BUTTON_OFFSET[0], HERO_CHARGED_ATTACK_BUTTON_OFFSET[1]))

        return button_shape