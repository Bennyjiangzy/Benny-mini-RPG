import pygame
from pygame.sprite import Sprite

from constants import (HERO_AREA_SIZE, HERO_IMG_OFFSET, HERO_INITIAL_HEALTH,
                       HERO_TXT_OFFSET, WHITE,BLACK_TEXT_COLOR,HERO_CHARGED_ATTACK_BUTTON_COLOR,HERO_CHARGED_ATTACK_BUTTON_OFFSET,HERO_INITIAL_ENERGY)

from .monster_custom import Giaprey,Genprey,Ioprey,Tignex,Zinogre,Rathalos

class Hero(Sprite):
    """The Hero class defines the hero of our game.

    We make it inherit from pygame.sprite.Sprite, so that
    it is easier to manage.
    """

    def __init__(self):
        super().__init__()

        self.font = pygame.font.SysFont("arial", 24, bold=True)

        # The left side of the main window is for the hero
        self.image = pygame.Surface(HERO_AREA_SIZE)
        self.image.fill(WHITE)

        hero_img = pygame.image.load("assets/img/greatsword.jpg").convert_alpha()
        hero_img = pygame.transform.scale(hero_img, (200,250))
        self.image.blit(hero_img, HERO_IMG_OFFSET)


        self._health = HERO_INITIAL_HEALTH
        self._energy = HERO_INITIAL_ENERGY
        self._power = 50
        self._coins = 20
        self._grades=0
        self._name=None
        self._burning=False
        self._fear=False
        self._nobuff_health=(0,0,0)
        self._nobuff_energy=(0,0,0)

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, val):
        if val <= 0:
            val = 0

        self._health = int(val)

    @property
    def energy(self):
        return self._energy
    
    @energy.setter
    def energy(self, val):
        if val <= 0:
            val = 0

        self._energy = int(val)

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, val):
        self._power = int(val)

    @property
    def coins(self):
        return self._coins

    @coins.setter
    def coins(self, val):
        if val < 0:
            raise NotImplementedError("We don't do credit, sorry!")
        self._coins = int(val)

    @property
    def charged(self):
        return self._charged

    @charged.setter
    def charged(self,val):
        self._charged = bool(val)


    @property
    def is_dead(self):
        return self._health <= 0

    def update(self):
        """This method defines what happens when the sprite should be updated.

        We will paint over the details (health, attack) and blit the values again.
        """

        # Paint white over text
        white_rect = pygame.Surface((HERO_AREA_SIZE[0], 50))
        white_rect.fill(WHITE)
        self.image.blit(white_rect, HERO_TXT_OFFSET)
        
        nobuff_color=(0,0,0)
        
        #if the palyer have a burning debuff then turn the health text to the orginge
        if self._burning == True:
            debuff_burining_color=(255,102,0)
            self._nobuff_health=debuff_burining_color
        #if no burinning debuff then turn to normal
        else:
            self._nobuff_health=nobuff_color

        #if the player have a fear debuff then turn the stamina text to the purple
        if self._fear == True:
            debuff_fear_color=(102, 0, 255)
            self._nobuff_energy=debuff_fear_color
        #if no fear debuff then trun to normal
        else:
            self._nobuff_energy=nobuff_color

        #health text
        text = self.font.render(
            f"HEALTH: {self._health}",
            True,
            self._nobuff_health,
        )

        #Stamina text
        text2= self.font.render(
            f"STAMINA: {self._energy}",
            True,
            self._nobuff_energy,
        )
        
        #Attck text
        text3 = self.font.render(
            f" | ATTACK: {self._power} | {self.coins}g",
            True,
            (0, 0, 0),
        )

        #put the text to the hero window
        self.image.blit(text, (10 + HERO_TXT_OFFSET[0], HERO_TXT_OFFSET[1]))
        self.image.blit(text2, (10 + HERO_TXT_OFFSET[0], HERO_TXT_OFFSET[1]+20))
        self.image.blit(text3, (133 + HERO_TXT_OFFSET[0], HERO_TXT_OFFSET[1]))
        

    def attack(self, monster):
        """This is a very simple method that attacks a monster.

        You should improve it - ain't nobody got time for that?
        """
        monster.health -=self._power
        self.health -= monster.power


    # add grades if a monster is dead.
    def add_grades(self,monster):
        if type(monster) == Giaprey and monster.is_dead:
            self._grades+=1
        elif type(monster) == Genprey and monster.is_dead:
            self._grades+=2
        elif type(monster) == Ioprey and monster.is_dead:
            self._grades+=2
        elif type(monster) == Rathalos and monster.is_dead:
            self._grades+=10
        elif type(monster) == Tignex and monster.is_dead:
            self._grades+=20
        elif type(monster) == Zinogre and monster.is_dead:
            self._grades+=30

    #update the grades
    def update_grades(self):
        fontsize=pygame.font.SysFont("arial", 24, bold=True)
        grades=fontsize.render(
            f"Score:{self._grades}",
            True,
            (0,0,0),
        )
        return grades

    #create the player name string
    def show_player_name(self):
        fontsize=pygame.font.SysFont("arial", 24, bold=True)
        name=fontsize.render(f"Player:{self._name}",True,(0,0,0))
        return name

    # add coins and energy if a monster is dead
    def add_coins_energy(self,monster):
        if type(monster) == Giaprey and monster.is_dead:
            self._coins+=1
            self.energy+=5
        elif type(monster) == Genprey and monster.is_dead:
            self._coins+=2
            self.energy+=5
        elif type(monster) == Ioprey and monster.is_dead:
            self._coins+=2
            self.energy+=5
        elif type(monster) == Rathalos and monster.is_dead:
            self._coins+=30
            self.energy+=20
        elif type(monster) == Tignex and monster.is_dead:
            self._coins+=40
            self.energy+=40
        elif type(monster) == Zinogre and monster.is_dead:
            self._coins+=50
            self.energy+=50
        
        if self.energy>100:
            self.energy=100