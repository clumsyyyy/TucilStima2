# Implementasi Convex Hull untuk Visualisasi Tes _Linear Separability Dataset_ dengan Algoritma Divide and Conquer

> Implementasi _library_ untuk melakukan pencarian _convex hull_ dalam data _scatter plot_ dua dimensi
> sebagai Tugas Kecil 2 Mata Kuliah IF2211 Strategi Algoritma

## Daftar Isi
- [Deskripsi Singkat](#deskripsi-singkat)
- [Requirements](#requirements)
- [Kompilasi](#kompilasi)
- [Penggunaan](#penggunaan)
- [Identitas](#identitas)

## Deskripsi Singkat
_Linear separability_ adalah sebuah properti dari dataset dimana dua buah set dari data dua-dimensi (_Euclidean plane_) dapat dipisahkan menggunakan suatu garis. Untuk dapat memisahkan data tersebut, salah satu metode yang dapat digunakan adalah dengan menyambungkan titik-titik luar dari data dua-dimensi tersebut sehingga membentuk suatu bangun datar cembung (_convex hull_). Separabilitas data dapat ditentukan dengan melihat apakah _convex hull_ dari dua buah dataset beririsan atau tidak (apabila tidak beririsan, maka data tersebut dapat dipisahkan dengan sebuah garis.

Algoritma yang digunakan dalam pembuatan pustaka ini adalah algoritma _divide and conquer_ dengan membagi permasalahan-permasalahan yang ada menjadi subpermasalahan yang lebih kecil. Cara kerja algoritma secara umum adalah sebagai berikut:
1. Menentukan titik dengan nilai absis minimum dan maksimum
2. Membentuk garis antara kedua titik di atas dan membagi titik-titik lainnya menjadi _cluster_ bagian kiri dan kanan, tergantung nilai determinan
3. Melakukan proses rekursif di _cluster_ kiri dan kanan untuk mencari titik terjauh dari garis utama dan menambahkan titik tersebut ke _cluster_
4. Melakukan proses rekursif untuk mencari titik terjauh dari garis tersebut hingga semua titik telah diperiksa
5. Menggabungkan hasil proses rekursif kepada sebuah list, dan mengurutkan list tersebut sehingga terbentuk _convex hull_ yang dapat digambarkan dalam sebuah _scatter plot_

## Requirements
**[RECOMMENDED]**
- Python 3.9.4 64-bit, namun pengujian pada Python 3.7 / Google Colaboratory dapat dilakukan.
- Package Installer for Python (pip) 22.0.2
- _Visual Studio Code / PyCharm Community Edition 2020.2_ sebagai IDE pengujian


**[IMPORTANT]** Pada folder `src` terdapat file `main.py` dan `main.ipynb` untuk pengujian. 

**Untuk menampilkan hasil _scatter plot_ dalam _Visual Studio Code_**, sangat direkomendasikan untuk melakukan instalasi _extension_ <a href = "https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter">Jupyter Notebook</a> dan <a href = "https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-extension-pack">Python Extension Pack</a> dengan langkah-langkah seperti berikut:
1. Pada _Visual Studio Code_, pilih opsi _Extensions_ pada bagian _sidebar_ kiri (bisa juga menggunakan _shortcut_ Ctrl + Shift + X)
2. Ketikkan `Jupyter` pada kolom pencarian, lalu pada opsi teratas (Jupyter by Microsoft), klik Install.
   > Lakukan langkah yang sama dengan Python Extension Pack dengan mengetikkan `Python Extension Pack` pada kolom pencarian
3. Apabila instalasi berhasil dilakukan, saat membuka file `main.py`, akan ada pilihan `Run Cell` di atas komentar #%%. Klik pilihan tersebut untuk mengaktifkan _kernel_ dan menampilkan hasil _scatter plot_.
4. Setelah _kernel_ berhasil diaktifkan, akan muncul dialog untuk melakukan input. Masukkan angka dataset yang diinginkan dan kolom yang diinginkan. Hasil _scatter plot_ akan muncul pada kernel.


## Kompilasi
1. Pastikan berada di folder `lib` (`root/src/lib`)
2. Jalankan perintah berikut:
```pip install -e .```
3. Tunggu hingga instalasi selesai, dan pustaka siap digunakan!


## Penggunaan

### Penggunaan Pustaka secara Umum
1. Untuk meng-import fungsi `ConvexHull`, gunakan perintah:
```py
from myConvexHull.process import Convex
```
2. Inisiasi _class_ Convex, misal:
```py
ConvexObj = Convex()
```
3. Saat penggunaan, pastikan fungsi `ConvexHull` menerima parameter berupa _multilist_/ matriks berisi titik (x, y), misal:
```
[[1.4 0.2]
 [1.4 0.2]
 [1.3 0.2]
 [1.5 0.2]
 [1.4 0.2]
 [1.7 0.4]
 ...
```
4. Pemanggilan fungsi ConvexHull (`ConvexObj.ConvexHull()`) dapat dilakukan seperti demikian (contoh di `main.py`):
```py
for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i].iloc[:, [2, 3]].values
    hull = ConvexObj.ConvexHull(bucket)
    # mendapatkan value x, y (kolom 2, 3) dan memasukkan data ke dalam fungsi ConvexHull()
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i], color = colors[i % len(colors)])
    
    #fungsi ConvexHull mengembalikan dua list
    plt.plot(hull[0], hull[1], color = colors[i % len(colors)])
```
Fungsi `ConvexHull()` mengembalikan dua list, satu list berupa daftar absis dari point[i] dan ordinat dari point[i]. Dengan memasukkan list tersebut ke dalam `plt.plot`, sebuah _convex hull_ dapat digambarkan di _scatter plot_

### Penggunaan File `main.py`
#### _Visual Studio Code_ 
1. Pastikan sudah menginstalasi _extensions_ yang dibutuhkan di poin [_requirements_](#requirements)
2. Jalankan _kernel_ dengan mengklik `Run Cell` (file `main.py`) atau `Run All` (file `main.ipynb`), lalu akan muncul dialog pengisian. Apabila menggunakan _Visual Studio Code_, engisian dialog dapat dilakukan di kotak _input box_ yang akan muncul di bagian atas layar
   - Masukkan integer untuk menentukan dataset yang akan dipakai (iris, wine, breast_cancer, atau digits
   - Masukkan integer kolom untuk menentukan kolom yang akan diambil
     [**IMPORTANT**] Karena fungsi akan mengambil dua buah kolom sebagai representasi x dan y, kolom untuk y merupakan **kolom yang berada persis di sebelah angka kolom x**
3. Hasil _scatter plot_ akan muncul di layar!


#### _Pycharm Community Edition_
[**IMPORTANT**] File yang digunakan adalah `main.py`
1. Klik kanan pada IDE, lalu klik opsi `Run`
2. Dialog akan muncul di terminal, dan setelah pengisian dialog (sama dengan cara untuk Visual Studio Code), hasil _scatter plot_ akan muncul!

## Identitas
13520124 - Owen Christian Wijaya
