import pygame
from constants import WHITE , SHOP_BUTTON_COLOR

class Menu_shop:
    def __init__(self,window):
        self._window=window
        self._back_button=None

    #show the back button
    def back_button(self):
        font = pygame.font.SysFont("arial", 24, bold=True)
        text = font.render("back", True, WHITE)
        button_shape= pygame.draw.rect(self._window, SHOP_BUTTON_COLOR, (10,550,50,35))
        self._window.blit(text, (10, 550))
        return button_shape

    #show the item
    def create_Whitestone(self):
        image = pygame.image.load("assets/img/whitestone.jpg")
        image = pygame.transform.scale(image, (50,50))
        return image

    #show the item
    def create_Potion(self):
        image = pygame.image.load("assets/img/potion.png")
        image = pygame.transform.scale(image, (50,50))
        return image

    #show the item
    def create_MaxPotion(self):
        image = pygame.image.load("assets/img/Maxpotion.png")
        image = pygame.transform.scale(image, (60,60))
        return image
    
    #show the item
    def create_Dashjuice(self):
        image = pygame.image.load("assets/img/Dashjuice.png")
        image = pygame.transform.scale(image, (55,55))
        return image
    
    #show the item
    def create_Ancient_Potion(self):
        image = pygame.image.load("assets/img/AncientPotion.png")
        image = pygame.transform.scale(image, (60,60))
        return image
    
    #show all the pictures and the buttons
    def display(self):
        self._window.fill(WHITE)
        
        Whitestone_img=self.create_Whitestone()
        self._window.blit(Whitestone_img, (25,50))

        Potion_img=self.create_Potion()
        self._window.blit(Potion_img, (425,50))

        MaxPotion_img=self.create_MaxPotion()
        self._window.blit(MaxPotion_img, (25,200))

        Dashjuice_img=self.create_Dashjuice()
        self._window.blit(Dashjuice_img, (425,200))

        Ancient_Potion_img=self.create_Ancient_Potion()
        self._window.blit(Ancient_Potion_img, (25,350))
       

        self._back_button=self.back_button()

        self.show_text()

        pygame.display.flip()

    #show all the instructions of each item
    def show_text(self):
        font=pygame.font.SysFont("arial", 20, bold=True)

        Whitestone="Whitestone 10g"
        Whitestone2="increase palyer's ap"
        Whitestone_text = font.render(Whitestone, True, (0, 0, 0))
        Whitestone_text2 = font.render(Whitestone2, True, (0, 0, 0))
        self._window.blit(Whitestone_text, (85, 45))
        self._window.blit(Whitestone_text2, (85, 65))

        Potion ="Potion 5g"
        Potion2="medium restore health"
        Potion_text = font.render(Potion, True, (0, 0, 0))
        Potion_text2 = font.render(Potion2, True, (0, 0, 0))
        self._window.blit(Potion_text, (480, 50))
        self._window.blit(Potion_text2, (480, 70))

        MaxPotion="Potion G 10g"
        MaxPotion2="fully restore health"
        MaxPotion_text = font.render(MaxPotion, True, (0, 0, 0))
        MaxPotion_text2 = font.render(MaxPotion2, True, (0, 0, 0))
        self._window.blit(MaxPotion_text, (85, 195))
        self._window.blit(MaxPotion_text2, (85, 215))

        Dashjuice="Dash Juice 10g"
        Dashjuice2="fully restore stamina"
        Dashjuice_text = font.render(Dashjuice, True, (0, 0, 0))
        Dashjuice_text2 = font.render(Dashjuice2, True, (0, 0, 0))
        self._window.blit(Dashjuice_text, (480, 195))
        self._window.blit(Dashjuice_text2, (480, 215))

        Ancient_Potion="Potion G+ 30g"
        Ancient_Potion2="fully restore health and stamina"
        Ancient_Potion_text = font.render(Ancient_Potion, True, (0, 0, 0))
        Ancient_Potion_text2 = font.render(Ancient_Potion2, True, (0, 0, 0))
        self._window.blit(Ancient_Potion_text, (85, 345))
        self._window.blit(Ancient_Potion_text2, (85, 365))