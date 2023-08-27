# List Menu 
listMenu= []
listBelanjaan=[]

Jalan= True
while Jalan: 
    print("Restaurant Saiz")
    print("1. Master ")
    print("2. Kasir")
    jawabUtama = int(input("jawab= "))
    match jawabUtama:
        case 1:
            print("1. Tambah menu")
            print("2. Hapus Menu")
            print("3. Lihat Menu")
            jawabMaster = int(input("Jawaban = "))

            match jawabMaster:
                case 1:
                    menuBaru= input("Masukan Menu= ")
                    listMenu.append(menuBaru)
                case 2:
                    menuDihapus = input("Masukan menu = ")
                    listMenu.remove(menuDihapus)
                case 3:
                    print(listMenu)
                

        case 2: 
            print("1. Tambah belanjaan ")
            print("2. Hapus belanjaan ")
            print("3. Lihat belanjaan ")
            jawabKasir = int(input("Jawaban = "))

            match jawabKasir:
                case 1:
                    for idx, menu in enumerate(listMenu):
                        print(f'{idx + 1}. {menu}')
                    belanjaanBaru= int(input("Masukan menu= "))
                    listBelanjaan.append(listMenu[belanjaanBaru - 1])
                case 2:
                    for idx, menu in enumerate(listMenu):
                        print(f'{idx + 1}. {menu}')
                    belanjaanDihapus= int(input("masukan menu = "))
                    listBelanjaan.pop(belanjaanDihapus - 1)
                case 3:
                    print(listBelanjaan)
        case 0:
            Jalan= False    
