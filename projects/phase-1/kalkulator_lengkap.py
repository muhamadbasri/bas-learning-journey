print("=" * 35)
print("   KALKULATOR LENGKAP BAS")
print("=" * 35)

while True:
    print("\n1. Tambah (+)")
    print("2. Kurang (-)")
    print("3. Kali (*)")
    print("4. Bagi (/)")
    print("5. Keluar")
    
    pilihan = input("\nPilihan (1-5): ")
    
    if pilihan == "5":
        print("Terima kasih! 👋")
        break
    
    if pilihan not in ["1", "2", "3", "4"]:
        print("❌ Pilihan tidak valid!")
        continue
    
    angka1 = float(input("Angka pertama: "))
    angka2 = float(input("Angka kedua: "))
    
    if pilihan == "1":
        hasil = angka1 + angka2
        simbol = "+"
    elif pilihan == "2":
        hasil = angka1 - angka2
        simbol = "-"
    elif pilihan == "3":
        hasil = angka1 * angka2
        simbol = "*"
    elif pilihan == "4":
        if angka2 == 0:
            print("❌ Error: Tidak bisa bagi nol!")
            continue
        hasil = angka1 / angka2
        simbol = "/"
    
    print(f"\n✅ Hasil: {angka1} {simbol} {angka2} = {hasil}")

