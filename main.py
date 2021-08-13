from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
        sprite.Sprite.__init__(self) 
        self.image = transform.scale(image.load(player_image),(player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class RightEnemy(GameSprite):
    side="left"
    def update(self):
        if self.rect.x <= 410:
            self.side = "right"
        if self.rect.x >= win_width - 85:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class LeftEnemy(GameSprite):
    side="left"
    def update(self):
        if self.rect.x <= 10:
            self.side = "right"
        if self.rect.x >= 160: 
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class UpEnemy(GameSprite):
    side="up"
    def update(self):
        if self.rect.y <= 10:
            self.side = "down"
        if self.rect.y >= 110: 
            self.side = "up"
        if self.side == "up":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        sprite.Sprite.__init__(self)
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
    
        # picture of the wall - a rectangle of the desired size and color
        self.image = Surface([self.width, self.height])
        self.image.fill((color_1, color_2, color_3))
    
        # each sprite should store the rect (rectangle) property
        self.rect = self.image.get_rect()
        self.rect = Rect(wall_x, wall_y, wall_width, wall_height)
    def draw_wall(self):
        draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))

win_width = 700
win_height = 500
display.set_caption("Labyrinth")
window = display.set_mode((win_width, win_height))

level = 1 
hero = Player("hero.png",50,400,10,80,80) 
enemy = RightEnemy("cyborg.png",600,250,12,72,72)
enemy2 = LeftEnemy("devil.png",20,100,6,110,110)
star = GameSprite("star.png",420,40,0,80,80) 
#level2
hero2 = Player("chef.png",50,400,10,90,100) 
enemy = RightEnemy("cyborg.png",600,250,12,72,72)
enemy2 = LeftEnemy("devil.png",20,100,6,110,110)
enemy3 = UpEnemy("alien.png",200,10,8,50,50) 
star2 = GameSprite("star.png",30,250,0,80,80)
#level1
w1 = Wall(1,2,3,270,100,10,400) 
w2 = Wall(1,2,3,0,380,160,5)
w3 = Wall(1,2,3,110,260,160,5)
w4 = Wall(1,2,3,400,0,10,400) 
w5 = Wall(1,2,3,540,390,160,8) 
w6 = Wall(1,2,3,400,140,180,10) 
w7 = Wall(1,2,3,570,0,5,50) 

walls = sprite.Group()
walls.add(w1)
walls.add(w2)
walls.add(w3)
walls.add(w4)
walls.add(w5)
walls.add(w6)
walls.add(w7)

#level2
w8 = Wall(1,2,3,0,300,100,10) 

walls2 = sprite.Group()
walls2.add(w8) 

run = True
finish = False

while run:
    time.delay(50)
    window.fill((255,255,255))
    for e in event.get():
        if e.type == QUIT:
            run=False
    if not finish:
        if level == 1:
            enemy.reset()  
            enemy2.reset()
            hero.reset()
            star.reset() 
            for w in walls:
                w.draw_wall() 
            enemy.update()  
            enemy2.update() 
            hero.update() 
            star.update() 
            if sprite.collide_rect(hero,star):
                #img = image.load("thumb.jpg")
                #window.fill((255,255,255))
                #window.blit(transform.scale(img, (win_width,win_height)),(0,0))
                level = level + 1
                star.kill()
                walls.remove(w1) 
                walls.remove(w2)
                walls.remove(w3)
                walls.remove(w4)
                walls.remove(w5)
                walls.remove(w6)
                walls.remove(w7)
                
            if sprite.collide_rect(hero,enemy) or sprite.collide_rect(hero,enemy2):
                finish = True
                img2 = image.load("game-over-3.jpg") 
                window.fill((255,255,255))
                window.blit(transform.scale(img2, (win_width,win_height)),(0,0))
            if sprite.spritecollide(hero, walls, False):
                finish = True
                img2 = image.load("game-over-3.jpg") 
                window.fill((255,255,255))
                window.blit(transform.scale(img2, (win_width,win_height)),(0,0))
            
            display.update() 
        if level == 2:
            for w in walls2:
                w.draw_wall()
            enemy.reset()  
            enemy2.reset()
            enemy3.reset() 
            hero2.reset()
            star2.reset() 

            enemy.update()  
            enemy2.update() 
            enemy3.update()  
            hero2.update() 
            star2.update()
            display.update() 
