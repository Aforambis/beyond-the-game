Rusydan Mujtaba Ibnu Ramadhan -
2406421081 -
PBP F

# Tugas 3

## Daftar Isi

1.  [Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?](#1-mengapa-kita-memerlukan-data-delivery-dalam-pengimplementasian-sebuah-platform)
2.  [Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?](#2-mana-yang-lebih-baik-antara-xml-dan-json-mengapa-json-lebih-populer-dibandingkan-xml)
3.  [Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?](#3-fungsi-dari-method-is_valid-pada-form-django-dan-mengapa-dibutuhkan)
4.  [Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?](#4-mengapa-kita-membutuhkan-csrf_token-saat-membuat-form-di-django-apa-yang-dapat-terjadi-jika-kita-tidak-menambahkan-csrf_token-bagaimana-hal-tersebut-dapat-dimanfaatkan-oleh-penyerang)
5.  [Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!](#5-jelaskan-bagaimana-cara-kamu-mengimplementasikan-checklist-di-atas-secara-step-by-step)
6.  [Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?](#6-apakah-ada-feedback-untuk-asdos-di-tutorial-2-yang-sudah-kalian-kerjakan)

---

### 1. Mengapa kita memerlukan _data delivery_ dalam pengimplementasian sebuah platform?

Secara mendasar, _data delivery_ adalah proses pengiriman data dari satu titik ke titik lain (misalnya, dari **server** ke **client**) secara terstruktur, andal, dan efisien. Ini adalah tulang punggung platform modern karena memastikan semua komponen dapat berkomunikasi dengan lancar.

Tanpa mekanisme _data delivery_ yang efektif:

- **Data Tidak Tersampaikan**: Client tidak akan pernah bisa menampilkan informasi terbaru dari server. Bayangkan sebuah platform _e-commerce_ di mana data produk tidak pernah sampai ke browser pengguna; platform tersebut praktis tidak berguna.
- **Inkonsistensi Data**: Informasi yang ditampilkan di berbagai bagian platform bisa menjadi tidak sinkron, membingungkan pengguna.
- **Integrasi Gagal**: Platform modern sering kali bergantung pada layanan pihak ketiga (API). Tanpa _data delivery_, integrasi antar-komponen ini menjadi mustahil.

Singkatnya, _data delivery_ adalah jembatan vital yang memungkinkan data mengalir dan menghidupkan sebuah platform. 🌉

---

### 2. Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Untuk sebagian besar kasus penggunaan web modern, **JSON (JavaScript Object Notation)** dianggap lebih baik dan lebih populer dibandingkan **XML (eXtensible Markup Language)**.

Alasan utamanya adalah:

| Aspek                 | JSON                                                                                                                       | XML                                                                                           |
| :-------------------- | :------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| **Keringkasan**       | Sintaksisnya minimalis dan **ringkas**, sehingga ukuran data lebih kecil dan lebih cepat ditransfer.                       | Lebih _verbose_ (bertele-tele) karena memerlukan tag pembuka dan penutup untuk setiap elemen. |
| **Keterbacaan**       | Sangat **mudah dibaca manusia** (_human-readable_) karena strukturnya mirip objek pada umumnya.                            | Bisa menjadi sulit dibaca jika strukturnya kompleks dan sangat dalam.                         |
| **Kecepatan Parsing** | **Parsing lebih cepat** di hampir semua bahasa, terutama di JavaScript, karena formatnya _native_ dengan objek JavaScript. | Membutuhkan _parser_ khusus yang cenderung lebih lambat dan memakan lebih banyak memori.      |

Meskipun XML memiliki keunggulan dalam hal dukungan skema yang kompleks dan _namespaces_ (berguna di lingkungan _enterprise_), kesederhanaan, kecepatan, dan kemudahan penggunaan menjadikan JSON standar de facto untuk RESTful API dan aplikasi web modern. 🚀

---

### 3. Fungsi dari method `is_valid()` pada form Django dan mengapa dibutuhkan

Method `is_valid()` adalah "penjaga gerbang" untuk data yang dikirimkan melalui form di Django. Fungsinya adalah **menjalankan semua aturan validasi** yang telah didefinisikan pada sebuah _form_ terhadap data yang diinput oleh pengguna.

Kita sangat membutuhkannya untuk tiga alasan utama:

1.  **Menjaga Integritas Data**: Memastikan **data yang disimpan di database selalu valid** dan sesuai dengan format yang ditentukan (tipe data, panjang karakter, email valid, dll.).
2.  **Mencegah Error**: Menghindari _bug_ atau _crash_ pada aplikasi yang disebabkan oleh data yang tidak sesuai format.
3.  **Keamanan**: Melindungi aplikasi dari _input_ berbahaya dengan membersihkan (_sanitizing_) data sebelum diproses lebih lanjut.

Jika `is_valid()` mengembalikan `True`, data yang aman dan bersih akan tersedia di `form.cleaned_data`. Jika `False`, Django akan menyimpan pesan kesalahan di `form.errors` yang bisa ditampilkan kembali ke pengguna sebagai umpan balik. ✅

---

### 4. Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token`? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Kita membutuhkan `{% csrf_token %}` untuk **melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF)**.

Secara sederhana, token ini berfungsi sebagai stempel rahasia yang unik untuk setiap sesi pengguna. Django akan menyisipkan stempel ini di dalam _form_ yang ditampilkan kepada pengguna. Ketika _form_ tersebut dikirim kembali, Django akan memeriksa apakah stempel yang disertakan cocok dengan yang seharusnya.

Ini memastikan bahwa permintaan untuk memproses _form_ tersebut **benar-benar berasal dari situs kita sendiri**, bukan dari situs lain yang mencoba meniru pengguna.

Jika sebuah _form_ tidak dilindungi oleh `csrf_token`, penyerang dapat **memaksa pengguna yang sedang _login_ untuk melakukan aksi yang tidak diinginkan tanpa sepengetahuan mereka**.

**Contoh Skenario Serangan:**

1.  User _login_ ke rekening bank di `bank-aman.com`.
2.  User kemudian membuka tab baru dan mengunjungi situs `situs-jahat.com` milik penyerang.
3.  Situs jahat tersebut memiliki sebuah _form_ tersembunyi yang datanya sudah diisi oleh penyerang (misalnya, untuk mentransfer uang ke rekening mereka). _Form_ ini secara otomatis terkirim ke `bank-aman.com`.
4.  Karena user masih memiliki sesi _login_ yang aktif di `bank-aman.com`, _browser_ user akan secara otomatis menyertakan _cookie_ autentikasi.
5.  Tanpa `csrf_token`, `bank-aman.com` akan menganggap permintaan transfer itu sah dan memprosesnya.

Penyerang dapat memanfaatkan celah ini untuk berbagai tindakan merugikan, seperti:

- Mengubah _password_ atau email akun pengguna.
- Mengirim pesan atas nama pengguna.
- Melakukan transaksi finansial, seperti mentransfer dana atau membeli barang.

---

### 5. Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_.

Berikut adalah langkah-langkah implementasi yang saya lakukan dari awal hingga akhir:

1.  **Inisiasi Proyek**: Membuat _project_ dan _app_ Django baru menggunakan perintah `django-admin startproject` dan `python manage.py startapp`.
2.  **Desain Model**: Mendefinisikan struktur data di `models.py` sesuai kebutuhan, seperti membuat model `Item` dengan berbagai tipe _field_ (`CharField`, `IntegerField`, `TextField`, dll.).
3.  **Migrasi Database**: Menyiapkan skema _database_ berdasarkan model yang telah dibuat dengan menjalankan `python manage.py makemigrations` diikuti `python manage.py migrate`.
4.  **Pembuatan Form**: Membuat _class form_ di `forms.py` (misalnya `ItemForm`) yang terhubung dengan model untuk mempermudah pembuatan dan validasi _form_.
5.  **Logika Views**: Mengimplementasikan logika di `views.py` untuk:
    - Menampilkan semua data dari _database_ (`show_main`).
    - Menangani pembuatan item baru, termasuk validasi _form_ dengan `form.is_valid()`.
    - Menyediakan data dalam format JSON dan XML (`show_json`, `show_xml`).
6.  **Pengaturan URL**: Mendaftarkan setiap _view_ ke _path_ URL yang sesuai di `urls.py` agar dapat diakses oleh pengguna.
7.  **Desain Template**: Membuat _file_ HTML di direktori `templates` untuk menampilkan halaman utama, _form_ tambah item, dan halaman lainnya. Di sinilah `{% csrf_token %}` ditambahkan di dalam setiap tag `<form>`.
8.  **Pengujian**: Melakukan pengujian menyeluruh:
    - Mengakses halaman melalui _browser_ untuk memastikan tampilan dan fungsionalitas UI berjalan baik.
    - Menggunakan _tools_ seperti Postman untuk menguji _endpoint_ API (JSON/XML).
9.  **Debugging & Iterasi**: Memperbaiki _bug_ yang ditemukan selama pengujian.
10. **Version Control**: Melakukan _commit_ secara berkala ke Git dan GitHub untuk melacak perubahan dan berkolaborasi.

---

### 6. Apakah ada _feedback_ untuk asdos di tutorial 2 yang sudah kalian kerjakan?

Tutorial yang diberikan sudah sangat jelas dan terstruktur secara _step-by-step_, sehingga mudah untuk diikuti. Saran saya, akan lebih bermanfaat jika ada contoh **penanganan _error form_** yang lebih mendalam, misalnya cara menampilkan pesan _error_ spesifik untuk setiap _field_. Lalu, bagian _URL routing_ terkadang bisa sedikit membingungkan bagi pemula, terutama saya pribadi. Mungkin bisa dibantu dengan menyertakan **diagram alur sederhana** yang menggambarkan bagaimana sebuah _request_ dari URL dipetakan ke _view_ yang sesuai.
