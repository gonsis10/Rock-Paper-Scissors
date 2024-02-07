from network import Network
from player_ui import PlayerUI
from opp_ui import OpponentUI
import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600

win = pygame.display.set_mode((WIDTH, HEIGHT))

ROCK = pygame.transform.rotate(pygame.image.load(
    'assets/rock.png').convert_alpha(), 90)
PAPER = pygame.transform.rotate(pygame.image.load(
    'assets/paper.png').convert_alpha(), 90)
SCISSORS = pygame.transform.rotate(pygame.image.load(
    'assets/scissors.png').convert_alpha(), 90)
UNKNOWN = pygame.transform.scale(pygame.image.load(
    'assets/question.png').convert_alpha(), (64, 64))

# net = Network()
player_ui = PlayerUI((WIDTH, HEIGHT), (ROCK, PAPER, SCISSORS))
opp_ui = OpponentUI((WIDTH, HEIGHT), (ROCK, PAPER, SCISSORS))


# def ask():
#     while True:
#         try:
#             opp_ui.rotate_signs(int(input()))
#         except:
#             pass


# start_new_thread(ask, ())


def check_winner():
    pass

def redraw(win, game, id):
    win.fill((0, 0, 0))
    player_ui.draw(win)
    opp_ui.draw(win)

run = True
while run:
    win.fill((0, 0, 0))
    player_ui.draw(win)
    opp_ui.draw(win)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            player_ui.check(pos)

    pygame.display.update()

pygame.quit()
