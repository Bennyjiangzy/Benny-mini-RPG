import pygame


class PygameController:


    #run a loop
    def _run_loop(self):
        running = True
        #define the fps
        clock = pygame.time.Clock()
        while running:
            clock.tick(30)
            #loop the events
            for event in pygame.event.get():
                # if player click the X the pass false to close the game
                if event.type == pygame.locals.QUIT:
                    return False
                # Pressed ESC return the ECS to call the menu view
                elif event.type == pygame.locals.KEYDOWN:
                    if event.key == pygame.locals.K_ESCAPE:
                        return event.key
                # Clicked the mouse
                elif event.type == pygame.locals.MOUSEBUTTONDOWN:
                    return event.pos
