# Izmantotās bibliotēkas

import random 

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

# Piemērs
spele = speles_stavoklis(skaitlu_virkne)
print(spele.virkne)
