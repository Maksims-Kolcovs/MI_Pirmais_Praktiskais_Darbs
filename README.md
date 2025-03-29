# MI Pirmais Praktiskais Darbs 🛠️
## Atsauces uz visiem lietotiem materiāliem:

1. Anohina-Naumeca A., *Pirmā praktiskā darba apraksts*. Uzdevuma nostādne. DSP332, 24/25-P. 1. lpp
2. Pygame Community, *Pygame documentation*, skatīts March 10, 2025. [tiešsaiste]. Pieejams: https://www.pygame.org/docs/
3. Tuychiev, B., *Minimax Algorithm for AI in Python* [tiešsaiste]. Publikācijas datums: Jan 31, 2025. [skatīts 2025.g. 10.martā]. Pieejams: https://www.datacamp.com/tutorial/minimax-algorithm-for-ai-in-python
4. Yawar, M., *Alpha Beta pruning* [tiešsaiste]. Publikācijas datums: Jun 24 2024. [skatīts 2025.g. 21.martā]. Pieejams: https://www.naukri.com/code360/library/alpha-beta-pruning-in-artificial-intelligence
5. chetanjha888, *How to create a text input box with Pygame?* [tiešsaiste]. Publikācijas datums: Mar 26 2021. [skatīts 2025.g. 22. martā]. Pieejams: https://www.geeksforgeeks.org/how-to-create-a-text-input-box-with-pygame/
6. Pygame Community, *pygame documentation*, skatīts March 22, 2025. [tiešsaiste]. Pieejams: https://www.pygame.org/docs/ref/time.html
7. antrikshmisri, *How to create Buttons in a game using PyGame?* [tiešsaiste]. Publikācijas datums: May 08 2020. [skatīts 2025.g. 29. martā]. Pieejams: https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/
8. Heiristiskās funkcijas inspirētas no DeepSeek algoritmiem un spēļu teorijas pamatiem [tiešaiste]. Pieprasījuma ziņas teksts: vai tu dotajai spēlēi vari piedāvāt kādas varētu būt heirestiskas funkcijas? Pieprasījuma datums: 2025. gada 29. marts 22:20.

## Komandas dalībnieki 👤

1. Maksims Koļcovs 231RDB363
2. Staņislava Šuļženko 231RDB330
3. Dmitrijs Borisevičs 231RDB352
4. Kārlis Neimanis 231LDB002
5. Dāvis Fomičevs 221RDB346

## Soļi izstrādājot darbu📌

1. Jāsaņem spēle no mācībspēka;
2. Jāizvēlas programmēšanas vide/valoda;
3. Jāizveido datu struktūra spēles stāvokļu glabāšanai;
4. Jāprojektē, jārealizē un jātestē spēles algoritmi;
5. Jāveic eksperimenti ar abiem algoritmiem;
6. Jāsagatavo atskaite par izstrādāto spēli un tā ir jāiesniedz e-studiju kursā;
7. jāatbild uz jautājumiem par mākslīgā intelekta rīku izmantošanu spēles izstrādē;
8. Jāveic komandas dalībnieku savstarpējā vērtēšana;
9. Jāpiesakās aizstāvēšanas laikam;
10. Jāaizstāv izstrādātais darbs.



## Prasības programmatūrai 🎯

Spēles sākumā cilvēks-spēlētājs norāda spēlē izmantojamas skaitļu virknes garumu, kas var būt diapazonā no **15 līdz 25** skaitļiem.

Spēles programmatūra gadījuma ceļā saģenerē skaitļu virkni atbilstoši uzdotajam garumam, tajā iekļaujot skaitļus **no 1 līdz 3**.

Programmatūrā obligāti ir jānodrošina šādas iespējas lietotājam: 

Izvēlēties, kurš uzsāk spēli: cilvēks vai dators;
Izvēlēties, kuru algoritmu izmantos dators: Minimaksa algoritmu vai Alfa-beta algoritmu;
Izpildīt gājienus un redzēt izmaiņas spēles laukumā pēc gājienu (gan cilvēka, gan datora) izpildes;
Uzsākt spēli atkārtoti pēc kārtējās spēles pabeigšanas.

Programmatūrai ir jānodrošina grafiskā lietotāja saskarne🧩

---

## Spēles apraksts 🎮

1. Spēles sākumā tiek ģenerēta skaitļu virkne.
2. Katram spēlētājam ir piešķirts **80 punktu**.
3. Spēlētāji izpilda gājienus pēc kārtas:
   - Spēlētājs izņem **vienu** skaitli no skaitļu virknes.
   - Izņemtais skaitlis tiek **atņemts** no spēlētāja pašreizējā punktu skaita.
4. Spēle beidzas, kad skaitļu virkne ir tukša.
5. Uzvarētājs tiek noteikts:
   - Ja spēlētāju punktu skaits ir **vienāds**, tad spēle beidzas **neizšķirti**.
   - Ja punktu skaits atšķiras, tad uzvar spēlētājs, kuram ir **vairāk punktu**.

---

## Piemērs

**Skaitļu virkne:** `2, 1, 3, 2, 1`

| Gājiens | Spēlētājs 1 | Spēlētājs 2 |
| ------- | ----------- | ----------- |
| Sākums  | 80          | 80          |
| 1.      | **78** (-2) | 80          |
| 2.      | 78          | **79** (-1) |
| 3.      | **75** (-3) | 79          |
| 4.      | 75          | **77** (-2) |
| 5.      | **74** (-1) | 77          |

---

## Spēles beigu scenāriji

✅ Uzvar spēlētājs ar lielāku punktu skaitu.
❌ Ja abi spēlētājiem ir vienāds punktu skaits, spēle beidzas neizšķirti.

---


