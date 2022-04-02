import pygame
import math

class LSystem:
    def __init__(self,axiome,dtheta,rules,init_position,ratio,starting_angle):
        self.sentence = axiome
        self.dtheta = dtheta
        self.starting_angle = starting_angle
        self.angle = self.starting_angle
        self.rules = rules
        self.init_position = init_position
        self.current_position = init_position
        self.stack = []
        self.length = 50
        self.ratio = ratio

    def __str__(self):
        return self.sentence
    
    def reset(self):
        self.current_position = self.init_position
        self.angle = self.starting_angle


    def generate(self):
        self.reset()
        newsentence = ""
        for char in self.sentence:
            if(char in self.rules):
                newsentence += self.rules[char]
            else:
                newsentence += char
        self.sentence = newsentence
        self.length = self.length * self.ratio

    def get_next_point(current_point,angle,length):
        x2 = current_point[0] - length*math.cos(math.radians(angle))
        y2 = current_point[1] - length*math.sin(math.radians(angle))

        return x2, y2

    def draw(self,screen):
        color = 0
        dcolor = 255 / len(self.sentence)
        for char in self.sentence:
            if char == 'F' or char == 'G':
                #next_point = self.get_next_point(self.current_position,self.angle%360,self.length)
                x2 = self.current_position[0] - self.length * math.cos(math.radians(self.angle))
                y2 = self.current_position[1] - self.length * math.sin(math.radians(self.angle))
                next_point = (x2,y2)
                pygame.draw.line(screen,(255 - color, color, 125 + color / 2),self.current_position,next_point)
                self.current_position = next_point
            elif char == '+':
                self.angle -= self.dtheta
            elif char == '-':
                self.angle +=  self.dtheta
            elif char == '[':
                self.stack.append({
                   "current_position":self.current_position,
                    "current_angle": self.angle,
                })
            elif char == ']':
                last_stack_entry = self.stack.pop()
                self.current_position = last_stack_entry["current_position"]
                self.angle = last_stack_entry["current_angle"]
            color += dcolor
            pygame.display.flip()

