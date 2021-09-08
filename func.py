import pygame
from pygame.math import Vector2
import numpy as np
import jupyterlab


# Pygame Properties
CAPTION = "Checkers"
WINDOW_SIZE = WINDOW_W, WINDOW_H = 600, 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAVITY = 0.05


def draw_circle(pos: Vector2, radius: float = 1.0, width=5, color=WHITE, surface=None):
    surface = surface if surface else pygame.display.get_surface()
    pygame.draw.circle(surface, color, pos, radius, width)


def draw_rect(x, y, width, height, borderWidth=1, color=WHITE, surface=None):
    surface = surface if surface else pygame.display.get_surface()
    pygame.draw.rect(surface, color, pygame.Rect(x, y, width, height), borderWidth)


def draw_line(point1: Vector2, point2: Vector2, color=WHITE, width=1, surface=None):
    surface = surface if surface else pygame.display.get_surface()
    pygame.draw.line(surface, color, point1, point2, width)


def draw_lines(points, color=WHITE, width=1, connected=True, surface=None):
    surface = surface if surface else pygame.display.get_surface()
    pygame.draw.lines(surface, color, connected, points, width)


def draw_shape(points, width=0, color=WHITE, surface=None):
    surface = surface if surface else pygame.display.get_surface()
    pygame.draw.polygon(surface, color, points, width)
