import pygame
from pygame.sprite import Group

from constants import (SHOP_ITEM_IMG_OFFSET, SHOP_ITEM_LINE_HEIGHT,
                       SHOP_ITEM_SIZE, SHOP_ITEM_TXT_OFFSET, WHITE,SHOP_BUTTON_COLOR)


class ShopView(Group):
    """ The view for the shop window """

    def __init__(self, shop):
        super().__init__()

        # These are the items from the Shop model
        self._items = shop.items
        # These are the sprites of the shop items
        self._sprites = list()

        self._back_button=None

        font = pygame.font.SysFont("arial", 24, bold=True)

        for idx, item in enumerate(self._items):
            # For each shop item, create a surface
            surface = pygame.Surface(SHOP_ITEM_SIZE)
            surface.fill(WHITE)

            # Item image
            surface.blit(item.image, SHOP_ITEM_IMG_OFFSET)

            # Item text
            text = font.render(f"{item.name:.<15} {item.price}g", True, (0, 0, 0))
            surface.blit(text, SHOP_ITEM_TXT_OFFSET)

            # We create a sprite to make it easier to detect collisions / clicks
            sprite = pygame.sprite.Sprite()
            sprite.image = surface
            sprite.rect = sprite.image.get_rect()
            sprite.rect.x = 0
            sprite.rect.y = 20 + SHOP_ITEM_LINE_HEIGHT * idx
            self._sprites.append(sprite)

        # Add all the sprites to the sprite group
        self.add(*self._sprites)
    
    def back_button(self,window):
        font = pygame.font.SysFont("arial", 24, bold=True)
        text = font.render("back", True, WHITE)
        button_shape= pygame.draw.rect(window, SHOP_BUTTON_COLOR, (10,550,50,35))
        window.blit(text, (10, 550))
        return button_shape

    def display(self, window):
        window.fill(WHITE)
        # Display all the sprites at once
        self.draw(window)
        self._back_button=self.back_button(window)

        pygame.display.flip()

    def find_item(self, pos):
        # We look for the shop item matching the sprite that was clicked
        # and return it
        for idx, sprite in enumerate(self._sprites):
            if sprite.rect.collidepoint(pos):
                return self._items[idx]


    def has_clicked_back(self, pos):
        #Did we click on the back button
        
        if self._back_button.collidepoint(pos):
            return True
        
        return False
