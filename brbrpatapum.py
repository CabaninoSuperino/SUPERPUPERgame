import pygame
import random

pygame.init()

screen_width = 900  
screen_height = 750 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SUPERPUPERgame")


background_color = (0, 0, 0)


player_scale = 0.2
enemy_scale = 0.35 


def load_scaled_image(image_path, player_scale):
    image = pygame.image.load(image_path)
    original_width, original_height = image.get_width(), image.get_height()
    new_width = int(original_width * player_scale)
    new_height = int(original_height * player_scale)
    return pygame.transform.scale(image, (new_width, new_height))


ship_image = load_scaled_image("Cosmo/ship.png", player_scale)
vrag_images = [
    load_scaled_image("Cosmo/exp1.png", enemy_scale),
    load_scaled_image("Cosmo/exp2.png", enemy_scale),
    load_scaled_image("Cosmo/exp3.png", enemy_scale),
    load_scaled_image("Cosmo/exp4.png", enemy_scale),
    load_scaled_image("Cosmo/exp5.png", enemy_scale),
    load_scaled_image("Cosmo/exp6.png", enemy_scale ),
]

player_x, player_y = screen_width // 2, screen_height - 100
enemy_ships = []


def create_enemy():
    enemy_image = random.choice(vrag_images)
    enemy_x = random.randint(0, screen_width - enemy_image.get_width())
    enemy_y = random.randint(-100, -40)
    return enemy_image, enemy_x, enemy_y

for _ in range(6):
    enemy_ships.append(create_enemy())

running = True
while running:
    screen.fill(background_color)
    
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player_x > 0:
        player_x -= 5
    if keys[pygame.K_d] and player_x < screen_width - ship_image.get_width():
        player_x += 5
    if keys[pygame.K_w] and player_y > 0:
        player_y -= 5
    if keys[pygame.K_s] and player_y < screen_height - ship_image.get_height():
        player_y += 5

    screen.blit(ship_image, (player_x, player_y))

    for i, (enemy_image, enemy_x, enemy_y) in enumerate(enemy_ships):

        enemy_y += 5
        if enemy_y > screen_height:
            enemy_image, enemy_x, enemy_y = create_enemy()  


        screen.blit(enemy_image, (enemy_x, enemy_y))


        if enemy_x > screen_width:
            enemy_x = screen_width - enemy_image.get_width()
        elif enemy_x < 0:
            enemy_x = 0

        enemy_ships[i] = (enemy_image, enemy_x, enemy_y)

    pygame.display.flip()
    
    pygame.time.Clock().tick(60)

pygame.quit()
