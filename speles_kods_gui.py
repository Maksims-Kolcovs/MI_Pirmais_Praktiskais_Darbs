# Izmantotās bibliotēkas
import pygame
import random
import math

## pygame koda avots https://www.pygame.org/docs/ 
# Avots teksta lauka izveidošanai un notikumu apstradei - https://www.geeksforgeeks.org/how-to-create-a-text-input-box-with-pygame/
# Avots pogu izveidošanai un ta uzspiešana ar peli apstrade - https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
fonts = pygame.font.Font(None, 36)

# Krāsas
balta = (255, 255, 255)
melna = (0, 0, 0)
sarkana = (255, 0, 0)
peleks = (128, 128, 128)

# Rezultati
win_sk = 0
lose_sk = 0
tie_sk = 0

# Ievades lauks
ievades_lauks = pygame.Rect(450, 200, 200, 40)
ievade = ""

# Pogas
pogas_1_lauks = pygame.Rect(450, 200, 80, 80)
poga_1 = "1"
pogas_2_lauks = pygame.Rect(550, 200, 80, 80)
poga_2 = "2"
pogas_3_lauks = pygame.Rect(650, 200, 80, 80)
poga_3 = "3"

# Paziņojumi
message_text = "Ievadiet virknes garumu (15-25):"
error_message = ""
gajiens = ""
punkti = ""
cipari = ""
upper_ievads = ""
rezultati = f"Uzvaras: {win_sk} | Zaudējumi: {lose_sk} | Neizšķirti: {tie_sk}"

running = True
d_pirmais_speletajs = False
solis = 1

max_dzilums = 2

# minimax algoritms
# https://www.datacamp.com/tutorial/minimax-algorithm-for-ai-in-python

# virkne - Katrā gājienā viens skaitlis tiek izņemts no šī saraksta.
# Algoritms pārbauda visus iespējamos nākamos gājienus, iterējot cauri sarakstam.

# dzilums - pašreizējais rekursijas dziļums
# Tas tiek palielināts katrā rekursijas solī (depth + 1).

# is_maximizing – norāda, vai šobrīd ir maksimizētāja (True) vai minimizētāja (False) gājiens.

