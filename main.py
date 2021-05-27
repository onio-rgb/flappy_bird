import pygame
import time
import random

pygame.init()
b_width=100
b_height=92
p_height=1200
p_width=120
display_width=1920
display_height=1080
gameDisplay=pygame.display.set_mode((display_width,display_height))
black=(0,0,0)
white=(255,255,255)
red = (200,0,0)
green = (0,200,0)
bg=pygame.image.load("background.png")
bird=pygame.image.load("bird.png")
pipe=pygame.image.load("pipe.png")
def things_dogded(count):
    font=pygame.font.SysFont(None,25)
    text=font.render("Dodged : "+str(count),True,red)
    gameDisplay.blit(text,(200,110))

def bird_display(x,y):
    gameDisplay.blit(bird,(x,y))
def pipe_display(x,y):
    gameDisplay.blit(pipe,(x,y))
def text_objects(text,font):
    textSurface=font.render(text, True, red)
    return textSurface,textSurface.get_rect()
def message_display(text):
    largeText=pygame.font.SysFont(None,75)
    TextSurf, TextRect=text_objects(text,largeText)
    TextRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)
    gameloop()
def crash():
    message_display('WASTED')




def gameloop():
    global bird
    x = 400
    y = 500
    px=[]
    py1=[]
    py2=[]
    dy=0
    dx=0
    k=0
    t=0
    b_speed=7

    dogded=0
    p_speed = 8
    clock = pygame.time.Clock()
    while not False:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    dy=-b_speed
                if event.key==pygame.K_DOWN:
                    dy=b_speed
                if event.key==pygame.K_LEFT:
                    dx=-b_speed/2.0
                if event.key == pygame.K_RIGHT:
                    dx=b_speed/2.0
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    dy=0
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    dx=0


        dy=dy+(1.0*(1/10))

        y=y+dy
        if x+dx>0 and x+dx<display_width-b_width:
            x=x+dx
        gameDisplay.fill(white)
        gameDisplay.blit(bg, (0, 0))

        if y<-b_height/2.0 or y>display_height-b_height/2.0:
            crash()
        for i in  range(0,k):
            print(px[i]," ")

        bird_display(x,y)
        for i in range(0,k):
            if px[i]!="NULL" and px[i]<0:
                dogded=dogded+1
                px[i]="NULL"
        if dogded%8==0 and dogded!=0:
            p_speed=p_speed+1.0/40.0
            b_speed = b_speed + 1.0 / 50.0

        t=t+1.0/60.0
        if t>2:
            t=0
            k=k+1
            px.append(random.randrange(display_width,display_width+30))
            c=random.randrange(-p_height+200,-p_height+800)
            py1.append(c)
            py2.append(c+p_height+250)

        for i in range(0,k):
            if px[i]!="NULL":
                pipe_display(px[i],py1[i])
                pipe_display(px[i], py2[i])
                px[i]=px[i]-p_speed
        things_dogded(dogded)
        for i in range(0, k):
            if px[i] !="NULL" and px[i]>-100 and px[i]<display_width:
                if y < py1[i] + p_height:
                    if x < px[i] + p_width and x + b_width > px[i] + p_width or x <px[i] and x + b_width > px[i]:
                        crash()
                if y+b_height > py2[i] :
                    if x < px[i] + p_width and x + b_width > px[i] + p_width or x <px[i] and x + b_width > px[i]:
                        crash()
        pygame.display.update()
        clock.tick(60)
gameloop()

pygame.quit()
quit()


