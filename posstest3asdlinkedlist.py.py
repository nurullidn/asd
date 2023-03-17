import os
os.system('cls')

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def is_empty(self):
        return self.head is None
    
    def enqueue(self, data):
        new_node = Node(data)
        
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
    def dequeue(self):
        if self.is_empty():
            return None
        
        temp = self.head
        self.head = temp.next
        
        if self.head is None:
            self.rear = None
        
        return temp.data
    
    def display(self):
        if self.is_empty():
            print("SAAT INI ANTRIAN SEDANG KOSONG")
            return
        
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
          
def main():
    queue = Queue()
    
    while True:
        print("\n=====================================")
        print(">>>SELAMAT DATANG DI BANK SI<<<")
        print("-------------------------------------")
        print("ANTRIAN PEMBUATAN REKENING BANK: ")
        print("1. Tambah Antrian")
        print("2. Tampilkan antrian")
        print("3. Panggil Antrian")
        print("4. Keluar")
        print("======================================")
        pilih = int(input("PILIH MENU : "))
        
        if pilih == 1:
            print("SILAHKAN MASUKAN NAMA ANDA!")
            nama = input("NAMA : ")
            queue.enqueue(nama)
                
        elif pilih == 2:
            print("NAMA DALAM ANTRIAN !")
            queue.display()

        elif pilih == 3:
            nama = queue.dequeue()
            if nama is None:
                print("ANTRIAN KOSONG")
            else:
                print(f"NAMA YANG TERHAPUS DARI DAFTAR ANTRIAN: {nama}\n\n")

        elif pilih == 4:
            print("ANDA TELAH KELUAR")
            break
        else:
            print("PILIHAN TIDAK ADA")
            
if __name__ == '__main__':
    main()
    
