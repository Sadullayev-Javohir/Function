"""O'ngga siklik siljishni amalga oshiruvchi ShiftRight3 (A, B, C) funksiyasini hosil qiling. 
Ya'ni A ning qiymati B ga, B ning qiymati C ga, C ning qiymati A ga o'tib qolsin. Bu funksiya 
orqali (A1, B1, C1) va (A2, B2, C2) sonlarini siljiting."""

def ShiftRight3(A, B, C):
    A, B, C = B, C, A

    return f"A: {A}, B: {B}, C: {C}"

print(ShiftRight3(12, 92, 123))