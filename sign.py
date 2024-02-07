import pygame


class Sign(pygame.sprite.Sprite):
    def __init__(self, value, image, pos, opp=False):
        super(Sign, self).__init__()
        self.value = value
        self.x, self.y = pos[0], pos[1]
        self.image = image if opp else pygame.transform.flip(
            image, True, False)
        self.rect = self.image.get_rect()
        self.rect.center = pos

        # self.orig = self.image
        # self.orig_rect = self.rect

        # self.large = pygame.transform.scale2x(self.image)
        # self.large_rect = self.large.get_rect()
        # self.large_rect.center = pos

        self.opp = opp

    def draw(self, win):
        win.blit(self.image, self.rect)

    def click(self, pos):
        if self.rect.collidepoint(pos):
            return True
        return False
