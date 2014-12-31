import pygame
from pygame.locals import *

from enum import Enum
from time import sleep

import Colors as Color


class Game_Mode(Enum):
    Start = 1
    Selection = 2
    Playing = 3
    Win = 4


class Menu_Mode(Enum):
    No_Menu = 0
    Menu_Options = 1
    How_To_Play = 2
    About_Me = 3
    Exit = 4


class Move(Enum):
    Forward =  1
    Left = 2
    Right = 3
    Backward = 4


class Game:
    def __init__(self):
        self._running = True
        self._window = None
        self.size = self.width, self.height = 800,700
        self.move_event = None

        self._game_mode = Game_Mode.Start
        self._menu_mode = Menu_Mode.No_Menu


    def Init(self):
        try:
            pygame.init()

            pygame.display.set_caption('Hungry Caterpillar :<')
            self._window = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)

            self._window.blit(self._Start_Window,(0,0)) #Draw start screen
            pygame.display.flip()
                
            self._running = True

        except:
            print('Init Failed')
            return False


    def Load(self):
        path = r"C:\Users\wajiha\Documents\Visual Studio 2013\Python\Snake Maze\Snake Maze\Images"      

        try:
            self._Start_Window = pygame.image.load(path + r'\Start_Game_Window_.jpg')
        except:
            print('Load Failed')
            return False


    def Event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                self._running = False

            elif event.key == pygame.K_w:
                self.move_event = Move.Forward

            elif event.key == pygame.K_a:
                self.move_event = Move.Left

            elif event.key == pygame.K_d:
                self.move_event = Move.Right

            elif event.key == pygame.K_s:
                self.move_event = Move.Backward


    def Loop(self):
        if self._game_mode == Game_Mode.Start:
            sleep(3)
            self._window.fill(Color.WHITE)
            pass

        elif self._game_mode == Game_Mode.Selection:
            pass

        elif self._game_mode == Game_Mode.Playing:
            pass

        elif self._game_mode == Game_Mode.Win:
            pass


    def Render(self):
        if self.move_event == Move.Forward:
            pass

        elif self.move_event == Move.Left:
            pass

        elif self.move_event == Move.Right:
            pass

        elif self.move_event == Move.Backward:
            pass

        pygame.display.flip()


    def Cleanup(self):
        pygame.quit()


    def Execute(self):
        if self.Load() == False:
            self._running = False

        if self.Init() == False:
            self._running = False

        while( self._running ):
            for event in pygame.event.get():
                self.Event(event)
            self.Loop()
            self.Render()

        self.Cleanup()