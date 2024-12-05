"""Natural sonning raqamlari soni va raqamlari yig'indisini hisoblovchi DigitCountSum
nomli funksiya hosil qiling. Bu funksiya orqali a, b, c sonlarining raqamlari soni va 
yig'indisini hisoblovchi programma tuzilsin."""

def DigitCountSum(a, b, c):
    numbercount_a = len(str(abs(a)))
    numbercount_b = len(str(abs(b)))
    numbercount_c = len(str(abs(c)))

    numberadd = abs(a) + abs(b) + abs(c)

    return f"raqamlar soni,\n A: {numbercount_a} \n B: {numbercount_b} \n C: {numbercount_c} \n\n raqamlar soni: {numberadd}"

a = int(input("a sonini kiriting: "))
b = int(input("b sonini kiriting: "))
c = int(input("c sonini kiriting: "))

print(DigitCountSum(a, b, c))