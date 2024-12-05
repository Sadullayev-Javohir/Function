"""Teng tomonli 3 burchakni yuzasi va perimetrini hisoblovchi Triange 
nomli funksiya hosil qiling. Triangle funksiyasi orqali 3 ta teng tomonli
uchburchakning perimetri va yuzini hisoblovchi programma tuzilsin."""

import math

def Triangle(a):
    P = 3 * a
    S = (math.sqrt(3) / 4) * (a**2)

    return f"Perimetri: {P}, Yuzasi: {S}"

print(Triangle(3))