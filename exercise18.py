""" Doiraning yuzini hisoblovchi funksiya hosil qiling. Bu funksiya 
yordamida 3 ta doira yuzini hisoblang. Doiraning yuzi S=πr**2 orqali 
hisoblanadi. Pi = 3.1415 ni o'zgarmas deb qabul qiling."""

def doiraYuzi(r):
    pi = 3.14
    S = pi * (r ** 2)

    return f"Doiraning yuzi: {S}"

print(doiraYuzi(14))
print(doiraYuzi(45))
print(doiraYuzi(98))