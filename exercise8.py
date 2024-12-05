"""Kiritilgan k butun musbat sonining o'nga tarafiga (oxiriga) R raqamini (1 <= R <= 9)
qo'shuvchi AddRightDigit nomli
funksiya hosil qiling."""


def AddRightDigit(k):
    add = []

    for k in range(1, k + 1):
        add.append(k)
        katta = max(add)
        katta += 1
    add.append(katta)
    
    return (add)

print(AddRightDigit(15))