import pygame

from views.Namebox import Namebox
from .menu import MenuController

from .base import PygameController


class NameboxController(PygameController):
    def __init__(self,window):
        self._window=window
        self._view = Namebox(window)
        self._active=False
        self._Checked_name=True
        self._name=None
        self._close=False

    def run(self):
        #Show the namebox page
        self._view.display()
        naming=True
        while naming:

            #get the event
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    naming= False
                    self._close=True
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the namebox.
                    if self._view.has_clicked_box(event.pos):
                        # Toggle the active variable.
                        self._active = True
                    else:
                        self._active = False

                    # Change the current color of the input box.
                    if self._active:
                        
                        self._view.change_color_active()
                        self._view.show_text()
                    else:

                        self._view.change_color_inactive()
                        self._view.show_text()

                #get the key events
                if event.type == pygame.KEYDOWN:
                    #if the namebox is active means user click the nambebox and do the following functions
                    if self._active:

                        #close the naming loop if press enter and save the name
                        if event.key == pygame.K_RETURN:
                            self._name=self._view._text
                            self._view._text = ''
                            naming=False

                        # delete one letter after press backspace
                        elif event.key == pygame.K_BACKSPACE:
                            self._view._text = self._view._text[:-1]
                            self._view.show_text()

                        # show what they are type and limit the name length
                        else:
                            if len(self._view._text)<=8:
                                self._view._text += event.unicode
                            self._view.show_text()

                    #If user press esc and the box is not active, show the menu page
                    if self._active == False and event.key == pygame.locals.K_ESCAPE:

                        menu_ctrl = MenuController(self._window)
                        menu_ctrl.run()
                        #If user click X in the menu page close the name loop and close the game.
                        if menu_ctrl._close == True:
                            self._close = True
                            naming=False
                        #if the menu loop closed but user not click the X(User click back button or just press another esc in the menu page)
                        # back to the namebox page and re-display this page in the end.
                        else:
                            self._view.display()
