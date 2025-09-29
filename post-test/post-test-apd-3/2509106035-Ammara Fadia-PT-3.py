
usia = int(input("Masukkan usia anda: "))
SIM = input("Apakah anda punya SIM A? (ya/tidak): ")
deposit = int(input("Masukkan deposit anda (minimal 500000): "))
pengalaman = int(input("Berapa tahun pengalaman anda mengemudi (harus berupa angka): "))

if usia < 21:
    print("Tolak: Usia tidak mencukupi")
elif SIM == "tidak":
    print("Tolak: Tidak memiliki sim A")
elif deposit < 500000:
    print("Tolak: Deposit tidak mencukupi")
elif pengalaman < 4:
    print("Setujui untuk mobil standar saja")
else:
    print("Setujui untuk semua jenis mobil")