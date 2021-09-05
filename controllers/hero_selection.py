import pygame

from views import Hero_selection
from .menu import MenuController
from .base import PygameController

class Hero_selection_controller(PygameController):
    def __init__(self,window):
        #pass the window
        self._window=window
        #show the view
        self._view = Hero_selection(window)
        #attributes check whether the palyer close the window
        self._close=False
        #attributes save the selection of the player 1 is long sword, 0 is great sword
        self._selection=None


    def run(self):

        #show the view
        self._view.display()
        selectionrunning=True
        while selectionrunning:
            #run the loop get the events
            mouse_position = self._run_loop()

            #if the event is esc call the menu view
            if mouse_position == pygame.locals.K_ESCAPE:
                menu_ctrl = MenuController(self._window)
                menu_ctrl.run()

                #if player close the menu window, break the selection loop and close the game
                if menu_ctrl._close == True:
                            self._close = True
                            return False
                else:
                    #refresh the view after the player close the menu view
                    self._view.display()
            #if player close the game in the current view then close the game
            elif mouse_position == False:
                self._close=True
                return False
            #if player click great sword pass 0 to the attributes and break the selection loop
            elif self._view.has_clicked_great_sword(mouse_position):
                self._selection=0
                return False
                #if player click long sword pass 1 to the attributes and break the selection loop
            elif self._view.has_clicked_long_sword(mouse_position):
                self._selection=1
                return False

                
 