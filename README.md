# labpy03

Ahmad Ibnu Abdillah

TI.24.A.5

312410489

Bahasa Pemrograman

# Tugas1
```python
from random import random
```
Kode ini mengimpor fungsi random() dari modul random. Fungsi ini menghasilkan bilangan acak dalam rentang [0, 1) (yaitu dari 0 sampai kurang dari 1).

```python
n = int(input("Masukkan nilai n: "))
```
Baris ini meminta pengguna memasukkan sebuah nilai integer, yang disimpan dalam variabel n. Nilai n ini menunjukkan berapa banyak angka acak yang diinginkan untuk dihasilkan.

```python
count = 0
```
Sebuah variabel count diinisialisasi dengan nilai 0. Ini digunakan untuk menghitung berapa banyak angka acak yang sudah diterima (yang kurang dari 0.5) hingga mencapai nilai n.

```python
while count < n:
```
Loop while akan terus berjalan selama count masih lebih kecil dari n. Artinya, proses akan berhenti setelah jumlah angka yang valid (kurang dari 0.5) mencapai nilai n.

```python
random_number = random()
```
Di dalam loop, random_number = random() akan menghasilkan bilangan acak antara 0 dan 1 setiap kali loop berjalan.

```python
if random_number < 0.5:
```
Kondisi ini memeriksa apakah bilangan acak yang dihasilkan lebih kecil dari 0.5. Jika benar, maka angka tersebut diterima dan akan ditampilkan, serta variabel count akan bertambah 1.

```python
print(f"Data ke-{count+1}: {random_number}")
count += 1
```
-Jika bilangan acak kurang dari 0.5, kode ini akan mencetak angka tersebut dengan format string f"Data ke-{count+1}". Penggunaan {count+1} berfungsi untuk menampilkan nomor urut (dimulai dari 1).

-Setelah itu, variabel count dinaikkan sebesar 1, untuk menunjukkan bahwa satu bilangan acak valid sudah dihasilkan.

