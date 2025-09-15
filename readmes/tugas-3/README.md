Rusydan Mujtaba Ibnu Ramadhan -
2406421081 -
PBP F

# Tugas 3

### 1. Mengapa kita memerlukan _data delivery_ dalam pengimplementasian sebuah platform?

Secara mendasar, _data delivery_ adalah proses pengiriman data dari satu titik ke titik lain (misalnya, dari **server** ke **client**) secara terstruktur, andal, dan efisien. Ini adalah tulang punggung platform modern karena memastikan semua komponen dapat berkomunikasi dengan lancar.

Tanpa mekanisme _data delivery_ yang efektif:

- **Data Tidak Tersampaikan**: Client tidak akan pernah bisa menampilkan informasi terbaru dari server. Bayangkan sebuah platform _e-commerce_ di mana data produk tidak pernah sampai ke browser pengguna; platform tersebut praktis tidak berguna.
- **Inkonsistensi Data**: Informasi yang ditampilkan di berbagai bagian platform bisa menjadi tidak sinkron, membingungkan pengguna.
- **Integrasi Gagal**: Platform modern sering kali bergantung pada layanan pihak ketiga (API). Tanpa _data delivery_, integrasi antar-komponen ini menjadi mustahil.

Singkatnya, _data delivery_ adalah jembatan vital yang memungkinkan data mengalir dan menghidupkan sebuah platform.

Sumber referensi:

