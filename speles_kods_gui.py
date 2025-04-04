
# Izmantotās bibliotēkas
import pygame
import random
import time

# Pygame Community, Pygame documentation, skatīts March 10, 2025. [tiešsaiste].
# Pieejams: https://www.pygame.org/docs/
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
# atsauksmes beigas.

# Krāsas
balta = (255, 255, 255)
melna = (0, 0, 0)
sarkana = (255, 0, 0)
peleks = (128, 128, 128)

# Rezultati
win_sk = 0
lose_sk = 0
tie_sk = 0

# chetanjha888, How to create a text input box with Pygame? [tiešsaiste]. Publikācijas datums: Mar 26 2021. [skatīts 2025.g. 22. martā].
# Pieejams: https://www.geeksforgeeks.org/how-to-create-a-text-input-box-with-pygame/
fonts = pygame.font.Font(None, 36)
ievades_lauks = pygame.Rect(450, 200, 200, 40)
ievade = ""
pogas_1_lauks = pygame.Rect(450, 200, 80, 80)
poga_1 = "1"
pogas_2_lauks = pygame.Rect(550, 200, 80, 80)
poga_2 = "2"
pogas_3_lauks = pygame.Rect(650, 200, 80, 80)
poga_3 = "3"
# atsauksmes beigas.

# Paziņojumi
message_text = "Ievadiet virknes garumu (15-25):"
error_message = ""
gajiens = ""
punkti = ""
cipari = ""
upper_ievads = ""
rezultati = f"Uzvaras: {win_sk} | Zaudējumi: {lose_sk} | Neizšķirti: {tie_sk}"

d_pirmais_speletajs = False
solis = 1

vid_laiks_visas_speles = []

max_dzilums = 2
visited_nodes = 0

# Optimizēta heiristiska funkcija (inspirēta no DeepSeek algoritmiem)
def kombineta_heiristika(virkne, speletaja_punkti, datora_punkti):
    """
    Kombinēta heiristika, kas ņem vērā:
    1. Punktu starpību starp spēlētājiem
    2. Vidējo vērtību atlikušajā virknē
    3. Divus lielākos atlikušos skaitļus
    """
    if not virkne:
        return 0
    
    # 1. Punktu starpība (60% svars)
    starpiba = datora_punkti - speletaja_punkti
    
    # 2. Vidējā vērtība (30% svars)
    videjais = sum(virkne) / len(virkne)
    
    # 3. Divi lielākie skaitļi (10% svars)
    sorted_virkne = sorted(virkne, reverse=True)
    lielakie = sum(sorted_virkne[:2]) if len(sorted_virkne) >= 2 else sum(sorted_virkne)
    
    # Kombinētais heiristiskais novērtējums
    return 0.6 * starpiba + 0.3 * videjais + 0.1 * lielakie

# Koka konstruēšana

# Enozeren, Building a Decision Tree From Scratch with Python [tiešsaiste]. Publikācijas datums: Oct 13 2023. [skatīts 2025.g. 29.martā]. 
# Pieejams: https://medium.com/@enozeren/building-a-decision-tree-from-scratch-324b9a5ed836
# mm6643, How to create a simple non-binary tree from a list of given nodes in Python [tiešsaiste]. Publikācijas datums: Aug 18 2020. [skatīts 2025.g. 29.martā]. 
# Pieejams: https://stackoverflow.com/questions/63465454/how-to-create-a-simple-non-binary-tree-from-a-list-of-given-nodes-in-python
class MoveNode:
    def __init__(self, virkne, speletaja_punkti, datora_punkti, move=None, parent=None):
        self.virkne = virkne.copy()                 # virkne, kurā tiek glabāti skaitļi (iespējamie gājieni), kurus vajag apskatīt
        self.speletaja_punkti = speletaja_punkti    # tēkošie spēlētaja punkti
        self.datora_punkti = datora_punkti          # tēkošie datora punkti
        self.move = move                            # Kurš skaitlis tiek izvēlēts
        self.parent = parent                        # Vecāks mezgls kokā
        self.children = []                          # Iespējamie nākamie gājieni
        self.score = None                           # Heirestiskais novērtējums
   
    def add_child(self, child_node):
        self.children.append(child_node)
# atsauksmes beigas.


# minimax algoritms

