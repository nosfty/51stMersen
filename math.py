import time

import pygame
import sys
import gmpy2
import math

from config import *

p = the_degree_of_the_51st_Mersenne_number
length = SLICE_END_POS
a = SLICE_START_POS
f = TIME_ELAPSED
dps = UPDATE_IN

mersen_number = gmpy2.mpz(2)**p - 1


mersen_str = str(mersen_number)



pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Счетчик")

black = (0, 0, 0)
font = pygame.font.Font(None, 36)

running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)

    text = font.render(mersen_str[a:length], True, (255, 255, 255))
    text2 = font.render("51 mersen number", True, (255, 255, 255))
    text3 = font.render( f"Estimated digits: {str(len(mersen_str) - length)}, estimated time {round(dps * len(mersen_str) - f, 2)}", True, (255, 255, 255))

    text_rect = text.get_rect(center=(screen_width//2, screen_height//2))
    text2_rect = text2.get_rect(center=(screen_width // 2, screen_height // 3))
    text3_rect = text3.get_rect(center=(screen_width // 2, screen_height // 1.5))
    screen.blit(text, text_rect)
    screen.blit(text2, text2_rect)
    screen.blit(text3, text3_rect)

    pygame.display.flip()

    if length < 40:

        length += 1

    else:
        a += 1
        length += 1

    f += dps
    time.sleep(dps)

pygame.quit()
sys.exit()
