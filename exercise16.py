"""Haqiqiy sonning ishorasini aniqlovchi ishora nomli funksiya hosil qiling.
Funksiya argumenti noldan kichik bo'lsa -1; noldan katta bo'lsa 1; nolga
teng bo'lsa O qiymat qaytarsin. Haqiqiy a va b sonlari uchun ishora
(a)+ ishora (b) ifodasi hisoblansin."""

def ishora(x):
    if 0 > x:
        x = -1
        return x
    elif 0 < x:
        x = 1
        return x
    elif x == 0:
        x = 0
        return x

a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))

print(f"a = {ishora(a)}, b = {ishora(b)}\n a + b = {ishora(a) + ishora(b)}")