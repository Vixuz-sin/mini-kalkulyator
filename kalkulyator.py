# Mini-kalkulyator: ikkita son va 4 ta asosiy amal

print("=" * 30)
print("      MINI-KALKULYATOR")
print("=" * 30)

# input() har doim str qaytaradi -> float ga o'giramiz
a_str = input("1-sonni kiriting: ")
b_str = input("2-sonni kiriting: ")

print("\nKiritilgan qiymat turi:", type(a_str).__name__)   # str

try:
    a = float(a_str)
    b = float(b_str)
except ValueError:
    print("Xato: faqat son kiriting!")
    raise SystemExit

print("O'girilgandan keyingi tur:", type(a).__name__)      # float

# Arifmetik amallar
qoshish    = a + b
ayirish    = a - b
kopaytirish = a * b

print("\n" + "-" * 30)
print("NATIJALAR:")
print("-" * 30)
print(f"{a} + {b} = {round(qoshish, 2)}")
print(f"{a} - {b} = {round(ayirish, 2)}")
print(f"{a} * {b} = {round(kopaytirish, 2)}")

# 0 ga bo'lishni tekshirish
if b == 0:
    print(f"{a} / {b} = Xato: 0 ga bo'lib bo'lmaydi!")
else:
    bolish = a / b
    print(f"{a} / {b} = {round(bolish, 2)}")
    print("\nBo'lish natijasi turi:", type(bolish).__name__)

print("-" * 30)
