"""X va Y sonlaridan kichigini X ga va kattasini Y ga yozuvchi Minmax(X, Y)
 funksiyasini hosil qiling. Minmax funksiyagini 4 marta chaqirish orqali a, b,
c, d butun sonlaridan kattasini va kichigini aniqlovchi programma tuzilsin."""

def MinMax(X, Y):
    max_Num = max(X, Y)
    min_Num = min(X, Y)

    X = min_Num
    Y = max_Num

    return f"{X}, {Y}"

print(MinMax(19, 17))