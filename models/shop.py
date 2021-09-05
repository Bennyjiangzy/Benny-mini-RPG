import pygame.font

from constants import SHOP_BUTTON_COLOR, WHITE, SHOP_BUTTON_OFFSET


class Shop:
    def __init__(self):
        self._items = list()

    #method for add items to the list 
    def add_item(self, item):
        self._items.append(item)

    #return the item list
    @property
    def items(self):
        return self._items

    #remove the item in the item list
    def remove_item(self, item):
        self._items.remove(item)

    #define the shop button
    @staticmethod
    def get_button_image(window):

        font = pygame.font.SysFont("arial", 24, bold=True)
        text = font.render("$ SHOP", True, WHITE)
        button_shape= pygame.draw.rect(window, SHOP_BUTTON_COLOR, (SHOP_BUTTON_OFFSET[0],SHOP_BUTTON_OFFSET[1],80,35))
        window.blit(text, (SHOP_BUTTON_OFFSET[0], SHOP_BUTTON_OFFSET[1]))

        return button_shape
