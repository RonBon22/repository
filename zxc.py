from pygame import *
from random import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y > 5:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y > 5:
            self.rect.y += self.speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Bool(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

win_width = 900
win_height = 700
window = display.set_mode((win_width,win_height))
display.set_caption("MAZE")
background = transform.scale(image.load("galaxy.jpg"),(win_width,win_height))

font.init()
font1 = font.Font(None, 80)
font2 = font.Font(None, 36)
main_font = font.Font(None, 70)
start_font = font.Font(None, 50)

win = main_font.render("YOU WIN!", True, (255,215,0))
lose = main_font.render("YOU LOST!", True, (180,0,0))




bowl = Bool("water.png", randint(80,win_width - 80), -40, 80, 50, randint(1,5))
player1 = Player("cat.png",700 ,win_height - 180, 80, 100, 10)
player2 = Player("rocket.png",5 ,win_height - 100, 80, 100, 10)

mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()


max_lost = 3

goal = 10

score = 0
lost = 0
clock = time.Clock()
run = True
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.blit(background,(0,0))
    
        text = font2.render("Счет: " + str(score), 1, (255,255,255))
        window.blit(text, (10,20))

        text_lose = font2.render("Пропущено: " + str(lost), 1, (255,255,255))
        window.blit(text_lose, (10,50))

        clock.tick(60)
        
        player2.update()
        player1.update()
        bowl.update()

        player1.reset()
        player2.reset()
        bowl.reset()


    if score >= goal:
        finish = True
        window.blit(win,(200,200))

    display.update()
time.delay(50)