# Tuychiev, B., Minimax Algorithm for AI in Python [tiešsaiste]. Publikācijas datums: Jan 31, 2025. [skatīts 2025.g. 10.martā]. 
# Pieejams: https://www.datacamp.com/tutorial/minimax-algorithm-for-ai-in-python
def minimax(node, dzilums, maksimizacija, max_dzilums):
    global visited_nodes
    visited_nodes += 1      # Skaitā katru apmeklēto mezglu
    
    # Pārbaude, vai saraksts jau ir tukšs vai ir maksimālais dziļums
    if len(node.virkne) == 0 or dzilums >= max_dzilums:
	  node.score = kombineta_heiristika(node.virkne, node.speletaja_punkti, node.datora_punkti)
        return node.score
    
    if maksimizacija:         # Maksimizācijas posms (datora gājiens)
        best_score = -float('inf')     # Sākumā labākais rezultāts ir negatīvā bezgalība, jo ir maksimizācija
        for i in range(len(node.virkne)):
           	jauna_virkne = node.virkne[:i] + node.virkne[i+1:]     # Jauns iespējamais spēles stāvoklis
            	jauni_datora_punkti = node.datora_punkti - node.virkne[i]
    		child = MoveNode(jauna_virkne, node.speletaja_punkti, jauni_datora_punkti, node.virkne[i], node)     # Bērna mezgls ar jauno stāvokli
            node.add_child(child)

            # Minimax vērtība
            score = minimax(child, dzilums + 1, False, max_dzilums) 
            best_score = max(best_score, score) # Saglabā labāko rezultātu 
        node.score = best_score
        return best_score

    else:                     # Minimizācijas posms (spēlētāja gājiens)
        best_score = float('inf')     # Sākumā labākais rezultāts ir pozitīvā bezgalība, jo ir minimizācija
        for i in range(len(node.virkne)):
            jauna_virkne = node.virkne[:i] + node.virkne[i+1:]     # Jauns iespējamais spēles stāvoklis
            jauni_speletaja_punkti = node.speletaja_punkti - node.virkne[i]
          child = MoveNode(jauna_virkne, jauni_speletaja_punkti, node.datora_punkti, node.virkne[i], node)     # Bērna mezgls ar jauno stāvokli
            node.add_child(child)

            # Minimax vērtība
            score = minimax(child, dzilums + 1, True, max_dzilums)
            best_score = min(best_score, score)     # Saglabā labāko rezultātu 
        node.score = best_score
        return best_score
# atsauksmes beigas.


# alphabeta algoritms

#Yawar, M., Alpha Beta pruning [tiešsaiste]. Publikācijas datums: Jun 24 2024. [skatīts 2025.g. 21.martā]. 
# Pieejams: https://www.naukri.com/code360/library/alpha-beta-pruning-in-artificial-intelligence
def alphabeta(node, dzilums, alpha, beta, maximizing_player, max_dzilums):
    global visited_nodes
    visited_nodes += 1     # Skaitā katru apmeklēto mezglu
    
    # Pārbaude, vai saraksts jau ir tukšs vai ir maksimālais dziļums
    if len(node.virkne) == 0 or dzilums >= max_dzilums:
	  node.score = kombineta_heiristika(node.virkne, node.speletaja_punkti, node.datora_punkti)
        return node.score

    if maximizing_player:         # Maksimizācijas posms (datora gājiens)
        best_score = -float('inf')     # Sākumā labākais rezultāts ir negatīvā bezgalība, jo ir maksimizācija
        for i in range(len(node.virkne)):
            jauna_virkne = node.virkne[:i] + node.virkne[i+1:]     # Jauns iespējamais spēles stāvoklis
           jauni_datora_punkti = node.datora_punkti - node.virkne[i]
         child = MoveNode(jauna_virkne, node.speletaja_punkti, jauni_datora_punkti, node.virkne[i], node)     # Bērna mezgls ar jauno stāvokli
           node.add_child(child)

           # Alfa-Beta vērtība
           score = alphabeta(child, dzilums + 1, alpha, beta, False, max_dzilums)
           best_score = max(best_score, score)     # Saglabā labāko rezultātu 
           alpha = max(alpha, best_score)          # Dodam alfai lielāko novērtējumu
           if beta <= alpha:                       # Pārbaude, ja beta jau ir sliktākā neka alfa
               break                               # Loka nogriešana (beta)
        node.score = best_score
        return best_score
    
    else:                         # Minimizācijas posms (spēlētāja gājiens)
        best_score = float('inf')     # Sākumā labākais rezultāts ir pozitīvā bezgalība, jo ir minimizācija
        for i in range(len(node.virkne)):
            jauna_virkne = node.virkne[:i] + node.virkne[i+1:]     # Jauns iespējamais spēles stāvoklis
           jauni_speletaja_punkti = node.speletaja_punkti - node.virkne[i]
         child = MoveNode(jauna_virkne, jauni_speletaja_punkti, node.datora_punkti, node.virkne[i], node)     # Bērna mezgls ar jauno stāvokli
           node.add_child(child)

           # Alfa-Beta vērtība
           score = alphabeta(child, dzilums + 1, alpha, beta, True, max_dzilums)
           best_score = min(best_score, score)     # Saglabā labāko rezultātu 
           beta = min(beta, best_score)            # Dodam betai mazāko novērtējumu
           if beta <= alpha:                       # Pārbaude, ja beta jau ir sliktākā neka alfa
               break                               # Loka nogriešana (alfa)
        node.score = best_score
        return best_score
