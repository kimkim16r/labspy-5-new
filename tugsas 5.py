data= {}

while True:
    print(" ")
    kim = input("A)dd, E)dit, D)elete, S)earch, L)ist, Q)uit: ")
    if kim.lower() == 'q':
        break
    elif kim.lower() == 'a':
        print("Tambah Data Siswa")
        nama = input("Nama\t\t: ")
        nim = input("NIM\t\t: ")
        tugas = float(input("Nilai Tugas\t: "))
        uts = float(input("Nilai Uts\t: "))
        uas = float(input("Nilai Uas\t: "))
        nilai_akhir = float(tugas)*30/100 + (uts)*30/100 + (uas)*30/100
        data [nim] = nama, tugas, uts, uas, nilai_akhir
    elif kim.lower() == 'e':
        print("Edit Data Siswa")
        nim = input("NIM\t\t: ")
        if nim in data.keys():
            nama = input("Nama new\t: ")
            tugas = float(input("Nilai Tugas new\t: "))
            uts = float(input("Nilai Uts new\t: "))
            uas = float(input("Nilai Uas new\t: "))
            nilai = float(tugas) *30/100 + (uts)*30/100 + (uas)*30/100
            data [nim] = nama, tugas, uts, uas, nilai_akhir
        else:
            print("nim {0} tidak ada".format(nim))
    elif kim.lower() == 'd':
        print("Hapus Data Siswa")
        nim = input("NIM\t\t: ")
        if nim in data.keys():
            del data[nim]
        else:
            print("Siswa Dengan NIM {0} tidak ada".format(nim))
    elif kim.lower() == 's':
        print("Search Siswa")
        nim = input("NIM\t\t: ")
        if nim in data.keys():
            print("Siswa dengan NIM : {0} adalah {1}".format(nim, data[nim]))
        else:
            print("Siswa Dengan NIM : {0} tidak ada".format(nim))
            
    elif kim.lower() == 'l':
        print("\n\tDaftar Data Siswa")
        print("=====================================================================")
        print("Nim | Nama | Nilai Tugas | Nilai Uts | Nilai Uas | Nilai Akhir |")
        print("=====================================================================")
        for x in data.items():
            print("{0:5s} | {1} | ".format(x[0][:30], x[1]))
            print("=================================================================")
    else :
        print(" Pilih menu yang tersedia")




print ("\n\t\t\t **TERIMA KASIH** ")
