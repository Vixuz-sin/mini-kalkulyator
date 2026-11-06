# Mini-kalkulyator: ikkita son va 4 ta asosiy amal

print("=" * 30)
print("      MINI-KALKULYATOR")
print("=" * 30)

# 1-qadam: kiritish. input() har doim str qaytaradi
print("\n1-QADAM: Sonlarni kiritish")
a_str = input("  1-son: ")
b_str = input("  2-son: ")

# 2-qadam: str -> float konvertatsiya
try:
    a = float(a_str)
    b = float(b_str)
except ValueError:
    print("Xato: faqat son kiriting!")
    raise SystemExit

# Har bir o'zgaruvchining konvertatsiyadan oldingi va keyingi turi
print("\n2-QADAM: str -> float konvertatsiya")
print(f"  a: {a_str!r} ({type(a_str).__name__})  ->  {a} ({type(a).__name__})")
print(f"  b: {b_str!r} ({type(b_str).__name__})  ->  {b} ({type(b).__name__})")

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
