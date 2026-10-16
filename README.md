# Tugas Backend - Refactor Separation of Concerns (SoC)

Proyek ini adalah implementasi REST API sederhana menggunakan **Flask** dengan menerapkan arsitektur **Separation of Concerns (SoC)**. Kode telah direfaktor menggunakan **Flask Blueprint** dan **Application Factory** untuk memisahkan antara *Routing* (Controller), Logika Bisnis (Service), dan Akses Data (Repository).

---

## 📁 Struktur Folder

```text
Tugas-Backend-4/
├── app/
│   ├── __init__.py           # Inisialisasi Application Factory & Blueprint
│   ├── config.py             # Konfigurasi aplikasi (Host, Port, Debug)
│   ├── repositories/
│   │   └── product_repo.py   # Akses dan manipulasi mock data (Database Layer)
│   ├── services/
│   │   └── product_service.py# Logika bisnis dan validasi data (Business Layer)
│   └── routes/
│       └── product_routes.py # Controller untuk menerima Request dan mengirim Response HTTP
├── run.py                    # Entry point untuk menjalankan server
└── README.md                 # Dokumentasi proyek

```

---

## Gambaran Alur Arsitektur (Flow)

Alur kerja aplikasi ini mengikuti pola berikut ketika ada permintaan dari Client (misalnya melalui Postman):

1. **Client (Postman / Web Browser)**
Client mengirimkan HTTP Request (contoh: `GET`, `PUT`, `DELETE`) ke server.
2. **Blueprint Route (`product_routes.py`)**
Berperan sebagai *Controller*. Route murni bertugas menerima request, mengekstrak data dari URL atau JSON Body, dan meneruskannya ke *Service*. Setelah mendapat hasil, Route merakitnya menjadi HTTP Response (JSON) untuk Client.
3. **Service (`product_service.py`)**
Berperan sebagai pemroses logika utama. Di sinilah **Aturan Bisnis** dijalankan. Service akan mengecek validitas data, lalu memanggil fungsi yang sesuai di *Repository* jika data valid.
4. **Repository (`product_repo.py`)**
Berperan khusus berinteraksi dengan sumber data (mock array/database). Repository mengeksekusi perintah (seperti *search*, *update*, atau *delete*) dan mengembalikan hasilnya ke *Service*.

---

## Aturan Bisnis (Business Rules)

Pada *endpoint* pembaruan data barang (`PUT /api/v1/items/<id>`), diterapkan aturan bisnis berikut pada *layer* Service:

* **Harga Barang Validasi**: Nilai `price` tidak boleh berupa angka minus (negatif).
* **Nama Barang Validasi**: Nilai `name` tidak boleh dikosongkan (*empty string*).

Jika aturan ini dilanggar, server akan menolak pembaruan dan mengembalikan status `400 Bad Request`.

---

## Cara Menjalankan Aplikasi

1. Pastikan Python sudah terinstal di sistem kamu.
2. Buka terminal di dalam folder *root* proyek.
3. Jalankan perintah berikut untuk menginstal Flask (jika belum ada):
```bash
pip install flask

```

  Jika ada file `requirements.txt` dan sudah ada Flask didalamnya, maka jalankan perintah berikut:
    ```bash
    pip install -r requirements.txt
    ```

4. Jalankan aplikasi:
```bash
python run.py

```


5. Server akan berjalan pada `http://127.0.0.1:5000`.

---

## Dokumentasi API Endpoints

### 1. Kategori

* **GET `/api/v1/categories**`
* **Deskripsi**: Mengambil semua daftar kategori barang.
* **Response**: `200 OK` (Menampilkan list kategori).



### 2. Barang (Items)

* **GET `/api/v1/items**`
* **Deskripsi**: Mengambil semua data barang. Mendukung Query Parameter `?category=...` dan `?min_price=...`.
* **Contoh URL**: `http://127.0.0.1:5000/api/v1/items?category=elektronik&min_price=5000000`
* **Response**: `200 OK`


* **GET `/api/v1/items/<id>**`
* **Deskripsi**: Mengambil spesifik data barang berdasarkan ID.
* **Response**: `200 OK` (jika ada), `404 Not Found` (jika barang tidak ada).


* **PUT `/api/v1/items/<id>**`
* **Deskripsi**: Memperbarui data barang.
* **Body JSON**:
```json
{
  "name": "Laptop Gaming",
  "category": "Elektronik",
  "price": 8500000
}

```


* **Response**:
* `200 OK` (Berhasil).
* `400 Bad Request` (Jika harga minus atau nama kosong).
* `404 Not Found` (Jika ID tidak ada).




* **DELETE `/api/v1/items/<id>**`
* **Deskripsi**: Menghapus data barang berdasarkan ID.
* **Response**: `200 OK` (Berhasil dihapus), `404 Not Found` (Jika ID tidak ditemukan).



```

***

**Penjelasan tambahan untuk perintah Bash di dalam README:**
*   `pip install flask`: Perintah ini memanggil `pip` (Package Installer for Python) untuk mengunduh dan menginstal pustaka eksternal bernama `flask` dari internet ke dalam lingkungan Python di komputermu, sehingga kode `import flask` dapat berjalan tanpa *error*.
*   `python run.py`: Perintah ini menyuruh *interpreter* Python untuk membaca dan mengeksekusi file `run.py`, yang berfungsi sebagai saklar utama untuk menghidupkan *server* lokalmu.

```