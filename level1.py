import pygame


clock = pygame.time.Clock()
def runlevel():
    pygame.init()

    pygame.display.set_caption("Snowgrave")
    icon = pygame.image.load("assets/images/snowflake_icon_project.png")
    pygame.display.set_icon(icon)

    W = 1280
    H = 720

    screen = pygame.display.set_mode((W, H), flags=pygame.NOFRAME)


    font = pygame.font.Font("assets/fonts/Adventurer/Adventurer.ttf", 100)
    font_small = pygame.font.Font("assets/fonts/Adventurer/Adventurer.ttf", 50)
    font_border = pygame.font.Font("assets/fonts/Adventurer/Adventurer.ttf", 105)

    level_1_back = pygame.image.load("assets/backgrounds/winter_back/winter 1/7.png")

    ##player

    player = pygame.image.load("assets/char_sprites/stand/stand1.png")
    player_speed = 5
    player_x = 500
    player_y = 550

    magic_x_r = player_x + 80 * 2
    magic_x_l = player_x - 80
    magic_y = player_y

    player_atck = 1

    player_hp = 12

    is_attack_sound = False
    jump_sound_played = False
    is_attack = False
    is_jump = False
    jump_count = 9

    player_anim_count = 0
    stand_anim_count = 0
    attack_anim_count = 0
    ice_attack_count = 0
    run_count = 0

    stand_right = [
        pygame.image.load("assets/char_sprites/stand/stand1.png"),
        pygame.image.load("assets/char_sprites/stand/stand1.png"),
        pygame.image.load("assets/char_sprites/stand/stand_blink1.png"),
        pygame.image.load("assets/char_sprites/stand/stand_blink2.png")
    ]

    stand_left = [
        pygame.transform.flip(pygame.image.load("assets/char_sprites/stand/stand1.png"), True, False),
        pygame.transform.flip(pygame.image.load("assets/char_sprites/stand/stand2.png"), True, False),
        pygame.transform.flip(pygame.image.load("assets/char_sprites/stand/stand_blink1.png"), True, False),
        pygame.transform.flip(pygame.image.load("assets/char_sprites/stand/stand_blink2.png"), True, False),

    ]

    walk_right = [
        pygame.image.load("assets/char_sprites/walk/right/walk1_right.png"),
        pygame.image.load("assets/char_sprites/walk/right/walk2_right.png"),
        pygame.image.load("assets/char_sprites/walk/right/walk3_right.png"),
        pygame.image.load("assets/char_sprites/walk/right/walk4_right.png"),
    ]
    walk_left = [
        pygame.image.load("assets/char_sprites/walk/left/walk1_left.png"),
        pygame.image.load("assets/char_sprites/walk/left/walk2_left.png"),
        pygame.image.load("assets/char_sprites/walk/left/walk3_left.png"),
        pygame.image.load("assets/char_sprites/walk/left/walk4_left.png"),
    ]

    run_right = [
        pygame.image.load("assets/char_sprites/run/run1.png"),
        pygame.image.load("assets/char_sprites/run/run2.png"),
        pygame.image.load("assets/char_sprites/run/run3.png"),
        pygame.image.load("assets/char_sprites/run/run4.png"),
        pygame.image.load("assets/char_sprites/run/run5.png"),
        pygame.image.load("assets/char_sprites/run/run6.png"),
        pygame.image.load("assets/char_sprites/run/run7.png"),
        pygame.image.load("assets/char_sprites/run/run8.png"),
    ]

    run_left = [
        pygame.transform.flip(pygame.image.load("assets/char_sprites/run/run1.png"), True, False),
        pygame.transform.flip(pygame.image.load("assets/char_sprites/run/run2.png"), True, False),
        pygame.transform.flip(pygame.image.load("assets/char_sprites/run/run3.png"), True, False),
        pygame.transform.flip(pygame.image.load("assets/char_sprites/run/run4.png"), True, False),
        pygame.transform.flip(pygame.image.load("assets/char_sprites/run/run5.png"), True, False),
        pygame.transform.flip(pygame.image.load("assets/char_sprites/run/run6.png"), True, False),
        pygame.transform.flip(pygame.image.load("assets/char_sprites/run/run7.png"), True, False),
        pygame.transform.flip(pygame.image.load("assets/char_sprites/run/run8.png"), True, False),
    ]

    attack_right = [
        pygame.image.load("assets/char_sprites/attack/atck1.png"),
        pygame.image.load("assets/char_sprites/attack/atck2.png"),
        pygame.image.load("assets/char_sprites/attack/atck3.png"),
        pygame.image.load("assets/char_sprites/attack/atck4.png"),
        pygame.image.load("assets/char_sprites/attack/atck5.png"),
        pygame.image.load("assets/char_sprites/attack/atck6.png"),
        pygame.image.load("assets/char_sprites/attack/atck7.png"),
        pygame.image.load("assets/char_sprites/attack/atck8.png")
    ]

    attack_left = [
        pygame.transform.flip(pygame.image.load("assets/char_sprites/attack/atck1.png"), True, False),
        pygame.transform.flip(pygame.image.load("assets/char_sprites/attack/atck2.png"), True, False),
        pygame.transform.flip(pygame.image.load("assets/char_sprites/attack/atck3.png"), True, False),
        pygame.transform.flip(pygame.image.load("assets/char_sprites/attack/atck4.png"), True, False),
        pygame.transform.flip(pygame.image.load("assets/char_sprites/attack/atck5.png"), True, False),
        pygame.transform.flip(pygame.image.load("assets/char_sprites/attack/atck6.png"), True, False),
        pygame.transform.flip(pygame.image.load("assets/char_sprites/attack/atck7.png"), True, False),
        pygame.transform.flip(pygame.image.load("assets/char_sprites/attack/atck8.png"), True, False),
    ]

    animation_delays = {
        "stand": 200,
        "walk": 30,
        "jump": 50,
        "attack": 80,
        "ice_attack": 40,
        "run": 100
    }

    attack_anim = [
        pygame.image.load("assets/animation/skill_animation/ice_attack_2/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Active2.png"),
        pygame.image.load("assets/animation/skill_animation/ice_attack_2/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Active3.png"),
        pygame.image.load("assets/animation/skill_animation/ice_attack_2/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Active5.png"),
        pygame.image.load("assets/animation/skill_animation/ice_attack_2/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending1.png"),
        pygame.image.load("assets/animation/skill_animation/ice_attack_2/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending3.png"),
        pygame.image.load("assets/animation/skill_animation/ice_attack_2/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending17.png"),
    ]

    dead_anim = [
        pygame.image.load("assets/char_sprites/dead/dead1.png"),
        pygame.image.load("assets/char_sprites/dead/dead2.png"),
        pygame.image.load("assets/char_sprites/dead/dead3.png"),
        pygame.image.load("assets/char_sprites/dead/dead4.png")
    ]

    jump_anim = [
        pygame.image.load("assets/char_sprites/jump/jump1.png"),
        pygame.image.load("assets/char_sprites/jump/jump2.png"),
        pygame.image.load("assets/char_sprites/jump/jump3.png"),
        pygame.image.load("assets/char_sprites/jump/jump4.png"),
        pygame.image.load("assets/char_sprites/jump/jump5.png"),
        pygame.image.load("assets/char_sprites/jump/jump6.png"),
        pygame.image.load("assets/char_sprites/jump/jump7.png"),
        pygame.image.load("assets/char_sprites/jump/jump8.png")
    ]

    hp_hearts = [
        pygame.image.load("assets/images/hp_hearts/hp_bars/hp_bar1.png"),
        pygame.image.load("assets/images/hp_hearts/hp_bars/hp_bar2.png"),
        pygame.image.load("assets/images/hp_hearts/hp_bars/hp_bar3.png"),
        pygame.image.load("assets/images/hp_hearts/hp_bars/hp_bar4.png"),
        pygame.image.load("assets/images/hp_hearts/hp_bars/hp_bar5.png"),
        pygame.image.load("assets/images/hp_hearts/hp_bars/hp_bar6.png"),
        pygame.image.load("assets/images/hp_hearts/hp_bars/hp_bar7.png"),
        pygame.image.load("assets/images/hp_hearts/hp_bars/hp_bar8.png"),
        pygame.image.load("assets/images/hp_hearts/hp_bars/hp_bar9.png"),
        pygame.image.load("assets/images/hp_hearts/hp_bars/hp_bar10.png"),
        pygame.image.load("assets/images/hp_hearts/hp_bars/hp_bar11.png"),
        pygame.image.load("assets/images/hp_hearts/hp_bars/hp_bar12.png"),
        pygame.image.load("assets/images/hp_hearts/hp_bars/hp_bar13.png"),
    ]

    border = pygame.image.load("assets/char_sprites/char_icon/border_1.png")

    ## Слаймы ааааа страшно
    slime_walk = [
        pygame.image.load("assets/animation/slimes/Blue_Slime/slime_walk/slime_walk1.png"),
        pygame.image.load("assets/animation/slimes/Blue_Slime/slime_walk/slime_walk2.png"),
        pygame.image.load("assets/animation/slimes/Blue_Slime/slime_walk/slime_walk3.png"),
        pygame.image.load("assets/animation/slimes/Blue_Slime/slime_walk/slime_walk4.png"),
        pygame.image.load("assets/animation/slimes/Blue_Slime/slime_walk/slime_walk5.png")
    ]

    slime_attack = [
        pygame.image.load("assets/animation/slimes/Blue_Slime/slime_attack/slime_attack1.png"),
        pygame.image.load("assets/animation/slimes/Blue_Slime/slime_attack/slime_attack2.png"),
        pygame.image.load("assets/animation/slimes/Blue_Slime/slime_attack/slime_attack3.png"),
        pygame.image.load("assets/animation/slimes/Blue_Slime/slime_attack/slime_attack4.png")
    ]

    slime_dead = [
        pygame.image.load("assets/animation/slimes/Blue_Slime/slime_dead/slime_dead1.png."),
        pygame.image.load("assets/animation/slimes/Blue_Slime/slime_dead/slime_dead2.png."),
        pygame.image.load("assets/animation/slimes/Blue_Slime/slime_dead/slime_dead3.png."),
        pygame.image.load("assets/animation/slimes/Blue_Slime/slime_dead/slime_dead3.png."),
        pygame.image.load("assets/animation/slimes/Blue_Slime/slime_dead/slime_dead3.png."),
        pygame.image.load("assets/animation/slimes/Blue_Slime/slime_dead/slime_dead3.png."),
    ]

    evgesha_red_walk = [
        pygame.image.load("assets/animation/slimes/Red_Slime/red_evgesha_walk/r_evgesha_w1.png"),
        pygame.image.load("assets/animation/slimes/Red_Slime/red_evgesha_walk/r_evgesha_w2.png"),
        pygame.image.load("assets/animation/slimes/Red_Slime/red_evgesha_walk/r_evgesha_w3.png"),
        pygame.image.load("assets/animation/slimes/Red_Slime/red_evgesha_walk/r_evgesha_w4.png"),
        pygame.image.load("assets/animation/slimes/Red_Slime/red_evgesha_walk/r_evgesha_w5.png"),
    ]

    evgesha_red_attack = [
        pygame.image.load("assets/animation/slimes/Red_Slime/red_evgesha_attack/r_evgesha_a1.png"),
        pygame.image.load("assets/animation/slimes/Red_Slime/red_evgesha_attack/r_evgesha_a2.png"),
        pygame.image.load("assets/animation/slimes/Red_Slime/red_evgesha_attack/r_evgesha_a3.png"),
        pygame.image.load("assets/animation/slimes/Red_Slime/red_evgesha_attack/r_evgesha_a4.png")
    ]

    evgesha_red_dead = [
        pygame.image.load("assets/animation/slimes/Red_Slime/red_evgesha_dead/r_evgesha_d1.png"),
        pygame.image.load("assets/animation/slimes/Red_Slime/red_evgesha_dead/r_evgesha_d2.png"),
        pygame.image.load("assets/animation/slimes/Red_Slime/red_evgesha_dead/r_evgesha_d3.png"),
    ]

    red_evgesha_x = -100
    red_evgesha_y = 550
    red_evgesha_speed = 3
    red_evgesha_hp = 3

    slime_x = 1280
    slime_y = 550
    slime_speed = 2
    slime_hp = 3
    is_slime_alive = True

    slime_hp_hearts = [
        pygame.image.load("assets/images/hp_hearts/slime_hp/Hearts_Yellow_5.png"),
        pygame.image.load("assets/images/hp_hearts/slime_hp/Hearts_Yellow_4.png"),
        pygame.image.load("assets/images/hp_hearts/slime_hp/Hearts_Yellow_3.png"),
        pygame.image.load("assets/images/hp_hearts/slime_hp/Hearts_Yellow_1.png"),
    ]

    numbers = [
        pygame.image.load("assets/images/numbers/0.png"),
        pygame.image.load("assets/images/numbers/1.png"),
        pygame.image.load("assets/images/numbers/2.png"),
        pygame.image.load("assets/images/numbers/3.png"),
        pygame.image.load("assets/images/numbers/4.png"),
        pygame.image.load("assets/images/numbers/5.png"),
        pygame.image.load("assets/images/numbers/6.png"),
        pygame.image.load("assets/images/numbers/7.png"),
        pygame.image.load("assets/images/numbers/8.png"),
        pygame.image.load("assets/images/numbers/9.png"),
    ]

    laying_scroll = pygame.image.load("assets/images/tutorial_scroll/tutorial.png")
    scroll_x = 300
    scroll_y = 610
    scroll = pygame.image.load("assets/images/tutorial_scroll/first.png")

    jump_sound = pygame.mixer.Sound("assets/audio/voice_jump/jump2.wav")
    jump_sound.set_volume(0.3)

    attack_sound = pygame.mixer.Sound("assets/audio/Magic/8_Atk_Magic_SFX/13_Ice_explosion_01.wav")
    attack_sound.set_volume(0.3)

    slime_sound = pygame.mixer.Sound("assets/audio/Magic/10_Battle_SFX/77_flesh_02.wav")
    slime_sound.set_volume(0.3)

    level_music = pygame.mixer.Sound("assets/audio/levelmusic/Let it snow.mp3")
    level_music.set_volume(0.3)

    last_stand_update = pygame.time.get_ticks()
    last_attack_update = pygame.time.get_ticks()
    last_animation_update = pygame.time.get_ticks()
    last_run_update = pygame.time.get_ticks()
    left = False
    right = True

    game_over_text = font.render("GAME OVER", True, 'red')
    game_over_text_border = font_border.render("GAME OVER", True, 'black')
    win_text = font.render("YOU WIN", True, 'green')
    win_text_border = font.render("YOU WIN", True, 'black')

    tutorial_text = font_small.render("Press E to interuct with items", True, 'black')


    class Slime:
        def __init__(self, x, y, speed, hp, player_hp, player_speed, is_win):
            self.x = x
            self.y = y
            self.speed = speed
            self.hp = hp
            self.player_hp = player_hp
            self.player_speed = player_speed
            self.is_win = is_win

        def draw(self, magic_x_r, magic_x_l, is_attack, right, left):
            if is_attack:
                if right:
                    if (magic_x_r + 50 >= self.x >= player_x):
                        self.hp -= 1
                elif left:
                    if (magic_x_l - 50 <= self.x <= magic_x_l + 50):
                        self.hp -= 1
            if self.hp == 3:
                screen.blit(pygame.transform.scale(slime_hp_hearts[3], (30, 30)), (self.x + 35, self.y))
            elif self.hp == 2:
                screen.blit(pygame.transform.scale(slime_hp_hearts[2], (30, 30)), (self.x + 35, self.y))
            elif self.hp == 1:
                screen.blit(pygame.transform.scale(slime_hp_hearts[1], (30, 30)), (self.x + 35, self.y))
            elif self.hp >= 0:
                screen.blit(pygame.transform.scale(slime_hp_hearts[0], (30, 30)), (self.x + 35, self.y))

            if self.hp > 0:
                if abs(self.x - player_x) <= 20 and player_y >= self.y:
                    self.player_hp -= 1
                    slime_sound.play()
                    if left:
                        self.x -= 50
                    else:
                        self.x += 50
                if self.player_hp < 0:
                    self.speed = 0
                elif self.is_win == True:
                    self.speed = 0

                if self.x < player_x:
                    self.x += self.speed
                    if player_x - self.x <= 250:
                        screen.blit(pygame.transform.scale(slime_attack[player_anim_count], (100, 100)),
                                    (self.x, self.y))
                    else:
                        screen.blit(pygame.transform.scale(slime_walk[player_anim_count], (100, 100)), (self.x, self.y))
                elif self.x > player_x:
                    self.x -= self.speed
                    if self.x - player_x <= 250:
                        screen.blit(pygame.transform.scale(slime_attack[player_anim_count], (100, 100)),
                                    (self.x, self.y))
                    else:
                        screen.blit(pygame.transform.scale(slime_walk[player_anim_count], (100, 100)), (self.x, self.y))

            else:
                screen.blit(pygame.transform.scale(slime_dead[player_anim_count], (100, 100)), (self.x, self.y))
                self.speed = 0

        def player_damage(self, player_damage):
            if self.player_hp == 12:
                screen.blit(pygame.transform.scale(hp_hearts[0], (150, 50)), (10, 10))
            elif self.player_hp == 11:
                screen.blit(pygame.transform.scale(hp_hearts[1], (150, 50)), (10, 10))
            elif self.player_hp == 10:
                screen.blit(pygame.transform.scale(hp_hearts[2], (150, 50)), (10, 10))
            elif self.player_hp == 9:
                screen.blit(pygame.transform.scale(hp_hearts[3], (150, 50)), (10, 10))
            elif self.player_hp == 8:
                screen.blit(pygame.transform.scale(hp_hearts[4], (150, 50)), (10, 10))
            elif self.player_hp == 7:
                screen.blit(pygame.transform.scale(hp_hearts[5], (150, 50)), (10, 10))
            elif self.player_hp == 6:
                screen.blit(pygame.transform.scale(hp_hearts[6], (150, 50)), (10, 10))
            elif self.player_hp == 5:
                screen.blit(pygame.transform.scale(hp_hearts[7], (150, 50)), (10, 10))
            elif self.player_hp == 4:
                screen.blit(pygame.transform.scale(hp_hearts[8], (150, 50)), (10, 10))
            elif self.player_hp == 3:
                screen.blit(pygame.transform.scale(hp_hearts[9], (150, 50)), (10, 10))
            elif self.player_hp == 2:
                screen.blit(pygame.transform.scale(hp_hearts[10], (150, 50)), (10, 10))
            elif self.player_hp == 1:
                screen.blit(pygame.transform.scale(hp_hearts[11], (150, 50)), (10, 10))
            elif self.player_hp <= 0:
                screen.blit(pygame.transform.scale(hp_hearts[12], (150, 50)), (10, 10))
            return self.player_hp

    class Red_Slime:
        def __init__(self, x, y, speed, hp, player_hp, player_speed, is_win):
            self.x = x
            self.y = y
            self.speed = speed
            self.hp = hp
            self.player_hp = player_hp
            self.player_speed = player_speed
            self.is_win = is_win

        def draw(self, magic_x_r, magic_x_l, is_attack, right, left):
            if is_attack:
                if right:
                    if (magic_x_r + 50 >= self.x >= player_x):
                        self.hp -= 1
                elif left:
                    if (magic_x_l - 50 <= self.x <= magic_x_l + 50):
                        self.hp -= 1
            if self.hp == 3:
                screen.blit(pygame.transform.scale(slime_hp_hearts[3], (30, 30)), (self.x + 35, self.y))
            elif self.hp == 2:
                screen.blit(pygame.transform.scale(slime_hp_hearts[2], (30, 30)), (self.x + 35, self.y))
            elif self.hp == 1:
                screen.blit(pygame.transform.scale(slime_hp_hearts[1], (30, 30)), (self.x + 35, self.y))
            elif self.hp <= 0:
                screen.blit(pygame.transform.scale(slime_hp_hearts[0], (30, 30)), (self.x + 35, self.y))

            if self.hp > 0:
                if self.x < player_x:
                    self.x += self.speed
                elif self.x > player_x:
                    self.x -= self.speed

                # Проверка отскока
                if abs(self.x - player_x) <= 20 and player_y >= self.y:
                    self.player_hp -= 1
                    slime_sound.play()
                    if left:
                        self.x -= 50
                    else:
                        self.x += 50
                if self.player_hp < 0:
                    self.speed = 0
                elif self.is_win == True:
                    self.speed = 0

                if player_x - self.x <= 250:
                    screen.blit(pygame.transform.scale(evgesha_red_attack[player_anim_count], (100, 100)),
                                (self.x, self.y))
                else:
                    screen.blit(pygame.transform.scale(evgesha_red_walk[player_anim_count], (100, 100)),
                                (self.x, self.y))

            elif self.hp < 0:
                screen.blit(pygame.transform.scale(evgesha_red_dead[2], (100, 100)), (self.x, self.y))
                self.speed = 0

        def player_damage(self, player_damage):
            if self.player_hp == 12:
                screen.blit(pygame.transform.scale(hp_hearts[0], (150, 50)), (10, 10))
            elif self.player_hp == 11:
                screen.blit(pygame.transform.scale(hp_hearts[1], (150, 50)), (10, 10))
            elif self.player_hp == 10:
                screen.blit(pygame.transform.scale(hp_hearts[2], (150, 50)), (10, 10))
            elif self.player_hp == 9:
                screen.blit(pygame.transform.scale(hp_hearts[3], (150, 50)), (10, 10))
            elif self.player_hp == 8:
                screen.blit(pygame.transform.scale(hp_hearts[4], (150, 50)), (10, 10))
            elif self.player_hp == 7:
                screen.blit(pygame.transform.scale(hp_hearts[5], (150, 50)), (10, 10))
            elif self.player_hp == 6:
                screen.blit(pygame.transform.scale(hp_hearts[6], (150, 50)), (10, 10))
            elif self.player_hp == 5:
                screen.blit(pygame.transform.scale(hp_hearts[7], (150, 50)), (10, 10))
            elif self.player_hp == 4:
                screen.blit(pygame.transform.scale(hp_hearts[8], (150, 50)), (10, 10))
            elif self.player_hp == 3:
                screen.blit(pygame.transform.scale(hp_hearts[9], (150, 50)), (10, 10))
            elif self.player_hp == 2:
                screen.blit(pygame.transform.scale(hp_hearts[10], (150, 50)), (10, 10))
            elif self.player_hp == 1:
                screen.blit(pygame.transform.scale(hp_hearts[11], (150, 50)), (10, 10))
            elif self.player_hp <= 0:
                screen.blit(pygame.transform.scale(hp_hearts[12], (150, 50)), (10, 10))
            return self.player_hp

    slime_spawn = []
    tutorial_spawn = []

    is_game_over = False
    is_win = False

    is_slime_count = False

    slime_count = 0
    slime_count_2 = 0
    slime_count_3 = 0
    slime_count_4 = 0
    slime_count_5 = 0
    slime_count_6 = 0
    red_evgesha_count = 0

    is_number_ten = False
    is_number_twenty = False
    is_number_therty = False
    is_number_fourty = False
    is_number_fifty = False

    is_tutorial = False
    is_e_pressed = False

    e_pressed = 0

    class Button:
        def __init__(self, text, position, action):
            self.text = text
            self.position = position
            self.action = action

        def draw(self):
            font = pygame.font.Font("assets/fonts/Adventurer/Adventurer.ttf", 70)
            text_surface = font.render(self.text, True, ('red'))
            screen.blit(text_surface, self.position)

        def is_clicked(self, mouse_pos):
            return pygame.Rect(self.position, (200, 50)).collidepoint(mouse_pos)

    ##level_music.play()
    button_restart = None
    button_menu = None

    running: bool = True
    while running:

        if slime_count == 50:
            is_win = True

        player_speed = 3

        magic_x_r = player_x + 80 * 2
        magic_x_l = player_x - 80 * 2
        magic_y = player_y

        screen.blit(pygame.transform.scale(level_1_back, (W, H)), (0, 0))

        keys = pygame.key.get_pressed()
        mods = pygame.key.get_mods()

        current_time = pygame.time.get_ticks()

        if is_tutorial == True:

            screen.blit(pygame.transform.scale(border, (313, 153)), (950, 0))

            ##счетчик, боже блять спасите
            if slime_count <= 9:
                screen.blit(pygame.transform.scale(numbers[slime_count], (50, 70)), (1000, 40))
            elif slime_count >= 9 and slime_count <= 19:
                is_number_ten = True
                screen.blit(pygame.transform.scale(numbers[1], (50, 70)), (1000, 40))
                screen.blit(pygame.transform.scale(numbers[slime_count_2], (50, 70)), (1050, 40))
            elif slime_count >= 19 and slime_count <= 29:
                is_number_twenty = True
                screen.blit(pygame.transform.scale(numbers[2], (50, 70)), (1000, 40))
                screen.blit(pygame.transform.scale(numbers[slime_count_3], (50, 70)), (1050, 40))
            elif slime_count >= 29 and slime_count <= 39:
                is_number_therty = True
                screen.blit(pygame.transform.scale(numbers[3], (50, 70)), (1000, 40))
                screen.blit(pygame.transform.scale(numbers[slime_count_4], (50, 70)), (1050, 40))
            elif slime_count >= 39 and slime_count <= 49:
                is_number_fourty = True
                screen.blit(pygame.transform.scale(numbers[4], (50, 70)), (1000, 40))
                screen.blit(pygame.transform.scale(numbers[slime_count_5], (50, 70)), (1050, 40))
            elif slime_count == 50:
                screen.blit(pygame.transform.scale(numbers[5], (50, 70)), (1000, 40))
                screen.blit(pygame.transform.scale(numbers[0], (50, 70)), (1050, 40))

            ##слаймы рот их ебала
            screen.blit(pygame.transform.scale(slime_walk[1], (100, 100)), (1150, -40))
            screen.blit(pygame.transform.scale(evgesha_red_walk[1], (100, 100)), (1150, 10))

            if slime_count % 2 == 0:
                is_slime_count = True

            if not slime_spawn:
                if not is_slime_count:
                    slime_spawn.append(Slime(slime_x, slime_y, slime_speed, slime_hp, player_hp, player_speed, is_win))
                else:
                    slime_spawn.append(Red_Slime(red_evgesha_x, red_evgesha_y, red_evgesha_speed, red_evgesha_hp, player_hp, player_speed, is_win))

            if red_evgesha_count % 2 == 0:
                is_slime_count = False

            if any(slime.hp > 0 for slime in slime_spawn):
                is_slime_alive = True

            else:
                is_slime_alive = False
                if not is_slime_count:
                    slime_count += 1
                    if is_number_ten == True:
                        slime_count_2 += 1
                    if is_number_twenty == True:
                        slime_count_2 = 0
                        slime_count_3 += 1
                    if is_number_therty == True:
                        slime_count_3 = 0
                        slime_count_4 += 1
                    if is_number_fourty == True:
                        slime_count_4 = 0
                        slime_count_5 += 1
                    if is_number_fifty == True:
                        slime_count_5 = 0
                        slime_count_6 += 1
                    print(slime_count)

            for slime in slime_spawn:
                slime.draw(magic_x_r, magic_x_l, is_attack, right, left)
            if not is_slime_alive:
                slime_spawn = [slime for slime in slime_spawn if slime.hp > 0]

            for slime in slime_spawn:
                if slime.player_hp != player_hp:
                    player_hp -= 1
                    slime.player_damage(player_hp)

            if player_hp <= 0:
                is_game_over = True

            for slime in slime_spawn:
                slime.player_damage(player_hp)
        else:
            screen.blit(pygame.transform.scale(laying_scroll, (70, 30)), (scroll_x, scroll_y))
            screen.blit(tutorial_text, (10, 0))
            if keys[pygame.K_e] and abs(player_x + 50 > scroll_x > player_x - 50):
                if not is_e_pressed:
                    is_e_pressed = True

                    if not tutorial_spawn:
                        tutorial_spawn.append(scroll)
                    else:

                        tutorial_spawn.remove(scroll)
                        is_tutorial = True
            else:
                is_e_pressed = False

            for tutorial in tutorial_spawn:
                screen.blit(pygame.transform.scale(tutorial, (1300, 600)), (-10, -20))

            # чекаем че там по анимациям и фреймам
        if (current_time - last_stand_update > animation_delays["stand"]):
            last_stand_update = current_time
            player_anim_count = (player_anim_count + 1) % 4
            stand_anim_count = (player_anim_count + 1) % 4

        elif(current_time - last_attack_update > animation_delays["attack"]):
            last_attack_update = current_time
            attack_anim_count = (attack_anim_count + 1) % 8

        elif(current_time - last_animation_update > animation_delays["ice_attack"]):
            last_animation_update = current_time
            ice_attack_count = (ice_attack_count + 1) % 6
        elif(current_time - last_run_update > animation_delays["run"]):
            last_run_update = current_time
            run_count = (run_count + 1) % 4


        if is_game_over == False and is_win == False:

            if keys[pygame.K_1]:
                is_attack = True
                if not is_attack_sound:
                    is_attack_sound = True
                    attack_sound.play()

            if is_attack:
                if right:
                    screen.blit(pygame.transform.scale(attack_right[attack_anim_count], (100, 100)), (player_x, player_y))
                    screen.blit(pygame.transform.scale(attack_anim[ice_attack_count], (100, 100)), (magic_x_r, magic_y))
                    left = False
                    right = True
                else:
                    left = True
                    right = False
                    screen.blit(pygame.transform.scale(attack_left[attack_anim_count], (100, 100)), (player_x, player_y))
                    screen.blit(pygame.transform.scale(attack_anim[ice_attack_count], (100, 100)), (magic_x_l, magic_y))

                if attack_anim_count >= 7:
                    is_attack = False
                    is_attack_sound = False


            elif keys[pygame.K_a]:
                left = True
                right = False
                if keys[pygame.K_a] and mods & pygame.KMOD_LSHIFT:
                    player_speed = 7
                    player_x -= player_speed
                    screen.blit(pygame.transform.scale(run_left[run_count], (100, 100)), (player_x, player_y))
                else:
                    left = True
                    right = False
                    player_x -= player_speed
                    screen.blit(pygame.transform.scale(walk_left[player_anim_count], (100, 100)), (player_x, player_y))


            elif keys[pygame.K_d]:
                if keys[pygame.K_d] and mods & pygame.KMOD_LSHIFT:
                    player_speed = 7
                    player_x += player_speed
                    screen.blit(pygame.transform.scale(run_right[run_count], (100, 100)), (player_x, player_y))
                    right = True
                    left = False
                else:
                    right = True
                    left = False
                    player_x += player_speed
                    screen.blit(pygame.transform.scale(walk_right[player_anim_count], (100, 100)), (player_x, player_y))

            else:
                if right == True and left == False:
                    screen.blit(pygame.transform.scale(stand_right[stand_anim_count], (100, 100)), (player_x, player_y))
                else:
                    screen.blit(pygame.transform.scale(stand_left[stand_anim_count], (100, 100)), (player_x, player_y))


            if not is_jump:
                if keys[pygame.K_SPACE]:
                    is_jump = True
                    if not jump_sound_played:
                        jump_sound.play()
                        jump_sound_played = True
            else:
                if jump_count >= -9:
                    if jump_count > 0:
                        player_y -= (jump_count ** 2) / 2
                    else:
                        player_y += (jump_count ** 2) / 2
                    jump_count -= 1
                else:
                    is_jump = False
                    jump_count = 9
                    jump_sound_played = False

        elif is_game_over == True:
            screen.blit(game_over_text_border, (377, 195))
            screen.blit(game_over_text, (380, 200))
            screen.blit(pygame.transform.scale(dead_anim[player_anim_count], (100, 100)), (player_x, player_y))
            button_restart = Button("Restart", (530, 300), runlevel)

            button_menu = Button("Menu", (550, 400), main_menu)
            button_menu.draw()
            button_restart.draw()

        elif is_win == True:
            screen.blit(win_text_border, (470, 200))
            screen.blit(win_text, (450, 200))
            screen.blit(pygame.transform.scale(jump_anim[player_anim_count], (100, 100)), (player_x, player_y))

            button_restart = Button("Restart", (530, 300), runlevel)

            button_menu = Button("Menu", (550, 400), main_menu)

            button_menu.draw()
            button_restart.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                running = False
                pygame.quit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_restart is not None and button_restart.is_clicked(pygame.mouse.get_pos()):
                    ##level_music.stop()
                    button_restart.action()
                elif button_menu is not None:
                    if button_menu.is_clicked(pygame.mouse.get_pos()):
                        button_menu.action()
                        break

        pygame.display.update()
        clock.tick(60)
        from main import main_menu