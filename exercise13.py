"""A, B, C sonlarini kamayish tartibida joylashtiruvchi SortDec3(A, B, C) funksiyasini hosil 
qiling. Ya'ni A, B, C sonlari qiymatlarini shunday almashtiringki, natijada A ning qiymati eng 
katta va C ning qiymati eng kichik bo'lsin. Bu funksiya orqali (A1, B1, C1) va (A2, B2, C2) 
sonlarini tartiblang."""

def Sortinc3(A, B, C):
    if A > B > C:
        return A, B, C
    elif A > C > B:
        return A, C, B
    elif B > A > C:
        return B, A, C
    elif B > C > A:
        return B, C, A
    elif C > B > A:
        return C, B, A

print(Sortinc3(521, 90, 82))