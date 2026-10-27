import formula as f

play = True

while play:
    awal = input("Mawu apa? ")
    if awal.upper() == "KELUAR":
        play = False
        break

    if awal.upper() == "TUNGGAL":
        M = int(input("Masukkan modal awal "))
        n = int(input("Masukkan periode ke-n "))
        i = int(input("Masukkan suku bunga "))

        Mn = f.tunggal(M, n, i)
        print(Mn)
    
    elif awal.upper() == "MAJEMUK":
        M = int(input("Masukkan modal awal "))
        n = int(input("Masukkan periode ke-n "))
        i = int(input("Masukkan suku bunga "))

        Mn = f.majemuk(M, n, i)
        print(Mn)