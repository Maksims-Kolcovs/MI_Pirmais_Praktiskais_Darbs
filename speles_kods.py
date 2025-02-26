# Izmantotās bibliotēkas
import pygame
import random 
## pygame koda avots https://www.pygame.org/docs/ : Kārlis
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            

    screen.fill((255,255,255)) # aizpilda ekrānu baltu
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60
pygame.quit()



# Lietotāja ievade ar pārbaudi
while True:
    try:
        skaitlu_virkne = int(input("Ievadiet virknes garumu (15-25): "))
        if 15 <= skaitlu_virkne <= 25:
            break
        else:
            print("Kļūda: Virknes garumam jābūt starp 15 un 25!")
    except ValueError:
        print("Kļūda: Lūdzu, ievadiet veselu skaitli!")

# Datu struktūra spēles stāvokļu glabāšanai

class speles_stavoklis:
    def __init__(self, skaitlu_virkne):
        self.virkne = [random.randint(1, 3) for _ in range(skaitlu_virkne)] # metode kas ģenerē skaitļus no 1 līdz 3
        self.speletaju_sakuma_punkti = [80, 80]  # Abi spēlētāji sāk ar 80 punktiem
    
    def spelebeidzas():  # funkcija prbauda vai spēle ir beigusies : Kārlis
        if len(spele.virkne) == 0:
            return True
        else:
            return False



# Piemērs
spele = speles_stavoklis(skaitlu_virkne)
print(spele.virkne)
print(spele.speletaju_sakuma_punkti)



for move in range(len(spele.virkne)+1):  # Test piemērs prikeš spēles stāvokļa : Kārlis
    if speles_stavoklis.spelebeidzas() == True:
        print("beidzās spēle")
        break
    else:
        print(move + 1)
        iznemtais = spele.virkne.pop()
        if (move+1) % 2 != 0:
            spele.speletaju_sakuma_punkti[0] -= iznemtais
        else:
            spele.speletaju_sakuma_punkti[1] -= iznemtais
        print(spele.virkne)
    print(spele.speletaju_sakuma_punkti)
