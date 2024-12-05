"""Butun musbat sonining raqamlarini teskari tartibda chiqaruvchi invertDigit nomli funksiya
hosil qiling. Bu funksiya orqali a, b, c sonlarining raqamlari teskari tartibda chiqaruvchi programma
tuzilsin."""

def invertDigit(a, b, c):
    a = str(a)[::-1]
    b = str(b)[::-1]
    c = str(c)[::-1]
    
    return a, b, c

print(invertDigit(2134, 13412, 13515))