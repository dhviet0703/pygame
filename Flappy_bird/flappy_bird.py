import pygame
from random import randint

pygame.init()
WIDTH, HEIGHT = (400, 600)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

GREY = (150, 150, 150)
GREEN = (0, 150, 0)
BLUE = (0, 0, 150)
RED = (150, 0, 0)
BLACK = (0, 0, 0)

TUBE_VELOCITY = 3
TUBE_WIDTH = 50
TUBE_GAP = 170
tube1_x = 0
tube2_x = 200
tube3_x = 400

tub1_height = randint(100, 400)
tub2_height = randint(100, 400)
tub3_height = randint(100, 400)
tube1_pass = False
tube2_pass = False
tube3_pass = False
pausing = False

BIRD_X = 50
bird_y = 200
BIRD_WIDTH = 35
BIRD_HIGHT = 35
bird_drop_velocity = 0
GRAVITY = 0.5

score = 0
font = pygame.font.SysFont('sans', 20)
background_image = pygame.image.load("background.png")
background_image = pygame.transform.scale(background_image, (400,600))
bird_image = pygame.image.load("bird.png")
bird_image = pygame.transform.scale(bird_image, (BIRD_WIDTH, BIRD_HIGHT))

while running:
	clock.tick(60)
	screen.fill(GREEN)
	screen.blit(background_image, (0,0))

	#Vẽ 3 ống
	tube1_rect = pygame.draw.rect(screen, BLUE, (tube1_x, 0, TUBE_WIDTH, tub1_height))
	tube2_rect = pygame.draw.rect(screen, BLUE, (tube2_x, 0, TUBE_WIDTH, tub2_height))
	tube3_rect = pygame.draw.rect(screen, BLUE, (tube3_x, 0, TUBE_WIDTH, tub3_height))

	#Vẽ 3 ống đối diện
	tube1_rect_inv = pygame.draw.rect(screen, BLUE, (tube1_x, tub1_height + TUBE_GAP, TUBE_WIDTH, HEIGHT - tub1_height - TUBE_GAP))
	tube2_rect_inv = pygame.draw.rect(screen, BLUE, (tube2_x, tub2_height + TUBE_GAP, TUBE_WIDTH, HEIGHT - tub2_height - TUBE_GAP))
	tube3_rect_inv = pygame.draw.rect(screen, BLUE, (tube3_x, tub3_height + TUBE_GAP, TUBE_WIDTH, HEIGHT - tub3_height - TUBE_GAP))

	# 3 ống di chuyển sang trái
	tube1_x = tube1_x - TUBE_VELOCITY
	tube2_x = tube2_x - TUBE_VELOCITY
	tube3_x = tube3_x - TUBE_VELOCITY

	# Vẽ chim
	bird_rect = screen.blit(bird_image, (BIRD_X, bird_y))


	# Chim rơi
	bird_y += bird_drop_velocity
	bird_drop_velocity += GRAVITY

	# Tạo ống mới
	if tube1_x < -TUBE_WIDTH:
		tube1_x = 550
		tub1_height = randint(100, 400)
		tube1_pass = False
	if tube2_x < -TUBE_WIDTH:
		tube2_x = 550
		tub2_height = randint(100, 400)
		tube2_pass = False
	if tube3_x < -TUBE_WIDTH:
		tube3_x = 550
		tub3_height = randint(100, 400)
		tube3_pass = False

	score_txt = font.render("Score: " + str(score), True, BLACK)
	screen.blit(score_txt, (5, 5))

	if tube1_x + TUBE_WIDTH <= BIRD_X and tube1_pass == False:
		score += 1
		tube1_pass = True
	if tube2_x + TUBE_WIDTH <= BIRD_X and tube2_pass == False:
		score += 1
		tube2_pass = True
	if tube3_x + TUBE_WIDTH <= BIRD_X and tube3_pass == False:
		score += 1
		tube3_pass = True

	#Chim chết
	for tube in [tube1_rect, tube2_rect, tube3_rect, tube1_rect_inv, tube2_rect_inv, tube3_rect_inv]:
		if bird_rect.colliderect(tube):
			TUBE_VELOCITY = 0
			bird_drop_velocity = 0
			game_over_txt = font.render("Game over, Score: " + str(score), True, BLACK)
			screen.blit(game_over_txt, (100, 250))
			press_space_txt = font.render("Press Space to continue", True, BLACK)
			screen.blit(press_space_txt, (85,270))
			pausing = True

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				bird_drop_velocity = 0
				bird_drop_velocity -= 10
				if pausing:
					tube1_x = 400
					tube2_x = 600
					tube3_x = 800
					bird_y = 400
					TUBE_VELOCITY = 2.5
					score = 0
					pausing = False


	pygame.display.flip()

pygame.quit()