# Foto Kode Beserta Hasilnya
![Foto](https://github.com/AhmadIbnuAbdillah/Foto2/blob/b5c696cbf0f27ab724d2cb6f9e728a19b9317921/Screenshot%202024-11-05%20190825.png)

# Tugas2
```python
modal_awal = 100_000_000
```
Di sini, modal_awal diinisialisasi dengan nilai 100.000.000. Ini adalah modal awal atau dana awal yang digunakan untuk menghitung laba selama 8 bulan.

```python
laba_bulan = [0, 0, 0.01, 0.01, 0.05, 0.05, 0.05, 0.03]
```
List laba_bulan berisi persentase laba bulanan yang diharapkan selama 8 bulan. Misalnya:

Bulan 1 dan 2 tidak ada laba (0% atau 0).

Bulan 3 dan 4, laba adalah 1% (0.01).

Bulan 5, 6, dan 7, laba adalah 5% (0.05).

Bulan 8, laba adalah 3% (0.03).

```python
modal = modal_awal
```
Variabel modal diinisialisasi dengan nilai yang sama seperti modal_awal, yaitu 100.000.000. Ini berarti modal pada bulan pertama sama dengan modal awal, dan akan diupdate setiap bulan berdasarkan laba.

```python
for i, presentase_laba in enumerate(laba_bulan):
```
Loop for ini digunakan untuk iterasi melalui setiap elemen dalam laba_bulan. Setiap iterasi memberikan nilai presentase_laba (persentase laba) dan i sebagai indeks bulan (dimulai dari 0).

Enumerasi ini berguna karena kita bisa menghitung laba untuk bulan tertentu dan menampilkan bulan ke berapa sedang dihitung.

```python
laba_bulan_ini = modal * presentase_laba
```
laba_bulan_ini menghitung jumlah laba pada bulan tertentu, dengan cara mengalikan modal saat ini (modal) dengan persentase laba bulan tersebut (presentase_laba).

```python
modal += laba_bulan_ini
```
Setelah laba bulan ini dihitung, modal diperbarui dengan cara menambahkan laba bulan tersebut ke dalam modal yang ada. Ini berarti modal terus bertambah setiap bulan jika ada laba.

```python
print(f"laba bulan ke{i+1}: sebesar {presentase_laba*100}& -> total modal: Rp{modal:,.0f}")
```
Baris ini mencetak laba bulan saat ini serta total modal setelah laba bulan tersebut ditambahkan.

i+1 digunakan untuk menampilkan bulan dalam format 1 hingga 8 (karena i dimulai dari 0).

{presentase_laba*100} mengubah persentase laba dari format desimal menjadi persentase (contohnya 0.05 menjadi 5%).

{modal:,.0f} memformat modal dengan tanda koma sebagai pemisah ribuan dan tanpa desimal, agar lebih mudah dibaca (contoh: Rp100,000,000).

```python
print(f"\nTotal modal pada akhir bulan ke-8: Rp{modal:,.0f}")
```
Setelah perulangan selesai (setelah bulan ke-8), total modal akhir setelah 8 bulan ditampilkan dalam format yang rapi.

# Foto Kode Beserta Hasilnya
![Foto](https://github.com/AhmadIbnuAbdillah/Foto2/blob/3ac42537f16709f77bde09d9990d9f1f3cbab850/Screenshot%202024-11-05%20191917.png)

# Tugas3
```python
saldo = 100000
```
Variabel saldo diinisialisasi dengan nilai 100.000. Ini adalah jumlah saldo awal yang dimiliki pengguna, yang akan berkurang ketika pengguna melakukan penarikan tunai.

```python
while True:
```
Loop while True adalah loop tanpa henti yang akan terus berjalan sampai pengguna memilih untuk keluar dari program. Loop ini memungkinkan pengguna untuk terus melakukan penarikan uang hingga mereka memutuskan untuk menghentikannya.

```python
print(f"\nSaldo saat ini: rp{saldo}")
print("1. tarik tunai")
print("2. keluar")
```
Setiap iterasi dari loop, program mencetak saldo saat ini dengan format string f-string: f"Saldo saat ini: rp{saldo}".

Setelah menampilkan saldo, program menampilkan dua opsi menu:

1. tarik tunai: Jika pengguna memilih opsi ini, mereka akan diminta untuk memasukkan jumlah yang ingin ditarik.
   
2. keluar: Opsi ini akan menghentikan program dan keluar dari loop jika pengguna memilihnya.


```python
pilihan = int(input("pilih menu (1/2): "))
```
Program meminta pengguna untuk memasukkan pilihan (1 atau 2) yang mewakili apakah pengguna ingin menarik tunai atau keluar dari program. Input dari pengguna akan dikonversi menjadi integer dengan int(). Jika pengguna memilih 1, maka program akan menjalankan logika untuk penarikan tunai. Jika memilih 2, program akan keluar (tetapi belum diimplementasikan dalam kode ini).

```python
if pilihan == 1:
    jumlah = int(input("masukan jumlah tarik: rp"))
```
Jika pilihan pengguna adalah 1, maka program akan meminta pengguna untuk memasukkan jumlah uang yang ingin ditarik. Nilai ini juga dikonversi menjadi integer agar bisa digunakan untuk perhitungan saldo.

```python
if jumlah <= saldo:
    saldo -= jumlah
    print(f"penarikan berhasil, sisa saldo anda: rp{saldo}")
else:
    print("saldo anda tidak cukup!")
```
Setelah pengguna memasukkan jumlah penarikan, program akan mengecek apakah jumlah yang dimasukkan lebih kecil atau sama dengan saldo.

Jika jumlah penarikan kurang dari atau sama dengan saldo, maka penarikan berhasil. Saldo akan dikurangi dengan jumlah penarikan (saldo -= jumlah), dan saldo yang tersisa akan ditampilkan ke layar.

Jika jumlah penarikan lebih besar dari saldo, program akan mencetak pesan "saldo anda tidak cukup!" yang menunjukkan bahwa pengguna tidak memiliki cukup uang untuk melakukan penarikan tersebut.

# Foto Kode Beserta Hasil
![Foto](https://github.com/AhmadIbnuAbdillah/Foto2/blob/eb301de72766a123d9e6e982ebe9efb7f8bb8a22/Screenshot%202024-11-05%20193436.png)
