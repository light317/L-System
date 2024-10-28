from LSystem import LSystem
import argparse
import pygame
import math
import json


WHITE = (255,255,255)
BLACK = (0,0,0)
LENGTH = 10

def get_system_params(filename):
    f = open(filename,"r")
    data = json.loads(f.read())
    f.close()
    return data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("screen_width",nargs='?',type=int, default=1200)
    parser.add_argument("screen_height",nargs='?',type=int,default=700)
    parser.add_argument("start_x",nargs='?',type=int, default=600)
    parser.add_argument("start_y",nargs='?',type=int, default=600)
    parser.add_argument("intial_drawing_angle",nargs='?',type=int, default=90)
    parser.add_argument("ratio",nargs='?',type=float, default=0.7)

    parser.add_argument("system_param",nargs='?',type=str,default="test_tree.json")

    args = parser.parse_args()

    screen_size = [int(args.screen_width),int(args.screen_height)]
    system_param_file_path = args.system_param

    # Initialize pygame
    pygame.init()

    # Set the HEIGHT and WIDTH of the screen
    screen = pygame.display.set_mode(screen_size)

    # Set title of screen
    pygame.display.set_caption("L System")

    # Loop until the user clicks the close button.
    running = True

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # rules = {
    #     "X":"F+[[X]-X]-F[-FX]+X",
    #     "F":"FF"
    # }

    # rules = {
    #     "F":"G-F-G",
    #     "G":"F+G+F"
    # }

    print( get_system_params(system_param_file_path))
    system_param = get_system_params(system_param_file_path)
    axiome = system_param["axiome"]
    dtheta = system_param["angle"]
    rules = system_param["rules"]
    ratio = args.ratio
    starting_angle = args.intial_drawing_angle

    #system = LSystem("F",60,rules,1,(int(args.start_x),int(args.start_y)),0.7)
    system = LSystem(axiome,dtheta,rules,(int(args.start_x),int(args.start_y)),ratio,starting_angle)

    while running:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                running = False  # Flag that we are done so we exit this loop
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the screen background
                screen.fill(BLACK)
                system.draw(screen)
                system.generate()

       
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

         # Limit to 60 frames per second
        clock.tick(30)

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

   

if __name__ == "__main__":
    main()
