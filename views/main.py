import pygame

from constants import HERO_OFFSET, SHOP_BUTTON_OFFSET, WHITE,SHOP_BUTTON_COLOR
from models import Shop,Hero_GS,Hero,Hero_LS


class MainView:
    """The main view

    It is divided in two areas: hero + shop button on the left side,
    and monsters on the right side.
    """

    def __init__(self, window, hero):
        self._window = window
        self._hero = hero
        self._team = None
        self._shop_button =None
        self._Charged_button =None
        self._menu_button=None
        self._Dodge_Slash_button=None
        

    
    def attach_team(self, team):
        self._team = team


    #show the menu button
    def menu_button(self):
        font = pygame.font.SysFont("arial", 24, bold=True)
        text = font.render("MENU", True, WHITE)
        button_shape= pygame.draw.rect(self._window, SHOP_BUTTON_COLOR, (700,550,60,35))
        self._window.blit(text, (700, 550))
        return button_shape
        

    def display(self):
        # Paints the window white
        self._window.fill(WHITE)
        # Show shop button
        self._shop_button = Shop.get_button_image(self._window)
        if type(self._hero) == type(Hero_GS()):
            self._Charged_button= Hero_GS.get_button_Charged_Attacks_image(self._window)
        else:
            self._Dodge_Slash_button=Hero_LS.get_button_Dodge_Slash_image(self._window)
        # Update the Hero sprite and display it
        self._hero.update()
        self._window.blit(self._hero.image, HERO_OFFSET)

        # Update the monsters sprite group and display it
        self._team.update()
        self._team.draw(self._window)

        self._menu_button=self.menu_button()

        #Update the grades when monster dead
        grades=self._hero.update_grades()
        self._window.blit(grades,(0,20))

        #Show the palyer name
        name=self._hero.show_player_name()
        self._window.blit(name,(0,0))



        pygame.display.flip()

    def has_clicked_shop(self, pos):
        # Did we click on the shop button
        if self._shop_button.collidepoint(pos):
            return True

        return False
    
    def has_clicked_Dodge_Slash(self, pos):
        #Did we click on the Dodge_Slash button
        if self._Dodge_Slash_button.collidepoint(pos):
            return True
        
        return False
    
    def has_clicked_charged(self, pos):
        #Did we click on the charged button
        if self._Charged_button.collidepoint(pos):
            return True
        
        return False

    def has_clicked_menu(self, pos):
        #Did we click on the menu button
        if self._menu_button.collidepoint(pos):
            return True
        
        return False


    def get_clicked_monster(self, pos):
        # Did we click on a monster?
        # We use sprite collisions, and return the clicked monster.

        for monster in self._team.sprites():
            if monster.rect.collidepoint(pos):
                return monster

        return None
