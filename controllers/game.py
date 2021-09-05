import pygame
import pygame.locals
import requests

from .score_manager import ScoreManager
from models import Score

from constants import WINDOW_SIZE
from models import MonsterTeam, Shop, Hero_GS,Hero_LS,Dashjuice,Ancient_Potion,Whitestone,Potion,MaxPotion
from views import MainView

from models import Giaprey,Genprey,Ioprey,Tignex,Zinogre,Rathalos

from .base import PygameController
from .game_over import GameOverController
from .level_done import LevelDoneController
from .shop import ShopController
from .menu import MenuController
from .Namebox import NameboxController
from .hero_selection import Hero_selection_controller

class GameController(PygameController):
    """The main controller

    This is the main controller. It creates the models, and manages the game
    logic.
    """

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("assets/music/backgroud.flac")
        pygame.mixer.music.set_volume(0.1)

        # The main window
        self._window = pygame.display.set_mode(WINDOW_SIZE)

        # Instantiate the Hero
        self._hero = None

        # Instantiate the Monsters
        self._level = 1
        self._team = MonsterTeam(self._level)


        # Create the shop
        self._shop = Shop()

        # Add items to the shop
        
        for item in (Whitestone(), Dashjuice(),Potion(),MaxPotion(),Ancient_Potion()):
            self._shop.add_item(item)
        
        #Check whether user type their name
        self._Check_name=False
        self._name=None

        #create the Score manager to read the data
        self._score_manager=ScoreManager()

        self._Selection=None

    def run(self):
        """ This method runs the "main loop", and reacts to events (clicks) """

        #change the game name
        pygame.display.set_caption("Monster Hunter Rise")
        running = True

        
        
        
        pygame.mixer.music.play()
        pygame.mixer.music.fadeout(120000)
        while running:
            # Type Player Name
            
            if not self._Check_name:
                
                Name_ctrl=NameboxController(self._window)
                Name_ctrl.run()
                #if user click X in the namebox page close the game
                if Name_ctrl._close == True:
                    return False
                #save the name to the attributes and turn the check name to True
                self._Check_name=Name_ctrl._Checked_name
                self._name=Name_ctrl._name
            
            # if the user do not select the hero do the following
            if not self._Selection:
                #call the heroselect manager
                Heroselect_ctrl=Hero_selection_controller(self._window)
                #run the manager
                Heroselect_ctrl.run()
                #if user click the X in the manager close the game
                if Heroselect_ctrl._close == True:
                    return False
                #after user select the hero, trun the boolean to True
                self._Selection=True

                #if user select Great Sword which is 0 in the manager do the following
                if Heroselect_ctrl._selection == 0:
                    #call the greate sword 
                    self._hero=Hero_GS()
                    #assign the player name
                    self._hero._name=self._name
                    # Create the main view
                    self._view = MainView(self._window, self._hero)

                    # "Attach" the team to the view
                    self._view.attach_team(self._team)
                

                #if user select the long Sword which is 1 in the manger do the following
                elif Heroselect_ctrl._selection == 1:
                    #call the long sword
                    self._hero=Hero_LS()
                    #assign the player name
                    self._hero._name=self._name
                    # Create the main view
                    self._view = MainView(self._window, self._hero)

                    # "Attach" the team to the view
                    self._view.attach_team(self._team)
            

            # Display the view
            self._view.display()

            # Iheritance FTW - run a Pygame loop until the mouse is clicked
            mouse_position = self._run_loop()
            if mouse_position == pygame.locals.K_ESCAPE:
                #if the event.key is esc show the menu page
                menu_ctrl = MenuController(self._window)
                menu_ctrl.run()
                #if user click X in menu page close the whole game
                if menu_ctrl._close == True:
                    running = False


            # Click on the close button
            if mouse_position is False:
                running = False
                continue

            #prevent bugs if the event.key is esc not a position
            if mouse_position!=pygame.locals.K_ESCAPE:
            # Click on the shop button
                if self._view.has_clicked_shop(mouse_position):
                    # Let's run the shop controller
                    shop_ctrl = ShopController(self._shop)
                    # Run its loop
                    shop_ctrl.run(self._window, self._hero)
                    if shop_ctrl._close == True:
                        running = False
                if type(self._hero) == type(Hero_GS()):
                    #Click on the charged button
                    if self._view.has_clicked_charged(mouse_position):
                        #if hero energy is not 0 then charge the attack
                        if self._hero.energy>0:
                            self._hero.charged_Attacks
                            self._hero.charged=True
                else:
                    if self._view.has_clicked_Dodge_Slash(mouse_position):
                        #if hero energy is not 0 then charge the attack
                        if self._hero.energy>0:
                            self._hero.Dodge_Slash(self._team)
                            self._team.next_turn(self._hero,self._level)

                #Click the menu button
                if self._view.has_clicked_menu(mouse_position):
                    menu_ctrl = MenuController(self._window)
                    menu_ctrl.run()
                    if menu_ctrl._close == True:
                        running = False

            # Did we click on a monster?
                monster = self._view.get_clicked_monster(mouse_position)
                if monster is not None:
                    if not monster.is_dead:
                        # YAAAAA
                        self._hero.attack(monster)
                        # Add grades when different monster dead
                        self._hero.add_grades(monster)
                        # add coins after a monster dead
                        self._hero.add_coins_energy(monster)
                        # monster use their skills after attack the monster
                        self._team.next_turn(self._hero,self._level)
                        # Update the display (the monster might be dead)
                        self._view.display()

            # Oh noes, me so sad
            if self._hero.is_dead:
                # This shows the game over screen
                game_over_ctrl = GameOverController()
                game_over_ctrl.run(self._window)
                # We are dead - stop the loop
                running = False
                continue

            # Are all monsters dead now?
            if self._team.all_monsters_dead():
                # Yay. Let's show a nice message
                level_done_ctrl = LevelDoneController(self._level)
                level_done_ctrl.run(self._window)

                # We move to the next level
                self._level = self._level + 1

                # Recreate and attach a new team of monsters
                self._team = MonsterTeam(self._level)
                self._view.attach_team(self._team)

        
        #get the player data from the website
        try:
            req = requests.get("http://localhost:5000/api/scores")
            data=req.json()
        except:
            print("cannot access the web")
        #check the current player exist on the rank website or not
        try:
            current_player_data=None

            for players in data:
                if self._hero._name == players['name']:
                    current_player_data=players

            #if exist use post method
            if current_player_data != None:
                if current_player_data['score'] < self._hero._grades:
                    
                    playerid=current_player_data['id']
                    requests.post("http://localhost:5000/api/score/%s"%(playerid), json={"score":self._hero._grades})

            #if not exist use put method
            if current_player_data == None:
                requests.put('http://localhost:5000/api/score', json={"name":self._hero._name, "score":self._hero._grades})
        except:
            print("cannot access the web")
                
        
        