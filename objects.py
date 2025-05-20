import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("objects and classes")

screen.fill("white")

pygame.display.update()

class Rectangle():
    def __init__(self, c, x ,y ,w,h):
        self.c = c
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        print("hello")
    def draw(self):
        pygame.draw.rect(screen, self.c,(self.x,self.y,self.w, self.h))


red = Rectangle("red", 100,200,100,50)
red.draw()

green = Rectangle("green", 300,200,100,150)
green.draw()

yellow = Rectangle("yellow", 300,200,150,50)
yellow.draw()
pygame.display.update()