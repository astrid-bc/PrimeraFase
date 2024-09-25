import pygame
import random

pygame.init()

WIDTH, HEIGHT = 550, 550
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Game")

WHITE = (255, 255, 255)

car_image = pygame.image.load('assets/car.png')
enemy_image = pygame.image.load('assets/enemy.png')
background_image = pygame.image.load('assets/background.png')

# Carro
class Car:
    def __init__(self):
        self.image = car_image
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 100))
        self.score = 0

    def move(self, dx):
        self.rect.x += dx
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > WIDTH - self.rect.width:
            self.rect.x = WIDTH - self.rect.width

# Enemigo
class Enemy:
    def __init__(self):
        self.image = enemy_image
        self.rect = self.image.get_rect(center=(random.randint(0, WIDTH), -50))

    def move(self):
        self.rect.y += 5
        if self.rect.y > HEIGHT:
            self.rect.y = -50
            self.rect.x = random.randint(0, WIDTH)

# Función principal
def main():
    clock = pygame.time.Clock()
    car = Car()
    enemies = [Enemy() for _ in range(3)]
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            car.move(-5) 
        if keys[pygame.K_RIGHT]:
            car.move(5)

        for enemy in enemies:
            enemy.move()
            if car.rect.colliderect(enemy.rect):
                running = False

        car.score += 1

        screen.blit(background_image, (0, 0))
        screen.blit(car.image, car.rect)
        for enemy in enemies:
            screen.blit(enemy.image, enemy.rect)

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Puntaje: {car.score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()