# Scraping YouTube Data API v3

Proyek ini digunakan untuk mengambil (scraping) data komentar dari video YouTube menggunakan YouTube Data API v3, serta melakukan analisis sentimen terhadap komentar tersebut.

## Struktur Folder
- `Scraping-comment-yt-MBG.py`: Skrip Python utama untuk melakukan scraping komentar dari YouTube.
- `analisis.ipynb`: Notebook Jupyter yang berisi proses analisis data dan analisis sentimen dari komentar yang telah diambil.
- `Requirements.txt`: Daftar library Python yang dibutuhkan untuk menjalankan proyek ini.
- `comment_data.csv`: File hasil scraping yang berisi data mentah komentar.
- `comment_sentiment.csv`: File hasil analisis yang berisi komentar beserta label sentimennya.
- `sentiment_distribution.png`: Gambar grafik yang menunjukkan distribusi hasil sentimen.

## Cara Penggunaan
1. Instal dependensi yang diperlukan dengan menjalankan `pip install -r Requirements.txt` di terminal.
2. (Opsional) Jalankan `Scraping-comment-yt-MBG.py` jika ingin mengambil data komentar baru. Pastikan konfigurasi API Key YouTube Anda sudah sesuai.
3. Buka dan jalankan `analisis.ipynb` untuk melihat hasil pengolahan data dan visualisasi sentimen.
