from collections import deque
from sign import Sign
import pygame


class OpponentUI:
    def __init__(self, dim, images):
        self.win_width, self.win_height = dim
        rock, paper, scissors = images
        self.signs = pygame.sprite.Group((Sign("S", scissors, (self.win_width - self.win_width//8, self.win_height//3), opp=True), Sign("R", rock, (self.win_width - self.win_width //
                                                                                                                                                    8, self.win_height//2), opp=True), Sign("P", paper, (self.win_width - self.win_width//8, self.win_height - self.win_height//3), opp=True)))
        self.order = deque(["S", "R", "P"])
        self.choice = None

    def draw(self, win):
        self.signs.draw(win)

    def rotate_signs(self, d):
        if d == 1:
            self.update_signs(1)
        elif d == 0:
            self.update_signs(-1)

    def update_signs(self, d):
        self.order.rotate(d)
        for sign in self.signs:
            i = self.order.index(sign.value)
            if i == 1:
                # sign.image = sign.large
                # sign.rect = sign.large_rect
                sign.rect.center = (
                    self.win_width - self.win_width//8, self.win_height//2)
            elif i == 0:
                # sign.image = sign.orig
                # sign.rect = sign.orig_rect
                sign.rect.center = (
                    self.win_width - self.win_width//8, self.win_height//3)
            elif i == 2:
                # sign.image = sign.orig
                # sign.rect = sign.orig_rect
                sign.rect.center = (self.win_width - self.win_width//8,
                                    self.win_height - self.win_height//3)
