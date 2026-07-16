# Spotify System Recommendation

Proyek ini berisi implementasi sistem rekomendasi untuk lagu-lagu di Spotify. 

## Penjelasan Teknis Singkat
Sistem ini dibangun menggunakan pendekatan **Content-Based Filtering**. Konsep teknis yang digunakan meliputi:
- **TF-IDF (Term Frequency-Inverse Document Frequency)**: Digunakan untuk mengubah fitur teks (gabungan nama genre dan artis) menjadi bentuk matriks vektor angka.
- **Cosine Similarity**: Digunakan untuk menghitung jarak atau tingkat kemiripan antar lagu berdasarkan matriks TF-IDF. Sistem akan merekomendasikan lagu-lagu dengan skor kemiripan tertinggi terhadap lagu yang sedang dicari.
- Library utama yang digunakan adalah `pandas` untuk pemrosesan data, serta `scikit-learn` untuk fungsi TF-IDF dan linear kernel (Cosine Similarity).

## Struktur Folder
- `Spotify_Recommender.ipynb`: Notebook Jupyter yang berisi kode untuk eksplorasi data dan pembuatan model rekomendasi.
- `dataset.csv`: Dataset yang digunakan dalam proyek ini.

## Cara Penggunaan
1. Buka file `Spotify_Recommender.ipynb` menggunakan Jupyter Notebook atau editor lain yang mendukung (seperti VS Code).
2. Pastikan lingkungan Python Anda sudah memiliki library yang dibutuhkan.
3. Jalankan sel-sel kode di dalam notebook untuk melihat proses sistem rekomendasi berjalan.
