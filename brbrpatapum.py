# import pygame
# import random

# pygame.init()


# # Размеры экрана
# WIDTH, HEIGHT = 1000, 700
# win = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Космическая битва")

# # FPS
# clock = pygame.time.Clock()
# FPS = 60

# # Загрузка изображений
# player_img = pygame.image.load("Cosmo//ship.png")

# enemy_imgs = [
#     pygame.image.load("Cosmo//vrag1.png"),
#     pygame.image.load("Cosmo//vrag2.png"),
#     pygame.image.load("Cosmo//vrag3.png"),
#     pygame.image.load("Cosmo//vrag4.png")
# ]

# boss_imgs = [
#     pygame.image.load("Cosmo//vrag5.png"),
#     pygame.image.load("Cosmo//vrag6.png"),
#     pygame.image.load("Cosmo//vrag7.png")
# ]

# # Игрок
# player_x = WIDTH // 2
# player_y = HEIGHT - 120
# player_speed = 5

# # Списки врагов
# enemies = []
# bosses = []

# # Таймер появления
# spawn_timer = 0

# # Основной цикл
# run = True
# while run:
#     clock.tick(FPS)
#     win.fill((10, 10, 30))  # Тёмный фон

#     # Обработка событий
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#     # Управление игроком
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT] and player_x > 0:
#         player_x -= player_speed
#     if keys[pygame.K_RIGHT] and player_x < WIDTH - player_img.get_width():
#         player_x += player_speed

#     # Спавн врагов и боссов
#     spawn_timer += 1
#     if spawn_timer > 60:
#         if random.random() < 0.1:
#             boss_img = random.choice(boss_imgs)
#             boss_x = random.randint(0, WIDTH - boss_img.get_width())
#             bosses.append([boss_img, boss_x, -boss_img.get_height(), 1])  # [image, x, y, speed]
#         else:
#             enemy_img = random.choice(enemy_imgs)
#             enemy_x = random.randint(0, WIDTH - enemy_img.get_width())
#             enemies.append([enemy_img, enemy_x, -enemy_img.get_height(), random.randint(2, 5)])
#         spawn_timer = 0

#     # Движение врагов
#     for enemy in enemies:
#         enemy[2] += enemy[3]
#         win.blit(enemy[0], (enemy[1], enemy[2]))

#     # Движение боссов
#     for boss in bosses:
#         boss[2] += boss[3]
#         win.blit(boss[0], (boss[1], boss[2]))

#     # Отображение игрока
#     win.blit(player_img, (player_x, player_y))

#     pygame.display.update()

# pygame.quit()

import os
print("Текущий рабочий каталог:", os.getcwd())
