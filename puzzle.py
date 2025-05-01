def draw_tiles():
    for i in range(len(tiles)):
        tile = tiles[i]
        row = i // ROWS
        col = i % COLS
        x = col * (tile_width + MARGIN) + MARGIN
        y = row * (tile_height + MARGIN) + MARGIN
        if i == selected:
            pygame.draw.rect(screen, (0, 250, 0), (x - MARGIN, y - MARGIN, tile_width + MARGIN*2, tile_height + MARGIN*2))
        screen.blit(tile, (x, y))

def draw_swaps():
    font = pygame.font.SysFont('Arial', 32)
    text = font.render(f'Количество перестоновок: {swaps}', True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (size[0] // 2, size[1] // 2 + 100)
    pygame.draw.rect(screen, (0, 0, 0), text_rect.inflate(4, 4))
    screen.blit(text, text_rect)

def game_over():
    font = pygame.font.SysFont('Arial', 64)
    text = font.render('Ура, картинка собрана!', True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (size[0] // 2, size[1] // 2 + 100)
    pygame.draw.rect(screen, (0, 0, 0), text_rect.inflate(4, 4))
    screen.blit(text, text_rect)


import random
import os
import pygame
pygame.init()

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Моя игра')
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)

pictures = os.listdir('pictures')
picture = random.choice(pictures)
image = pygame.image.load('pictures/' + picture)

ROWS = 6
COLS = 6
MARGIN = 2

image_width, image_height = image.get_size()
tile_width = image_width // COLS
tile_height = image_height // ROWS

tiles = []

for i in range(ROWS):
    for j in range(COLS):
        rect = pygame.Rect(j * tile_width, i * tile_height, tile_width, tile_height)
        tile = image.subsurface(rect)
        tiles.append(tile)


origin_tiles = tiles.copy()
random.shuffle(tiles)

selected = None
swaps = 0

FPS = 60
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for i in range(len(tiles)):
                row = i // ROWS
                col = i % COLS
                x = col * (tile_width + MARGIN) + MARGIN
                y = row * (tile_height + MARGIN) + MARGIN

                if x <= mouse_x <= x + tile_width and y <= mouse_y <= y + tile_height:
                    if selected is not None and selected != i:
                        tiles[i], tiles[selected] = tiles[selected], tiles[i]
                        selected = None
                        swaps += 1
                    elif selected == i:
                        selected = None
                    else:
                        selected = i


    screen.fill(BACKGROUND)

    draw_tiles()
    draw_swaps()

    if tiles == origin_tiles:
        game_over()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
