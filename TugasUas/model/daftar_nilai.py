from view.input_nilai import *
dict = {}

def tambah_data():
    print('Tambah Data')
    nama = namamahasiswa()
    nim = nimmahasiswa()
    tugas = nilai_tugas()
    uts = nilai_uts()
    uas = nilai_uas()
    akhir = tugas * 0.30 + uts * 0.35 + uas * 0.35
    dict[nama] = nim, uts, uas, tugas, akhir

def hapus_data():
    print("Hapus Data")
    nama = input("Masukan Nama      : ")
    if nama in dict.keys():
       del dict[nama]
       print()
       print('========================================')
       print('=============DATA TERHAPUS==============')
       print('========================================')
    else:
        print("Data {0} Tidak di Temukan".format(nama))

def ubah_data():
    print('         MENGUBAH DATA MAHASISWA         ')
    print('=========================================')
    nama = input("Masukan Nama         : ")
    if nama in dict.keys():
        nim = int(input("Masukan NIM     : "))
        tugas = int(input("Nilai Tugas  : "))
        uts = int(input("Nilai UTS      : "))
        uas = int(input("Nilai UAS      : "))
        akhir = tugas * 0.30 + uts * 0.35 + uas * 0.35
        dict[nama] = nim, tugas, uts, uas, akhir
    else:
        print("Nama {0} Tidak di Tentukan".format(nama))
