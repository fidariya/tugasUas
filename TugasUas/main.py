from view.view_nilai import*

while True:
    print('=====================================')
    print('|    PROGRAM NILAI DATA MAHASISWA   |')
    print('=====================================')
    data = input('(L)ihat \n(T)ambah \n(U)bah \n(H)apus \n(K)eluar \nPilih Menu Yang Tersedia :')
    if data in ('l', 'L'):
        cetak_daftar_nilai()
    elif data in ('t','T'):
        tambah_data()
    elif data in ('u','U'):
        ubah_data()
    elif data in ('h','H'):
        hapus_data()
    elif data in ('k','K'):
        print("Terima Kasih")
        break
    else:
        print('     Pilih Menu Yang Tersedia       ')
        print('====================================')
