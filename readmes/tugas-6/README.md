Rusydan Mujtaba Ibnu Ramadhan -
2406421081 -
PBP F

# Tugas 5

### 1.   Apa perbedaan antara synchronous request dan asynchronous request?

Perbedaan mendasar antara Synchronous Request (Sinkron) dan Asynchronous Request (Asinkron) terletak pada cara program menangani antrean tugas. Dalam request sinkron, eksekusi kode bersifat blocking; artinya, ketika sebuah request dikirim ke server, program akan berhenti total dan harus menunggu hingga respons dari server diterima sebelum melanjutkan ke tugas berikutnya. Ini sering kali menyebabkan keseluruhan halaman web mengalami loading ulang. 

Sebaliknya, request asinkron bersifat non-blocking. Ketika request dikirim (seperti melalui AJAX), program tidak perlu menunggu respons; ia dapat melanjutkan eksekusi kode atau tugas lain. Respons dari server akan ditangani kemudian, sering kali untuk memperbarui sebagian kecil dari halaman web tanpa mengganggu interaksi pengguna yang sedang berlangsung.

---

### 2.  Bagaimana AJAX bekerja di Django (alur request–response)?

Mekanisme AJAX (Asynchronous JavaScript and XML) dalam konteks Django memungkinkan pertukaran data secara asinkron antara browser dan server tanpa memuat ulang seluruh halaman. Alurnya dimulai ketika sebuah event terjadi di browser (misalnya, klik tombol). JavaScript kemudian membuat dan mengirimkan HTTP Request ke endpoint URL tertentu di Django. Di sisi server, Django menerima request ini dan mengarahkannya ke View yang telah dikonfigurasi untuk menangani request AJAX. View ini memproses data (request.POST atau request.GET), melakukan operasi database yang diperlukan, dan kemudian mengembalikan Response yang ringan, biasanya dalam format JSON (menggunakan JsonResponse). 

Response JSON pun diterima oleh JavaScript di browser, yang kemudian bertanggung jawab untuk membaca data tersebut dan secara dinamis memperbarui elemen tertentu di Document Object Model (DOM) halaman web, menyelesaikan proses pembaruan tanpa full page reload.

---

### 3.  Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?

Keuntungan utama menggunakan AJAX di Django, dibandingkan dengan mekanisme render tradisional yang memuat ulang seluruh halaman, adalah pada peningkatan efisiensi dan User Experience (UX). Karena AJAX hanya mengirimkan dan menerima data yang diperlukan, ini secara signifikan mengurangi bandwidth dan mempercepat waktu loading, karena server tidak perlu merender dan mengirimkan seluruh template HTML untuk setiap pembaruan kecil. 

Hal ini menghasilkan aplikasi web yang terasa lebih cepat dan responsif, menyerupai aplikasi desktop. Selain itu, karena operasi bersifat asinkron, pengguna dapat terus berinteraksi dengan bagian lain dari halaman saat server sedang memproses request AJAX di background.

---

### 4.  Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?

Memastikan keamanan saat mengimplementasikan fitur Login dan Register menggunakan AJAX di Django memerlukan perhatian khusus terhadap beberapa ancaman standar. Yang paling krusial adalah pencegahan CSRF (Cross-Site Request Forgery). Kita harus memastikan bahwa CSRF token (yang secara default disediakan oleh Django) diambil oleh JavaScript dan disertakan dalam header (e.g., X-CSRFToken) dari setiap request AJAX berjenis POST. Kedua, validasi data harus selalu dilakukan di sisi server (di view Django) untuk memverifikasi kredensial Login atau memvalidasi input Register, meskipun validasi client-side sudah dilakukan. Terakhir, penggunaan HTTPS sangat penting untuk mengenkripsi username dan password yang dikirimkan melalui request AJAX selama transit, dan menerapkan rate limiting dapat mencegah serangan Brute Force pada endpoint Login.

---

### 5.  Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?

AJAX secara revolusioner meningkatkan Pengalaman Pengguna (UX) sebuah website dengan membuatnya terasa lebih dinamis dan modern. Dengan menghilangkan kebutuhan untuk memuat ulang seluruh halaman untuk setiap interaksi kecil (seperti memberikan like, mengirim comment, atau memuat hasil search), AJAX menciptakan transisi yang mulus dan real-time. Pengguna tidak perlu melihat layar putih loading atau kehilangan fokus dari apa yang sedang mereka lakukan. Dampaknya adalah perasaan kecepatan yang lebih tinggi dan pengurangan frustrasi, membuat aplikasi web terasa lebih intuitif dan efisien digunakan, pada akhirnya meningkatkan retensi dan kepuasan pengguna.