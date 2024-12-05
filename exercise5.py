"""To'g'ri to'rtburchakning yuzini va perimetrini uning qarama-qarshi uchlari koordinatasi
orqali hisoblovchi RectIps nomli funksiya hosil qiling. (x1, y1, x2, y2) to'g'ri to'rtburchakning qarama
qarshi uchlari RectIps funksiyasi orqali 2 ta to'rtburchak yuzi va perimetrini hisoblang. To'rtburchak tomonlari
koordinatalar o'qiga parallel."""

def RectIps(x1, y1, x2, y2):
    a = abs(x2 - x1)
    b = abs(y2 - y1)
    S = a * b
    P = 2 * (a + b)

    return f"Yuzasi: {S}, Perimetri: {P}"

x1 = int(input("x1 ni kiriting: "))
x2 = int(input("x2 ni kiriting: "))
y1 = int(input("y1 ni kiriting: "))
y2 = int(input("y2 ni kiriting: "))

print(RectIps(x1, y1, x2, y2))