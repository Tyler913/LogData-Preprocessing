import pygame
import random

# 游戏窗口尺寸
WIDTH = 640
HEIGHT = 480

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 蛇的方向
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("贪吃蛇")
        self.font = pygame.font.SysFont(None, 36)
        self.reset()

    def reset(self):
        self.score = 0
        self.snake_pos = [(WIDTH // 2, HEIGHT // 2)]
        self.snake_dir = random.choice([UP, DOWN, LEFT, RIGHT])
        self.food_pos = self.generate_food_pos()

    def generate_food_pos(self):
        while True:
            pos = (random.randint(0, WIDTH - 1) // 20 * 20, random.randint(0, HEIGHT - 1) // 20 * 20)
            if pos not in self.snake_pos:
                return pos

    def draw_snake(self):
        for pos in self.snake_pos:
            pygame.draw.rect(self.screen, GREEN, (pos[0], pos[1], 20, 20))

    def draw_food(self):
        pygame.draw.rect(self.screen, RED, (self.food_pos[0], self.food_pos[1], 20, 20))

    def move_snake(self):
        x, y = self.snake_pos[0]
        if self.snake_dir == UP:
            y -= 20
        elif self.snake_dir == DOWN:
            y += 20
        elif self.snake_dir == LEFT:
            x -= 20
        elif self.snake_dir == RIGHT:
            x += 20
        self.snake_pos.insert(0, (x, y))

        if self.snake_pos[0] == self.food_pos:
            self.score += 1
            self.food_pos = self.generate_food_pos()
        else:
            self.snake_pos.pop()

    def check_collision(self):
        x, y = self.snake_pos[0]
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or self.snake_pos[0] in self.snake_pos[1:]:
            return True
        return False

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.snake_dir != DOWN:
                        self.snake_dir = UP
                    elif event.key == pygame.K_DOWN and self.snake_dir != UP:
                        self.snake_dir = DOWN
                    elif event.key == pygame.K_LEFT and self.snake_dir != RIGHT:
                        self.snake_dir = LEFT
                    elif event.key == pygame.K_RIGHT and self.snake_dir != LEFT:
                        self.snake_dir = RIGHT

            self.screen.fill(BLACK)

            self.move_snake()
            if self.check_collision():
                self.reset()

            self.draw_snake()
            self.draw_food()

            score_text = self.font.render("Score: " + str(self.score), True, WHITE)
            self.screen.blit(score_text, (10, 10))

            pygame.display.flip()
            self.clock.tick(10)

        pygame.quit()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()