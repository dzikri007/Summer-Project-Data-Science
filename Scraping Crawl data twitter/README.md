# Crawl Data Twitter (X) Menggunakan Tweet-Harvest

Repositori ini berisi notebook Jupyter untuk melakukan *crawling* data dari Twitter (X) menggunakan tool **Tweet-Harvest** (dikembangkan oleh [Helmi Satria](https://github.com/helmisatria)). Notebook ini dirancang untuk dapat dijalankan secara lancar, baik di lingkungan lokal maupun Google Colab, lengkap dengan penanganan dependensi Node.js dan browser (*headless Chromium*).

Dalam contoh konfigurasi saat ini, proyek ini digunakan untuk mengumpulkan tweet bertopik ekonomi dengan kata kunci `ekonomi OR economy` dalam rentang waktu **1 April 2023** hingga **2 Februari 2026**.

---

## ⚙️ Persyaratan Sistem & Instalasi

Tweet-Harvest dibuat menggunakan Node.js dan memanfaatkan Playwright (Chromium) untuk mensimulasikan pencarian di Twitter. Oleh karena itu, langkah-langkah berikut diperlukan:

### 1. Kebutuhan Library Python
```bash
pip install pandas
```

### 2. Node.js
Pastikan Node.js (versi 20 atau terbaru) terinstal di sistem Anda. Pada notebook, Node.js diinstal secara otomatis menggunakan perintah berikut (untuk Linux/Colab):
```bash
sudo apt-get update
sudo apt-get install -y ca-certificates curl gnupg
curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg
NODE_MAJOR=20 && echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | sudo tee /etc/apt/sources.list.d/nodesource.list
sudo apt-get update && sudo apt-get install nodejs -y
```

### 3. Dependensi Browser (Playwright / Chromium)
Jika dijalankan di sistem Linux server (seperti Google Colab) tanpa antarmuka grafis, library sistem berikut wajib diinstal agar Chromium dapat berjalan dalam mode *headless*:
```bash
sudo apt-get install -y libatk-adaptor libatk-bridge2.0-0 libgtk-3-0 libxss1 libgbm1 libdrm-dev
```

---

## Cara Menjalankan

1. **Dapatkan Twitter Auth Token**:
   - Buka X/Twitter di browser Anda dan pastikan sudah masuk (login).
   - Klik kanan, pilih **Inspect Element** (F12) untuk membuka Developer Tools.
   - Masuk ke tab **Application** (Chrome/Edge) atau **Storage** (Firefox).
   - Di bagian **Cookies**, pilih domain `https://x.com` atau `https://twitter.com`.
   - Cari cookie bernama `auth_token` dan salin nilainya.

2. **Jalankan Notebook** (`Crawl_data_twitter_1000_tweets.ipynb`):
   - Masukkan token yang telah disalin ke variabel `twitter_auth_token` di sel pertama:
     ```python
     twitter_auth_token = 'MASUKKAN_AUTH_TOKEN_ANDA_DISINI'
     ```
   - Jalankan sel instalasi dependensi.
   - Konfigurasikan kata kunci, nama file output, dan batas jumlah data pada sel **Crawl Data**:
     ```python
     filename = 'economy.csv'
     search_keyword = 'ekonomi OR economy since:2023-04-01 until:2026-02-02 lang:id'
     limit = 1000
     ```
   > - note untuk mengubah keyword pencarian, bahasa, dan rentang waktu 
   > - syntax nya: keyword lang:kode_bahasa since:YYYY-MM-DD until:YYYY-MM-DD
   > - contoh: ekonomi OR economy lang:id since:2023-04-01 until:2026-02-02
     
   - Jalankan sel crawling untuk mengeksekusi Tweet-Harvest melalui `npx`:
     ```bash
     !npx -y tweet-harvest@latest -o "{filename}" -s "{search_keyword}" --tab "LATEST" -l {limit} --token {twitter_auth_token}
     ```

> [!WARNING]
> Jagalah kerahasiaan `auth_token` Anda! Jangan membagikannya kepada siapa pun atau mengunggah notebook yang berisi token aktif ke repositori publik.

---

## Skema Data Output (`economy.csv`)

Data hasil crawling disimpan dalam format CSV di dalam folder `tweet-data/` dengan kolom-kolom sebagai berikut:

| Nama Kolom | Deskripsi |
| :--- | :--- |
| `id_str` | ID unik tweet (dalam tipe data string/numeric) |
| `created_at` | Waktu tweet diunggah (ISO UTC format) |
| `username` | Username akun pengunggah tweet |
| `full_text` | Isi lengkap teks tweet |
| `favorite_count` | Jumlah suka (*likes*) yang diperoleh tweet |
| `retweet_count` | Jumlah retweet yang diperoleh tweet |
| `reply_count` | Jumlah balasan (*replies*) pada tweet |
| `quote_count` | Jumlah kutipan (*quotes*) pada tweet |
| `tweet_url` | Tautan langsung menuju tweet terkait |
| `user_id_str` | ID unik akun pengunggah tweet |
| `conversation_id_str` | ID percakapan awal (berguna untuk pelacakan thread/balasan) |
| `image_url` | Tautan gambar/media jika tweet melampirkan media |
| `in_reply_to_screen_name` | Username akun yang dibalas oleh tweet tersebut (jika ada) |
| `lang` | Kode bahasa tweet (misal: `id`, `en`, `tr`) |
| `location` | Lokasi pengguna (jika diaktifkan) |

---

## Pemecahan Masalah (Troubleshooting)

> [!IMPORTANT]
> **Error parsing response json / Rate Limit**:
> Twitter menerapkan pembatasan akses (*rate limit*) yang cukup ketat. Jika Anda melihat pesan error berupa `TimeoutError: page.click: Timeout 60000ms exceeded` atau pesan mengenai limit akses terlampaui, itu menandakan token Anda sedang dibatasi sementara oleh Twitter.
> 
> **Solusi**: 
> - Hentikan proses crawling dan tunggu beberapa jam sebelum mencoba kembali.
> - Pastikan keyword pencarian tidak terlalu luas untuk menghindari pembatasan cepat.
> - Tangkapan layar otomatis saat terjadi kegagalan sistem akan disimpan langsung di dalam folder `tweet-data/Error-*.png` untuk mempermudah investigasi.
