# Prediksi Harga Sewa AirBnb

Memprediksi harga sewa AirBnB berdasarkan fitur-fitur listing seperti grup lingkungan (neighbourhood group), tipe kamar, lokasi, jumlah malam minimum, dan ketersediaan. Melakukan prapemrosesan data, analisis outlier, label encoding, dan melatih model Regresi Linear.

## Dataset

`dataSP23.csv` -- berisi 27.379 listing AirBnB dengan kolom termasuk grup lingkungan, lintang (latitude), bujur (longitude), tipe kamar, harga, jumlah malam minimum, jumlah listing tuan rumah, dan ketersediaan.

## Tech Stack (Teknologi yang Digunakan)

- Pandas
- NumPy
- scikit-learn (LinearRegression, LabelEncoder, StandardScaler, train_test_split, r2_score)
- Matplotlib

## Hasil

Model Regresi Linear mencapai skor R2 sebesar 0,14 pada data uji (test set). Skor yang rendah ini disebabkan oleh adanya outlier yang signifikan dalam dataset, yang berdampak negatif pada kinerja model.

## Cara Menjalankan

1. Pastikan file `dataSP23.csv` berada di direktori yang sama dengan notebook.
2. Buka `AirBnB.ipynb` di Jupyter Notebook atau JupyterLab.
3. Jalankan semua sel untuk melakukan prapemrosesan data, melatih model, serta melihat prediksi dan visualisasi.
