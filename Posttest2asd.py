# Nurul Indriani 2209116067
# Sistem informasi B

# list data yang akan digunakan dalam program
pertama = ['Arsel', 'Avivah', 'Daiva', ['Wahyu', 'Wibi']]
# Arsel, Avivah, Daiva masuk ke dalam variabel kedua
kedua = [] 
# Wahyu, Wibi atau nested list masuk pada variabel ketiga
ketiga = {}

# mensorting data pada list
for a in range(len(pertama)):
    if type(pertama[a]) == str:
        kedua.append(pertama[a])
    else:ketiga[a] = pertama[a]
kedua.sort()
for b in ketiga:
    ketiga[b].sort()
    kedua.insert(b,ketiga[b])
print(kedua)

# mencari index dari data yang berada pada list
while (True):
    x = str(input("Nama yang ingin dicari : ")) #setelah memasukkan nama yang ingin di cari maka index dari nama tersebut akan muncul
    for a in range(len(kedua)):
        if type(kedua[a]) == list:
            for b in range(len(kedua[a])):
                if kedua[a][b] == x:
                    print(f"{x} ditemukan pada index {a} kolom ke - {b}")
        elif kedua[a] == x:
            print(f"{x} ditemukan pada index ke - {a}")