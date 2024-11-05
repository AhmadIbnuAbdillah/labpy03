saldo = 100000
while True:
    print(f"\nSaldo saat ini: rp{saldo}")
    print("1. tarik tunai")
    print("2. keluar")
    pilihan = int(input("pilih menu (1/2): "))

    if pilihan == 1:
        jumlah = int(input("masukan jumlah tarik: rp"))
        if jumlah <= saldo:
            saldo -= jumlah
            print(f"penarikan berhasil, sisa saldo anda: rp{saldo}")
        else:
            print("saldo anda tidak cukup!")