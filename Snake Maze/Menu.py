import pygame
from pygame.locals import *

from enum import Enum
import Colors as Color


''' ENUMs'''
class Option_Style(Enum):

    Highlighted = 1
    Not_Highlighted = 2

class Option_Mode(Enum):

    Selected = 1
    Not_Selected = 2



''' CLASS OPTION '''
class Option:

    # SET ATTRIBUTES #
    def __init__(self,name,pos):

        self._mode = Option_Mode.Not_Selected #Clicked by user or not
        self._style = None
        self._name =  name
        self._pos = pos
        self._writing = "algerian"


    # SET THAT THE OPTION IS HIGHLIGHTED TO BE SELECTED BY USER #
    def Set_Highlighted(self):

        self._style = Option_Style.Highlighted
        try:
            self._font = pygame.font.SysFont(self._writing,65)
            self._color = Color.WHITE
        except:
            print('Fonts Not Load')


    # SET IF THE OPTION IS NOT HIGHLIGHTED TO BE NOT-SELECTED BY USER #
    def Set_Not_Highlighted(self):

        self._style = Option_Style.Not_Highlighted
        try:
            self._font = pygame.font.SysFont(self._writing, 60)
            self._color = Color.ORANGE_RED
        except:
            print('Fonts Not Load')


    # DRAW THE OPTION ON MENU SCREEn #
    def Draw(self,window):

        text = self._font.render(self._name, True, self._color)
        window.blit(text, self._pos)



''' CLASS MENU '''
class Menu:

    # CREATE INSTANCES OF OPTION CLASS #
    def __init__(self):

        self._opt_1 = Option("PLAY", (520,480))
        self._opt_2 = Option("EXIT", (540,600))

        self.initial = True


    # LOAD MENU IMAGE FROM FILE #
    def Load(self,path):
        self._img = pygame.image.load(path + r'\Menu_.jpg')


    # DRAW COMPLETE MENU #
    def Draw(self,window):

        #Draw menu screen
        window.blit(self._img,(0,0)) 

        #Highlight 1st option and unhighlight 2nd one at the first view of menu
        if self.initial is True:
            self.initial = False
            self._opt_1.Set_Highlighted()
            self._opt_2.Set_Not_Highlighted()

        #Draw options
        self._opt_1.Draw(window)
        self._opt_2.Draw(window)


    # SWITCH OPTIONS ON EVENTS #
    def Switch_Option(self):

            if self._opt_1._style == Option_Style.Highlighted:
                self._opt_1.Set_Not_Highlighted()
                self._opt_2.Set_Highlighted()

            elif self._opt_2._style == Option_Style.Highlighted:
                self._opt_1.Set_Highlighted()
                self._opt_2.Set_Not_Highlighted()


    # HANDLES EVENTS FOR MENU #
    def Handle_Events(self,event):
            
            #Switching options
            if ( event.key == pygame.K_UP and self._opt_2._style == Option_Style.Highlighted ) or ( event.key == pygame.K_DOWN and self._opt_1._style == Option_Style.Highlighted ):
                self.Switch_Option()

            #Selecting options
            elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:

                if self._opt_1._style == Option_Style.Highlighted:
                    self._opt_1._mode = Option_Mode.Selected

                elif self._opt_2._style == Option_Style.Highlighted:
                    self._opt_2._mode = Option_Mode.Selected