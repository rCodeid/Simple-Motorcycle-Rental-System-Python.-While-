print("========== SEWA MOTOR ==========")
import datetime
nama=(input("nama penyewa : "))
tanggal_sewa=(input("masukkan tanggal (YYYYMMDD) : "))
tanggal=datetime.datetime.strptime(tanggal_sewa,"%Y%m%d" ).date()

while True:
    print("===== MENU SEWA MOTOR =====")
    print("1. NMAX tarif Rp100.000/hari")
    print("2. ZX tarif Rp350.000/hari")
    print("3. Vario tarif Rp70.000/hari")
    print("4. Keluar")

    pilihan= (input("pilih motor (nomor) : "))
   
    if pilihan == "4":
        print("anda keluar")
        break
        
    elif pilihan == "1":
       motor= "NMAX"
       harga=100000
       
    elif pilihan == "2":
        motor = "ZX"
        harga= 350000
     
    elif pilihan == "3":
        motor= "VARIO"
        harga= 70000
       
    else:
         print("motor tidak tersedia")
         continue

    hari=int(input("lama sewa (hari) : "))
    total = hari * harga

    if hari <= 2:
      diskon= total * 0 /100

    elif hari>= 7:
      diskon = total * 20 /100

    else:
        diskon = total * 10 / 100

    uang= int(input("masukkan uang : "))

    kembalian_diskon= total - diskon
    while uang < kembalian_diskon:
         print("uang tidak cukup : ", kembalian_diskon - uang)
         uang=int(input("masukkan uang lagi : "))

    kembalian= uang - kembalian_diskon

    print("\n========== STRUK MOTOR ==========")
    print(f"{'nama':<15} : {nama}")
    print(f"{'motor':<15} : {motor}")
    print(f"{'hari':<15} : {hari}")
    print(f"{'tanggal sewa':<15} : {tanggal}")
    print(f"{'total sewa':<15} : Rp{total:,.0f}")
    print(f"{'diskon':<15} : Rp{diskon:,.0f}")
    print(f"{'total bayar':<15} : Rp{kembalian_diskon:,.0f}")
    print(f"{'uang':<15} : Rp{uang:,.0f}")
    print(f"{'kembalian':<15} : Rp{kembalian:,.0f}")
    print("================================")
     
    break
