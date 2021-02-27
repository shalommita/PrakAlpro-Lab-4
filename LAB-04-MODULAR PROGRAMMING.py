# SHALOMMITA PRANATANTRI
# 71200640
# INFORMATIKA UKDW
# LAB - 4 - MODULAR PROGRAMMING

# SOAL
# REFERENSI ILMUCODING.COM
# MEMBUAT PROGRAM MENGENAI LIST BIODATA MAHASISWA/I BESERTA GRUP MATAKULIAH MAHASISWA TERSEBUT
# DAN NAMA DOSEN PENGAMPUU, MATKUL, BESERTA GRUP YANG DIAMPU

print("-"*27,"NAMA MAHASISWA-MAHASISWI TAHUN 2021","-"*27)
print()

def mahasiswa(nama,nim,sks,grup):
    print("Nama                     : ",nama) # PROSES
    print("NIM                      : ",nim) # PROSES
    print("SKS                      : ",sks) # PROSES
    print("Grup                     : ",grup) # PROSES
    print() # PROSES


# INPUT 
# Input mahasiswa terdiri dari nama mahasiswa, nim, sks, grup
mahasiswa("Jojo","71200677","20","A")
mahasiswa("Teo","71200687","23","B")
mahasiswa("Kanti","71190687","43","B")
mahasiswa("Teli","71200287","23","A")
mahasiswa("Leon","71200685","23","B")
mahasiswa("Tania","71200667","43","A")

print()
print("-"*20,"BERIKUT NAMA DOSEN PENGAMPU BESERTA MATA KULIAH","-"*20)
print()

def dosen(nama,matkul,grup):
    print("Nama                     : ",nama) # PROSES
    print("Mata kuliah yang diampu  : ",matkul) # PROSES
    print("Grup                     : ",grup) # PROSES
    print() # PROSES

# INPUT 
# Input dosen terdiri dari nama, matkul, dan grup yang diampu
dosen("Sapto","JarKom","A")
dosen("Ibnu","JarKom","B")
dosen("Santhia","Bahasa Indonesia","B")
dosen("Hestyn","Bahasa Indonesia","A")
dosen("Tomo","AlPro","A")
dosen("Laurentius","AlPro","B")

# OUTPUT
# ADA 6 MAHASISWA DENGAN BIODATA (NAMA,NIM,SKS,GRUP)
# ADA 6 DOSEN DENGAN BIODATA (NAMA,MATKUL,GRUP YANG DIAMPU)