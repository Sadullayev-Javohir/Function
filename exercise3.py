"""2 ta sonning o'rta arifmetigi va geometrigini hisoblovchi Mean nomli funksiya
hosil qiling. Mean funksiyasi orqali A, B, C, D sonlaridan (A, B), (A, C), (A, D), juftliklarining
o'rta arifmetigi va geometrigini hisoblovchi programma tuzilsin. """

import math

def Mean(A, B, C, D):
    averageArifAB = (A + B) / 2
    averageArifAC = (A + C) / 2
    averageArifAD = (A + D) / 2

    averageGeometrigAB = math.sqrt((A * B)) 
    averageGeometrigAC = math.sqrt((A * C)) 
    averageGeometrigAD = math.sqrt((A * D)) 

    return f"O'rta arifmetik: \n AB: {averageArifAB}\n AC: {averageArifAC} \n AD: {averageArifAD} \n\n O'rta geometrigi: \n AB: {averageGeometrigAB}\n AC: {averageGeometrigAC} \n AD: {averageGeometrigAD}"

print(Mean(2, 3, 4, 6))