# atsauksmes beigas.

gajienu_laiki = []              # Saglabā katra gājiena izpildes laikus
kopējais_virsotņu_skaits = 0    # Saglabā kopējo apmeklēto virsotņu skaitu

# Funkcija, kas aprēķina labāko datora gājienu
def datora_gajiens(virkne, algoritms, speletaja_punkti, datora_punkti):
    global visited_nodes
    visited_nodes = 0          # Katru reizi skaitam mezglus no 0
    start_time = time.time()   # Laika sākums, lai uzzināt algoritma ilgumu 
    
    root = MoveNode(virkne, speletaja_punkti, datora_punkti)
    best_move = None
    best_score = -float('inf') # No sākuma labākais gājiens ir negatīvā bezgalība 
    
    for i in range(len(virkne)):
        jauna_virkne = virkne[:i] + virkne[i+1:]
        jauni_datora_punkti = datora_punkti - virkne[i]
        child = MoveNode(jauna_virkne, speletaja_punkti, jauni_datora_punkti, virkne[i], root)
        root.add_child(child)
        
        if algoritms == "MM":  # Ja spēlētajs izvēlēja "MM", tad dators izmanto Minimax algoritmu
            score = minimax(child, 0, False, max_dzilums)
        else:                  # Ja spēlētajs izvēlēja "AB", tad dators izmanto Alfa-Beta algoritmu
            score = alphabeta(child, 0, -float('inf'), float('inf'), False, max_dzilums) 
            
        if score > best_score: # Labaka rezultāta pieškiršana
            best_score = score
            best_move = i 
            
    end_time = time.time()                               # Laika beigumd
    algoritma_izpildes_laiks = end_time - start_time     # Skaita, cik laika aizņema algoritms 
    gajienu_laiki.append(algoritma_izpildes_laiks)       # Pievieno šī gājiena laiku
    kopējais_virsotņu_skaits += visited_nodes            # Pieskaita virsotnes kopējam skaitam
    print("Algoritma izpildes laiks ir: " + str(algoritma_izpildes_laiks))
    print(f"Dators apmeklēja {visited_nodes} virsotnes šajā gājienā.")
    return best_move, root


# Spēles stāvokļa klase
class SpelesStavoklis:
    def __init__(self, skaitlu_virkne):
        self.virkne = [random.randint(1, 3) for _ in range(skaitlu_virkne)]  # Ģenerē skaitļus no 1 līdz 3
        self.speletaju_sakuma_punkti = [80, 80]  # Abi spēlētāji sāk ar 80 punktiem
    
    def spelebeidzas(self):  # Funkcija pārbauda, vai spēle ir beigusies
        return len(self.virkne) == 0

# Galvenā spēles cilpa
# Pygame Community, Pygame documentation, skatīts March 10, 2025. [tiešsaiste].
# Pieejams: https://www.pygame.org/docs/
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Pygame loga aizveršana
            running = False
