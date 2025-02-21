# MI Pirmais Praktiskais Darbs

## Prasības programmatūrai

Spēles sākumā cilvēks-spēlētājs norāda spēlē izmantojamas skaitļu virknes garumu, kas var būt diapazonā no **15 līdz 25** skaitļiem.

Spēles programmatūra gadījuma ceļā saģenerē skaitļu virkni atbilstoši uzdotajam garumam, tajā iekļaujot skaitļus **no 1 līdz 3**.

---

## Spēles apraksts

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


