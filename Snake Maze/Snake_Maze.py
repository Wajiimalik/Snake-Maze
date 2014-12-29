import pygame
from pygame.locals import *

class App:
    def __init__(self):
        self._running = True
        self._window = None
        self.size = self.weight, self.height = 800,700


    def Init(self):
        pygame.init()
        pygame.display.set_caption('Snake Maze')
        self._window = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._window.fill(pygame.color.Color("white"))       
        self._running = True


    def Load(self):
        pass


    def Event(self, event):
        if event.type == pygame.QUIT:
            self._running = False


    def Loop(self):
        pass


    def Render(self):
        pygame.display.flip()
        pass


    def Cleanup(self):
        pygame.quit()


    def Execute(self):
        if self.Init() == False:
            self._running = False

        if self.Load() == False:
            self._running = False

        while( self._running ):
            for event in pygame.event.get():
                self.Event(event)
            self.Loop()
            self.Render()

        self.Cleanup()



if __name__ == "__main__":
    game=App()
    game.Execute()