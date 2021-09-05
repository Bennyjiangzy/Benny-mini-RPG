import pygame
from pygame.sprite import Sprite
from constants import (HERO_AREA_SIZE, HERO_IMG_OFFSET, HERO_INITIAL_HEALTH,
                       HERO_TXT_OFFSET, WHITE,BLACK_TEXT_COLOR,HERO_CHARGED_ATTACK_BUTTON_COLOR,HERO_CHARGED_ATTACK_BUTTON_OFFSET,HERO_INITIAL_ENERGY)

from .monster_custom import Giaprey,Genprey,Ioprey,Tignex,Zinogre,Rathalos
from .hero import Hero

class Hero_LS(Hero):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.SysFont("arial", 24, bold=True)

        # The left side of the main window is for the hero
        self.image = pygame.Surface(HERO_AREA_SIZE)
        self.image.fill(WHITE)

        hero_img = pygame.image.load("assets/img/longsword.jpg").convert_alpha()
        hero_img = pygame.transform.scale(hero_img, (200,250))
        self.image.blit(hero_img, HERO_IMG_OFFSET)

    
    def Dodge_Slash(self,monster_team):
        """Three times power to monster and no damage to the hero """
        for monster in monster_team.sprites():
            if not monster.is_dead:
                monster.health-=self._power*0.7

        self.energy -= 20
    
    #create the charged button
    @staticmethod
    def get_button_Dodge_Slash_image(window):

        font = pygame.font.SysFont("arial", 24, bold=True)
        text = font.render("Dodge Slash", True, WHITE)
        button_shape= pygame.draw.rect(window, (0,0,255), (HERO_CHARGED_ATTACK_BUTTON_OFFSET[0],HERO_CHARGED_ATTACK_BUTTON_OFFSET[1],120,35))
        window.blit(text, (10,550))

        return button_shape
