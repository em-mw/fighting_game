import pygame

WIDTH, HEIGHT = 900, 500
BG_COLOR = (255, 255, 255)
FPS = 60

Window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Whatever master David wants here🤔🤔🤔")
#pygame.display.set_icon(master david's picture) we will set this up later

def window_init(player1, player2):
    Window.fill(BG_COLOR)
    pygame.draw.rect(Window, (255, 0, 0), player1)
    pygame.draw.rect(Window, (0, 0, 255), player2)
    pygame.display.update()



def main():
    player1 = pygame.Rect(700, 380, 44, 38)
    player1_health=100
    player2 = pygame.Rect(100, 380, 56, 45)
    player2_health=100
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:player1.x-=5
        if keys_pressed[pygame.K_RIGHT]:player1.x+=5
        if keys_pressed[pygame.K_a]:player2.x-=3
        if keys_pressed[pygame.K_d]:player2.x+=3
        if keys_pressed[pygame.K_f]:
            player1_health-=7
            print(f"player1: {player1_health} player2: {player2_health}")
        if keys_pressed[pygame.K_PAGEDOWN]:
            player2_health-=3
            print(f"player1: {player1_health} player2: {player2_health}")
        window_init(player1, player2)
    
    pygame.quit()

if __name__ == '__main__':
    main()