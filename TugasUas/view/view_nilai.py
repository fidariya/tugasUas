from model.daftar_nilai import *

def cetak_daftar_nilai():
    if dict.items:
        print("-" * 75)
        print("                                 Daftar Nilai                             ")
        print("-" * 75)
        print("|No. |    Nama    |     NIM     |  Tugas  |  UTS  |  UAS  |  Akhir       |")
        print("-" * 75)
        i = 0
        for y in dict.items():
            i += 1
            print("| {no:2} | {0:10} | {1:11} | {2:5} | {3:5} | {4:7} | {5:7}      |".format
                  (y[0][:13], y[1][0], y[1][1], y[1][2], y[1][3], y[1][4], no=i))
    else:
        print("-" * 75)
        print("                                 Daftar Nilai                              ")
        print("-" * 75)
        print("|No. |    Nama    |     NIM     |  TUGAS  |  UTS  |  UAS  |  Akhir       |")
        print("-" * 75)
        print("|                             TIDAK ADA DATA                               |")
        print("-" * 75)

def cetak_hasil_pencarian():
    nama = input("Masukan Nama       : ")
    if nama in dict.keys:
        print("-" * 75)
        print("                                 Daftar Nilai                             ")
        print("-" * 75)
        print("|No. |    Nama    |     NIM     |  Tugas  |  UTS  |  UAS  |  Akhir       |")
        print("-" * 75)
        print("|  {0:10} | {1:11} | {2:5} | {3:5} | {4:7} | {5:7}      |".format(nama, dict[nama][0], dict[nama][1], dict[nama][2], dict[nama][3], dict[nama][4]))
    else:
        print("Data {0} Tidak di Temukan".format(nama))




