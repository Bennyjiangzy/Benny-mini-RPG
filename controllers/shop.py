import pygame

from views.shop import ShopView
from .menu import MenuController
from models import Whitestone
from .base import PygameController


class ShopController(PygameController):
    def __init__(self, shop):
        self._shop = shop
        # We will have access to the shop in the view
        self._view = ShopView(shop)
        self._close=False

    def run(self, window, hero):
        """ Does anyone read my docstrings? I wonder. """

        self._view.display(window)
        shoprunning=True
        while shoprunning:

            # Run the loop (inheritance)
            mouse_position = self._run_loop()
            # if user press ESC in the shop page show the menu page
            if mouse_position==pygame.locals.K_ESCAPE:
                menu_ctrl = MenuController(window)
                menu_ctrl.run()
                # if user click X in the menu page stop the current loop and close the game
                if menu_ctrl._close == True:
                    self._close = True
                    shoprunning=False
                # if user just click the back buttion or press ESC in the menu page, show the shop page again.
                else:
                    self._view.display(window)
            # if user click X in the shop page stop the loop and close the game
            elif mouse_position == False:
                self._close=True
                shoprunning=False

            else:
                # We can determine which item was bought based on the mouse click
                item_bought = self._view.find_item(mouse_position)

                # ME WANTS THIS
                
                if item_bought is not None:
                    # Let's see if I can buy it
                    if hero.coins >= item_bought.price:
                        if type(item_bought) == Whitestone:
                            self._shop.remove_item(item_bought)
                        hero.coins = hero.coins - item_bought.price
                        # OH YES - ME LIKEY
                        item_bought.use(hero)
                        shoprunning=False
                    else: 
                        # Just paid your rent in Vancouver?
                        print("You don't have enough money to buy this item.")
                # if user click the back button, close the loop and back to the previous page.
                if self._view.has_clicked_back(mouse_position):
                        shoprunning=False