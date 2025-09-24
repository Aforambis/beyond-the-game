Rusydan Mujtaba Ibnu Ramadhan -
2406421081 -
PBP F

# Tugas 4

### 1. Apa itu `Django AuthenticationForm`? Jelaskan juga kelebihan dan kekurangannya!

AuthenticationForm adalah form bawaan Django yang digunakan untuk melakukan proses login pengguna. Form ini otomatis memvalidasi username dan password berdasarkan model User bawaan Django.

Kelebihan:

- Mudah digunakan karena sudah terintegrasi dengan model User.
- Otomatis memvalidasi username dan password.
- Hemat waktu, tidak perlu membuat form login sendiri dari awal.

Kekurangan :

- Kurang fleksibel jika ingin menambahkan validasi custom yang kompleks.
- Tampilan defaultnya sederhana dan perlu disesuaikan dengan template sendiri.

---

### 2. Apa perbedaan antara `autentikasi` dan `otorisasi`? Bagaimana Django mengimplementasikan kedua konsep tersebut?

Autentikasi (_authentication_) adalah proses memverifikasi identitas pengguna. Misalnya, memastikan username dan password sesuai.
- Di Django, autentikasi diimplementasikan melalui `AuthenticationForm`, `authenticate()`, dan `login()`.

Otorisasi (_authorization_) adalah proses memberikan izin kepada pengguna berdasarkan perannya. Misalnya, hanya admin yang bisa menambahkan produk.
- Di Django, otorisasi dilakukan melalui permissions dan decorators seperti `@login_required`, `user.is_staff`, dan `user.has_perm()`.

---

### 3. Apa saja kelebihan dan kekurangan _session_ dan _cookies_ dalam konteks menyimpan state di aplikasi web?

`Session`:
- Kelebihan: Data tersimpan di server sehingga lebih aman; pengguna tidak bisa memodifikasi.
- Kekurangan: Membutuhkan storage server, bisa memakan memory jika banyak pengguna.

`Cookies`:
- Kelebihan: Disimpan di client, ringan, dan mudah diakses di browser.
- Kekurangan: Bisa dimanipulasi pengguna; ukuran terbatas (~4KB); risiko keamanan jika menyimpan data sensitif.

---

### 4. Apakah penggunaan _cookies_ aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

Tidak selalu aman secara default, karena cookies bisa diubah oleh pengguna (client-side). Beberapa risiko, di antaranya pencurian session, manipulasi data, cross-site scripting (XSS).

Django menangani ini dengan cara:
- Menggunakan _signed cookies_ untuk mencegah manipulasi data.
- Menggunakan `session ID` di cookie, bukan menyimpan data sensitif langsung.
- Mendukung opsi `HttpOnly` dan `Secure` untuk melindungi cookies.

---

### 5. Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_!

Langkah-langkah yang saya lakukan:

1. **Pada Models & Forms**

   - Menghubungkan model Product dengan User dengan cara menambahkan field user dengan `models.ForeignKey(User, on_delete=models.CASCADE, null=True)` di model Product.
   - Membuat `AuctionSeasonForm` dan `BidForm` di `forms.py` yang terhubung ke model `AuctionSeason` dan `Bid`.
   - Menggunakan `AuthenticationForm` dan `UserCreationForm` untuk login dan registrasi.

2. **Pada Views & Templates**

   - Membuat `register`, `login_user`, `logout_user`.
   - Menyimpan waktu login di cookie `last_login`
   - Menampilkan cookies `last_login` di template `show_main` yang akan dihapus ketika logout.
   - Membuat dua template tambahan, yaitu auction season (`add_auction_season`) dan place bid (`place_bid`).

3. **Commit dan Push ke GitHub**
   - Setelah semua berjalan, saya melakukan `git add`, `git commit -m`, dan `git push origin main` untuk mengunggah perubahan ke repository GitHub.

### Credentials akun user
User 1:
- username:
- password: 

User 2:
- username:
- password: