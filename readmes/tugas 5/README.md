Rusydan Mujtaba Ibnu Ramadhan -
2406421081 -
PBP F

# Tugas 5

### 1.  Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Ketika beberapa aturan CSS menargetkan elemen HTML yang sama, browser akan menentukan gaya mana yang akan diterapkan melalui sebuah sistem prioritas yang disebut CSS Specificity. Ini adalah cara untuk menilai seberapa spesifik sebuah selector. Aturan dengan selector yang lebih spesifik akan selalu diutamakan.

Prioritas tertinggi dipegang oleh inline styles, yaitu gaya yang ditulis langsung di dalam atribut style pada tag HTML. Tepat di bawahnya adalah ID selectors (seperti #header), yang memiliki bobot tinggi karena ID seharusnya unik dalam satu halaman. Selanjutnya, pada tingkat prioritas yang sama, adalah class selectors (seperti .tombol), attribute selectors ([type="text"]), dan pseudo-classes (:hover). Di tingkat paling dasar dengan prioritas terendah adalah element selectors yang menargetkan tag HTML secara umum (seperti div atau p). Jika terjadi nilai specificity yang sama persis, maka aturan yang ditulis paling akhir di dalam file CSS akan menjadi pemenangnya. Ada juga aturan !important yang bisa ditambahkan pada properti CSS untuk mengesampingkan semua hirarki ini,

---

### 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!

Responsive design adalah sebuah konsep fundamental dalam pengembangan web modern yang memastikan sebuah aplikasi dapat tampil dan berfungsi dengan baik di berbagai ukuran layar, dari ponsel kecil hingga monitor desktop yang besar. Konsep ini sangat penting karena mayoritas pengguna internet saat ini mengakses web melalui perangkat mobile. Tanpa desain yang responsif, pengguna ponsel akan dipaksa untuk terus-menerus memperbesar dan menggeser layar, menciptakan pengalaman pengguna (UX) yang buruk dan berpotensi membuat mereka meninggalkan situs.

Selain meningkatkan UX, desain yang responsif juga lebih efisien karena pengembang hanya perlu mengelola satu basis kode untuk semua perangkat. Hal ini juga berdampak positif pada SEO, karena mesin pencari seperti Google secara aktif memprioritaskan situs yang mobile-friendly.

Sebagai contoh, situs berita The Guardian secara cerdas mengubah layout multi-kolomnya di desktop menjadi satu kolom yang mudah di-scroll di ponsel, dengan navigasi yang disederhanakan.  Sebaliknya, situs web lama seperti situs asli Space Jam dari tahun 1996 menunjukkan kelemahan desain non-responsif, di mana tampilannya tetap kaku dan kecil di layar ponsel, sehingga практически tidak bisa digunakan.
---

### 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

Margin, border, dan padding adalah tiga properti inti dari CSS Box Model, yang secara kolektif mendefinisikan ruang di sekitar konten sebuah elemen. Cara termudah untuk memahaminya adalah dengan analogi sebuah bingkai foto. Padding adalah ruang transparan di antara foto (konten) dan bingkainya, memberikan jarak agar foto tidak menempel pada bingkai. Border adalah bingkai itu sendiri, yang memiliki ketebalan, gaya, dan warna. Sementara itu, margin adalah ruang di luar bingkai, yang berfungsi untuk menciptakan jarak antara bingkai tersebut dengan bingkai lain atau dinding di sekitarnya.

Dalam implementasinya di CSS, ketiga properti ini bisa diatur untuk semua sisi sekaligus (shorthand) atau untuk masing-masing sisi secara spesifik (misalnya padding-top atau margin-left).

---

### 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

Flexbox dan Grid adalah dua sistem layout CSS modern yang memungkinkan pengembang untuk menyusun elemen dengan cara yang jauh lebih fleksibel dan kuat. Keduanya memiliki kegunaan yang berbeda berdasarkan dimensi yang mereka atur.

Flexbox adalah sistem layout satu dimensi, yang berarti ia sangat baik dalam mengatur elemen-elemen dalam satu baris (row) atau satu kolom (column). Flexbox sangat berguna untuk mendistribusikan ruang di antara item-item dalam sebuah komponen, seperti menyusun menu navigasi, membuat barisan kartu produk, atau memusatkan sebuah item di tengah-tengah wadahnya.

Di sisi lain, Grid Layout adalah sistem dua dimensi yang dirancang untuk mengatur layout dalam baris dan kolom secara bersamaan. Ini membuatnya sempurna untuk menyusun keseluruhan tata letak halaman yang kompleks, seperti menempatkan header, sidebar, area konten utama, dan footer secara presisi. Aturan praktisnya adalah: gunakan Flexbox untuk komponen dan Grid untuk layout halaman. Keduanya bahkan bisa dikombinasikan; misalnya, menggunakan Grid untuk struktur halaman utama, dan di dalam salah satu area Grid tersebut, menggunakan Flexbox untuk mengatur kontennya.

---

### 5. Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_!

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