import pygame
from sys import exit
from random import randint, choice
from time import sleep
pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
CELEST = (50, 153, 204)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)
DARK_GREEN = (0, 128, 0)
screen = pygame.display.set_mode((1000, 600))#1000, 600
pygame.display.set_caption("War Game")
icon = pygame.image.load('C:\\Users\\ruycv\\Desktop\\PyThOn\\War Game\\war.jpg')
pygame.display.set_icon(icon)
nation1 = pygame.Rect(350, 300, 250, 100)
nation2 = pygame.Rect(350, 200, 250, 100)
button1c1 = pygame.Rect(900, 510, 90, 70)
button1c2 = pygame.Rect(910, 520, 70, 50)
button2c1 = pygame.Rect(800, 510, 90, 70)
button2c2 = pygame.Rect(810, 520, 70, 50)
button3c1 = pygame.Rect(900, 430, 90, 70)
button3c2 = pygame.Rect(910, 440, 70, 50)
cor1 = BLUE
S1 = cor1
cor2 = RED
S2 = cor2
pygame.mixer.music.load('C:\\Users\\ruycv\\Desktop\\PyThOn\\War Game\\hino-nacional-brasileiro-mp3-3.wav')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(loops=-1)

apertar = pygame.mixer.Sound('C:\\Users\\ruycv\\Desktop\\PyThOn\\War Game\\smw_coin.wav')
apertar.set_volume(0.2)
select = YELLOW
soldier1 = pygame.Rect(nation1.centerx, nation1.centery, 40, 40)
soldier1.center = nation1.center
soldier2 = pygame.Rect(nation2.centerx, nation2.centery, 40, 40)
soldier2.center = nation2.center
numsold1 = 0
numsold2 = randint(10, 30) *5
points = 0
price = 20
gerador = pygame.USEREVENT + 1
gerador_enemy = pygame.USEREVENT + 3
quan = 5
quan_enemy = 5
pygame.time.set_timer(gerador, 1000)
pygame.time.set_timer(gerador_enemy, 3000)
conquest = False
lost = False

def write(text, cor, tam, cords):
    text = str(text)
    fonte = pygame.font.SysFont('Arial', tam)
    texto = fonte.render(text, True, cor)
    textorect = texto.get_rect()
    textorect.center = (cords[0], cords[1])
    screen.blit(texto, textorect)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        screen.fill(CELEST)
        pygame.draw.rect(screen, cor1, nation1)
        pygame.draw.rect(screen, cor2, nation2)
        pygame.draw.rect(screen, DARK_GRAY, button1c1)
        pygame.draw.rect(screen, GRAY, button1c2)
        pygame.draw.rect(screen, DARK_GRAY, button3c1)
        pygame.draw.rect(screen, GRAY, button3c2)
        pygame.draw.rect(screen, DARK_GREEN, soldier1)
        pygame.draw.rect(screen, DARK_GREEN, soldier2)
        
        write(points, YELLOW, 56, (920, 45))
        write("Buy Soldiers", YELLOW, 18, button1c2.center)
        write("+ Ganho", YELLOW, 18, button3c2.center)
        write(numsold1, WHITE, 16, soldier1.center)
        write(numsold2, WHITE, 16, soldier2.center)
        pos = pygame.mouse.get_pos()
        if event.type == gerador and not lost:
            points+=quan
        if event.type == gerador_enemy and not conquest and not lost:
            numsold2+=quan_enemy
        if numsold2 >= 275:
            cor1 = S2
            numsold2-=numsold1
            numsold1 = 0
            lost = True
        if event.type == pygame.MOUSEBUTTONDOWN and not lost:
            if event.button == 3:
                points+=5
                if cor1 == select:
                    if nation2.collidepoint(pos) and numsold1 > numsold2 and not conquest:
                        numsold1-=numsold2
                        numsold2 = 0
                        conquest = True
                        quan*=2

            if event.button == 1 and not lost:
                if nation1.collidepoint(pos):
                    cor1 = select
                    if cor2 == select:
                        cor2 = S1
                if nation2.collidepoint(pos) and conquest:
                    cor2 = select
                    if cor1 == select:
                        cor1 = S1
                if button1c1.collidepoint(pos) or button1c2.collidepoint(pos):
                    if points >= 15:
                        points-=15
                        numsold1+=5
                        apertar.play()
                if button2c1.collidepoint(pos) or button2c2.collidepoint(pos) and conquest:
                    if points >= 15:
                        points-=15
                        numsold2+=5
                        apertar.play()
                if button3c1.collidepoint(pos) or button3c2.collidepoint(pos) and not lost:
                    if points >= price:
                        points-=20
                        quan+=5
                        price+=25
                        apertar.play()
        if conquest and not lost:
            pygame.draw.rect(screen, DARK_GRAY, button2c1)
            pygame.draw.rect(screen, GRAY, button2c2)
            write("Buy Soldiers", YELLOW, 18, button2c2.center)
            
        if lost:
            write("Perdeu...", BLACK, 84, (500, 300))
            frases = ["Lixo!","Talvez da próxima vez...", "Até Mussolini seria melhor que você!", "Duque de Caxias vai te matar!", "Falhaste em teu objetivo..."]
            write(choice(frases), BLACK, 68, (540, 360))            
    pygame.display.update()