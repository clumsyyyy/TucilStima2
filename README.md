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
**[RECOMMENDED]** Pengujian dilakukan pada Python 3.9.4 64-bit, namun pengujian pada Python 3.7 / Google Colaboratory dapat dilakukan.

## Kompilasi
1. Pastikan berada di folder `lib` (`root/src/lib`)
2. Jalankan perintah berikut:
```pip install -e .```
3. Tunggu hingga instalasi selesai, dan pustaka siap digunakan!

## Penggunaan
1. Untuk meng-import fungsi `ConvexHull`, gunakan perintah:\
```py
from myConvexHull.process import Convex
```
2. Inisiasi _class_ Convex, misal:\
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

## Identitas
13520124 - Owen Christian Wijaya
