-PENJELASAN PROGRAM
pertama kita membuat class. class ini sebagai prototipe yang ditentukan pengguna untuk objek yang mendefinisikan seperangkat atribut yang menjadi ciri objek kelas apapun.
1. Class Node, fungsinya membuat suatu antrian baru yang kosong. tidak memerlukan parameter dan mengembalikan suatu
   antrian kosong. 
2. Class Queue, Queue dalam bahasa indonesia disebut antrian adalah kumpulan data berurut dimana penambah data baru
   berada di ujung ekor sedangkan penghapusan data berada diujung kepala. queue ini menerapkan metode pengurutan atau lebih dikenal dengan sebutan FIFO (First In First Out). Dimana data yang masuk pertama akan keluar pertama kali. 
3. Kemudian, Pada class Queue kita membuat fungsi __init__() fungsi ini dipanggil saat kita membuat objek disetiap
   data class harus ada (self) sebagai variabel utamanya. variabel (self) menunjuk pada objek tersebut.
3. __init__(), Fungsi Method Init Pada Pemrograman Python yaitu merupakan method yang pertama kali di jalankan atau
    di proses sebelum method-method yang lainnya dan method __init__() berguna untuk melakukan inisialisasi pembuatan object dari class.
4. is_Empty(), menguji untuk melihat apakah antrian dalam keadaan kosong. Tidak memerlukan parameter dan
    mengembalikan nilai boolean.
5. enqueue(), menambahkan suatu item baru keujung antrian.
6. dequeue(), menghapus item depan dari antrian.
7. fungsi main(), memanggil Queue untuk menampil 4 menu program. kita tinggal menginputkan angka 1/2/3/4 untuk
   memilih apa yang ingin kita lakukan.


- FUNGSIONALITAS PROGRAM
program ini berfungsi untuk mempermudah suatu hal agar pekerjaan bisa lebih produktif dan lebih efisien dan aktifitas yang dilakukan pun dapat dilakukan dengan tertib. Linked list memiliki fungsi dan kegunaan sebagai berikut.
1. linked list dapat digunakan untuk mengimplementasikan struktur data lain seperti stack, queue, graf 
    dan lain-lain.
2. digunakan untuk melakukan operasi aritmatika pada bilangan long integer.
3. dipakai untuk representasi mattriks rongga.
4. digunakan dalam alokasi file yang ditautkan
5. membantu dalam manajemen memori


- OUTPUT PROGRAM
jika user menjalankan program, maka akan muncul 4 menu yaitu
1. Tambah antrian. pada menu ini kita akan diminta untuk memasukkan nama kita. dan nama tersebut akan tersimpan
   kedalam  antrian. kita juga bisa menginputkan lebih dari satu nama.
2. Tampilkan antrian. pada menu ini nama yang sudah kita masukkan pada menu tambah antrian akan dimunculkan.
3. panggil antrian. jika kita memilih menu yang ketiga ini, maka nama pertama yang sedang mengantri akan otomatis
   terhapus, karena pada program kali ini menerapkan metode FIFO(First In First Out).
4. Keluar. jika memilih 4 maka program akan terhenti dan jika ingin masuk ke program lagi kita tinggal menjalankan
   ulang program.

