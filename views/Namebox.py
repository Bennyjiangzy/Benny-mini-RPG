import pygame
from constants import WHITE

class Namebox:
    def __init__(self,window):
        self._window=window
        self._color=pygame.Color('lightskyblue3')
        self._box= None
        self._font=pygame.font.SysFont("arial", 24, bold=True)
        self._text=""
    

    def create_box(self):
        box=pygame.draw.rect(self._window, self._color,(325, 280, 140, 32))
        return box

    def display(self):
        self._window.fill(WHITE)
        #show the namebox
        self._box=self.create_box()
        #show the instructions
        self.show_text2()

        pygame.display.flip()


    
    def has_clicked_box(self, pos):
        #Did we click on the namebox
        if self._box.collidepoint(pos):
        
            return True
        
        return False

    def change_color_active(self):
        self._color=pygame.Color('dodgerblue2')
        self.display()
    
    def change_color_inactive(self):
        self._color=pygame.Color('lightskyblue3')
        self.display()

    #Show the text player press
    def show_text(self):
        self.display()
        self.show_text2()
        txt_surface = self._font.render(self._text, True, (0,0,0))
        self._window.blit(txt_surface, (330, 285))
        pygame.display.flip()
    
    #Show the instructions
    def show_text2(self):
        font=pygame.font.SysFont("arial", 30, bold=True)
        
        ins1="Click the box Type Your name"
        text1 = font.render(ins1, True, (0,0,0))
        self._window.blit(text1, (220, 220))

        ins2="Press Enther key after type"
        text2 = font.render(ins2, True, (0,0,0))
        self._window.blit(text2, (220, 330))

        ins3="You can press esc to call the menu in any time"
        text3 = font.render(ins3, True, (0,0,0))
        self._window.blit(text3, (150, 45))
    