import pygame
from pygame.locals import *

from enum import Enum
from time import sleep

import Colors as Color
from Menu import Menu, Option_Mode


class Game_Mode(Enum):
    Start = 1
    Selection = 2
    Playing = 3
    Win_End = 4

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
        self._menu = Menu()


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
            self._menu.Load(path)
            
        except:
            print('Load Failed')
            return False


    def Event(self, event):
        if event.type == pygame.QUIT:
            self._game_mode = Game_Mode.Win_End
            self._running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                    self._game_mode = Game_Mode.Win_End
                    self._running = False

            if self._game_mode == Game_Mode.Playing:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.move_event = Move.Forward

                elif event.key == pygame.K_a or event.key == pygame.K_RIGHT:
                    self.move_event = Move.Left

                elif event.key == pygame.K_d or event.key == pygame.K_LEFT:
                    self.move_event = Move.Right

                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.move_event = Move.Backward


            elif self._game_mode == Game_Mode.Selection:
                self._menu.Handle_Events(event)

                if self._menu._opt_1._mode == Option_Mode.Selected:
                    pass
                    self._game_mode = Game_Mode.Playing
                    self._window.fill(Color.WHITE)

                elif self._menu._opt_2._mode == Option_Mode.Selected:
                    self._game_mode = Game_Mode.Win_End
                    self._running = False


    def Loop(self):
        if self._game_mode == Game_Mode.Start:
            sleep(2)
            self._game_mode = Game_Mode.Selection
            pass

        elif self._game_mode == Game_Mode.Selection:
            self._menu.Draw(self._window)
            pass

        elif self._game_mode == Game_Mode.Playing:
            pass

        elif self._game_mode == Game_Mode.Win_End:
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