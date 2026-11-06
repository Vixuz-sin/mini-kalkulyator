# Mini-kalkulyator

Foydalanuvchidan ikkita son olib, to'rt asosiy arifmetik amal natijalarini chiqaradigan Python dasturi.

## Imkoniyatlar
- `input()` + `float()` bilan tur o'zgartirish
- `+`, `-`, `*`, `/` amallari (0 ga bo'lish tekshiriladi)
- Natijalar `round()` bilan 2 xonagacha yaxlitlanadi
- `type()` bilan har bir son uchun konvertatsiyadan oldingi/keyingi tur va har bir amal natijasining turi ko'rsatiladi

## Ishga tushirish
```
python3 kalkulyator.py
```

## Namuna natija
```
1-QADAM: Sonlarni kiritish
  1-son: 12.5
  2-son: 4

2-QADAM: str -> float konvertatsiya
  a: '12.5' (str)  ->  12.5 (float)
  b: '4' (str)  ->  4.0 (float)

3-QADAM: Natijalar
----------------------------------------
  12.5 + 4.0     = 16.5       tur: float
  12.5 - 4.0     = 8.5        tur: float
  12.5 * 4.0     = 50.0       tur: float
  12.5 / 4.0     = 3.12       tur: float
----------------------------------------
```
