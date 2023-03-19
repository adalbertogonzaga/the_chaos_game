"""
An implementation of "The Chaos Game!" / Sierpinski Triangle 
"""
import random
import pygame
import pygame_menu

BACKGROUND_COLOR = (128, 128, 128)
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
GAME_SCREEN = None
GAME_MENU = None
STARTED = False


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


def draw_score(screen, score):
    """
    Draw a box with a text that represent the number of points already drawn on the screen.

    Puts that box always at the same damn place, so it creates the illusion that the number is changing.
    """
    score_surface_width = 200
    score_surface = pygame.Surface((score_surface_width, 10))
    score_surface.fill(BACKGROUND_COLOR)

    my_font = pygame.font.SysFont('Comic Sans MS', 16)
    score_text = score.zfill(6)
    score_text = my_font.render(f"Drawn dots {score_text}", True, (0, 0, 0))
    width, height = screen.get_size()

    score_surface.blit(score_text, (0, 0))
    screen.blit(score_surface, (width - score_surface_width, 5))


def draw_random_points(screen, click_position, points):
    """
    Based on an initial click, starts drawing points on the halfway
    between this initial clicked/picked point and one of 3 points from
    the triangle (random picked)
    """

    MAX_DOTS_COUNTS = points
    top_dot_position, left_dot_position, right_dot_position = get_triangle_points(screen)
    triangle_points = [top_dot_position, left_dot_position, right_dot_position]

    next_point_pos = random.choice( (0, 1, 2) )
    next_point = get_halfway_point( triangle_points[next_point_pos], click_position)

    for i in range(0, MAX_DOTS_COUNTS):
        pygame.draw.circle(screen, (0,128,255), next_point, 1)
        next_point_pos = random.choice( (0, 1, 2) )
        next_point = get_halfway_point( triangle_points[next_point_pos], next_point)

        draw_score(screen, str(i + 1))

        # Update the display
        if i % 99 == 0:
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

    POINTS_TO_DRAW = 50000
    draw_random_points(screen, mouse_position, POINTS_TO_DRAW)


def init_screen(**kwargs):
    """
    Calls all the necessary functions to setup the init screen
    """
    print("init_screen", kwargs)
    global GAME_SCREEN
    global STARTED

    draw_labels(GAME_SCREEN)
    top_dot_position, left_dot_position, right_dot_position = get_triangle_points(GAME_SCREEN)
    draw_initial_triangle(GAME_SCREEN, top_dot_position, left_dot_position, right_dot_position)
    
    STARTED = True
    GAME_MENU.full_reset()
    pygame.display.flip()

def set_fractal(value, fractal):
    """
    Sets the chosen fractal
    """
    print(value, fractal)

def create_initial_menu():
    """
    Draws the initial menu
    """
    menu = pygame_menu.Menu(
        'Welcome',
        SCREEN_WIDTH-50, SCREEN_HEIGHT-50,
        theme=pygame_menu.themes.THEME_BLUE
    )

    # menu.add.text_input("What's your name?", default='John Capybara')
    menu.add.selector(
        'Fractal :',
        [
            ('Sierpinski Triangle', 1),
            ('Restricted Chaos - Square 01', 2),
        ],
        onchange=set_fractal
    )
    menu.add.button('Start', init_screen)
    menu.add.button('Quit', pygame_menu.events.EXIT)

    return menu


if __name__ == "__main__":
    # Initialize Pygame
    pygame.init()

    # Set the window size
    window_size = (SCREEN_WIDTH, SCREEN_HEIGHT)

    # Create the window
    my_screen = pygame.display.set_mode(window_size)
    # global GAME_SCREEN
    GAME_SCREEN = my_screen

    # Set the background color
    my_screen.fill(BACKGROUND_COLOR)

    pygame.display.set_caption("The Chaos Game! - A Sierpinski Triangle visualization")

    # Update the display
    pygame.display.flip()

    # Run the Pygame loop
    running = True

    # init_screen(my_screen)
    menu = create_initial_menu()
    GAME_MENU = menu

    while running:
        events = pygame.event.get()
        if STARTED:
            pass
            #menu.full_reset()
            #menu.disable()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

            elif menu.is_enabled() and not STARTED:
                menu.update(events)
                menu.draw(my_screen)
                
            elif event.type == pygame.MOUSEBUTTONDOWN and STARTED:
                # Get the mouse position
                mouse_pos = pygame.mouse.get_pos()
                start_chaos_game(my_screen, mouse_pos)
            
            pygame.display.update()

    # Quit Pygame
    pygame.quit()
