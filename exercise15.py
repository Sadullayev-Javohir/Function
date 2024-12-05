"""Chapga siklik siljishni amalga oshiruvchi ShiftLeft3(A, B, C) funksiyasini hosil qiling. 
Ya'ni C ning qiymati B ga, B ning qiymati A ga, A ning qiymati C ga o'tib qolsin. Bu funksiya 
orqali (A1, B1, C1) va (A2, B2, C2) sonlarini siljiting."""

def ShiftLeft3(A, B, C):
    C, B, A = B, A, C

    return f"C: {C}, B: {B}, A: {A}"

print(ShiftLeft3(123, 32, 64))