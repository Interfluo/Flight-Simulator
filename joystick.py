from pygame.locals import *
import pygame
import sys

# TODO: 1.) make the target change direction into a random orientation, not just always in the diaganol
#       2.) fix the issue where the score is counted just for being lined up horizontally or vertically with the target
#           instead of being on target
#       3.) get the score to display
#       4.) rename variables to correctly reflect function
#       5.) clearly comment the code
#       6.) combine the rudder and stick code so that they can be run simultaneously
#       7.) create nicer animations
#       8.) implement a gui to test/select the appropriate joystick ports
#       9.) release the code

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
        screen_size = screen_width, screen_height = 1000, 1000
        center = (screen_width//2, screen_height//2)
        screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption('rudder')
        counterx = countery = 0

        variable = 1
        clock = pygame.time.Clock()
        rpx = tpx = center[0]
        rpy = tpy = center[1]
        vpx = vpy = 0
        score = 0
        SCORE = 0
        possible = 0
        # ============================================================================ #
        while True:
            for i in range(self.joycount):
                joy = self.joy[i]
                if i == 2:
                    for j, v in enumerate(joy.axis):

                        # horizontal movement
                        if j == 0:
                            possible += 1
                            print(SCORE, '/', possible)
                            # ============================================================================ #
                            vpx += int(0.5*v*10)
                            rpx = center[0] + vpx
                            rudder_position = (rpx, rpy)
                            pygame.draw.circle(screen, (120, 0, 200), rudder_position, 8)
                            if counterx == 500*variable:
                                variable *= -1
                            counterx += variable
                            delta = 25
                            tpx = center[0] + counterx
                            if tpx + delta > rpx > tpx - delta:
                                target_color = (0, 0, 255)
                                score += 1
                                SCORE += 1
                                # This if statement reverses the direction of the target if you are on it for 100 frames
                                if score == 100:
                                    target_color = (255, 255, 255)
                                    variable *= -1
                            else:
                                target_color = (255, 0, 0)
                                score = 0
                            dt = clock.tick(100)  # set fps to 100

                        # vertical movement
                        if j == 1:
                            possible += 1
                            print(SCORE, '/', possible)
                            # ============================================================================ #
                            vpy -= int(0.5*v*10)
                            rpy = center[1] + vpy
                            rudder_position = (rpx, rpy)
                            pygame.draw.circle(screen, (120, 0, 200), rudder_position, 8)
                            if countery == 500*variable:
                                variable *= -1
                            countery += variable
                            delta = 25
                            tpy = center[1] + countery
                            if tpy + delta > rpy > tpy - delta:
                                target_color = (0, 0, 255)
                                score += 1
                                SCORE += 1
                                # This if statement reverses the direction of the target if you are on it for 100 frames
                                if score == 100:
                                    target_color = (255, 255, 255)
                                    variable *= -1
                            else:
                                target_color = (255, 0, 0)
                                score = 0
                            dt = clock.tick(100)  # set fps to 100


                        target_position = (tpx, tpy)
                        pygame.draw.circle(screen, target_color, target_position, 25, 3)
                        pygame.display.flip()



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

