import pygame

def main_menu():
    pygame.init()

    W = 1280
    H = 720

    screen = pygame.display.set_mode((W,H),flags=pygame.NOFRAME)
    icon = pygame.image.load("assets/images/snowflake_icon_project.png")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Snowgrave")

    ## text
    font = pygame.font.Font("assets/fonts/Adventurer/Adventurer.ttf", 100)
    text_surf = font.render("Snowgrave", True, 'white')

    ## menu
    menu_back = pygame.image.load("assets/backgrounds/menu_back/null_background.jpg")
    menu_music = pygame.mixer.Sound("assets/audio/menu_music/Snowfall Symphony.mp3")
    menu_music.set_volume(0.5)


    class Button:
        def __init__(self, text, position, action):
            self.text = text
            self.position = position
            self.action = action

        def draw(self):
            font = pygame.font.Font("assets/fonts/Adventurer/Adventurer.ttf", 70)
            text_surface = font.render(self.text, True, (255, 255, 255))
            screen.blit(text_surface, self.position)

        def is_clicked(self, mouse_pos):
            return pygame.Rect(self.position, (200,50)).collidepoint(mouse_pos)

    from level1 import runlevel
    button_start = Button("Start", (1000,400), runlevel)
    ##menu_music.play()

    running = True
    while running:
        screen.blit(pygame.transform.scale(menu_back, (1280, 720)), (0, 0))
        screen.blit(text_surf, (50, 200))
        button_start.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_start.is_clicked(pygame.mouse.get_pos()):
                    ##menu_music.stop()
                    button_start.action()
                    break
        pygame.display.update()

if __name__ == "__main__":
    main_menu()