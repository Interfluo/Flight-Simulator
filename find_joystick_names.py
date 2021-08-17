from __future__ import division
from __future__ import print_function
import sys
import pygame
from pygame.locals import *


class JoystickHandler(object):
    def __init__(self, id):
        self.id = id
        self.joy = pygame.joystick.Joystick(id)
        self.name = self.joy.get_name()
        self.joy.init()
        self.numaxes    = self.joy.get_numaxes()
        self.numballs   = self.joy.get_numballs()
        self.numbuttons = self.joy.get_numbuttons()
        self.numhats    = self.joy.get_numhats()

        self.axis = []
        for i in range(self.numaxes):
            self.axis.append(self.joy.get_axis(i))

        self.ball = []
        for i in range(self.numballs):
            self.ball.append(self.joy.get_ball(i))

        self.button = []
        for i in range(self.numbuttons):
            self.button.append(self.joy.get_button(i))

        self.hat = []
        for i in range(self.numhats):
            self.hat.append(self.joy.get_hat(i))


class input_test(object):

    def init(self):
        pygame.init()
        pygame.event.set_blocked((MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN))
        self.joycount = pygame.joystick.get_count()
        if self.joycount == 0:
            print("no joystick(s) detected!")
            self.quit(1)
        self.joy = []
        for i in range(self.joycount):
            self.joy.append(JoystickHandler(i))

    def run(self):

        while True:
            for i in range(self.joycount):
                self.draw_joy(i)

            for event in [pygame.event.wait(), ] + pygame.event.get():

                if event.type == QUIT:
                    self.quit()
                elif event.type == KEYDOWN and event.key in [K_ESCAPE, K_q]:
                    self.quit()
                elif event.type == VIDEORESIZE:
                    self.screen = pygame.display.set_mode(event.size, RESIZABLE)
                elif event.type == JOYAXISMOTION:
                    self.joy[event.joy].axis[event.axis] = event.value
                elif event.type == JOYBALLMOTION:
                    self.joy[event.joy].ball[event.ball] = event.rel
                elif event.type == JOYHATMOTION:
                    self.joy[event.joy].hat[event.hat] = event.value
                elif event.type == JOYBUTTONUP:
                    self.joy[event.joy].button[event.button] = 0
                elif event.type == JOYBUTTONDOWN:
                    self.joy[event.joy].button[event.button] = 1

    def draw_joy(self, joyid):
        joy = self.joy[joyid]

        # ============================================================================ #
        # Rudder Output
        if joyid == 0:
            print("\033[93m", joy.name, "\033[0m")
            for i, v in enumerate(joy.axis):
                if i == 2:
                    print("rudder position: ", v)
        print("\033[91m-------------------------------------------------------------------------\033[0m")
        # Throttle Output
        if joyid == 1:
            print("\033[94m", joy.name, "\033[0m")
            for i, v in enumerate(joy.axis):
                if i == 0:
                    print("throttle position: ", v)
        print("\033[91m-------------------------------------------------------------------------\033[0m")
        # Stick Output
        if joyid == 2:
            print("\033[95m", joy.name, "\033[0m")
            for i, v in enumerate(joy.axis):
                if i == 0:
                    print("roll position: ", v)
                if i == 1:
                    print("pitch position: ", v)

        # ============================================================================ #



    def quit(self, status=0):
        pygame.quit()
        sys.exit(status)


if __name__ == "__main__":
    program = input_test()
    program.init()
    program.run()