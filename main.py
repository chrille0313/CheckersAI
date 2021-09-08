from func import *
from checkers import Checkers


class App(object):
    def __init__(self, window: pygame.surface, windowSize: tuple, fps: int = 60):
        self.window = window
        self.windowSize = self.windowW, self.windowH = windowSize
        self.windowCenter = Vector2(self.windowW / 2, self.windowH / 2)
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.running = True

        self.keys = pygame.key.get_pressed()

        self.game = Checkers(10, 10, self.windowW, self.windowH)

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or self.keys[pygame.K_ESCAPE]:
                self.running = False

            if event.type in (pygame.KEYDOWN, pygame.KEYUP):
                self.keys = pygame.key.get_pressed()

        if self.keys[pygame.K_UP]:
            self.fps = FPS
        elif self.keys[pygame.K_DOWN]:
            self.fps = 0

    def draw(self):
        self.window.fill(BLACK)

        self.game.draw()

        pygame.display.update()

    def main_loop(self):
        while self.running:
            self.event_loop()

            self.draw()
            self.clock.tick(self.fps)


def main():
    pygame.init()
    pygame.display.set_caption(CAPTION)
    pygame.display.set_mode(WINDOW_SIZE)

    App(pygame.display.get_surface(), WINDOW_SIZE, FPS).main_loop()

    pygame.quit()


if __name__ == '__main__':
    main()