# atsauksmes beigas.

        # antrikshmisri, How to create Buttons in a game using PyGame? [tiešsaiste]. Publikācijas datums: May 08 2020. [skatīts 2025.g. 29. martā].
        # Pieejams: https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/
        if d_pirmais_speletajs or event.type == pygame.MOUSEBUTTONDOWN and solis == 4:
            d_pirmais_speletajs = False
            if 450 <= mouse[0] <= 450+80 and 200 <= mouse[1] <= 200+80:
                iznemtais = 1
                poga_izveleta = True
            elif 550 <= mouse[0] <= 550+80 and 200 <= mouse[1] <= 200+80:
                iznemtais = 2
                poga_izveleta = True
            elif 650 <= mouse[0] <= 650+80 and 200 <= mouse[1] <= 200+80:
                iznemtais = 3
                poga_izveleta = True
        # atsauksmes beigas.

            if speletaja_gajiens and poga_izveleta:
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

            # Atjauno ekrānu
            # chetanjha888, How to create a text input box with Pygame? [tiešsaiste]. Publikācijas datums: Mar 26 2021. [skatīts 2025.g. 22. martā].
            # Pieejams: https://www.geeksforgeeks.org/how-to-create-a-text-input-box-with-pygame/
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
            # atsauksmes beigas.

            if not speletaja_gajiens and solis == 4:
                # Pygame Community, pygame documentation, skatīts March 22, 2025. [tiešsaiste].
                # Pieejams: https://www.pygame.org/docs/ref/time.html
                pygame.time.delay(1500)
                # atsauksmes beigas.
                dators, move_tree = datora_gajiens(spele.virkne, algoritms, spele.speletaju_sakuma_punkti[0], spele.speletaju_sakuma_punkti[1])
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
                abc = sum(gajienu_laiki) / len(gajienu_laiki)
                vid_laiks_visas_speles.append(abc)

        # chetanjha888, How to create a text input box with Pygame? [tiešsaiste]. Publikācijas datums: Mar 26 2021. [skatīts 2025.g. 22. martā].
        # Pieejams: https://www.geeksforgeeks.org/how-to-create-a-text-input-box-with-pygame/
        if event.type == pygame.KEYDOWN and solis != 4:
            if event.key == pygame.K_RETURN:
        # atsauksmes beigas.
                if solis == 1:
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

                elif solis == 2:
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

                elif solis == 3:
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

                elif solis == 5:
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
                            gajienu_laiki = []
                            kopējais_virsotņu_skaits = 0
                        else:
                            running = False
                    else:
                        error_message = "Kļūda: Ievadiet Y vai N!"
                        ievade = ""

            # chetanjha888, How to create a text input box with Pygame? [tiešsaiste]. Publikācijas datums: Mar 26 2021. [skatīts 2025.g. 22. martā].
            # Pieejams: https://www.geeksforgeeks.org/how-to-create-a-text-input-box-with-pygame/
            elif event.key == pygame.K_BACKSPACE:
                ievade = ievade[:-1]
            else:
                ievade += event.unicode
            # atsauksmes beigas.

    # antrikshmisri, How to create Buttons in a game using PyGame? [tiešsaiste]. Publikācijas datums: May 08 2020. [skatīts 2025.g. 29. martā].
    # Pieejams: https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/
    mouse = pygame.mouse.get_pos()
    # atsauksmes beigas.

    # chetanjha888, How to create a text input box with Pygame? [tiešsaiste]. Publikācijas datums: Mar 26 2021. [skatīts 2025.g. 22. martā].
    # Pieejams: https://www.geeksforgeeks.org/how-to-create-a-text-input-box-with-pygame/
    screen.fill(balta)
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
    # Paziņojumi
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
    # atsauksmes beigas.

# Aprēķina un parāda veiktspējas datus pēc spēles
if gajienu_laiki:
    videjais_laiks = sum(gajienu_laiki) / len(gajienu_laiki)
    print("\n=== ALGORITMA VEIKTSPĒJAS DATI PĒDĒJAI SPĒLEI ===")
    print(f"Kopējais gājienu skaits: {len(gajienu_laiki)}")
    print(f"Kopējais apmeklēto virsotņu skaits: {kopējais_virsotņu_skaits}")
    print(f"Vidējais izpildes laiks: {videjais_laiks:.6f} sekundes")
    print(f"Visi izpildes laiki: {[f'{t:.4f}s' for t in gajienu_laiki]}")

atbilde = sum(vid_laiks_visas_speles)/len(vid_laiks_visas_speles)
print(f"Vidējais laiks par visām spēlēm {atbilde}")
# Pygame Community, Pygame documentation, skatīts March 10, 2025. [tiešsaiste].
# Pieejams: https://www.pygame.org/docs/
pygame.quit()
# atsauksmes beigas.
