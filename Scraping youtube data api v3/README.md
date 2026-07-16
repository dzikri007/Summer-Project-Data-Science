# Scraping YouTube Data API v3

Proyek ini digunakan untuk mengambil (scraping) data komentar dari video YouTube menggunakan YouTube Data API v3, serta melakukan analisis sentimen terhadap komentar tersebut.

## Penjelasan Teknis Singkat
- **Data Scraping**: Menggunakan pustaka `google-api-python-client` untuk memanggil antarmuka YouTube Data API v3 dan mengekstrak data komentar, nama pengguna, serta jumlah like dari video tertentu.
- **Data Preprocessing**: Melibatkan pembersihan teks menggunakan RegEx (`re`) untuk menghapus tag HTML, URL, dan mention username agar data lebih bersih sebelum dianalisis.
- **Analisis Sentimen**: Proses klasifikasi sentimen menggunakan model bahasa *pre-trained* NLP dari Hugging Face, yaitu `w11wo/indonesian-roberta-base-sentiment-classifier`. Model ini dijalankan menggunakan pustaka `transformers` (pipeline) untuk menentukan apakah sebuah komentar bernada positif, negatif, atau netral.

## Struktur Folder
- `Scraping-comment-yt-MBG.py`: Skrip Python utama untuk melakukan scraping komentar dari YouTube.
- `analisis.ipynb`: Notebook Jupyter yang berisi proses pembersihan data, analisis sentimen, dan pembuatan visualisasi.
- `Requirements.txt`: Daftar library Python yang dibutuhkan untuk menjalankan proyek ini.
- `comment_data.csv`: File hasil scraping yang berisi data mentah komentar.
- `comment_sentiment.csv`: File hasil analisis yang berisi komentar beserta skor dan label sentimennya.
- `sentiment_distribution.png`: Gambar grafik yang menunjukkan distribusi hasil sentimen.

## Cara Penggunaan
1. Instal dependensi yang diperlukan dengan menjalankan `pip install -r Requirements.txt` di terminal.
2. (Opsional) Jalankan `Scraping-comment-yt-MBG.py` jika ingin mengambil data komentar baru. Pastikan konfigurasi API Key YouTube Anda di dalam file sudah diset dengan benar.
3. Buka dan jalankan `analisis.ipynb` untuk melihat hasil pengolahan data dan visualisasi sentimen.
