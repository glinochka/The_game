import pygame, sys, random

pygame.font.init()
pygame.mixer.init()
WIDTH = 1366
HEIGHT = 768
FPS = 60
isJump = False
isAtack = False
# Для анимации смерти
isDeath = False
die = False
f = 0
f1 = 0
isDeath1 = False
die1 = False
f_1 = 0
f1_1 = 0
Count = 0

# Для прыжка
JumpCount = 11
a = 10
DOWN = 682
isFall = False
isSmoke = False
inair = True
sm_anim = 0
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# Для движения фона
x1 = 0
x2 = 0
x3 = 0
x4 = 0
x5 = 0
x6 = 0
# Для анимаций удара
i = 0
i1 = 0
i2 = 0
isCharge = False
isChargeE = True
ch_anim = 0
ch_alf = 255
isAlfing = False
# Для движения
isMoveL = False
isMoveR = False

Coun = 0
H_Coun = 0
time_count = 240
iskra_anim = 0
bam_anim = 0
bam_count = 0
isBam = False
isBam2 = False
isChel = False
bam_window = pygame.Surface((WIDTH, HEIGHT))
bam_window.fill((255, 255, 255))
bam_window.set_alpha(0)
X = 0

class Bam(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = bam[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (X-200, 230)
        self.anim = 0
        self.alf = 0
        self.ising = False
    def update(self):
        global bam_anim, isBam2
        self.image = bam[self.anim // 8]
        self.anim += 3
        if self.alf <= 254:
            self.alf += 40
            bam_window.set_alpha(self.alf)
        elif self.alf > 254 and not self.ising and isBam2:
            bam_window.set_alpha(0)
            self.ising = True
            isBam2 = False
        elif self.alf > 254 and not self.ising and not isBam2:
            bam_window.set_alpha(0)
            self.ising = True
        if self.anim > 119:
            all_sprites.remove(self)
            molniya.remove(self)


class Iskra(pygame.sprite.Sprite):
    def __init__(self):
        global X
        pygame.sprite.Sprite.__init__(self)
        self.image = iskra[0]
        self.rect = self.image.get_rect()
        X = random.randint(50, 1000)
        self.rect.topleft = (X , DOWN - 200)
    def update(self):
        global iskra_anim
        self.image = iskra[iskra_anim // 8]
        iskra_anim += 3
        if iskra_anim > 87:
            iskra_anim = 0
            all_sprites.remove(self)


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = clowds[random.randint(0, 7)]
        self.rect = self.image.get_rect()
        self.rect.topleft = (WIDTH, random.randint(0, 400))
        if self.rect.y // 50 == 1:
            self.image = pygame.transform.scale(self.image, (self.image.get_width()/1.25, self.image.get_height()/1.25))
            self.sp = random.uniform(1, 9)
        elif self.rect.y // 50 == 2:
            self.image = pygame.transform.scale(self.image, (self.image.get_width() / 1.5, self.image.get_height() / 1.5))
            self.sp = random.uniform(1, 8)
        elif self.rect.y // 50 == 3:
            self.image = pygame.transform.scale(self.image, (self.image.get_width() / 1.75, self.image.get_height() / 1.75))
            self.sp = random.uniform(1, 7)
        elif self.rect.y // 50 == 4:
            self.image = pygame.transform.scale(self.image, (self.image.get_width()/2, self.image.get_height()/2))
            self.sp = random.uniform(1, 6)
        elif self.rect.y // 50 == 5:
            self.image = pygame.transform.scale(self.image, (self.image.get_width()/2.25, self.image.get_height()/2.25))
            self.sp = random.uniform(0.01, 0.999)
        elif self.rect.y // 50 == 6:
            self.image = pygame.transform.scale(self.image, (self.image.get_width()/2.5, self.image.get_height()/2.5))
            self.sp = random.uniform(0.01, 0.75)
        elif self.rect.y // 50 >= 7:
            self.image = pygame.transform.scale(self.image, (self.image.get_width()/2.75, self.image.get_height()/2.75))
            self.sp = random.uniform(0.01, 0.5)
        else:
            self.sp = random.uniform(1, 10)
    def update(self):
        self.rect.x -= self.sp
        if self.sp < 1 and self.rect.x <= 0:
            self.sp = 1
        if self.rect.right <= 0:
            sprites_clouds.remove(self)

class Object(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = foe_moving[0]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (WIDTH+30, DOWN)

    def update(self):
        global f, isDeath, die, f1

        if not isDeath and not die:
            self.image = foe_moving[f // 60]
            f += 9
            if f > 170:
                f = 0
        elif isDeath:
            self.image = foe_death[f1 // 40]
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
            f1 += 1
            if f1 > 190:
                f1 = 0
                isDeath = False
                die = True
        elif die:
            self.image = foe_death[4]
            self.rect.x += 2
        self.rect.x -= 10
# хз но скорость анимаций настраивается только тут (у врага) и вообще всё.....
class Object1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = foe_moving[0]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (WIDTH+30, DOWN)

    def update(self):
        global f_1, isDeath1, die1, f1_1

        if not isDeath1 and not die1:
            self.image = foe_moving[f_1 // 60]
            f_1 += 6
            if f_1 > 170:
                f_1 = 0
        elif isDeath1:
            self.image = foe_death[f1_1 // 40]
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
            f1_1 += 8
            if f1_1 > 190:
                f1_1 = 0
                isDeath1 = False
                die1 = True
        elif die1:
            self.image = foe_death[4]
            self.rect.x += 2
        self.rect.x -= 10

class Smoke(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = eJUMP[0]
        self.rect = self.image.get_rect()
        self.rect.right = 0
    def anim(self):
        global sm_anim, isSmoke
        self.rect.x -= 5
        if isSmoke:
            self.image = pygame.transform.scale(eJUMP[sm_anim // 20], (eJUMP[sm_anim // 20].get_width()/1.7, eJUMP[sm_anim // 20].get_height()/1.7))
            sm_anim += 7
            if sm_anim > 190:
                sm_anim = 0
                isSmoke = False
                self.image.set_alpha(0)

class Cdown(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = ChargeBar[0]
        self.rect = self.image.get_rect()
        self.rect.right = 0

    def anim(self):
        global ch_anim, isCharge, ch_alf, isAlfing, isChargeE
        if isAlfing and isCharge:
            self.rect.bottomright = (player.rect.left + 230, player.rect.top + 24)
            ch_alf = 255
            ch_anim = 0
            isAlfing = False
        elif isAlfing:
            self.rect.bottomright = (player.rect.left + 230, player.rect.top + 24)
            ch_alf -= 15
            self.image.set_alpha(ch_alf)
            if ch_alf <= 0:
                ch_alf = 255
                ch_anim = 0
                isAlfing = False
        if isCharge:
            isChargeE = False
            self.rect.bottomright = (player.rect.left+230, player.rect.top + 24)
            self.image = ChargeBar[ch_anim // 10]
            ch_anim += 8
            if ch_anim > 170:
                self.image = ChargeBar[18]
                isCharge = False
                isChargeE = True
                isAlfing = True
                chargeE.play()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/bf897da319614071edd52021b08b67707TdWjECYjwgQoIJJ-0.png')
        self.image.set_colorkey((61, 73, 119))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (WIDTH / 4, DOWN)
    def update(self):
        global JumpCount, isJump, i, isAtack, i1, a, isFall, isSmoke, isMoveL, isMoveR, inair
        self.rect.y += a
        if self.rect.bottom > DOWN:
            self.rect.bottom = DOWN
        if isFall:
            self.image = player_jumping[1]
            pygame.mixer.music.set_volume(1)
            isFall = False
            isSmoke = True
            smoke.rect.center = (player.rect.right + 12, player.rect.bottom + 25)
        smoke.anim()
        Ch_B.anim()
        if self.rect.right > 0 and isMoveL:
            self.rect.x -= 10
        if self.rect.right < WIDTH and isMoveR:
            self.rect.x += 2
        if isJump:
            self.rect.y -= (JumpCount ** 2) / 3
            JumpCount -= 0.25
            self.image = player_jumping[0]
            a += 0.25
            if JumpCount == 0:
                JumpCount = 11
                sJUMPe.play()
                a = 10
                isJump = False
                isFall = True
                if self.rect.right < WIDTH-50:
                    self.rect.x += 40
        if isAtack and isJump:
            inair = True
            self.image = player_attinjump[i1 // 30]
            i1 += 7
            if i1 > 151:
                i1 = 0
                isAtack = False
                inair = False
        if isAtack and inair and not isJump:
            i1 = 120
            inair = False

        if isAtack and not isJump:
            self.image = player_attack[i1 // 30]
            i1 += 7
            if i1 > 240:
                i1 = 0
                isAtack = False
                pygame.mixer.music.set_volume(1)
        if not isAtack and not isJump:
            self.image = player_moving[i // 40]
            self.image.set_colorkey((61, 73, 119))
            i += 5
            if i > 230:
                i = 0

    def Dying(self):
        global i2
        if self.rect.bottom < DOWN:
            self.rect.bottom += 13
        elif self.rect.bottom > DOWN:
            self.rect.bottom = DOWN
        if i2 < 199:
            self.image = player_dying[i2 // 50]
            i2 += 4
        else:
            self.image = player_dying[3]

class Menu():
    def __init__(self):
        self.image = window
    def menu(self, str1, str2):
        global x, x1, isMoveR, isMoveL
        done = False
        col = WHITE
        col1 = (232, 46, 46)
        pygame.mixer.music.set_volume(0)
        while not done:
            screen.blit(fon6, (0, 0))
            sprites_clouds.draw(screen)
            rel_x4 = x4 % fon4.get_rect().width
            screen.blit(fon4, (rel_x4 - fon4.get_rect().width, 230))
            if rel_x4 < WIDTH:
                screen.blit(fon4, (rel_x4, 230))

            rel_x3 = x3 % fon3.get_rect().width
            screen.blit(fon3, (rel_x3 - fon3.get_rect().width, 300))
            if rel_x3 < WIDTH:
                screen.blit(fon3, (rel_x3, 300))

            rel_x2 = x2 % fon2.get_rect().width
            screen.blit(fon2, (rel_x2 - fon2.get_rect().width, 230))
            if rel_x2 < WIDTH:
                screen.blit(fon2, (rel_x2, 230))

            rel_x1 = x1 % fon1.get_rect().width
            screen.blit(fon1, (rel_x1 - fon1.get_rect().width, 600))
            if rel_x1 < WIDTH:
                screen.blit(fon1, (rel_x1, 600))
            mp = pygame.mouse.get_pos()

            self.image.blit(font.render(str1, 1, (col1)), (600, 200))
            self.image.blit(font.render(str2, 1, (col)), (600, 250))
            if mp[0] > 600 and mp[0] < 750 and mp[1] > 200 and mp[1] < 250:
                col1 = (232, 46, 46)
                col = WHITE
            elif mp[0] > 600 and mp[0] < 750 and mp[1] > 250 and mp[1] < 300:
                col = (232, 46, 46)
                col1 = WHITE
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    if event.key == pygame.K_UP:
                        if col1 == WHITE:
                            col1 = (232, 46, 46)
                            col = WHITE
                        else:
                            col1 = WHITE
                            col = (232, 46, 46)
                    if event.key == pygame.K_DOWN:
                        if col1 == WHITE:
                            col1 = (232, 46, 46)
                            col = WHITE
                        else:
                            col1 = WHITE
                            col = (232, 46, 46)
                    if event.key == pygame.K_RETURN:
                        if col1 == (232, 46, 46):
                            done = True
                            isMoveL = False
                            isMoveR = False
                            pygame.mixer.music.set_volume(1)
                        elif col == (232, 46, 46):
                            sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if col1 == (232, 46, 46):
                        done = True
                        isMoveL = False
                        isMoveR = False
                        pygame.mixer.music.set_volume(1)
                    elif col == (232, 46, 46):
                        sys.exit()
            screen.blit(font.render(str1, 1, (col1)), (600, 200))
            screen.blit(font.render(str2, 1, (col)), (600, 250))
            all_sprites.draw(screen)
            pygame.display.flip()

class Death():
    def __init__(self):
        self.image = window
    def menu(self, str1, str2):
        global x, x1, i2, isMoveL, isMoveR, Coun, H_Coun
        done = False
        col = WHITE
        col1 = (232, 46, 46)
        pygame.mixer.music.set_volume(0)
        pl_sprite = pygame.sprite.Group()
        pl_sprite.add(player)
        alf = 0
        wdeath = pygame.Surface((WIDTH, HEIGHT))
        wdeath.fill((0, 0, 0))
        deaths_s.play()
        while not done:
            screen.blit(fon6, (0, 0))
            sprites_clouds.draw(screen)
            rel_x4 = x4 % fon4.get_rect().width
            screen.blit(fon4, (rel_x4 - fon4.get_rect().width, 230))
            if rel_x4 < WIDTH:
                screen.blit(fon4, (rel_x4, 230))

            rel_x3 = x3 % fon3.get_rect().width
            screen.blit(fon3, (rel_x3 - fon3.get_rect().width, 300))
            if rel_x3 < WIDTH:
                screen.blit(fon3, (rel_x3, 300))

            rel_x2 = x2 % fon2.get_rect().width
            screen.blit(fon2, (rel_x2 - fon2.get_rect().width, 230))
            if rel_x2 < WIDTH:
                screen.blit(fon2, (rel_x2, 230))

            rel_x1 = x1 % fon1.get_rect().width
            screen.blit(fon1, (rel_x1 - fon1.get_rect().width, 600))
            if rel_x1 < WIDTH:
                screen.blit(fon1, (rel_x1, 600))

            mp = pygame.mouse.get_pos()

            self.image.blit(font.render(str1, 1, (col1)), (600, 200))
            self.image.blit(font.render(str2, 1, (col)), (600, 250))
            if mp[0] > 600 and mp[0] < 750 and mp[1] > 200 and mp[1] < 250:
                col1 = (232, 46, 46)
                col = WHITE
            elif mp[0] > 600 and mp[0] < 750 and mp[1] > 250 and mp[1] < 300:
                col = (232, 46, 46)
                col1 = WHITE
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    if event.key == pygame.K_UP:
                        if col1 == WHITE:
                            col1 = (232, 46, 46)
                            col = WHITE
                        else:
                            col1 = WHITE
                            col = (232, 46, 46)
                    if event.key == pygame.K_DOWN:
                        if col1 == WHITE:
                            col1 = (232, 46, 46)
                            col = WHITE
                        else:
                            col1 = WHITE
                            col = (232, 46, 46)
                    if event.key == pygame.K_RETURN:
                        if col1 == (232, 46, 46):
                            done = True
                            for el in sprites_clouds:
                                sprites_clouds.remove(el)
                            isMoveL = False
                            isMoveR = False
                            if Coun > H_Coun:
                                H_Coun = Coun
                            Coun = 0
                            i2 = 0
                            player.rect.bottomleft = (WIDTH / 4, DOWN)
                            deaths_s.stop()
                            pygame.mixer.music.set_volume(1)
                        elif col == (232, 46, 46):
                            sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if col1 == (232, 46, 46):
                        done = True
                        for el in sprites_clouds:
                            sprites_clouds.remove(el)
                        isMoveL = False
                        isMoveR = False
                        i2 = 0
                        deaths_s.stop()
                        pygame.mixer.music.set_volume(1)
                        if Coun > H_Coun:
                            H_Coun = Coun
                        Coun = 0
                        player.rect.bottomleft = (WIDTH / 4, DOWN)
                    elif col == (232, 46, 46):
                        sys.exit()
            foe_sprites.draw(screen)
            wdeath.set_alpha(alf)
            if alf != 254:
                alf += 2
            if alf == 38:
                sJUMPe.play()
            screen.blit(wdeath, (0, 0))
            screen.blit(font.render(str1, 1, (col1)), (600, 200))
            screen.blit(font.render(str2, 1, (col)), (600, 250))
            player.Dying()
            pl_sprite.draw(screen)
            pygame.display.flip()

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ну уже..")
fon1 = pygame.image.load('images/forest-1.png').convert_alpha()
fon2 = pygame.image.load('images/forest-2.png').convert_alpha()
fon3 = pygame.image.load('images/forest-3.png').convert_alpha()
fon4 = pygame.image.load('images/forest-4.png').convert_alpha()
fon6 = pygame.image.load('images/forest-6.png').convert_alpha()

# Анимации
bam = [pygame.image.load('images/bam-1.png').convert_alpha(), pygame.image.load('images/bam-2.png').convert_alpha(), pygame.image.load('images/bam-3.png').convert_alpha(), pygame.image.load('images/bam-4.png').convert_alpha(), pygame.image.load('images/bam-5.png').convert_alpha(), pygame.image.load('images/bam-6.png').convert_alpha(), pygame.image.load('images/bam-7.png').convert_alpha(), pygame.image.load('images/bam-8.png').convert_alpha(), pygame.image.load('images/bam-9.png').convert_alpha(), pygame.image.load('images/bam-10.png').convert_alpha(), pygame.image.load('images/bam-11.png').convert_alpha(), pygame.image.load('images/bam-12.png').convert_alpha(), pygame.image.load('images/bam-13.png').convert_alpha(), pygame.image.load('images/bam-14.png').convert_alpha(), pygame.image.load('images/bam-15.png').convert_alpha()]
iskra = [pygame.image.load('images/iskra-1.png').convert_alpha() ,pygame.image.load('images/iskra-2.png').convert_alpha() ,pygame.image.load('images/iskra-3.png').convert_alpha() ,pygame.image.load('images/iskra-4.png').convert_alpha() ,pygame.image.load('images/iskra-5.png').convert_alpha() ,pygame.image.load('images/iskra-6.png').convert_alpha() ,pygame.image.load('images/iskra-7.png').convert_alpha() ,pygame.image.load('images/iskra-8.png').convert_alpha() ,pygame.image.load('images/iskra-9.png').convert_alpha() ,pygame.image.load('images/iskra-10.png').convert_alpha() ,pygame.image.load('images/iskra-11.png').convert_alpha()]
ChargeBar = [pygame.image.load('images/New Piskel-1.png.png').convert_alpha(), pygame.image.load('images/New Piskel-2.png.png').convert_alpha(), pygame.image.load('images/New Piskel-3.png.png').convert_alpha(), pygame.image.load('images/New Piskel-4.png.png').convert_alpha(), pygame.image.load('images/New Piskel-5.png.png').convert_alpha(), pygame.image.load('images/New Piskel-6.png.png').convert_alpha(), pygame.image.load('images/New Piskel-7.png.png').convert_alpha(), pygame.image.load('images/New Piskel-8.png.png').convert_alpha(), pygame.image.load('images/New Piskel-9.png.png').convert_alpha(), pygame.image.load('images/New Piskel-10.png.png').convert_alpha(), pygame.image.load('images/New Piskel-11.png.png').convert_alpha(), pygame.image.load('images/New Piskel-12.png.png').convert_alpha(), pygame.image.load('images/New Piskel-13.png.png').convert_alpha(), pygame.image.load('images/New Piskel-14.png.png'), pygame.image.load('images/New Piskel-15.png.png'), pygame.image.load('images/New Piskel-16.png.png'), pygame.image.load('images/New Piskel-17.png.png'), pygame.image.load('images/New Piskel-18.png.png'), pygame.image.load('images/New Piskel-19.png.png'),]
eJUMP = [pygame.image.load('images/eJUMP-1.png.png').convert_alpha(), pygame.image.load('images/eJUMP-2.png.png').convert_alpha(), pygame.image.load('images/eJUMP-3.png.png').convert_alpha(), pygame.image.load('images/eJUMP-4.png.png').convert_alpha(), pygame.image.load('images/eJUMP-5.png.png').convert_alpha(), pygame.image.load('images/eJUMP-6.png.png').convert_alpha(), pygame.image.load('images/eJUMP-7.png.png').convert_alpha(), pygame.image.load('images/eJUMP-8.png.png').convert_alpha(), pygame.image.load('images/eJUMP-9.png.png').convert_alpha(), pygame.image.load('images/eJUMP-10.png.png').convert_alpha()]
player_attinjump = [pygame.image.load('images/a-jump-1.png.png').convert_alpha(), pygame.image.load('images/a-jump-2.png.png').convert_alpha(), pygame.image.load('images/a-jump-3.png.png').convert_alpha(), pygame.image.load('images/a-jump-4.png.png').convert_alpha(), pygame.image.load('images/a-jump-5.png.png').convert_alpha(), pygame.image.load('images/a-jump-6.png.png').convert_alpha()]
player_jumping = [pygame.image.load('images/jump.png.png').convert_alpha(), pygame.image.load('images/jump-1.png.png').convert_alpha()]
player_dying = [pygame.image.load('images/anim_d-1.png.png').convert_alpha(), pygame.image.load('images/anim_d-2.png.png').convert_alpha(), pygame.image.load('images/anim_d-3.png.png').convert_alpha(), pygame.image.load('images/anim_d-4.png.png').convert_alpha()]
player_moving = [pygame.image.load('images/bf897da319614071edd52021b08b67707TdWjECYjwgQoIJJ-0.png').convert_alpha(), pygame.image.load('images/bf897da319614071edd52021b08b67707TdWjECYjwgQoIJJ-1.png').convert_alpha(), pygame.image.load('images/bf897da319614071edd52021b08b67707TdWjECYjwgQoIJJ-2.png').convert_alpha(),pygame.image.load('images/bf897da319614071edd52021b08b67707TdWjECYjwgQoIJJ-3.png').convert_alpha(),pygame.image.load('images/bf897da319614071edd52021b08b67707TdWjECYjwgQoIJJ-4.png').convert_alpha(),pygame.image.load('images/bf897da319614071edd52021b08b67707TdWjECYjwgQoIJJ-5.png').convert_alpha()]
player_attack = [pygame.image.load('images/Attack-1.png').convert_alpha(), pygame.image.load('images/Attack-2.png').convert_alpha(), pygame.image.load('images/Attack-3.png').convert_alpha(), pygame.image.load('images/Attack-4.png').convert_alpha(), pygame.image.load('images/Attack-5.png').convert_alpha(), pygame.image.load('images/Attack-6.png').convert_alpha(), pygame.image.load('images/Attack-7.png').convert_alpha(), pygame.image.load('images/Attack-8.png').convert_alpha(), pygame.image.load('images/Attack-9.png').convert_alpha()]
foe_moving = [pygame.image.load('images/image-1.png.png').convert_alpha(), pygame.image.load('images/image-2.png.png').convert_alpha(), pygame.image.load('images/image-3.png.png').convert_alpha()]
foe_death = [pygame.image.load('images/Untitled_02-22-2022_05-46-56_1-1.png.png').convert_alpha() ,pygame.image.load('images/Untitled_02-22-2022_05-46-56_1-2.png.png').convert_alpha() ,pygame.image.load('images/Untitled_02-22-2022_05-46-56_1-3.png.png').convert_alpha() ,pygame.image.load('images/Untitled_02-22-2022_05-46-56_1-4.png.png').convert_alpha() ,pygame.image.load('images/Untitled_02-22-2022_05-46-56_1-5.png.png').convert_alpha()]
# Время
clock = pygame.time.Clock()
# создание объектов и спрайтов
clowds = [pygame.image.load('images/clowd-1.png').convert_alpha(), pygame.image.load('images/clowd-2.png').convert_alpha(), pygame.image.load('images/clowd-3.png').convert_alpha(), pygame.image.load('images/clowd-4.png').convert_alpha(), pygame.image.load('images/clowd-5.png').convert_alpha(), pygame.image.load('images/clowd-6.png').convert_alpha(), pygame.image.load('images/clowd-7.png').convert_alpha(), pygame.image.load('images/clowd-8.png').convert_alpha()]
all_sprites = pygame.sprite.Group()
foe_sprites = pygame.sprite.Group()
molniya = pygame.sprite.Group()
sprites_clouds = pygame.sprite.Group()
player = Player()
villiant = Object()
new_foe = Object1()
smoke = Smoke()
Ch_B = Cdown()
all_sprites.add(player)
all_sprites.add(villiant)
all_sprites.add(smoke)
all_sprites.add(Ch_B)
foe_sprites.add(villiant)


# Меню
window = pygame.Surface((WIDTH//2, HEIGHT//2))
window.fill((0, 0, 255))
window.set_alpha(0)
menu = Menu()
dmenu = Death()
font = pygame.font.Font('fonts/Main_font.ttf', 50)
menu.menu(u'играть', u'выход')
# Счетчик
Count_win = pygame.Surface((200, 100))


bamming = 0

# Музыка
m_bam = pygame.mixer.Sound('Sounds/thunderstorm.wav')
m_iskra = pygame.mixer.Sound('Sounds/iskra.wav')
chargeE = pygame.mixer.Sound('Sounds/chargeE.wav')
sJUMPs = pygame.mixer.Sound('Sounds/jumps-start.wav')
sJUMPe = pygame.mixer.Sound('Sounds/jump-land.wav')
sattack = pygame.mixer.Sound('Sounds/Attack.wav')
sPAIN = pygame.mixer.Sound('Sounds/pain.wav')
sDeath = pygame.mixer.Sound('Sounds/Death.wav')
deaths_s = pygame.mixer.Sound('Sounds/death_theme.wav')
pygame.mixer.music.load('Sounds/running_og.wav')
pygame.mixer.music.play(-1)
# Цикл игры
while True:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not isAtack:
                if not isJump:
                    sJUMPs.play()
                isJump = True
                player.image = player_jumping[1]
                pygame.mixer.music.set_volume(0)
            elif event.key == pygame.K_SPACE and isChargeE:
                isAtack = True
                isCharge = True
                sattack.play()
                pygame.mixer.music.set_volume(1)
            elif event.key == pygame.K_ESCAPE:
                menu.menu(u'возобновить', u'выход')
            elif event.key == pygame.K_LEFT:
                isMoveL = True
            elif event.key == pygame.K_RIGHT:
                isMoveR = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                isMoveL = False
            elif event.key == pygame.K_RIGHT:
                isMoveR = False

    # Проверка на столкновение и чередование классов врагов
    if i1 > 30 and pygame.sprite.spritecollide(player, foe_sprites, False) and player.rect.right > villiant.rect.left+50:
        isDeath = True
        sDeath.play()
        foe_sprites.remove(villiant)
        isDeath1 = False
        die1 = False
        f_1 = 0
        f1_1 = 0
        Coun += 1
    elif i1 > 30 and pygame.sprite.spritecollide(player, foe_sprites, False) and player.rect.right > new_foe.rect.left+50:
        isDeath1 = True
        sDeath.play()
        foe_sprites.remove(new_foe)
        isDeath = False
        die = False
        f = 0
        f1 = 0
        Coun += 1
    if villiant in foe_sprites:
            if pygame.sprite.spritecollide(player, foe_sprites, False) and player.rect.right > villiant.rect.left+50:
                dmenu.menu(u'заново', u'выход')
                sPAIN.play()
            all_sprites.remove(villiant)
            new_foe = Object1()
            foe_sprites.remove(villiant)
            all_sprites.add(new_foe)
            foe_sprites.add(new_foe)
            isDeath1 = False
            die1 = False
    elif new_foe in foe_sprites:
        if pygame.sprite.spritecollide(player, foe_sprites, False) and player.rect.right > new_foe.rect.left + 50:
            sPAIN.play()
            dmenu.menu(u'заново', u'выход')
            all_sprites.remove(new_foe)
            villiant = Object()
            foe_sprites.remove(new_foe)
            all_sprites.add(villiant)
            foe_sprites.add(villiant)
            isDeath = False
            die = False
    if pygame.sprite.spritecollide(player, molniya, False):
        sPAIN.play()
        dmenu.menu(u'заново', u'выход')
        all_sprites.remove(new_foe)
        villiant = Object()
        foe_sprites.remove(new_foe)
        bam_window.set_alpha(0)
        all_sprites.remove(bamming)
        molniya.remove(bamming)
        all_sprites.add(villiant)
        foe_sprites.add(villiant)
    # Проверка на уход из поля зрения
    if villiant in all_sprites:
        if villiant.rect.right < 0:
            all_sprites.remove(villiant)
            new_foe = Object1()
            if villiant in foe_sprites:
                foe_sprites.remove(villiant)
            all_sprites.add(new_foe)
            foe_sprites.add(new_foe)

    else:
        if new_foe.rect.right < -0:
            all_sprites.remove(new_foe)
            villiant = Object()
            if new_foe in foe_sprites:
                foe_sprites.remove(new_foe)
            all_sprites.add(villiant)
            foe_sprites.add(villiant)
    # Молния
    time_count -= 1
    if random.randint(1, 300) == 1 and time_count < 0:
        time_count = 240
        all_sprites.add(Iskra())
        m_iskra.play()
        isBam = True
    if isBam and time_count < 120:
        if not bamming in all_sprites:
            bamming = Bam()
            all_sprites.add(bamming)
            molniya.add(bamming)
            m_bam.play()
            isBam = False
    # Обновлениe
    all_sprites.update()
    sprites_clouds.update()
    # Фон
    screen.blit(fon6, (0, 0))
    Count += 1
    if Count % 5 == 0:
        sprites_clouds.add(Cloud())
    sprites_clouds.draw(screen)
    rel_x4 = x4 % fon4.get_rect().width
    screen.blit(fon4, (rel_x4 - fon4.get_rect().width, 230))
    if rel_x4 < WIDTH:
        screen.blit(fon4, (rel_x4, 230))
    x4 -= 3

    rel_x3 = x3 % fon3.get_rect().width
    screen.blit(fon3, (rel_x3 - fon3.get_rect().width, 300))
    if rel_x3 < WIDTH:
        screen.blit(fon3, (rel_x3, 300))
    x3 -= 4

    rel_x2 = x2 % fon2.get_rect().width
    screen.blit(fon2, (rel_x2 - fon2.get_rect().width, 230))
    if rel_x2 < WIDTH:
        screen.blit(fon2, (rel_x2, 230))
    x2 -= 6

    rel_x1 = x1 % fon1.get_rect().width
    screen.blit(fon1, (rel_x1 - fon1.get_rect().width, 600))
    if rel_x1 < WIDTH:
        screen.blit(fon1, (rel_x1, 600))
    x1 -= 8

    # Рендеринг
    all_sprites.draw(screen)
    screen.blit(font.render(u'Score: ' + str(Coun), 1, (WHITE)), (20, 10))
    screen.blit(font.render(u'High: ' + str(H_Coun), 1, (GREEN)), (20, 50))
    screen.blit(bam_window, (0, 0))
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()