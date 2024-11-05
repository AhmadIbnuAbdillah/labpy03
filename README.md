# labpy03
Nama: Ahmad Ibnu Abdillah
Kelas: TI.24.A.5
NIM: 312410489
Matkul: Bahasa Pemrograman

#Tugas1
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
Jika bilangan acak kurang dari 0.5, kode ini akan mencetak angka tersebut dengan format string f"Data ke-{count+1}". Penggunaan {count+1} berfungsi untuk menampilkan nomor urut (dimulai dari 1).
Setelah itu, variabel count dinaikkan sebesar 1, untuk menunjukkan bahwa satu bilangan acak valid sudah dihasilkan.
