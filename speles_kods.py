# Izmantotās bibliotēkas
import pygame
import random 
import math 

## pygame koda avots https://www.pygame.org/docs/ 

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
            
    screen.fill((255, 255, 255))  # Aizpilda ekrānu balti
    pygame.display.flip()
    clock.tick(60)  # Limits FPS to 60

pygame.quit()

# minimax algoritms
# https://www.datacamp.com/tutorial/minimax-algorithm-for-ai-in-python

# virkne - Katrā gājienā viens skaitlis tiek izņemts no šī saraksta.
# Algoritms pārbauda visus iespējamos nākamos gājienus, iterējot cauri sarakstam.

# dzilums - pašreizējais rekursijas dziļums
# Tas tiek palielināts katrā rekursijas solī (depth + 1).

# is_maximizing – norāda, vai šobrīd ir maksimizētāja (True) vai minimizētāja (False) gājiens.


def minimax(virkne, dzilums, maksimizacija):
    if len(virkne) == 0:  # Ja virkne ir tukša, spēle beigusies
        return 0

    if maksimizacija:  # Datora gājiens (maksimizētājs)
        best_score = -float('inf')
        for i in range(len(virkne)):
            jauna_virkne = virkne[:i] + virkne[i+1:]  # Izņem skaitli
            score = minimax(jauna_virkne, dzilums + 1, False) - virkne[i]  # Atņem skaitli no punktiem
            best_score = max(best_score, score)
        return best_score
        
    else:  # Cilvēka gājiens (minimizētājs)
        best_score = float('inf')
        for i in range(len(virkne)):
            jauna_virkne = virkne[:i] + virkne[i+1:]  # Izņem skaitli
            score = minimax(jauna_virkne, dzilums + 1, True) + virkne[i]  # Pieskaita skaitli punktiem
            best_score = min(best_score, score)
        return best_score

# Funkcija, kas aprēķina labāko datora gājienu, izmantojot minimax
def datora_gajiens(virkne):
    best_move = None
    best_score = -float('inf')
    for i in range(len(virkne)):
        new_virkne = virkne[:i] + virkne[i+1:]  # Simulē gājienu
        score = minimax(new_virkne, 0, False) - virkne[i]  # Aprēķina minimax vērtību
        if score > best_score:  # Atjauno labāko gājienu
            best_score = score
            best_move = i
    return best_move

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

# Spēles stāvokļa klase
class SpelesStavoklis:
    def __init__(self, skaitlu_virkne):
        self.virkne = [random.randint(1, 3) for _ in range(skaitlu_virkne)]  # Ģenerē skaitļus no 1 līdz 3
        self.speletaju_sakuma_punkti = [80, 80]  # Abi spēlētāji sāk ar 80 punktiem
    
    def spelebeidzas(self):  # Funkcija pārbauda, vai spēle ir beigusies
        return len(self.virkne) == 0

# Spēles piemērs
spele = SpelesStavoklis(skaitlu_virkne)
print(spele.virkne)
print(spele.speletaju_sakuma_punkti)

# Simulē spēli
for move in range(len(spele.virkne) + 1):
    if spele.spelebeidzas():
        print("Spēle beigusies")
        break
    else:
        print(f"Gājiens: {move + 1}")
        iznemtais = spele.virkne.pop()
        
        if (move + 1) % 2 != 0:  # Nepara gājieni - cilvēks
            spele.speletaju_sakuma_punkti[0] -= iznemtais
        else:  # Para gājieni - dators
            spele.speletaju_sakuma_punkti[1] -= iznemtais
        
        print("Atlikusī virkne:", spele.virkne)
        print("Spēlētāju punkti:", spele.speletaju_sakuma_punkti)
