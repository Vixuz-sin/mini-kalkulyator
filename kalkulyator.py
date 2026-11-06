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

# 3-qadam: arifmetik amallar
qoshish     = a + b
ayirish     = a - b
kopaytirish = a * b
bolish      = a / b if b != 0 else None   # 0 ga bo'lishni tekshirish


def natija_chiqar(belgi, natija):
    """Bitta amal natijasini va uning turini bir xil formatda chiqaradi."""
    ifoda = f"{a} {belgi} {b}"
    if natija is None:
        print(f"  {ifoda:<14} = Xato: 0 ga bo'lib bo'lmaydi!")
    else:
        print(f"  {ifoda:<14} = {round(natija, 2):<10} tur: {type(natija).__name__}")


print("\n3-QADAM: Natijalar")
print("-" * 40)
natija_chiqar("+", qoshish)
natija_chiqar("-", ayirish)
natija_chiqar("*", kopaytirish)
natija_chiqar("/", bolish)
print("-" * 40)
