import pygame

from views.menu import Menu
from views import Menu_shop, Menu_monster, Menu_hero

from .base import PygameController


class MenuController(PygameController):
    def __init__(self,window):
        self._window=window
        self._view = Menu(window)
        self._close=False

    def run(self):

        #Show the menu screen
        self._view.display()
        menurunning=True
        while menurunning:
            
            
            
            #get the position
            mouse_position = self._run_loop()
            # if the position variable is esc close the menu loop and back to tne previous page
            if mouse_position == pygame.locals.K_ESCAPE:
                return False
            # if user click X close the loop and turn the attributes close to True Then close the game
            elif mouse_position == False:
                self._close=True
                return False
            # if user click back button close the menu loop back to the previous page
            elif self._view.has_clicked_back(mouse_position):
                return False
            #if player click the hero buttion open the hero view and dispaly it
            elif self._view.has_clicked_Hero(mouse_position):
                Hero_ctrl=Menu_hero(self._window)
                Hero_ctrl.display()

                #call the loop (similar to the base loop) for the hero instruction
                self.menu_loop()
                #player click X then close the game
                if self._close == True:
                    return False
                else:
                    #if player just quit the hero insturction then refresh the menu view
                    self._view.display()

            #if the player click the monster buttion go the monster instruction view
            elif self._view.has_clicked_monster(mouse_position):
                Monster_ctrl=Menu_monster(self._window)
                Monster_ctrl.display()

                #call the loop for the monster instruction view
                self.menu_loop()
                #player click X then close the game
                if self._close == True:
                    return False
                else:
                    #if player just quit the monster insturction then refresh the menu view
                    self._view.display()

            #if player click the shop button go the shop instruction view
            elif self._view.has_clicked_Shop(mouse_position):
                Shop_ctrl=Menu_shop(self._window)
                Shop_ctrl.display()
                #call the loop for the view
                self.menu_loop()
                
                #player click X then close the game
                if self._close == True:
                    return False
                else:
                    #if player just quit the shop insturction then refresh the menu view
                    self._view.display()
            
    
    def menu_loop(self):
        #define the loop
        inside_loop=True
        while inside_loop:
            #call the base loop for the events
            mouse_position = self._run_loop()

            #if player press ESC quit the current view back to the menu
            if mouse_position == pygame.locals.K_ESCAPE:
                inside_loop=False
            #if player click the X close the whole ganme
            elif mouse_position == False:
                self._close=True
                return False
            #if player click the back button, back to the menu
            elif self._view.has_clicked_back(mouse_position):
                return False
