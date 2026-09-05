# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding

Jaya Jaya Institut merupakan institusi pendidikan yang telah berdiri sejak tahun 2000 dan dikenal dalam mencetak lulusan-lulusan berkualitas. Akan tetapi, institusi ini menghadapi tantangan serius yaitu tingginya angka mahasiswa yang tidak menyelesaikan pendidikan alias *dropout*.

Tingginya tingkat *dropout* berdampak negatif terhadap reputasi dan mutu institusi secara keseluruhan. Oleh karena itu, Jaya Jaya Institut membutuhkan sistem yang mampu mendeteksi mahasiswa yang berpotensi *dropout* sedini mungkin agar pihak institusi dapat memberikan intervensi atau bimbingan khusus untuk mencegah hal tersebut.

### Permasalahan Bisnis

Berikut adalah permasalahan bisnis yang akan diselesaikan dalam proyek ini:

1. **Faktor apa saja yang paling berpengaruh terhadap tingkat dropout mahasiswa?**
2. **Bagaimana cara mengidentifikasi mahasiswa yang berisiko dropout secara dini?**
3. **Langkah strategis apa yang dapat dilakukan institusi untuk menekan angka dropout?**

### Cakupan Proyek

Proyek ini mencakup beberapa tahapan utama:

- **Data Understanding & Exploratory Data Analysis (EDA):** Menganalisis karakteristik data, distribusi variabel, dan korelasi antar fitur terhadap status dropout.
- **Data Preprocessing:** Melakukan pembersihan data, encoding fitur kategorikal, penanganan korelasi tinggi, dan seleksi fitur.
- **Modeling:** Membangun dan membandingkan beberapa model klasifikasi (Logistic Regression, SVM, Gradient Boosting) kemudian melakukan hyperparameter tuning dengan XGBoost.
- **Evaluasi:** Menganalisis performa model menggunakan accuracy, classification report, dan confusion matrix.
- **Dashboard:** Membuat dashboard monitoring performa mahasiswa menggunakan Metabase.
- **Deployment:** Membangun aplikasi prediksi dropout berbasis Streamlit yang dapat diakses secara online.

### Persiapan

**Sumber data:**

Dataset yang digunakan berasal dari data mahasiswa Jaya Jaya Institut yang mencakup informasi demografi, latar belakang keluarga, performa akademik, dan indikator ekonomi makro.

