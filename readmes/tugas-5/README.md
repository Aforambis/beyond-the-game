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

Implementasi untuk Tugas 5 ini saya lakukan secara bertahap, dengan fokus utama untuk mengubah aplikasi dari fungsionalitas dasar menjadi sebuah platform yang matang secara visual, responsif, dan memiliki pengalaman pengguna yang baik. Berikut adalah langkah-langkahnya:

1. Revitalisasi Desain Halaman Utama (Landing Page)

Langkah pertama adalah merombak total tampilan halaman utama untuk menciptakan kesan yang eksklusif namun tetap energik, sesuai dengan tema produk memorabilia sepak bola.

Navbar Responsif: Saya mengganti navbar standar dengan konsep header yang "melayang" (position: fixed).

Desktop: Mengadopsi layout yang menampilkan link teks secara menyebar (justify-content: space-between). Awalnya header ini transparan, dan menggunakan JavaScript untuk mendeteksi scroll (window.scrollY). Jika user scroll ke bawah, sebuah class .scrolled ditambahkan untuk mengubah background menjadi putih solid dengan backdrop-filter untuk efek frosted glass.

Mobile: Menggunakan CSS @media query (pada max-width: 1024px), link teks disembunyikan dan ikon hamburger menu dimunculkan kembali. Fungsionalitas buka-tutup menu diatur oleh JavaScript dengan event listener pada ikon tersebut.

Hero Section Dinamis: Mengganti gambar statis dengan video background fullscreen menggunakan tag <video> HTML5 dengan atribut autoplay, muted, dan loop. Properti CSS seperti height: 100vh dan object-fit: cover digunakan untuk memastikan video memenuhi seluruh layar. Sebuah overlay gelap ditambahkan menggunakan pseudo-elemen ::after untuk menjamin keterbacaan teks di atasnya.

Tipografi & Styling: Saya mengimpor beberapa font dari Google Fonts (Inter, Cormorant Garamond, Playfair Display) dan melakukan beberapa iterasi untuk menemukan kombinasi yang pas antara brand identity di navbar dan hero text di tengah.

2. Implementasi Fungsionalitas CRUD (Create, Read, Update, Delete)

Setelah tampilan utama solid, saya memastikan fungsionalitas inti berjalan sesuai checklist.

Menampilkan Produk (Read):

Daftar produk ditampilkan dalam format kartu (cards) yang responsif menggunakan CSS Grid.

Saya mengimplementasikan partial rendering dengan AJAX (fetch API di JavaScript). Ketika user mengklik filter "All Products" atau "My Products", JavaScript akan memanggil URL Django yang didesain khusus untuk me-render sebagian kecil dari HTML (product_list.html). Hasil HTML ini kemudian disuntikkan ke dalam div kontainer utama tanpa perlu me-reload seluruh halaman, sehingga memberikan UX yang lebih cepat.

Menambah Produk (Create): Fungsionalitas ini diimplementasikan secara standar menggunakan ProductForm dari forms.py yang di-render dalam sebuah view dan template khusus.

Edit & Delete (Update & Delete):

Saya membuat URL patterns di urls.py yang menyertakan ID unik produk (misal: /products/<id>/edit/).

Di views.py, saya membuat fungsi edit_product dan delete_product. Yang terpenting, saya menambahkan pengecekan otorisasi (if product.user == request.user) untuk memastikan hanya pemilik produk yang bisa mengubah atau menghapusnya.

Tombol "Edit" dan "Delete" ditambahkan pada setiap kartu produk di dalam template, namun hanya ditampilkan jika user yang sedang login adalah pemilik item tersebut.

3. Penyempurnaan & Debugging

Tahap terakhir adalah memperbaiki detail-detail kecil untuk menyempurnakan pengalaman pengguna.

Memperbaiki Smooth Scroll: Karena navbar dibuat position: fixed, scroll otomatis ke sebuah section (#collection-section) membuat judulnya tertutup navbar. Masalah ini diatasi dengan menambahkan properti CSS scroll-margin-top pada section target, memberikan "ruang kosong" virtual seukuran tinggi navbar.

Refactoring CSS: Awalnya, semua CSS custom ditulis dalam tag <style> di base.html. Untuk kebersihan kode, semua style tersebut saya pindahkan ke file eksternal main_style.css, menyisakan hanya satu aturan CSS di base.html yang memerlukan tag template Django ({% static '...' %}).

Menyelesaikan Konflik CSS: Selama proses styling, terjadi beberapa bug di mana style tidak teraplikasi. Dengan menggunakan Browser DevTools (Inspect Element), saya berhasil melacak penyebabnya, yaitu adanya aturan CSS yang lebih spesifik di file main_style.css (.hero-section h1) yang mengalahkan aturan yang saya inginkan (.main-title). Masalah ini diselesaikan dengan menghapus aturan CSS yang konflik tersebut.