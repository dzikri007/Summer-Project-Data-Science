# Scraping YouTube Comments: Rupiah Melemah

<p align="center">
  <img src="rupiah melemah.jpg" alt="Data Rupiah Melemah" width="700">
  <br>
  <em>Gambar: Data Rupiah Melemah</em>
</p>

Proyek ini berisi sebuah Jupyter Notebook (`Indonesian_YouTube_Comments_Rupiah_Melemah.ipynb`) yang bertujuan untuk melakukan web scraping data komentar dari YouTube berdasarkan kata kunci tertentu menggunakan **YouTube Data API v3**. Pada contoh ini, kata kunci yang digunakan adalah **"Rupiah melemah"**.

## Dataset

Dataset hasil ekstraksi dari script ini telah dipublikasikan dan dapat diakses secara publik di Kaggle:  
👉 **[Indonesian YouTube Comments - Rupiah Melemah](https://www.kaggle.com/datasets/dzikriraihan/indonesian-youtube-comments-rupiah-melemah)**

## Fitur Utama

- **Pencarian Video Otomatis**: Mencari hingga 100 video yang relevan dengan kata kunci di region Indonesia (`regionCode='ID'`).
- **Ekstraksi Komentar**: Mengambil semua *top-level comments* (komentar utama, tidak termasuk balasan) dari masing-masing video yang ditemukan.
- **Penyimpanan Data**: Menyimpan hasil ekstraksi secara terstruktur ke dalam file CSV (`rupiah_melemah_comments.csv`).

## Data yang Dikumpulkan

File CSV hasil ekstraksi akan memiliki kolom-kolom berikut:
1. `Video ID`: ID unik dari video YouTube
2. `Comment ID`: ID unik dari komentar
3. `Comment Link`: Tautan langsung (URL) ke komentar tersebut
4. `Commenter Name`: Nama pengguna yang memberikan komentar
5. `Commenter ID`: ID channel dari pemberi komentar
6. `Comment`: Teks isi komentar
7. `Likes`: Jumlah *like* atau suka yang didapatkan komentar tersebut

## Prasyarat

Sebelum menjalankan notebook ini, pastikan Anda telah menyiapkan hal-hal berikut:

1. **Python**: Pastikan Python versi 3.x telah terinstal di komputer Anda.
2. **Library**: Anda perlu menginstal pustaka `google-api-python-client`. Bisa dilakukan dengan menjalankan perintah:
   ```bash
   pip install google-api-python-client
   ```
3. **API Key YouTube Data API v3**: Anda harus memiliki API Key dari [Google Cloud Console](https://console.cloud.google.com/). Gantilah nilai variabel `api_key` di dalam script dengan API Key milik Anda sendiri.


## Catatan

- Script ini dibatasi untuk mengambil maksimal 100 video (lihat pada parameter `max_videos=100` saat pemanggilan fungsi `search_videos_by_keyword`).
- Pengambilan data ini terikat oleh limit kuota penggunaan harian dari YouTube Data API. Pastikan Anda memperhatikan jumlah *quota cost* untuk mencegah error API (seperti `HttpError 403: quotaExceeded`).
