from prettytable import PrettyTable


# dictionary berisi akun (nama, PIN, saldo, E-pay)
thisdict = {
    'davina'  : {'PIN'    : '6666', 'saldo':    208000,     'E-Pay': 1000000},
    'salma'   : {'PIN'    : '8888', 'saldo':    39000,      'E-Pay': 1000000},
    'aura99'  : {'PIN'    : '7777', 'saldo':    433000,     'E-Pay': 1000000}
}

voucher_toko = {"kode": "dora", "diskon": 0.20, "status": 15}


# tabel dengan pretty table

table_candyshop = PrettyTable()
table_candyshop.field_names = ['no', 'candies', 'price']
table_candyshop.add_row([1, 'Lollipop', 10000])
table_candyshop.add_row([2, 'cotton candy', 20000])
table_candyshop.add_row([3, 'nougat', 30000])
table_candyshop.add_row([4, 'chewing gum', 40000])

# fungsi transaksi
def candyshop_transaksi():
    print('======================================')
    print('     lakukan transaksi candyshop      ')
    print('======================================')
    print(table_candyshop)
    try:
        nomor_permen = int(input("\nselect your favorite candy's number : "))
        if 1 <= nomor_permen <= len(table_candyshop._rows):
            jumlah_permen = int(input("how many candies do you want to buy: "))
            harga_permen = table_candyshop._rows[nomor_permen - 1][2]
            total_harga = jumlah_permen * harga_permen
            print(f" how much you need to pay Rp. {total_harga} ")

        else:
            print("there is no product, try again\n")
    except:
        print("Invalid input. Please enter a valid number.\n")

# fungsi tukar voucher
def redeem_voucher(total_harga, nama):
    nama = nama_login
    print("===================")
    print("------payment------")
    print("===================")
    print("1. E-pay")
    print("2. voucher")
    bayar = input("choose payment method : ")

    if bayar == "1":
        if thisdict[nama]["E-Pay"] >= total_harga:
            thisdict[nama]["E-Pay"] -= total_harga
            print("payment with E-pay successful.")
        else:
            print("not enough E-pay.")
    elif bayar == "2":
        voucher_toko_input = input("enter your voucher code : ")
        if (
            voucher_toko["kode"] == voucher_toko_input
            and voucher_toko["status"] >= 2
        ):
            diskon = total_harga - (total_harga * 0.20)
            thisdict[nama]["E-Pay"] -= diskon
            voucher_toko["status"] -= 1
            print(
                "Congratulations, you saved 20% off the price {diskon}\npayment with voucher is successful "
            )
        else:
            print("voucher code is wrong or voucher is not available, try again.")
    else:
        print("suggestion is not valid.")


def redeem_voucher(total_harga, nama):
    voucher_toko_input = input("Enter your voucher code : ")
    if voucher_toko["kode"] == voucher_toko_input and voucher_toko["status"] >= 2:
        diskon = total_harga - (total_harga * 0.20)
        thisdict[nama]["E-Pay"] -= diskon
        voucher_toko["status"] -= 1
        print(f"Congratulations, you saved 20% off the price {diskon}\nVoucher redeemed successfully.")
    else:
        print("Voucher code is wrong or voucher is not available, try again.")

# fungsi member
def member():
    pin_member = '1975'  
    nama = nama_login
    member_status = input("Apakah Anda memiliki kartu member? (y/n): ")
    if member_status.lower() == "y":
        pin = input("Masukkan PIN Anda: ")
        if pin == pin_member:  
            print('data_valid')
            try:
                total_harga = int(input("Masukkan total harga belanja: "))
                if thisdict[nama]["E-Pay"] >= total_harga:
                    print("Selamat, Anda mendapatkan diskon 30%.")
                    diskon = total_harga * 0.30
                    thisdict[nama]["E-Pay"] -= diskon
                    print(f"Harga belanja setelah diskon: {total_harga - diskon}")
                else:
                    print("E-pay tidak mencukupi.")
            except ValueError:
                print("Invalid input. Please enter a valid number.\n")
        else:
            print("PIN Anda tidak terdaftar atau salah.")
    elif member_status.lower() == "n":
        try:
            total_harga = int(input("Masukkan total harga belanja: "))
            redeem_voucher(total_harga, nama)
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")
    else:
        print("Pilihan tidak valid.")



# fungsi tambah saldo
def tambah_saldo():
    nama = input("Masukkan nama akun Anda: ")
    print("=============================")
    print("--------tambah saldo---------")
    print("=============================")
    try:
        uang = int(input("Enter the nominal amount of money : "))
        if uang > 0:
            thisdict[nama]["saldo"] += uang
            print(f"currently account balance: {thisdict[nama]['saldo']}")
        else:
            print("cannot enter 0")
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")

# fungsi cek saldo
def cek_saldo():
    nama = input("Masukkan nama akun Anda: ")
    print("======================= Cek Saldo ========================")
    print(f"Saldo anda saat ini : {thisdict[nama]['saldo']}")
    print(f"Saldo e-pay anda saat ini : {thisdict[nama]['E-Pay']}")


# fungsi menu utama
def menu():
    
    while True:
        print("=================================")
        print("~~~~~~~~~candyshop~~~~~~~~~~")
        print("================================")

        print("1. order here!")
        print("2. top-up")
        print("3. balance checking")
        print("4. redeem voucher")

        print("5. EXIT")
        pilihan = input("Masukkan pilihan menu : ")
        if pilihan == "1":
            candyshop_transaksi()
            member()
            
        elif pilihan == "2":
            tambah_saldo()
        elif pilihan == "3":
            cek_saldo()

        elif pilihan == "4":
            total_harga = 0
            redeem_voucher(total_harga, nama_login)
        elif pilihan == "5":
            print ('see you again, customer!')
            return
        else:
            print("data not valid, try again")


while True:
    tabel = PrettyTable
    print("================================================================")
    print("-------------------please login candies!------------------------")
    print("================================================================")
    
    nama_login = input("enter your name : ")

    entered_pin = input("Enter your PIN : ")
    if (
        nama_login in thisdict
        and thisdict[nama_login]["PIN"] == entered_pin
    ):
        menu()
    else:
        print("Nama atau pin anda salah, coba lagi\n")
