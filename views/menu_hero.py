import pygame
from constants import WHITE , SHOP_BUTTON_COLOR


class Menu_hero:
    def __init__(self,window):
        self._window=window
        self._back_button=None

    #show picture of GS  
    def create_great_sword(self):
        hero_img = pygame.image.load("assets/img/greatsword.jpg").convert_alpha()
        hero_img = pygame.transform.scale(hero_img, (200,250))
        return hero_img

    #show picture of LS
    def create_long_sword(self):
        hero_img = pygame.image.load("assets/img/longsword.jpg").convert_alpha()
        hero_img = pygame.transform.scale(hero_img, (200,250))
        return hero_img

    #show the back button in the menu
    def back_button(self):
        font = pygame.font.SysFont("arial", 24, bold=True)
        text = font.render("back", True, WHITE)
        button_shape= pygame.draw.rect(self._window, SHOP_BUTTON_COLOR, (10,550,50,35))
        self._window.blit(text, (10, 550))
        return button_shape
    
    #display all the pictures and texts
    def display(self):
        self._window.fill(WHITE)
        #Show the back button

        great_sword_img=self.create_great_sword()
        self._window.blit(great_sword_img, (0,40))

        long_sword_img=self.create_long_sword()
        self._window.blit(long_sword_img, (40,320))

        self._back_button=self.back_button()

        self.show_text()

        pygame.display.flip()

    #show the instruction of the both hero
    def show_text(self):
        font=pygame.font.SysFont("arial", 30, bold=True)
        ins1="Great Sword can charged attack the monsters"
        text1 = font.render(ins1, True, (179, 0, 0))
        self._window.blit(text1, (220, 50))

        ins3 ="No damage caused during that attack"
        text3 = font.render(ins3, True, (179, 0, 0))
        self._window.blit(text3, (220, 75))

        ins2="Long Sword can use dodge slash"
        text2 = font.render(ins2, True, (51, 102, 255))
        self._window.blit(text2, (220, 350))

        ins4="Dodge slash will damage all the monsters"
        text4 = font.render(ins4, True, (51, 102, 255))
        self._window.blit(text4, (220, 375))