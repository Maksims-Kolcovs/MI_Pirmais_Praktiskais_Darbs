# Izmantotās bibliotēkas
import pygame
import random
import math
import sys

## pygame koda avots https://www.pygame.org/docs/ 

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Joker.lv - Izvēdini prātu!")
clock = pygame.time.Clock()
fonts = pygame.font.SysFont(None, 36)

# Krāsas
balta = (255, 255, 255)
melna = (0, 0, 0)
sarkana = (255, 0, 0)

# Ievades lauks
ievades_lauks = pygame.Rect(490, 300, 300, 40)
ievades_lauks_krasa = melna
active = True
ievade = ""

running = True
error_message = ""
punkti = ""
cipari = ""
gajiens = ""
solis = 1
skaitlu_virkne = None
algoritms = None
iznemtais = None

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

def alphabeta(virkne, dzilums, alpha, beta, maximizing_player):
    if len(virkne) == 0:
        return 0
    
    if maximizing_player:
        best_score = -float('inf')
        for i in range(len(virkne)):
            jauna_virkne = virkne[:i] + virkne[i+1:]
            score = alphabeta(jauna_virkne, dzilums + 1, alpha, beta, False) - virkne[i]
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score
    
    else:
        best_score = float('inf')
        for i in range(len(virkne)):
            jauna_virkne = virkne[:i] + virkne[i+1:]
            score = alphabeta(jauna_virkne, dzilums + 1, alpha, beta, False) + virkne[i]
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score

# Funkcija, kas aprēķina labāko datora gājienu, izmantojot minimax
def datora_gajiens(virkne, algoritms):
    best_move = None
    best_score = -float('inf')
    for i in range(len(virkne)):
        new_virkne = virkne[:i] + virkne[i+1:]  # Simulē gājienu
        if algoritms == "MM":
            score = minimax(new_virkne, 0, False) - virkne[i]
        else:
            score = alphabeta(new_virkne, 0, -float('inf'), float('inf'), False) - virkne[i]
        if score > best_score:  # Atjauno labāko gājienu
            best_score = score
            best_move = i
    return best_move

# Spēles stāvokļa klase
class SpelesStavoklis:
    def __init__(self, skaitlu_virkne):
        self.virkne = [random.randint(1, 3) for _ in range(skaitlu_virkne)]  # Ģenerē skaitļus no 1 līdz 3
        self.speletaju_sakuma_punkti = [80, 80]  # Abi spēlētāji sāk ar 80 punktiem
    
    def spelebeidzas(self):  # Funkcija pārbauda, vai spēle ir beigusies
        return len(self.virkne) == 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:

                    if solis == 1:
                        if ievade.isdigit():
                            skaitlu_virkne = int(ievade)
                            if 15 <= skaitlu_virkne <= 25:
                                error_message = ""
                                solis = 2
                                ievade = ""
                            else:
                                error_message = "Kļūda: Virknes garumam jābūt starp 15 un 25!"
                                ievade = ""
                        else:
                            error_message = "Kļūda: Lūdzu, ievadiet veselu skaitli!"
                            ievade = ""

                    elif solis == 2:
                        algoritms = ievade.strip().upper()
                        if algoritms == "MM" or algoritms == "AB":
                            spele = SpelesStavoklis(skaitlu_virkne)
                            solis = 3
                            move = 1
                            speletaja_gajiens = True
                            ievade = ""
                            error_message = ""
                        else:
                            error_message = "Kļūda: Ievadiet MM vai AB!"
                            ievade = ""

                    elif solis == 3:
                        # Cilvēka gajiens
                        if speletaja_gajiens:
                            if ievade.isdigit():
                                iznemtais = int(ievade)
                                if iznemtais in spele.virkne:
                                    spele.speletaju_sakuma_punkti[0] -= iznemtais
                                    spele.virkne.remove(iznemtais)
                                    speletaja_gajiens = False
                                    move += 1
                                    ievade = ""
                                    error_message = ""
                                else:
                                    error_message = "Kļūda: Virknē nav tāda skaitļa!"
                                    ievade = ""
                            else:
                                error_message = "Kļūda: Lūdzu, ievadiet veselu skaitli!"
                                ievade = ""
                        
                        # Pievienoja šo daļu tikai lai pēc cilvēka gajiena arī atjaunot datus
                        gajiens = f"Gājiens: {move}"
                        punkti = f"Tavi punkti: {spele.speletaju_sakuma_punkti[0]} | Datora punkti: {spele.speletaju_sakuma_punkti[1]}"
                        cipari = f"Virkne: {spele.virkne}"
                        screen.fill(balta)
                        message = fonts.render(message_text, True, melna)
                        screen.blit(message, (460, 200))
                        pygame.draw.rect(screen, ievades_lauks_krasa, ievades_lauks, 3)
                        teksts = fonts.render(ievade, True, melna)
                        screen.blit(teksts, (ievades_lauks.x + 10, ievades_lauks.y + 10))
                        if gajiens:
                            turn = fonts.render(gajiens, True, melna)
                            screen.blit(turn, (450, 450))
                        if punkti:
                            points = fonts.render(f"{punkti}", True, melna)
                            screen.blit(points, (450, 500))
                        if cipari:
                            numbers = fonts.render(f"{cipari}", True, melna)
                            screen.blit(numbers, (450, 550))
                        pygame.display.flip()


                        # Datora gajiens
                        if spele.spelebeidzas():
                            error_message = "Spēle beigusies"
                            solis = 4
                        elif not speletaja_gajiens:
                            pygame.time.delay(1500)
                            dators = datora_gajiens(spele.virkne, algoritms)
                            iznemtais = spele.virkne.pop(dators)
                            spele.speletaju_sakuma_punkti[1] -= iznemtais
                            speletaja_gajiens = True
                            move += 1
                            if spele.spelebeidzas():
                                error_message = "Spēle beigusies"
                                solis = 4

                elif event.key == pygame.K_BACKSPACE:
                    ievade = ievade[:-1]
                else:
                    if len(ievade) < 2:
                        ievade += event.unicode

    screen.fill(balta)

    if solis == 1:
        message_text = "Ievadiet virknes garumu (15-25):"
    elif solis == 2:
        message_text = "Ievadiet algoritma veidu (MM vai AB):"
    elif solis == 3:
        message_text = "Ievadiet skaitli (1-3):"
        gajiens = f"Gājiens: {move}"
        punkti = f"Tavi punkti: {spele.speletaju_sakuma_punkti[0]} | Datora punkti: {spele.speletaju_sakuma_punkti[1]}"
        cipari = f"Virkne: {spele.virkne}"
    elif solis == 4:
        running = False

    message = fonts.render(message_text, True, melna)
    screen.blit(message, (460, 200))

    # Ievades lauks
    pygame.draw.rect(screen, ievades_lauks_krasa, ievades_lauks, 3)
    teksts = fonts.render(ievade, True, melna)
    screen.blit(teksts, (ievades_lauks.x + 10, ievades_lauks.y + 10))

    # Paziņojumi
    if error_message:
        error = fonts.render(error_message, True, sarkana)
        screen.blit(error, (450, 400))
    if gajiens:
        turn = fonts.render(gajiens, True, melna)
        screen.blit(turn, (450, 450))
    if punkti:
        points = fonts.render(f"{punkti}", True, melna)
        screen.blit(points, (450, 500))
    if cipari:
        numbers = fonts.render(f"{cipari}", True, melna)
        screen.blit(numbers, (450, 550))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()