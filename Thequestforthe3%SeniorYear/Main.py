import pygame as pg
import sys
from config import *
from Sprites import *
class Game:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('test')
        self.clock = pg.time.Clock()
        self.load_data()
        self.wallsyb = "W"
        self.playersyb = "P"
        self.doorsyb = "D"
        self.enemysyb = "E"
        self.obsticlelist = []
        self.doorlist = []
        self.enemylist = []

    def load_data(self):
        pass
    #Generates the sprite groups and sprite objects such as the walls and the player
    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.obsticles = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.doors = pg.sprite.Group()
        self.enemys = pg.sprite.Group()

        for y in range(len(MAP1)):
            for i in range(len(MAP1[y])):
                if MAP1[y][i] == self.doorsyb:
                    self.doorlist.append(Door(self, i, y))

        for y in range(len(MAP1)):
            for i in range(len(MAP1[y])):
                if MAP1[y][i].upper() == self.wallsyb:
                    self.obsticlelist.append(Wall(self,i,y))
                elif MAP1[y][i] == self.enemysyb:
                    self.enemylist.append(Enemy(self, i, y, 1))
                elif MAP1[y][i].upper() == self.playersyb:
                   self.player = Player(self, i, y)







    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
    #Self Explanitory
    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.obsticles.update()
    #Draw the grid over the screen
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))
    #Draw attribute
    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.obsticles.draw(self.screen)
        self.all_sprites.draw(self.screen)
        pg.display.flip()
    #Event loop
    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    for i in range(len(self.obsticlelist)):
                        self.obsticlelist[i].move(dx=1)
                    for i in range(len(self.doorlist)):
                        self.doorlist[i].move(dx=1)
                    for i in range(len(self.enemylist)):
                            self.enemylist[i].move(dx=1)
                if event.key == pg.K_RIGHT:
                    for i in range(len(self.obsticlelist)):
                        self.obsticlelist[i].move(dx= -1)
                    for i in range(len(self.doorlist)):
                        self.doorlist[i].move(dx=-1)
                    for i in range(len(self.enemylist)):
                            self.enemylist[i].move(dx=-1)
                if event.key == pg.K_UP:
                    for i in range(len(self.obsticlelist)):
                        self.obsticlelist[i].move(dy=1)
                    for i in range(len(self.doorlist)):
                        self.doorlist[i].move(dy=1)
                    for i in range(len(self.enemylist)):
                            self.enemylist[i].move(dy=1)
                if event.key == pg.K_DOWN:
                    for i in range(len(self.obsticlelist)):
                        self.obsticlelist[i].move(dy= -1)
                    for i in range(len(self.doorlist)):
                        self.doorlist[i].move(dy=-1)
                    for i in range(len(self.enemylist)):
                            self.enemylist[i].move(dy=-1)
            if event.type == pg.KEYUP:
                if pg.sprite.spritecollide(self.player,self.walls,False,pg.sprite.collide_mask):
                    if event.key == pg.K_DOWN:
                        for i in range(len(self.obsticlelist)):
                            self.obsticlelist[i].move(dy = 1)
                        for i in range(len(self.doorlist)):
                            self.doorlist[i].move(dy=1)
                    elif event.key == pg.K_UP:
                        for i in range(len(self.obsticlelist)):
                            self.obsticlelist[i].move(dy=-1)
                        for i in range(len(self.doorlist)):
                            self.doorlist[i].move(dy=-1)
                    elif event.key == pg.K_LEFT:
                        for i in range(len(self.obsticlelist)):
                            self.obsticlelist[i].move(dx=-1)
                        for i in range(len(self.doorlist)):
                            self.doorlist[i].move(dx=-1)
                    elif event.key == pg.K_RIGHT:
                        for i in range(len(self.obsticlelist)):
                            self.obsticlelist[i].move(dx= 1)
                        for i in range(len(self.doorlist)):
                            self.doorlist[i].move(dx=1)
                if pg.sprite.spritecollide(self.player,self.doors,False,pg.sprite.collide_mask):
                    collied = pg.sprite.spritecollide(self.player, self.doors, False, pg.sprite.collide_mask)[0]
                    collied.opened = True
                for i in range(len(self.enemylist)):
                    if self.enemylist[i].active:
                        if self.player.x > self.enemylist[i].x:
                            self.enemylist[i].move(dx=1)
                            self.enemylist[i].movementdirection = "right"
                        elif self.player.x < self.enemylist[i].x:
                            self.enemylist[i].move(dx= -1)
                            self.enemylist[i].movementdirection ="left"
                        elif self.player.y > self.enemylist[i].y:
                            self.enemylist[i].move(dy=1)
                            self.enemylist[i].movementdirection = "up"
                        elif self.player.y < self.enemylist[i].y:
                            self.enemylist[i].move(dy=-1)
                            self.enemylist[i].movementdirection = "down"
            if pg.sprite.spritecollide(self.player, self.enemys, False, pg.sprite.collide_mask):
                print(pg.sprite.spritecollide(self.player, self.enemys, False, pg.sprite.collide_mask))


            #Check for collisions, then check what direction the collision is in based on what key was pressed, then back up the player in the corresponding direction


    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game objectf\
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
