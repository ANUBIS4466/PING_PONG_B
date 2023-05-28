#Sidorenko - 1
from pygame import*
'''Необходимые классы'''

#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
    #конструктор класса
        #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()

        self.image = transform.scale(image.load(player_image),(widt, height))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#Fedaev - 2

#Zhiharev - 3
while game:	
    for e in event.get():	
        if e.type == QUIT:
    game = False
    if finish != True:	
        window.fill(back)
        racketl.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(racketl, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
#3ralenno - 4



