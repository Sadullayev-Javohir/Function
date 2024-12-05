"""Ikkita sonning qiymatini almashtiruvchi Swap nomli funksiya 
hosil qiling. Swap funksiyasi A, B, C, D sonlaridan (A, B), (D, C) 
juftliklarining qiymatlarini alamashtiruvchi programma tuzilsin."""

def Swap(A, B, C, D):
    A, B = B, A
    D , C = C, D

    return A, B, C, D

print(Swap(14, 12, 54, 17))