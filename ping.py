from pygame import *
from random import randint
from time import time as timer

window = display.set_mode((700, 500))
display.set_caption("fight")
background = transform.scale(image.load("Background.jpg"),(700, 500))
window.blit(background,(0, 0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (55, 55))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_R(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y < 640:
            self.rect.y += self.speed
        if keys_pressed[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
    def update_L(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y < 640:
            self.rect.y += self.speed
        if keys_pressed[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed



player_1 = Player("Gojo.jpg", 650, 100, 25)
player_2 = Player("Sukuna.jpg", 0, 100, 25)
ball = GameSprite("Purple.png", 200, 400, 3)


game = True
finish = False
FPS = 60
clock = time.Clock()
speed_y = -3
speed_x = 3


while game:
    window.blit(background, (0,0))

    for e in event.get():
        if e.type == QUIT:
            game = False
            
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y -= speed_y
    
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if sprite.collide_rect(player_1, ball) or sprite.collide_rect(player_2, ball):
            speed_x *= -1 

        if ball.rect.y > 500 or ball.rect.y < 0:
            speed_y *= -1

            player_1.reset()
            player_2.reset()
            ball.reset()



            player_1.update_R()
            player_2.update_L()






        display.update()
    clock.tick(FPS)
    time.delay(50)
