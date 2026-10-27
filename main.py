import formula as f

play = True

while play:
    awal = input("Mawu apa? ")
    if awal.upper() == "KELUAR":
        play = False
        break

    M = int(input("Masukkan modal awal "))
    n = int(input("Masukkan periode ke-n "))
    i = int(input("Masukkan suku bunga "))

    if awal.upper() == "TUNGGAL":
        Mn = f.tunggal(M, n, i)
        print(Mn)
    
    elif awal.upper() == "MAJEMUK":
        Mn = f.majemuk(M, n, i)
        print(Mn)