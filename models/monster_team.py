import pygame
from pygame.sprite import Group

from constants import (MONSTER_SPACING_X, MONSTER_SPACING_Y, MONSTERS_OFFSET_X,
                       MONSTERS_OFFSET_Y)

from .monster_custom import Giaprey,Genprey,Ioprey,Tignex,Zinogre,Rathalos


class MonsterTeam(Group):
    """This is a group of monsters. It inherits from pygame.sprite.Group.

    All monsters inside this group are sprites too.
    """

    def __init__(self, level=0):
        super().__init__()

        # Let's pretend we have some logic to create the monsters
        if level %5 != 0:
            if level >15:
                level_adjust=level-10
            else:
                level_adjust=level
            giaprey = [Giaprey(level) for _ in range(level_adjust % 3)]
            genprey = [Genprey(level)] if level_adjust % 3 == 0 else []
            ioprey = [Ioprey(level) for _ in range(level_adjust // 3)]
            self.add(giaprey)
            self.add(genprey)
            self.add(ioprey)
        #if level is 5,10,15 add the boss
        else:
            #if level is below 10 add rathalos
            if level <=10:
                rathalos=[Rathalos(level)]
                tignex = []
                zinogre =[]
            #if level is below 20 but greater than 10 add tignex
            elif level <= 20:
                tignex = [Tignex(level)]
                rathalos=[]
                zinogre =[]
            #if level is greater than 20 add  zinogre
            else:
                zinogre =[Zinogre(level)]
                rathalos=[]
                tignex = []
            self.add(tignex)
            self.add(zinogre)
            self.add(rathalos)

        

    def all_monsters_dead(self):
        """ We check each monster - if one is not dead, not all monsters are dead """
        for monster in self.sprites():
            if not monster.is_dead:
                return False
        return True

    def update(self):
        """Update the sprite group.

        We display the monsters two by two. We can use modulo (%) and integer division (//)
        to easily compute the coordinates.

        Who thought math classes would come in useful one day?
        """
        super().update()

        for idx, sprite in enumerate(self.sprites()):
            line = idx // 2
            col = idx % 2
            sprite.rect.x = MONSTERS_OFFSET_X + col * MONSTER_SPACING_X
            sprite.rect.y = MONSTERS_OFFSET_Y + line * MONSTER_SPACING_Y

    def next_turn(self,hero,level):
        Gouprofmonsters=self.sprites()
        #count numbers of Giaprey
        if level %5 != 0:
            numberofGiaprey=0
            for monster in Gouprofmonsters:
                if not monster.is_dead and type(monster) == Giaprey:
                    numberofGiaprey+=1
                    
            #increase Giaprey ap based on their numbers and Genprey heal other monster excpet Genprey
            for monster in Gouprofmonsters:
                if type(monster) == Giaprey:
                    if numberofGiaprey != 1:
                        monster.power+=numberofGiaprey
                elif type(monster) == Genprey and not monster.is_dead:
                    for healingMonster in Gouprofmonsters:
                        if type(healingMonster) != Genprey and not healingMonster.is_dead:
                            healingMonster.health+=healingMonster.health*0.1
        else:
            #if the level is 5 10 15 then there will be a boss and do the following
            for monster in Gouprofmonsters:
                #if the monster is Rathalos, give the player burinning debuff
                #if monster is dead, the buff disappear
                if type(monster) == Rathalos:
                    if monster.is_dead:
                        hero._burning=False
                        break
                    #if there is a burning debuff , deduct the player's health points
                    if hero._burning:
                        hero.health-=5
                    else:
                        hero._burning = True
                #if the monster is Tignex, give them a fear debuff
                #if the mosnter is dead, debuff disappear
                elif type(monster) == Tignex:
                    if monster.is_dead:
                        hero._fear=False
                        break
                    #if there is a fear debuff, then deduct the palyer's stamina
                    if hero._fear:
                        hero.energy-=5
                    else:
                        hero._fear=True
                #if the mosnter is Zinogre, the player will dead if their health point is below 20
                elif type(monster) == Zinogre:
                    if monster.is_dead:
                        break
                    if hero.health<20:
                        hero.health=0
        

