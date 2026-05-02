import pygame
import sys
import random
import math

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (150, 0, 0)

class BoiledOneGame:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("THE BOILED ONE IS WATCHING")
        self.clock = pygame.time.Clock()
        self.running = True

        try:
            self.scare_img = pygame.image.load("boiled_one.jpg").convert()
            self.entity_img = pygame.transform.scale(self.scare_img, (150, 250))
            self.full_scare = pygame.transform.scale(self.scare_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
            self.static_snd = pygame.mixer.Sound("static.wav")
            self.scream_snd = pygame.mixer.Sound("scream.wav")
            self.static_snd.play(loops=-1)
            self.static_snd.set_volume(0.1)
        except:
            print("Missing files! Check for boiled_one.jpg, static.wav, and scream.wav")
            self.entity_img = pygame.Surface((150, 250))
            self.entity_img.fill(RED)
            self.full_scare = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            self.full_scare.fill(RED)
            self.static_snd = None
            self.scream_snd = None

        self.player_pos = pygame.math.Vector2(500, 400)
        self.player_speed = 4

        self.entity_pos = pygame.math.Vector2(random.randint(0, 1000), random.randint(0, 800))
        self.entity_speed = 1.5

        self.is_scared = False
        self.scare_timer = 0

    def draw_static(self, intensity):
        for _ in range(int(intensity * 100)):
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)
            pygame.draw.rect(self.screen, (150, 150, 150), (x, y, 2, 2))

    def run(self):
        while self.running:
            self.screen.fill(BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            if not self.is_scared:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]: self.player_pos.y -= self.player_speed
                if keys[pygame.K_s]: self.player_pos.y += self.player_speed
                if keys[pygame.K_a]: self.player_pos.x -= self.player_speed
                if keys[pygame.K_d]: self.player_pos.x += self.player_speed

                direction = (self.player_pos - self.entity_pos)
                dist = direction.length()
                if dist > 0:
                    direction = direction.normalize()
                    self.entity_pos += direction * self.entity_speed

                if self.static_snd:
                    volume = max(0.1, 1.0 - (dist / 600))
                    self.static_snd.set_volume(min(volume, 0.8))

                if dist < 60:
                    self.is_scared = True
                    self.scare_timer = 60
                    if self.scream_snd:
                        self.scream_snd.play()

                rel_pos = self.entity_pos - self.player_pos + pygame.math.Vector2(500, 400)
                self.screen.blit(self.entity_img, (rel_pos.x - 75, rel_pos.y - 125))

                overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
                overlay.fill((5, 5, 5))
                pygame.draw.circle(overlay, (255, 255, 255), (500, 400), 250)
                self.screen.blit(overlay, (0, 0), special_flags=pygame.BLEND_MULT)

                if dist < 300:
                    self.draw_static((300 - dist) / 50)

            else:
                shake = (random.randint(-30, 30), random.randint(-30, 30))
                self.screen.blit(self.full_scare, shake)
                self.draw_static(10)
                self.scare_timer -= 1
                if self.scare_timer <= 0:
                    self.is_scared = False
                    self.player_pos = pygame.math.Vector2(500, 400)
                    self.entity_pos = pygame.math.Vector2(random.randint(-500, 1500), random.randint(-500, 1300))

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = BoiledOneGame()
    game.run()
