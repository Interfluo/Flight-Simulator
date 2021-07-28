from pygame.locals import *
import pygame
import sys


class JoystickHandler(object):
    def __init__(self, id):
        self.id = id
        self.joy = pygame.joystick.Joystick(id)
        self.name = self.joy.get_name()
        self.joy.init()
        self.numaxes = self.joy.get_numaxes()
        self.axis = []
        for i in range(self.numaxes):
            self.axis.append(self.joy.get_axis(i))


class InputTest(object):
    def init(self):
        pygame.init()
        self.joycount = pygame.joystick.get_count()
        if self.joycount == 0:
            print("no joystick(s) detected!")
            pygame.quit()
            sys.exit(0)
        self.joy = []
        for i in range(self.joycount):
            self.joy.append(JoystickHandler(i))

    def run(self):
        # ============================================================================ #
        screen_size = screen_width, screen_height = 1000, 100
        center = (screen_width//2, screen_height//2)
        screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption('rudder')
        counter = 0
        variable = 1
        clock = pygame.time.Clock()
        vpx = 0
        score = 0
        # ============================================================================ #
        while True:
            for i in range(self.joycount):
                joy = self.joy[i]
                if i == 0:
                    for j, v in enumerate(joy.axis):
                        if j == 2:
                            # print("rudder position: ", v)
                            # ============================================================================ #
                            # TODO: Adjust the travel parameter, make it to where the velocity depends on the rudder
                            #       position, not directly the position
                            vpx += int(0.5*v*10)
                            rpx = center[0] + vpx
                            rudder_position = (rpx, center[1])
                            pygame.draw.circle(screen, (120, 0, 200), rudder_position, 8)

                            # TODO: make the target change color when the rudder position is within a certain bounds of
                            #       the target position (green -> red maybe?)
                            tpx = center[0]+counter
                            target_position = (tpx, center[1])
                            if counter == 500*variable:
                                variable *= -1
                            counter += variable

                            delta = 25
                            if tpx + delta > rpx > tpx - delta:
                                target_color = (0, 255, 0)
                                score += 1
                                print(score)
                            else:
                                target_color = (255, 0, 0)
                            pygame.draw.circle(screen, target_color, target_position, 25, 3)
                            pygame.display.flip()

                            dt = clock.tick(100)  # set fps to 100

            # clear screen between frames
            screen = pygame.display.set_mode(screen_size)
            # ============================================================================ #

            for event in [pygame.event.wait(), ] + pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit(0)
                elif event.type == JOYAXISMOTION:
                    self.joy[event.joy].axis[event.axis] = event.value


if __name__ == "__main__":
    program = InputTest()
    program.init()
    program.run()

