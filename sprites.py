import pygame


menu_back = pygame.image.load("assets/backgrounds/menu_back/null_background.jpg")

telegram = pygame.image.load("assets/images/social_media/telegram.png")

##Игрок

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

attack_anim = [
    pygame.image.load(
        "assets/animation/skill_animation/ice_attack_2/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Active2.png"),
    pygame.image.load(
        "assets/animation/skill_animation/ice_attack_2/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Active3.png"),
    pygame.image.load(
        "assets/animation/skill_animation/ice_attack_2/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Active5.png"),
    pygame.image.load(
        "assets/animation/skill_animation/ice_attack_2/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending1.png"),
    pygame.image.load(
        "assets/animation/skill_animation/ice_attack_2/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending3.png"),
    pygame.image.load(
        "assets/animation/skill_animation/ice_attack_2/Ice Effect 01/Ice VFX 2/Separated Frames/Ice VFX 2 Ending17.png"),
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

##сердца хп
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

slime_hp_hearts = [
    pygame.image.load("assets/images/hp_hearts/slime_hp/Hearts_Yellow_5.png"),
    pygame.image.load("assets/images/hp_hearts/slime_hp/Hearts_Yellow_4.png"),
    pygame.image.load("assets/images/hp_hearts/slime_hp/Hearts_Yellow_3.png"),
    pygame.image.load("assets/images/hp_hearts/slime_hp/Hearts_Yellow_1.png"),
]

##цифры для счетчика

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
