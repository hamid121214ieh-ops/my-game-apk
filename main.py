import pygame
import sys

# --- Audio Module ---
class Audio:
    def __init__(self):
        try:
            pygame.mixer.init()
            pygame.mixer.music.load("assets/audio/background_music.mp3")
            pygame.mixer.music.play(-1)
        except:
            print("Audio files load nahi ho saki.")

# --- UI Module ---
class UI:
    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 28)
    def draw_score(self, surface, score):
        text = self.font.render(f"Score: {score}", True, (255, 255, 255))
        surface.blit(text, (25, 25))

# --- Enemy Module ---
class Enemy:
    def __init__(self, x, y):
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 255))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 4
    def update(self, screen_width):
        self.rect.x -= self.speed
        if self.rect.right < 0: self.rect.left = screen_width + 100
    def draw(self, surface): surface.blit(self.image, self.rect)

# --- Player Module ---
class Player:
    def __init__(self, x, y):
        self.image = pygame.Surface((50, 80))
        self.image.fill((255, 0, 127))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocity = pygame.math.Vector2(0, 0)
        self.gravity = 0.6
        self.jump_power = -12
        self.on_ground = False
        self.speed = 6
    def update(self, keys, touch_pos, screen_width, screen_height):
        self.velocity.x = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]: self.velocity.x = -self.speed
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]: self.velocity.x = self.speed
        elif touch_pos and touch_pos[0] < screen_width / 2: self.velocity.x = -self.speed
        elif touch_pos: self.velocity.x = self.speed
        if (keys[pygame.K_SPACE] or pygame.mouse.get_pressed()[0]) and self.on_ground:
            self.velocity.y = self.jump_power
            self.on_ground = False
        self.velocity.y += self.gravity
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
        if self.rect.bottom >= screen_height - 100:
            self.rect.bottom = screen_height - 100
            self.velocity.y = 0
            self.on_ground = True
    def draw(self, surface): surface.blit(self.image, self.rect)

# --- Renderer Module ---
class Renderer:
    def __init__(self, screen_width, screen_height):
        self.screen_width, self.screen_height = screen_width, screen_height
    def draw(self, surface, player, enemies):
        surface.fill((15, 15, 30))
        pygame.draw.rect(surface, (40, 40, 60), (0, self.screen_height - 100, self.screen_width, 100))
        player.draw(surface)
        for enemy in enemies: enemy.draw(surface)

# --- Main Game Loop ---
pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Pixel Runner - Final")
CLOCK = pygame.time.Clock()
renderer = Renderer(1280, 720)
player = Player(150, 500)
enemies = [Enemy(1200, 500)]
ui = UI()
audio = Audio()
score = 0
running = True
while running:
    touch_pos = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        elif event.type == pygame.FINGERDOWN: touch_pos = (event.x * 1280, event.y * 720)
    if pygame.mouse.get_pressed()[0]: touch_pos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    player.update(keys, touch_pos, 1280, 720)
    for enemy in enemies: 
        enemy.update(1280)
        if player.rect.colliderect(enemy.rect): score = 0
    score += 1
    renderer.draw(SCREEN, player, enemies)
    ui.draw_score(SCREEN, score // 10)
    pygame.display.flip()
    CLOCK.tick(60)
pygame.quit()
sys.exit()

