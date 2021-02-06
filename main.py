from speedtest import Speedtest
import pygame
yazdir = False
st = Speedtest()


ekran = pygame.display.set_mode((400,400))
pygame.init()
color_dark = (100,100,100)
color_light = (170,170,170)
pygame.display.set_caption("İnternet Hızı Hesaplama")
Font = pygame.font.SysFont("ComicSansMs",18)
Font1 = pygame.font.SysFont("Helvetica",24)
Yazı = Font.render("Leave",1,(255,0,0))
Yazı1 = Font.render("Test",1,(255,0,0))
Yazı2 = Font.render("Delete",1,(255,0,0))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:

            if 400 / 2 <= mouse[0] <= 400 / 2 + 140 and 100 / 2 <= mouse[1] <= 100 / 2 + 40:
                pygame.quit()
                quit()



        mouse = pygame.mouse.get_pos()
        ekran.fill((60,25,60))
    if event.type == pygame.MOUSEBUTTONDOWN:
        if 100 / 2 <= mouse[0] <= 100 / 2 + 140 and 100 / 2 <= mouse[1] <= 100 / 2 + 40:

            download = str(st.download() / 1000000)

            upload = str(st.upload() / 1000000)
            DownloadYazı = Font1.render("Download Hızı: " + download, 1, (255, 0, 0))
            UploadYazı = Font1.render("Upload Hızı: " + upload, 1, (255, 0, 0))

            yazdir = True

        if 250/2 <= mouse[0] <= 250/2+140 and 200 / 2 <= mouse[1] <= 200/2+40:
            yazdir = False
    if yazdir:
        ekran.blit(DownloadYazı, (50, 200))
        ekran.blit(UploadYazı, (50, 300))




    if 400 / 2 <= mouse[0] <= 400 / 2 + 140 and 100 / 2 <= mouse[1] <= 100 / 2 + 40:
        pygame.draw.rect(ekran, color_light, [400 / 2, 100 / 2, 140, 40])

    else:
        pygame.draw.rect(ekran, color_dark, [400 / 2, 100 / 2, 140, 40])

    ekran.blit(Yazı, (400 / 2 + 50, 100 / 2))
    if 100/2<=mouse[0] <= 100/2 + 140 and 100/2<= mouse[1] <= 100/2+40:
        pygame.draw.rect(ekran,color_light,[100/2,100/2,140,40])
    else:
        pygame.draw.rect(ekran, color_dark, [100 / 2, 100 / 2, 140, 40])
    ekran.blit(Yazı1,(100/2+50,100/2))

    if 250/2 <= mouse[0] <= 250/2 + 140 and 200/2<=mouse[1]<=200/2+40:
        pygame.draw.rect(ekran, color_light, [250 / 2, 200 / 2, 140, 40])
    else:
        pygame.draw.rect(ekran, color_dark, [250 / 2, 200 / 2, 140, 40])
    ekran.blit(Yazı2,(250/2+50,200/2))
    pygame.display.update()