def minimax(virkne, dzilums, maksimizacija):
    if len(virkne) == 0 or dzilums >= max_dzilums:  # Ja virkne ir tukša, spēle beigusies
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
    if len(virkne) == 0 or dzilums >= max_dzilums:
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
        if event.type == pygame.QUIT: # Pygame loga aizveršana
            running = False

        if d_pirmais_speletajs or event.type == pygame.MOUSEBUTTONDOWN and solis == 4: # Cilvēks uzpieža pogu no peles
            d_pirmais_speletajs = False # Nepieciešams, lai dators izdara pirmo gajienu bez papildu darbībam no lietotaja
            if 450 <= mouse[0] <= 450+80 and 200 <= mouse[1] <= 200+80:
                iznemtais = 1
                poga_izveleta = True
            elif 550 <= mouse[0] <= 550+80 and 200 <= mouse[1] <= 200+80:
                iznemtais = 2
                poga_izveleta = True
            elif 650 <= mouse[0] <= 650+80 and 200 <= mouse[1] <= 200+80:
                iznemtais = 3
                poga_izveleta = True
            if speletaja_gajiens and poga_izveleta: # Cilvēka gajiens
                if iznemtais in spele.virkne:
                    spele.speletaju_sakuma_punkti[0] -= iznemtais
                    spele.virkne.pop(spele.virkne.index(iznemtais))
                    speletaja_gajiens = False
                    poga_izveleta = False
                    move += 1
                    error_message = ""
                    ievade = ""
                    gajiens = f"Gājiens: {move}"
                    punkti = f"Tavi punkti: {spele.speletaju_sakuma_punkti[0]} | Datora punkti: {spele.speletaju_sakuma_punkti[1]}"
                    cipari = f"Virkne: {spele.virkne}"
                    if spele.spelebeidzas():
                        solis = 5
                else:
                    error_message = "Kļūda: Virknē nav tāda skaitļa!"
                    ievade = ""

            # Atjauno info par spēles stavokli uz ekrana
            screen.fill(balta)
            pygame.draw.rect(screen, peleks, pogas_1_lauks)
            poga_one = fonts.render(poga_1, True, melna)
            screen.blit(poga_one, (pogas_1_lauks.x + 30, pogas_1_lauks.y + 30))
            pygame.draw.rect(screen, peleks, pogas_2_lauks)
            poga_two = fonts.render(poga_2, True, melna)
            screen.blit(poga_two, (pogas_2_lauks.x + 30, pogas_2_lauks.y + 30))
            pygame.draw.rect(screen, peleks, pogas_3_lauks)
            poga_three = fonts.render(poga_3, True, melna)
            screen.blit(poga_three, (pogas_3_lauks.x + 30, pogas_3_lauks.y + 30))
            message = fonts.render(message_text, True, melna)
            screen.blit(message, (450, 100))
            error = fonts.render(error_message, True, sarkana)
            screen.blit(error, (450, 300))
            turn = fonts.render(gajiens, True, melna)
            screen.blit(turn, (450, 350))
            points = fonts.render(punkti, True, melna)
            screen.blit(points, (450, 400))
            numbers = fonts.render(cipari, True, melna)
            screen.blit(numbers, (450, 450))
            rez = fonts.render(rezultati, True, melna)
            screen.blit(rez, (450, 500))
            pygame.display.flip()
            clock.tick(60)

            if not speletaja_gajiens and solis == 4: # Datora gajiens
                pygame.time.delay(1500) # Dators gaida 1.5 sekundes
                dators = datora_gajiens(spele.virkne, algoritms)
                iznemtais = spele.virkne.pop(dators)
                spele.speletaju_sakuma_punkti[1] -= iznemtais
                speletaja_gajiens = True
                move += 1
                gajiens = f"Gājiens: {move}"
                punkti = f"Tavi punkti: {spele.speletaju_sakuma_punkti[0]} | Datora punkti: {spele.speletaju_sakuma_punkti[1]}"
                cipari = f"Virkne: {spele.virkne}"
                if spele.spelebeidzas():
                    solis = 5
                    
            if solis == 5:
                gajiens = f"Gājiens: {move - 1}"
                cipari = ""
                message_text = "Vai vēlaties spēlēt vēlreiz? (Y vai N):"
                if (spele.speletaju_sakuma_punkti[0] > spele.speletaju_sakuma_punkti[1]):
                    error_message = "Uzvara"
                    win_sk += 1
                elif (spele.speletaju_sakuma_punkti[0] < spele.speletaju_sakuma_punkti[1]):
                    error_message = "Zaudējums"
                    lose_sk += 1
                else:
                    error_message = "Neizšķirts"
                    tie_sk += 1
                rezultati = f"Uzvaras: {win_sk} | Zaudējumi: {lose_sk} | Neizšķirti: {tie_sk}"

        if event.type == pygame.KEYDOWN and solis != 4: # Cilvēks uzpieža pogu no tastaturas
            if event.key == pygame.K_RETURN: # Ievade apstiprinašana (enter)

                if solis == 1: # Virknes garuma izvēle
                    if ievade.isdigit():
                        skaitlu_virkne = int(ievade)
                        if 15 <= skaitlu_virkne <= 25:
                            error_message = ""
                            message_text = "Ievadiet algoritma veidu (MM vai AB):"
                            ievade = ""
                            solis = 2
                        else:
                            error_message = "Kļūda: Virknes garumam jābūt starp 15 un 25!"
                            ievade = ""
                    else:
                        error_message = "Kļūda: Lūdzu, ievadiet veselu skaitli!"
                        ievade = ""

                elif solis == 2: # Algoritma izvēle
                    algoritms = ievade.strip().upper()
                    if algoritms == "MM" or algoritms == "AB":
                        spele = SpelesStavoklis(skaitlu_virkne)
                        error_message = ""
                        ievade = ""
                        message_text = "Ievadiet kurš sāks spēli - cilvēks vai dators (C vai D):"
                        solis = 3
                    else:
                        error_message = "Kļūda: Ievadiet MM vai AB!"
                        ievade = ""

                elif solis == 3: # Izvēle kurš uzsāk spēli
                    upper_ievads = ievade.strip().upper()
                    if upper_ievads == "C" or upper_ievads == "D":
                        move = 1
                        error_message = ""
                        ievade = ""
                        message_text = "Ievadiet skaitli (1-3):"
                        gajiens = f"Gājiens: {move}"
                        punkti = f"Tavi punkti: {spele.speletaju_sakuma_punkti[0]} | Datora punkti: {spele.speletaju_sakuma_punkti[1]}"
                        cipari = f"Virkne: {spele.virkne}"
                        solis = 4
                        if upper_ievads == "C":
                            speletaja_gajiens = True
                        else:
                            speletaja_gajiens = False
                            d_pirmais_speletajs = True
                    else:
                        error_message = "Kļūda: Ievadiet C vai D!"
                        ievade = ""

                elif solis == 5: # Izvele meģināt vēlreiz vai pabeigt spēli
                    upper_ievads = ievade.strip().upper()
                    if upper_ievads == "Y" or upper_ievads == "N":
                        if upper_ievads == "Y":
                            solis = 1
                            message_text = "Ievadiet virknes garumu (15-25):"
                            error_message = ""
                            gajiens = ""
                            punkti = ""
                            cipari = ""
                            ievade = ""
                            upper_ievads = ""
                        else:
                            running = False
                    else:
                        error_message = "Kļūda: Ievadiet Y vai N!"
                        ievade = ""

            elif event.key == pygame.K_BACKSPACE: # Pedeja simbola dzešana
                ievade = ievade[:-1]
            else:
                ievade += event.unicode

    screen.fill(balta)
    mouse = pygame.mouse.get_pos()

    # Ievades lauks
    if solis != 4:
        pygame.draw.rect(screen, peleks, ievades_lauks)
        input = fonts.render(ievade, True, melna)
        screen.blit(input, (ievades_lauks.x + 90, ievades_lauks.y + 10))

    # Pogas
    if solis == 4:
        pygame.draw.rect(screen, peleks, pogas_1_lauks)
        poga_one = fonts.render(poga_1, True, melna)
        screen.blit(poga_one, (pogas_1_lauks.x + 30, pogas_1_lauks.y + 30))
        pygame.draw.rect(screen, peleks, pogas_2_lauks)
        poga_two = fonts.render(poga_2, True, melna)
        screen.blit(poga_two, (pogas_2_lauks.x + 30, pogas_2_lauks.y + 30))
        pygame.draw.rect(screen, peleks, pogas_3_lauks)
        poga_three = fonts.render(poga_3, True, melna)
        screen.blit(poga_three, (pogas_3_lauks.x + 30, pogas_3_lauks.y + 30))

    # Paziņojumi un info par spēles stavokli
    message = fonts.render(message_text, True, melna)
    screen.blit(message, (450, 100))
    error = fonts.render(error_message, True, sarkana)
    screen.blit(error, (450, 300))
    turn = fonts.render(gajiens, True, melna)
    screen.blit(turn, (450, 350))
    points = fonts.render(punkti, True, melna)
    screen.blit(points, (450, 400))
    numbers = fonts.render(cipari, True, melna)
    screen.blit(numbers, (450, 450))
    rez = fonts.render(rezultati, True, melna)
    screen.blit(rez, (450, 500))


    pygame.display.flip()
    clock.tick(60)

pygame.quit()