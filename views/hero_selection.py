import pygame
from constants import WHITE, HERO_AREA_SIZE,HERO_IMG_OFFSET

class Hero_selection:
    def __init__(self,window):
        self._window=window
        self._button_GS=None
        self._button_LS=None
        

       
    #add the great sword picture
    def create_great_sword(self):
        hero_img = pygame.image.load("assets/img/greatsword.jpg").convert_alpha()
        hero_img = pygame.transform.scale(hero_img, (200,250))
        return hero_img

    #add the long sword picture
    def create_long_sword(self):
        hero_img = pygame.image.load("assets/img/longsword.jpg").convert_alpha()
        hero_img = pygame.transform.scale(hero_img, (200,250))
        return hero_img

    #add the great sword button
    def GS_button(self):
        font = pygame.font.SysFont("arial", 24, bold=True)
        text = font.render("Great Sword", True, WHITE)
        button_shape= pygame.draw.rect(self._window, (255,0,0), (215, 400,120,35))
        self._window.blit(text, (215, 400))
        return button_shape

     #add the long sword button
    def LS_button(self):
        font = pygame.font.SysFont("arial", 24, bold=True)
        text = font.render("Long Sword", True, WHITE)
        button_shape= pygame.draw.rect(self._window, (0,0,255), (490, 398,120,35))
        self._window.blit(text, (490, 400))
        return button_shape

    #show the text for instruction
    def show_text(self):
        font=pygame.font.SysFont("arial", 28, bold=True)

        ins="Choose your Weapon"
        text = font.render(ins, True, (0, 0, 0))
        self._window.blit(text, (290, 45))

    #display the text and the picture
    def display(self):
        self._window.fill(WHITE)
        #show the namebox
        great_sword_img=self.create_great_sword()
        self._window.blit(great_sword_img, (150,150))
        #show the instructions
        long_sword_img=self.create_long_sword()
        self._window.blit(long_sword_img, (490,180))

        self._button_GS=self.GS_button()
        self._button_LS=self.LS_button()

        self.show_text()
        pygame.display.flip()


    
    def has_clicked_great_sword(self, pos):
        #Did we click on the namebox
        if self._button_GS.collidepoint(pos):
            
            return True
        
        return False

    def has_clicked_long_sword(self, pos):
        #Did we click on the namebox
        if self._button_LS.collidepoint(pos):
            
            return True
        
        return False
