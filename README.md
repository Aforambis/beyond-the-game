Rusydan Mujtaba Ibnu Ramadhan
2406421081
PBP F

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
   Jawab:
   a. Membuat sebuah proyek Django baru.
      -> Saya menjalankan instruksi "django-admin startproject beyond_the_game" di terminal di dalam env. Outputnya, tercipta struktur dasar project Django dengan folder utama `
         (beyond_the_game) yang berisi file settings.py, urls.py, dan sebagainya.
   b. Membuat aplikasi dengan nama main pada proyek tersebut.
      -> Saya menjalankan instruksi "python manage.py startapp main" di terminal, sehingga muncul folder main yang berisi views.py, models.py, dan sebagainya. Setelah itu, saya 
         menambahkan 'main' ke dalam variabel INSTALLED_APPS di settings.py agar Django mengenalinya.
   c. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
      -> Saya menambahkan kode "path('', include('main.urls'))" di file urls.py pada root project, sehingga urls.py di tingkat project akan terhubung dengan urls.py di aplikasi 
         main. 
   d. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagaimana tercantum di soal.
      -> Saya membuat model Product di models.py dengan field sesuai instruksi, serta beberapa field tambahan, seperti club, player, dan match date. Selain itu, saya juga 
         menambahkan dua model tambahan sebagai berikut.
         1. 'AuctionSeason': untuk mengelola periode auction tertentu, dengan atribut nama season, start_date, dan end_date.
         2. 'Bid': untuk menyimpan data penawaran user terhadap produk tertentu, dengan atribut user, product, amount, dan created_at.
         Kedua model ini saya tambahkan agar sistem yang saya buat lebih sesuai dengan konsep auction/pelelangan.
   e. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
      -> Saya membuat function show_main di views.py untuk mengirimkan data ke template. Fungsi tersebut akan me-render template main.html berisi nama aplikasi, nama, dan kelas.
   f. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
      -> Saya membuat file urls.py di main secara manual untuk menghubungkan fungsi view dengan URL. Jadinya, ketika user mengakses root URL (/), Django akan memanggil fungsi 
         show_main dan menampilkan halaman main.html.
   g. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
      -> 
   h. Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
      -> 

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan    
   berkas html.
   Jawab:

3. Jelaskan peran settings.py dalam proyek Django!
   Jawab:

4. Bagaimana cara kerja migrasi database di Django?
   Jawab:

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
   Jawab:

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
   Jawab: