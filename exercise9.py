"""Kiritilgan k butun musbat sonining chap tarafiga (boshiga) R raqamini (1 <= R <= 9)
qo'shuvchi AddRightDigit nomli
funksiya hosil qiling."""

def AddRightDigit(k):
    add = []

    for k in range(1, k + 1):
        add.append(k)
        kichik = min(add)
        kichik += 1
    add.insert(0, kichik)
    
    return (add)

print(AddRightDigit(15))