[Link Dataset](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

**Setup Environment:**

```bash
# Membuat virtual environment (opsional)
python -m venv venv

# Aktivasi virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

**Menjalankan Aplikasi Streamlit:**

```bash
streamlit run prediksi_dropout_app.py
```

## Business Dashboard

Dashboard dibuat menggunakan **Metabase** yang terhubung ke database PostgreSQL untuk memvisualisasikan data performa mahasiswa secara interaktif.

Dashboard ini menampilkan beberapa informasi penting, antara lain:

1. **Distribusi Status Mahasiswa** — Perbandingan jumlah mahasiswa yang Graduate, Dropout, dan Enrolled.
2. **Tingkat Dropout Berdasarkan Usia** — Visualisasi hubungan antara usia saat mendaftar dengan tingkat dropout.
3. **Analisis Dropout Berdasarkan Gender** — Perbandingan persentase dropout antara mahasiswa laki-laki dan perempuan.
4. **Pengaruh Status Debitur** — Korelasi antara status keuangan (debtor) dengan kemungkinan dropout.
5. **Dropout Berdasarkan Mode Pendaftaran** — Distribusi dropout pada setiap mode pendaftaran yang tersedia.
6. **Performa Akademik vs Dropout** — Hubungan antara nilai semester 1 & 2 dengan status dropout.

**Akses Dashboard:**

Email: `root@mail.com`
Password: `wvh2ldOygMeDkH`


## Menjalankan Sistem Machine Learning

Prototype machine learning yang telah dibangun menggunakan **Streamlit** dapat diakses melalui tautan berikut:

🔗 **[Link Aplikasi Streamlit](https://owiaja-prediksi-dropout.streamlit.app/)**

### Cara Penggunaan Aplikasi:

1. Buka link aplikasi di atas atau jalankan secara lokal dengan perintah `streamlit run prediksi_dropout_app.py`.
2. Pada panel **sidebar** di sebelah kiri, lengkapi seluruh data mahasiswa yang diminta, meliputi:
   - **Data Demografi:** Jenis kelamin, usia, kebangsaan, status pernikahan
   - **Data Pendaftaran:** Mode pendaftaran, pilihan kursus, program studi
   - **Data Keluarga:** Pendidikan dan pekerjaan orang tua
   - **Data Akademik:** Performa semester 1 & 2 (SKS, evaluasi, nilai)
   - **Data Finansial:** Status tunggakan, beasiswa, biaya kuliah
   - **Indikator Ekonomi:** Tingkat pengangguran, inflasi, GDP
3. Klik tombol **"🔍 Analisis Sekarang"**.
4. Hasil prediksi akan muncul berupa probabilitas dropout dan status risiko mahasiswa.

### Informasi Model:

| Aspek | Detail |
|-------|--------|
| **Algoritma** | XGBoost (dengan GridSearchCV) |
| **Preprocessing** | StandardScaler + PowerTransformer (numerik), OneHotEncoder (kategorikal) |
| **Cross Validation** | StratifiedKFold (5-fold) |
| **Baseline Terbaik** | Gradient Boosting (Akurasi ~83%) |
| **Model Final** | XGBoost dengan hyperparameter tuning |

## Conclusion

Berdasarkan analisis yang telah dilakukan, berikut adalah temuan utama dari proyek ini:

### 1. Faktor Utama yang Mempengaruhi Dropout

- **Performa Akademik** merupakan faktor paling dominan. Nilai mata kuliah semester 1 dan 2 memiliki korelasi negatif yang sangat kuat terhadap dropout (`Curricular_units_2nd_sem_grade`: -0.572, `Curricular_units_2nd_sem_approved`: -0.570).
- **Usia saat mendaftar** berkorelasi positif dengan dropout (0.254). Mahasiswa yang mendaftar di usia lebih tua (>21 tahun) memiliki tingkat dropout yang jauh lebih tinggi, mencapai 55-70%.
- **Status keuangan (Debtor)** berkorelasi signifikan dengan dropout (0.229). Mahasiswa yang memiliki tunggakan memiliki tingkat dropout sebesar 62.03%, dibandingkan 28.28% untuk yang tidak memiliki tunggakan.
- **Gender** juga berpengaruh, dimana mahasiswa laki-laki memiliki tingkat dropout (45.05%) yang jauh lebih tinggi dibandingkan perempuan (25.10%).
- **Mode pendaftaran** "Over 23 years old" memiliki tingkat dropout tertinggi sebesar 55.41%.

### 2. Profil Mahasiswa Berisiko Tinggi

- Mendaftar pada usia di atas 21 tahun
- Berstatus *single* dengan orang tua yang bekerja sebagai pekerja tidak terampil (*unskilled workers*)
- Memiliki tunggakan biaya kuliah dan tidak menerima beasiswa
- Memiliki kinerja akademik yang rendah pada semester pertama dan kedua
- Terdaftar pada program studi Management (evening attendance)

### 3. Performa Model Prediksi

Model XGBoost dengan hyperparameter tuning berhasil menjadi model terbaik dibandingkan Logistic Regression dan SVM, dengan akurasi baseline Gradient Boosting sebesar ~83% yang kemudian dioptimasi lebih lanjut.

### Rekomendasi Action Items

Berdasarkan temuan di atas, berikut adalah rekomendasi *action items* yang dapat diterapkan oleh Jaya Jaya Institut:

1. **Implementasi Sistem Peringatan Dini (*Early Warning System*)**
   - Menerapkan model prediksi dropout yang telah dibangun ke dalam sistem akademik institusi untuk secara otomatis mengidentifikasi mahasiswa berisiko tinggi di awal semester.
   - Melakukan pemantauan progres akademik mahasiswa secara berkala, terutama setelah semester pertama.

2. **Program Bantuan Keuangan yang Lebih Terarah**
   - Memprioritaskan pemberian beasiswa atau keringanan biaya kuliah kepada mahasiswa yang teridentifikasi sebagai debitur, khususnya yang memiliki latar belakang orang tua pekerja tidak terampil.
   - Menyediakan program cicilan biaya kuliah yang lebih fleksibel untuk meringankan beban finansial mahasiswa.

3. **Fleksibilitas Jadwal Perkuliahan**
   - Menawarkan kelas dengan jadwal yang lebih fleksibel atau opsi pembelajaran *hybrid/daring* untuk mengakomodasi mahasiswa usia menengah (>23 tahun) yang kemungkinan besar juga bekerja.
   - Menyediakan program *part-time study* yang memungkinkan mahasiswa menyesuaikan beban studi dengan kondisi pekerjaan.

4. **Program Bimbingan Akademik Khusus**
   - Memberikan bimbingan akademik intensif bagi mahasiswa yang menunjukkan penurunan performa di semester pertama.
   - Menyediakan program mentoring dari senior atau alumni untuk mahasiswa baru, terutama yang mendaftar pada usia lebih tua.
   - Mengadakan workshop manajemen waktu dan strategi belajar efektif.

5. **Monitoring Kelompok Berisiko Secara Berkala**
   - Membentuk tim khusus yang bertugas memantau dan melakukan *follow-up* terhadap mahasiswa yang teridentifikasi berisiko tinggi berdasarkan output model prediksi.
   - Melakukan evaluasi efektivitas intervensi yang diberikan setiap akhir semester untuk terus menyempurnakan strategi pencegahan dropout.