- [K2view](https://www.k2view.com/what-is-a-data-pipeline)

---

### 2. Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Untuk sebagian besar kasus penggunaan web modern, **JSON (JavaScript Object Notation)** dianggap lebih baik dan lebih populer dibandingkan **XML (eXtensible Markup Language)**.

Alasan utamanya adalah:

| Aspek                 | JSON                                                                                                                       | XML                                                                                           |
| :-------------------- | :------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| **Simplicity**        | Sintaksisnya minimalis dan **ringkas**, sehingga ukuran data lebih kecil dan lebih cepat ditransfer.                       | Lebih _verbose_ (bertele-tele) karena memerlukan tag pembuka dan penutup untuk setiap elemen. |
| **Readability**       | Sangat **mudah dibaca manusia** (_human-readable_) karena strukturnya mirip objek pada umumnya.                            | Bisa menjadi sulit dibaca jika strukturnya kompleks dan sangat dalam.                         |
| **Kecepatan Parsing** | **Parsing lebih cepat** di hampir semua bahasa, terutama di JavaScript, karena formatnya _native_ dengan objek JavaScript. | Membutuhkan _parser_ khusus yang cenderung lebih lambat dan memakan lebih banyak memori.      |

Meskipun XML memiliki keunggulan dalam hal dukungan skema yang kompleks dan _namespaces_ (berguna di lingkungan _enterprise_), kesederhanaan, kecepatan, dan kemudahan penggunaan menjadikan JSON standar de facto untuk RESTful API dan aplikasi web modern.

Sumber referensi:

- [Sitepoint](https://www.sitepoint.com/json-vs-xml/)
- [Amazon Web Services](https://aws.amazon.com/compare/the-difference-between-json-xml/)

---

### 3. Fungsi dari method `is_valid()` pada form Django dan mengapa dibutuhkan

Method `is_valid()` adalah "penjaga gerbang" untuk data yang dikirimkan melalui form di Django. Fungsinya adalah **menjalankan semua aturan validasi** yang telah didefinisikan pada sebuah _form_ terhadap data yang diinput oleh pengguna.

Kita sangat membutuhkannya untuk tiga alasan utama:

1.  **Menjaga Data Integrity**: Memastikan **data yang disimpan di database selalu valid** dan sesuai dengan format yang ditentukan (tipe data, panjang karakter, email valid, dll.).
2.  **Mencegah Error**: Menghindari _bug_ atau _crash_ pada aplikasi yang disebabkan oleh data yang tidak sesuai format.
3.  **Keamanan**: Melindungi aplikasi dari _input_ berbahaya dengan membersihkan (_sanitizing_) data sebelum diproses lebih lanjut.

Jika `is_valid()` mengembalikan `True`, data yang aman dan bersih akan tersedia di `form.cleaned_data`. Jika `False`, Django akan menyimpan pesan kesalahan di `form.errors` yang bisa ditampilkan kembali ke pengguna sebagai feedback.

Sumber referensi:

- [Stack Overflow](https://stackoverflow.com/questions/73173747/django-form-is-valid-what-does-it-check?)
- [Django Documentation](https://django.readthedocs.io/en/latest/topics/forms/)

---

### 4. Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token`? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Kita membutuhkan `{% csrf_token %}` untuk **melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF)**.

Secara sederhana, token ini berfungsi sebagai stempel rahasia yang unik untuk setiap sesi pengguna. Django akan menyisipkan stempel ini di dalam _form_ yang ditampilkan kepada pengguna. Ketika _form_ tersebut dikirim kembali, Django akan memeriksa apakah stempel yang disertakan cocok dengan yang seharusnya. Ini memastikan bahwa permintaan untuk memproses _form_ tersebut **benar-benar berasal dari situs kita sendiri**, bukan dari situs lain yang mencoba meniru pengguna.

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

Sumber referensi:

- [Django Documentation](https://django.readthedocs.io/en/stable/topics/security.html)
- [Django Documentation](https://docs.djangoproject.com/en/5.2/ref/csrf/)

---

### 5. Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_.

Berikut adalah langkah-langkah implementasi yang saya lakukan:

1. **Membuat Form Input untuk Menambahkan Objek**

   - Saya membuat `ProductForm` di `forms.py` yang terhubung ke model `Product`.
   - Di `views.py` saya menambahkan fungsi `add_product` yang memproses form:
     - Jika `request.method == "POST"`, data form akan divalidasi dan disimpan ke database, lalu redirect ke halaman daftar produk.
     - Jika bukan POST, maka akan ditampilkan form kosong.
   - Template `add_product.html` menampilkan form dengan `{% csrf_token %}` dan `{{ form.as_p }}`.

2. **Menambahkan Fungsi Views untuk Menampilkan Halaman HTML**

   - `show_products` → menampilkan semua produk dalam template `products.html`.
   - `product_detail` → menampilkan detail satu produk berdasarkan `id` di template `product_detail.html`.
   - `add_product` → menampilkan form tambah produk (`add_product.html`) sekaligus memproses penyimpanan data jika ada request POST.

3. **Menambahkan Fungsi Views untuk Data Delivery**

   - Saya juga menambahkan empat fungsi untuk serialisasi data `Product`:
     - `show_json` → menampilkan semua produk dalam format JSON.
     - `show_xml` → menampilkan semua produk dalam format XML.
     - `show_json_by_id` → menampilkan produk tertentu (berdasarkan ID) dalam format JSON.
     - `show_xml_by_id` → menampilkan produk tertentu (berdasarkan ID) dalam format XML.

4. **Menambahkan Routing URL untuk Semua Views**

   - Di `urls.py`, saya menambahkan path untuk:
     - `/json/` dan `/xml/` (semua data).
     - `/json/<uuid:id>/` dan `/xml/<uud:id>/` (by ID).
     - `/products/` → daftar produk.
     - `/products/<uuid:id>/` → detail produk.
     - `/products/add/` → tambah produk.

5. **Membuat Template HTML**

   - `products.html` → menampilkan daftar produk + link detail tiap produk.
   - `product_detail.html` → menampilkan detail satu produk.
   - `add_product.html` → halaman form untuk menambahkan produk baru.

6. **Pengujian dengan Postman**

   - Saya menguji endpoint JSON/XML (semua data dan by ID) menggunakan Postman.
   - Hasilnya sesuai format dan data pada model `Product`. Screenshot hasil uji saya lampirkan di README.

7. **Commit dan Push ke GitHub**
   - Setelah semua berjalan, saya melakukan `git add`, `git commit -m`, dan `git push origin main` untuk mengunggah perubahan ke repository GitHub.

---

### 6. Apakah ada _feedback_ untuk asdos di tutorial 2 yang sudah kalian kerjakan?

Tutorial yang diberikan sudah sangat jelas dan terstruktur secara _step-by-step_, sehingga mudah untuk diikuti. Saran saya, akan lebih bermanfaat jika ada contoh **penanganan _error form_** yang lebih mendalam, misalnya cara menampilkan pesan _error_ spesifik untuk setiap _field_. Lalu, bagian _URL routing_ terkadang bisa sedikit membingungkan bagi pemula, terutama saya pribadi. Mungkin bisa dibantu dengan menyertakan **diagram alur sederhana** yang menggambarkan bagaimana sebuah _request_ dari URL dipetakan ke _view_ yang sesuai.

---

### 7. Screenshot hasil akses URL pada Postman

| JSON                                     | XML                                    |
| ---------------------------------------- | -------------------------------------- |
| ![Postman JSON](../images/postman-json.png) | ![Postman XML](../images/postman-xml.png) |

| JSON by ID                                           | XML by ID                                          |
| ---------------------------------------------------- | -------------------------------------------------- |
| ![Postman JSON by ID](../images/postman-json-by-id.png) | ![Postman XML by ID](../images/postman-xml-by-id.png) |
