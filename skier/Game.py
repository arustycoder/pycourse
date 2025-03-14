import random
import sys

from pygame.sprite import Sprite

import cfg
import pygame
import os

class SkierClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.direction = 0 # 0: forward, 1,2: right, 3,4: left
        self.image_paths = cfg.SKIER_IMAGE_PATHS[:-1]
        self.image = pygame.image.load(self.image_paths[self.direction])
        self.rect = self.image.get_rect()
        self.rect.center = (320, 100)
        self.speed = [self.direction, 6 - abs(self.direction) * 2]
        self.flag_count = 0
        self.score = 0

    def turn(self, num):
        self.direction += num
        self.direction = max(-2, self.direction)
        self.direction = min(2, self.direction)
        center = self.rect.center
        self.image = pygame.image.load(self.image_paths[self.direction])
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speed = [self.direction, 6 - abs(self.direction) * 2]
        return self.speed

    def move(self):
        self.rect.centerx += self.speed[0]
        self.rect.centerx = max(20, self.rect.centerx)
        self.rect.centerx = min(620, self.rect.centerx)

    def set_fall(self):
        self.image = pygame.image.load(cfg.SKIER_IMAGE_PATHS[-1])

    def set_forward(self):
       self.direction = 0
       self.image = pygame.image.load(self.image_paths[self.direction])


class ObstacleClass(pygame.sprite.Sprite):
    def __init__(self, img_path, location, attribute):
        pygame.sprite.Sprite.__init__(self)
        self.img_path = img_path
        self.image = pygame.image.load(self.img_path)
        self.location = location
        self.rect = self.image.get_rect()
        self.rect.center = self.location
        self.attribute = attribute
        self.passed = False

    def move(self, num):
        self.rect.centery = self.location[1] - num

def create_obstacle_group(s, e, num=10):
    obstacle_group = pygame.sprite.Group()
    locations = []
    for i in range(num):
        row = random.randint(s, e)
        col = random.randint(0,10)
        location = [col*64+20, row*64+20]
        if location not in locations:
            locations.append(location)
            if i % 4 == 0:
                attribute = "tree"
            if i % 4 == 1:
                attribute = "stone"
            else:
                attribute = "flag"
            image_path = cfg.OBSTACLE_PATHS[attribute]
            obstacle = ObstacleClass(image_path, location, attribute)
            obstacle_group.add(obstacle)
    return obstacle_group

def add_obstacles(obstacles0, obstacles1):
    obstacle_group = pygame.sprite.Group()
    for obstacle in obstacles0:
        obstacle_group.add(obstacle)
    for obstacle in obstacles1:
        obstacle_group.add(obstacle)
    return obstacle_group

def show_score(screen, score, pos=(10, 10)):
    font = pygame.font.Font(cfg.FONT_PATH, 30)
    score_text = font.render("Score: %d" % score, True, (0,0,0))
    screen.blit(score_text, pos)

def show_start_interface(screen, screen_size):
    screen.fill((255, 255, 255))
    tfont = pygame.font.Font(cfg.FONT_PATH, screen_size[0] // 10)
    cfont = pygame.font.Font(cfg.FONT_PATH, screen_size[0] // 20)
    title = tfont.render(u'Skier Game', True, (255, 0, 0))
    content = cfont.render(u'Press any key to start', True, (0, 0, 255))
    trect = title.get_rect()
    trect.midtop = (screen_size[0] / 2, screen_size[1] / 5)
    crect = content.get_rect()
    crect.midtop = (screen_size[0] / 2, screen_size[1] / 2)
    screen.blit(title, trect)
    screen.blit(content, crect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                return
        pygame.display.update()

def update_frame(screen, obstacles, skier):
    screen.fill((255, 255, 255))
    obstacles.draw(screen)
    screen.blit(skier.image, skier.rect)
    show_score(screen, skier.score)
    pygame.display.update()

def main():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(cfg.BGM_PATH)
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)

    screen = pygame.display.set_mode(cfg.SCREEN_SIZE)
    pygame.display.set_caption('Skier Game')

    show_start_interface(screen, cfg.SCREEN_SIZE)

    while True:
        skier = SkierClass()
        obstacles0 = create_obstacle_group(20,29, num=15)
        obstacles1 = create_obstacle_group(10,19, num=15)
        obstacles_flag = 0
        obstacles = add_obstacles(obstacles0, obstacles1)

        clock = pygame.time.Clock()

        distance = 0

        restart = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        skier.turn(-1)
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        skier.turn(1)
                    elif event.key == pygame.K_q: # Press `q` to quit the game
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_r: # Press `r` to restart the game
                        restart = True

            if restart:
                break # Exit the inner loop to restart the game

            skier.move()
            distance += skier.speed[1]
            if distance >= 640 and obstacles_flag == 0:
                obstacles_flag = 1
                obstacles0 = create_obstacle_group(20,29, num=15)
                obstacles = add_obstacles(obstacles0, obstacles1)

            if distance >= 1280 and obstacles_flag == 1:
                obstacles_flag = 0
                distance -= 1280
                for obstacle in obstacles0:
                    obstacle.location[1] -= 1280
                obstacles1 = create_obstacle_group(10,19, num=15)
                obstacles = add_obstacles(obstacles0, obstacles1)

            for obstacle in obstacles:
                obstacle.move(distance)

            hit_obstacles = pygame.sprite.spritecollide(skier, obstacles, False)
            if hit_obstacles:
                if hit_obstacles[0].attribute == "tree" and not hit_obstacles[0].passed:
                    skier.set_fall()
                    skier.score -= 5
                    skier.speed[1] = 2
                    update_frame(screen, obstacles, skier)
                    skier.set_forward()
                    skier.speed[1] = 6
                    hit_obstacles[0].passed = True
                elif hit_obstacles[0].attribute == "stone" and not hit_obstacles[0].passed:
                    skier.set_fall()
                    skier.score -= 10
                    skier.speed[1] = 2
                    update_frame(screen, obstacles, skier)
                    pygame.time.delay(1000)
                    skier.set_forward()
                    skier.speed[1] = 6
                    hit_obstacles[0].passed = True
                elif hit_obstacles[0].attribute == "flag" and not hit_obstacles[0].passed:
                    skier.score += 10
                    skier.flag_count += 1
                    if skier.flag_count >= 10:
                        skier.speed[1] = 8
                    obstacles.remove(hit_obstacles[0])

            update_frame(screen, obstacles, skier)
            if skier.score < 0:
                screen.fill((255, 255, 255))
                font = pygame.font.Font(cfg.FONT_PATH)
                game_over_text = font.render("Game Over", True, (255,0,0))
                prompt_text = font.render("Press 'r' to restart or 'q' to quit.", True, (0,0,255))
                game_over_rect = game_over_text.get_rect(center=(cfg.SCREEN_SIZE[0] // 2, cfg.SCREEN_SIZE[1] // 2))
                prompt_rect = prompt_text.get_rect(center=(cfg.SCREEN_SIZE[0] // 2, cfg.SCREEN_SIZE[1] // 2 + 50))
                screen.blit(game_over_text, game_over_rect)
                screen.blit(prompt_text, prompt_rect)
                pygame.display.update()

                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                pygame.quit()
                                sys.exit()
                            elif event.key == pygame.K_r:
                                restart = True
                                #break

                    if restart:
                        break # Exit the inner loop to restart the game

            clock.tick(cfg.FPS)

        if not restart:
            break # Exit the outer loop  if the game should quit

    # End of `While True`


if __name__ == '__main__':
    main()