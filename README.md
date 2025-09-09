Rusydan Mujtaba Ibnu Ramadhan,
NPM 2406421081,
Kelas PBP F

## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
#### a. Membuat sebuah proyek Django baru.
Saya menjalankan instruksi 'django-admin startproject beyond_the_game' di terminal di dalam env. Outputnya, tercipta struktur dasar project Django dengan folder utama (beyond_the_game) yang berisi file settings.py, urls.py, dan sebagainya.

#### b. Membuat aplikasi dengan nama main pada proyek tersebut.
Saya menjalankan instruksi 'python manage.py startapp main' di terminal, sehingga muncul folder main yang berisi views.py, models.py, dan sebagainya. Setelah itu, saya menambahkan 'main' ke dalam variabel INSTALLED_APPS di settings.py agar Django mengenalinya.

#### c. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
Saya menambahkan kode 'path('', include('main.urls'))' di file urls.py pada root project, sehingga urls.py di tingkat project akan terhubung dengan urls.py di aplikasi main. 

#### d. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagaimana tercantum di soal.
Saya membuat model Product di models.py dengan field sesuai instruksi, serta beberapa field tambahan, seperti club, player, dan match date. Selain itu, saya juga menambahkan dua model tambahan sebagai berikut.
1. **'AuctionSeason'**: untuk mengelola periode auction tertentu, dengan atribut nama season, start_date, dan end_date.
2. **'Bid'**: untuk menyimpan data penawaran user terhadap produk tertentu, dengan atribut user, product, amount, dan created_at.
Kedua model ini saya tambahkan agar sistem yang saya buat lebih sesuai dengan konsep auction/pelelangan.

#### e. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
Saya membuat function show_main di views.py untuk mengirimkan data ke template. Fungsi tersebut akan me-render template main.html berisi nama aplikasi, nama, dan kelas.
   
#### f. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
Saya membuat file urls.py di main secara manual untuk menghubungkan fungsi view dengan URL. Jadinya, ketika user mengakses root URL (/), Django akan memanggil fungsi show_main dan menampilkan halaman main.html.

#### g. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
Saya membuat branch master khusus untuk PWS, dan branch main khusus untuk GitHub. Ini saya lakukan agar push ke PWS tidak mengganggu GitHub. Di settings.py, saya menambahkan domain PWS ke ALLOWED_HOSTS dan memastikan template HTML (main.html) tersedia agar server dapat me-render view. Setelah itu, saya melakukan push ke PWS, yang otomatis membuild Docker image dan menjalankan server Django. Hasilnya, aplikasi berhasil berjalan di URL https://rusydan-mujtaba-beyondthegame.pbp.cs.ui.ac.id dan dapat diakses teman-teman melalui internet.

#### h. Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
[Aplikasi PWS](https://rusydan-mujtaba-beyondthegame.pbp.cs.ui.ac.id/)
---

## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Bagan Alur Django](images/alur-django.png)
Kaitan antara urls.py, views.py, models.py, dan berkas html sebagai berikut.
1. HTTP request: user mengirimkan request lewat browser
2. Forward request: Django menerima request tersebut, lalu urls.py akan mencocokkan dengan fungsi view yang sesuai.
3. Query: views.py akan melakukan query ke database melalui models.py (jika diperlukan)
4. Transaksi data: models.py berinteraksi langsung dengan database untuk mengambil, menyimpan, atau memodifikasi data
5. Data diperoleh views.py: hasil query models.py diberikan kepada views.py
6. Data diteruskan ke templates: views.py mengirimkan data ke file template HTML agar bisa ditampilkan kepada user dalam bentuk halaman
7. Templates me-render page: template HTML menggabungkan data dari views dan membentuk webpage
8. Respons ke user: halaman yang sudah jadi dikirim kembali ke browser user sebagai HTTP response
.
---

## 3. Jelaskan peran settings.py dalam proyek Django!
`settings.py` berfungsi sebagai pusat konfigurasi proyek Django, misalnya:  
- Menentukan aplikasi yang digunakan (`INSTALLED_APPS`)  
- Mengatur database (`DATABASES`)  
- Menentukan host yang diizinkan (`ALLOWED_HOSTS`)  
- Mengatur lokasi template (`TEMPLATES`) 

Referensi: [Django Docs – Settings](https://docs.djangoproject.com/en/5.2/topics/settings)
---

## 4. Bagaimana cara kerja migrasi database di Django?
Migrasi adalah mekanisme untuk sinkronisasi database dengan `models.py`.  
- `makemigrations`: membuat file migrasi berdasarkan perubahan model.  
- `migrate`: mengeksekusi file migrasi, menerapkan perubahan ke database.  

- Referensi: [Django Docs – Migrations](https://docs.djangoproject.com/en/5.2/topics/migrations)
---

## 5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, Django sering dipilih sebagai framework awal karena:  
- Strukturnya jelas, membuat pemula mudah memahami alur kerja software.  
- Banyak memiliki fitur penting (routing, database, autentikasi) siap pakai, sehingga pengguna dapat fokus mengerjakan logika aplikasi.  
- Mengajarkan best practice melalui prinsip DRY dan KISS.  
- Fleksibel karena cocok untuk proyek kecil maupun aplikasi skala besar seperti Instagram dan Youtube.  
- Memberikan gambaran full-stack (backend, template frontend, database) holistik dalam satu framework.  

Referensi:  
- [Finoit](https://www.finoit.com/blog/choose-django-framework-for-web-development)  
- [GeeksforGeeks](https://www.geeksforgeeks.org/blogs/why-django-framework-is-best-for-web-development)  
- [DjangoStars](https://djangostars.com/blog/top-14-pros-using-django-web-development)
. 
--- 

## 6. Apakah ada feedback untuk asisten dosen terkait tutorial 1 yang telah kamu kerjakan sebelumnya?
Tutorial 1 sudah sangat baik menjelaskan struktur proyek Django. Instruksi pembuatan aplikasi, konfigurasi database, dan pembuatan tampilan awal sangat detail dan membantu. Thank you Asdos!