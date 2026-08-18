import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions (Mobile portrait friendly)
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Professional Mobile Game")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
GREEN = (0, 255, 128)
RED = (255, 60, 60)

# Fonts for Score
font = pygame.font.SysFont(None, 40)

# Player settings
player_width = 100
player_height = 80
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - 150
player_speed = 10

# Target/Item settings
target_width = 60
target_height = 60
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = -100
target_speed = 6

score = 0

def run_game():
    global player_x, target_x, target_y, target_speed, score
    
    while True:
        screen.fill(BLACK)
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Keyboard controls (For testing in terminal/PC)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed

        # Touch / Mouse controls (For Mobile APK)
        if pygame.mouse.get_pressed()[0]:
            mouse_x, _ = pygame.mouse.get_pos()
            player_x = mouse_x - player_width // 2

        # Keep player inside screen boundaries
        if player_x < 0:
            player_x = 0
        elif player_x > SCREEN_WIDTH - player_width:
            player_x = SCREEN_WIDTH - player_width

        # Target falling movement
        target_y += target_speed
        if target_y > SCREEN_HEIGHT:
            target_y = -100
            target_x = random.randint(0, SCREEN_WIDTH - target_width)
            score -= 1 # Penalty for missing

        # Collision detection (Rectangles)
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        target_rect = pygame.Rect(target_x, target_y, target_width, target_height)

        if player_rect.colliderect(target_rect):
            score += 1
            target_y = -100
            target_x = random.randint(0, SCREEN_WIDTH - target_width)
            target_speed += 0.2 # Difficulty increases as score goes up

        # Draw Player (Green Box)
        pygame.draw.rect(screen, GREEN, player_rect, border_radius=15)

        # Draw Target/Falling Item (Red Box)
        pygame.draw.rect(screen, RED, target_rect, border_radius=15)

        # Render Score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (30, 30))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    run_game()

