def tunggal(M, n, i):
    if type(i) is int:
        i = i / 100
    print(f"{n}\n{i}")
    Mn = M * (1 + n * i)
    return Mn

def majemuk(M, n, i):
    if type(i) is int:
        i = i / 100
    print(f"{n}\n{i}")
    Mn = M * ((1 + i) ** n)
    return Mn

