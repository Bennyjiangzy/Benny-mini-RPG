import pygame
from constants import WHITE , SHOP_BUTTON_COLOR


class Menu_monster:
    def __init__(self,window):
        self._window=window
        self._back_button=None


    #show the monster picture
    def create_giaprey(self):
        monster_img = pygame.image.load("assets/img/Giaprey.png").convert_alpha()
        monster_img = pygame.transform.scale(monster_img, (150,150))
        return monster_img

    #show the monster picture
    def create_genprey(self):
        monster_img = pygame.image.load("assets/img/Genprey.png").convert_alpha()
        monster_img = pygame.transform.scale(monster_img, (150,150))
        return monster_img

    #show the monster picture
    def create_ioprey(self):
        monster_img = pygame.image.load("assets/img/Ioprey.png").convert_alpha()
        monster_img = pygame.transform.scale(monster_img, (150,150))
        return monster_img

    #show the monster picture
    def create_tignex(self):
        monster_img = pygame.image.load("assets/img/Tigrex.jpg").convert_alpha()
        monster_img = pygame.transform.scale(monster_img, (150,150))
        return monster_img
    #show the monster picture
    def create_zinogre(self):
        monster_img = pygame.image.load("assets/img/zinogre.jpg").convert_alpha()
        monster_img = pygame.transform.scale(monster_img, (150,150))
        return monster_img

    #show the monster picture
    def create_rathalos(self):
        monster_img = pygame.image.load("assets/img/rathalos.png").convert_alpha()
        monster_img = pygame.transform.scale(monster_img, (150,150))
        return monster_img

    #show the monster picture
    def back_button(self):
        font = pygame.font.SysFont("arial", 24, bold=True)
        text = font.render("back", True, WHITE)
        button_shape= pygame.draw.rect(self._window, SHOP_BUTTON_COLOR, (10,550,50,35))
        self._window.blit(text, (10, 550))
        return button_shape
    
    #display all the monster pictures and the instructions
    def display(self):
        self._window.fill(WHITE)
        
        giaprey_img=self.create_giaprey()
        self._window.blit(giaprey_img, (20,40))

        genprey_img=self.create_genprey()
        self._window.blit(genprey_img, (20,240))

        ioprey_img=self.create_ioprey()
        self._window.blit(ioprey_img, (20,440))

        tignex_img=self.create_tignex()
        self._window.blit(tignex_img, (400,40))

        zinogre_img=self.create_zinogre()
        self._window.blit(zinogre_img, (400,240))

        rathalos_img=self.create_rathalos()
        self._window.blit(rathalos_img, (400,440))

        self.show_text()
        self._back_button=self.back_button()

        pygame.display.flip()


    #show the instructions of each monster
    def show_text(self):
        font=pygame.font.SysFont("arial", 24, bold=True)

        giaprey="Giaprey"
        giaprey2="small dragon will"
        giaprey3="gain ap if have other"
        giaprey4="giaprey"
        giaprey_text = font.render(giaprey, True, (0, 0, 0))
        giaprey_text2 = font.render(giaprey2, True, (0, 0, 0))
        giaprey_text3 = font.render(giaprey3, True, (0, 0, 0))
        giaprey_text4 = font.render(giaprey4, True, (0, 0, 0))
        self._window.blit(giaprey_text, (190, 40))
        self._window.blit(giaprey_text2, (190, 70))
        self._window.blit(giaprey_text3, (190, 95))
        self._window.blit(giaprey_text4, (190, 120))

        genprey ="Genprey"
        genprey2="small dragon will"
        genprey3="heal others ecept"
        genprey4="themself"
        genprey_text = font.render(genprey, True, (0, 0, 0))
        genprey_text2 = font.render(genprey2, True, (0, 0, 0))
        genprey_text3 = font.render(genprey3, True, (0, 0, 0))
        genprey_text4 = font.render(genprey4, True, (0, 0, 0))
        self._window.blit(genprey_text, (190, 240))
        self._window.blit(genprey_text2, (190, 270))
        self._window.blit(genprey_text3, (190, 295))
        self._window.blit(genprey_text4, (190, 320))

        ioprey ="Ioprey"
        ioprey2 ="small dragon have"
        ioprey3 ="high hp but low ap"
        ioprey_text = font.render(ioprey, True, (0, 0, 0))
        ioprey_text2 = font.render(ioprey2, True, (0, 0, 0))
        ioprey_text3 = font.render(ioprey3, True, (0, 0, 0))
        self._window.blit(ioprey_text, (190, 440))
        self._window.blit(ioprey_text2, (190, 470))
        self._window.blit(ioprey_text3, (190, 495))

        tignex ="Tignex"
        tignex2="can use sonic shock wave"
        tignex3="player fear and - 5 stamina "
        tignex4="everny turn"
        tignex_text = font.render(tignex, True, (0, 0, 0))
        tignex_text2 = font.render(tignex2, True, (0, 0, 0))
        tignex_text3 = font.render(tignex3, True, (0, 0, 0))
        tignex_text4 = font.render(tignex4, True, (0, 0, 0))
        self._window.blit(tignex_text, (550, 40))
        self._window.blit(tignex_text2, (550, 65))
        self._window.blit(tignex_text3, (550, 90))
        self._window.blit(tignex_text4, (550, 115))

        zinogre ="Zinogre"
        zinogre2="control lightning can"
        zinogre3="eliminate palyer when hp"
        zinogre4="below 20"
        zinogre_text = font.render(zinogre, True, (0, 0, 0))
        zinogre_text2 = font.render(zinogre2, True, (0, 0, 0))
        zinogre_text3 = font.render(zinogre3, True, (0, 0, 0))
        zinogre_text4 = font.render(zinogre4, True, (0, 0, 0))
        self._window.blit(zinogre_text, (550, 240))
        self._window.blit(zinogre_text2, (550, 265))
        self._window.blit(zinogre_text3, (550, 290))
        self._window.blit(zinogre_text4, (550, 315))




        rathalos ="Rathalos"
        rathalos2 ="powerful dragon can caused"
        rathalos3 = "a burn -10 hp every turn"
        rathalos_text = font.render(rathalos, True, (0, 0, 0))
        rathalos_text2 = font.render(rathalos2, True, (0, 0, 0))
        rathalos_text3 = font.render(rathalos3, True, (0, 0, 0))
        self._window.blit(rathalos_text, (550, 440))
        self._window.blit(rathalos_text2, (550, 465))
        self._window.blit(rathalos_text3, (550, 490))