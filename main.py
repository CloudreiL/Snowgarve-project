import pygame
import sprites
import webbrowser

def main_menu():
    pygame.init()

    W = 1280
    H = 720

    screen = pygame.display.set_mode((W,H),flags=pygame.NOFRAME)
    icon = pygame.image.load("assets/main_icon/photo_2024-03-28_23-50-04.jpg")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Snowgrave")

    ## text
    font = pygame.font.Font("assets/fonts/Adventurer/Adventurer.ttf", 100)
    text_surf = font.render("Snowgrave", True, 'white')

    ## menu
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

    class ButtonLinK:
        def __init__(self, image_path, position, link):
            self.original_image = sprites.telegram
            self.position = position
            self.link = link
            self.image = pygame.transform.scale(self.original_image, (100, 100))

        def draw(self):
            screen.blit(self.image, self.position)

        def is_clicked(self, mouse_pos):
            rect = self.image.get_rect(topleft=self.position)
            return rect.collidepoint(mouse_pos)

    from level1 import runlevel
    button_start = Button("Start", (1000,400), runlevel)
    menu_music.play()

    button_telegram = "https://t.me/snowgravedev"
    telegramButt = ButtonLinK("sprites.telegram.png", (0,0), button_telegram)

    running = True
    while running:
        screen.blit(pygame.transform.scale(sprites.menu_back, (1280, 720)), (0, 0))
        screen.blit(text_surf, (50, 200))
        button_start.draw()
        telegramButt.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_start.is_clicked(pygame.mouse.get_pos()):
                    menu_music.stop()
                    button_start.action()
                    break
                if telegramButt.is_clicked(pygame.mouse.get_pos()):
                    webbrowser.open(telegramButt.link)
        pygame.display.update()

if __name__ == "__main__":
    main_menu()