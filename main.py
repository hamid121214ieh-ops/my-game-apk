import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Neon Overdrive")

BLACK = (10, 10, 20)
NEON_PINK = (255, 0, 127)

clock = pygame.time.Clock()

class PlayerCar:
    def __init__(self):
        self.x = WIDTH // 2 - 25
        self.y = HEIGHT - 120
        self.width = 50
        self.height = 90
        self.speed = 6

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed
        
        if self.x < 50: self.x = 50
        if self.x > WIDTH - 100: self.x = WIDTH - 100

    def draw(self, surface):
        pygame.draw.rect(surface, NEON_PINK, (self.x, self.y, self.width, self.height), border_radius=10)

player = PlayerCar()

running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.handle_input()
    pygame.draw.rect(screen, (30, 30, 40), (40, 0, WIDTH - 80, HEIGHT))
    player.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

