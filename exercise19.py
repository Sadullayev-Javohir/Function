"""Markazi bir nuqtada bo'lgan, R1 va R2 radiusga ega 2 ta aylananing 
ustma-ust tushmaydigan (kesishmaydigan) qismining yuzasini topuvchi Rings 
nomli funksiya hosil qiling. Doiraning yuzini hisoblash formulasidan 
foydalaning."""

def kesishmaydigan(R1, R2):
    pi = 3.14
    S = pi * ((R1 ** 2)- (R2 ** 2))

    return f"Aylananing ustma-ust tushmaydigan qismining yuzi: {S}"

print(kesishmaydigan(6, 5))