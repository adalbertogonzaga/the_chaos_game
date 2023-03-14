"""
An implementation of "The Chaos Game!" / Sierpinski Triangle 
"""
import random
import pygame

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

def draw_labels(screen):
    """
    Draws a label on screen
    """
    pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
    my_font = pygame.font.SysFont('Comic Sans MS', 20)
    text_surface_1 = my_font.render('The Chaos Game!', False, (0, 0, 0))

    my_font = pygame.font.SysFont('Comic Sans MS', 16)
    text_surface_2 = my_font.render('Sierpinski Triangle', False, (32, 64, 32))

    screen.blit(text_surface_1, (5,5))
    screen.blit(text_surface_2, (5,30))


def draw_initial_triangle(screen, top_dot_position, left_dot_position, right_dot_position):
    """
    Draws initial triangle dots on screen
    """
    dot_color = (0, 0, 255) # rgb blue

    pygame.draw.circle(screen, dot_color, top_dot_position, 4)
    pygame.draw.circle(screen, dot_color, left_dot_position, 4)
    pygame.draw.circle(screen, dot_color, right_dot_position, 4)

    # Update the display
    pygame.display.flip()


def get_triangle_points(screen):
    """
    Based on screen size it calculates where the triangle dots should be placed.

    Returns top_dot_position, left_dot_position, right_dot_position
    """
    width, height = screen.get_size()
    top_dot_position = (width/2, 20)
    left_dot_position = (20, height-20)
    right_dot_position = (width-20, height-20)

    return top_dot_position, left_dot_position, right_dot_position


def draw_random_points(screen, click_position):
    """
    Based on an initial click, starts drawing points on the halfway
    between this initial clicked/picked point and one of 3 points from
    the triangle (random picked)
    """

    MAX_DOTS_COUNTS = 30000
    top_dot_position, left_dot_position, right_dot_position = get_triangle_points(screen)
    triangle_points = [top_dot_position, left_dot_position, right_dot_position]

    next_point_pos = random.choice( (0, 1, 2) )
    next_point = get_halfway_point( triangle_points[next_point_pos], click_position)

    ###################################################################
    my_font = pygame.font.SysFont('Comic Sans MS', 16)
    score_text = "0"
    score_text = score_text.zfill(6)
    score_surface = my_font.render(f"Draw dots {score_text}", True, (0, 0, 0))
    width, height = screen.get_size()

    screen.blit(score_surface, (width-200,5))

    ###################################################################



    for i in range(0, MAX_DOTS_COUNTS):
        pygame.draw.circle(screen, (0,128,255), next_point, 1)
        next_point_pos = random.choice( (0, 1, 2) )
        next_point = get_halfway_point( triangle_points[next_point_pos], next_point)

        score_text = str(i)
        score_text = score_text.zfill(6)
        score_surface = my_font.render(f"Draw dots {score_text}", True, (0, 0, 0))
        screen.blit(score_surface, (width-200,5))

        # Update the display
        pygame.display.flip()


def get_halfway_point(point_a, point_b):
    """
    Gets the point in half of the distance between supplied points A & B.
    """
    x =  int( (point_a[0] + point_b[0]) / 2)
    y =  int( (point_a[1] + point_b[1]) / 2)
    return (x,y,)


def start_chaos_game(screen, mouse_position):
    """
    Starts the Chaos Game system
    """
    # Draw a point at the mouse position
    pygame.draw.circle(screen, (0, 0, 0), mouse_position, 2)
    # Update the display
    pygame.display.flip()
    draw_random_points(screen, mouse_position)


def init_screen(screen):
    """
    Calls all the necessary functions to setup the init screen
    """
    draw_labels(screen)
    top_dot_position, left_dot_position, right_dot_position = get_triangle_points(screen)
    draw_initial_triangle(screen, top_dot_position, left_dot_position, right_dot_position)


if __name__ == "__main__":
    # Initialize Pygame
    pygame.init()

    # Set the window size
    window_size = (SCREEN_WIDTH, SCREEN_HEIGHT)

    # Create the window
    my_screen = pygame.display.set_mode(window_size)

    # Set the background color
    my_screen.fill((128, 128, 128))

    pygame.display.set_caption("The Chaos Game! - A Sierpinski Triangle visualization")

    # Update the display
    pygame.display.flip()

    # Run the Pygame loop
    running = True

    init_screen(my_screen)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the mouse position
                mouse_pos = pygame.mouse.get_pos()
                start_chaos_game(my_screen, mouse_pos)

    # Quit Pygame
    pygame.quit()
