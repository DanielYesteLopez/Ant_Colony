# Import the pygame library and initialise the game engine
import pygame
pygame.init()
if __name__ == '__main__':
    print("Init")
    '''
    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("My First Game")
    carryOn = True

    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while carryOn:
        # --- Main event loop
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                carryOn = False  # Flag that we are done so we exit this loop

            # --- Game logic should go here

            # --- Drawing code should go here
            # First, clear the screen to white.
        screen.fill(WHITE)



        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    # Once we have exited the main program loop we can stop the game engine:
    pygame.quit()
    '''