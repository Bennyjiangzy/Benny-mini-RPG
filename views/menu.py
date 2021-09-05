import pygame
from constants import WHITE , SHOP_BUTTON_COLOR

class Menu:
    def __init__(self,window):
        self._window=window
        self._Hero_button=None
        self._monster_button=None
        self._Shop_button=None
        self._back_button=None
        self.font=pygame.font.SysFont("arial", 24, bold=True)

    #show the hero button
    def Hero_button(self):
        text = self.font.render("Hero", True, WHITE)
        button_shape= pygame.draw.rect(self._window, (0,0,0), (360,180,80,35))
        self._window.blit(text, (360, 180))
        return button_shape

    #show the monster button
    def monster_button(self):
        text = self.font.render("Monster", True, WHITE)
        button_shape= pygame.draw.rect(self._window, (0,0,0), (360,280,80,35))
        self._window.blit(text, (360, 280))
        return button_shape

    #show the shop button
    def Shop_button(self):
        text = self.font.render("Shop", True, WHITE)
        button_shape= pygame.draw.rect(self._window, (0,0,0), (360, 380,80,35))
        self._window.blit(text, (360, 380))
        return button_shape

    #show the back button
    def back_button(self):
        text = self.font.render("back", True, WHITE)
        button_shape= pygame.draw.rect(self._window, SHOP_BUTTON_COLOR, (10,550,50,35))
        self._window.blit(text, (10, 550))
        return button_shape

    #show the instruction text
    def show_text(self):
        font=pygame.font.SysFont("arial", 28, bold=True)

        ins="You can press esc to exit the menu in any time"
        text = font.render(ins, True, (0, 0, 0))
        self._window.blit(text, (160, 45))

    #display all the instruction and the buttons
    def display(self):
        self._window.fill(WHITE)
        #Show the back button
        self._back_button=self.back_button()

        #The rest of the button do not have functions yet

        #Show the Hero button
        self._Hero_button=self.Hero_button()

        #Show the Shop button
        self._Shop_button=self.Shop_button()

        #Show the monster button
        self._monster_button=self.monster_button()

        self.show_text()

        pygame.display.flip()



    def has_clicked_Hero(self, pos):
        #Did we click on the Hero button
        
        if self._Hero_button.collidepoint(pos):
            return True
        
        return False

    def has_clicked_monster(self, pos):
        #Did we click on the monster button
        
        if self._monster_button.collidepoint(pos):
            return True
        
        return False

    def has_clicked_Shop(self, pos):
        #Did we click on the Shop button
        
        if self._Shop_button.collidepoint(pos):
            return True
        
        return False

    def has_clicked_back(self, pos):
        #Did we click on the back button
        
        if self._back_button.collidepoint(pos):
            return True
        
        return False

        