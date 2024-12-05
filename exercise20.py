"""To'g'ri burchakli uchburchakning katetlari A va B berilganda, uning 
perimetrini hisoblovchi TriangleP nomli funksiya hosil qiling."""

import math

def TriangleP(A, B):
    C = math.sqrt((A ** 2) + (B ** 2))
    P = A + B + C

    return f"Perimetri: {P}"

print(TriangleP(5, 6))