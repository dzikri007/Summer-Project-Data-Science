# Proyek Analisis Retensi Karyawan: Jaya Jaya Maju

Aplikasi dan analisis ini dirancang untuk membantu departemen Human Resources (HR) di perusahaan [Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee) dalam memitigasi *attrition rate* (tingkat pengunduran diri karyawan) yang saat ini melampaui angka 10%. Proyek ini bertujuan untuk menyediakan *insight* berbasis data agar perusahaan dapat melakukan intervensi strategis yang tepat dalam mempertahankan talenta terbaik.

## 1. Business Understanding

### Latar Belakang Bisnis
[Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee) adalah perusahaan multinasional yang berdiri sejak tahun 2000 dengan lebih dari 1.000 karyawan. Tingginya angka attrition memberikan dampak negatif yang signifikan, di antaranya:
- **Peningkatan Biaya Operasional**: Tingginya perputaran karyawan mengakibatkan pembengkakan biaya rekrutmen, proses seleksi, hingga *onboarding* dan pelatihan ulang.
- **Penurunan Produktivitas**: Kepergian karyawan, terutama yang memiliki masa kerja lama, menyebabkan hilangnya akumulasi pengalaman dan keterampilan yang vital bagi operasional perusahaan.
- **Gangguan Moral Kerja**: Ketidakpuasan karyawan yang tidak terdeteksi sejak dini dapat menciptakan budaya kerja yang tidak kondusif.

### Permasalahan Bisnis
Permasalahan utama yang diangkat dalam proyek ini adalah:
- **Identifikasi Faktor Utama**: Menentukan faktor yang paling berpengaruh terhadap attrition, mencakup data demografi, kompensasi finansial, hingga kepuasan kerja.
- **Analisis Perilaku Karyawan**: Memahami pola perilaku yang memicu attrition, seperti dampak lembur berlebihan (*overtime*) serta pengaruh jarak tempuh rumah ke kantor terhadap kelelahan karyawan.
- **Evaluasi Stagnasi Karier dan Manajemen**: Menganalisis sejauh mana durasi karyawan dalam peran saat ini (*YearsInCurrentRole*) serta hubungan dengan manajer (*YearsWithCurrManager*) menjadi pendorong utama keputusan untuk keluar, terlepas dari tingkat pendapatan mereka.
- **Pengembangan Alat Bantu Visual (Dashboard)**: Menyediakan business dashboard yang interaktif dan mudah dipahami bagi tim HR untuk memonitor faktor risiko attrition dan melakukan analisis data secara berkala.

### Nilai Tambah bagi HR
Melalui analisis ini, HR dapat bergeser dari pendekatan reaktif menjadi proaktif:
- **Optimalisasi Karier**: Mengidentifikasi titik jenuh karyawan untuk memberikan penawaran rotasi atau pengembangan karier sebelum terjadi *resign*.
- **Audit Kepemimpinan**: Menggunakan data hubungan dengan manajer untuk mendeteksi *bottleneck* kepemimpinan di departemen tertentu.
- **Retensi yang Tersegmentasi**: Memberikan dasar bagi HR untuk membuat program retensi yang lebih personal berdasarkan profil risiko masing-masing karyawan.

## 2. Cakupan Proyek
- **Eksplorasi dan Pembersihan Data**: Menangani outliers dan memproses dataset agar siap digunakan untuk analisis.
- **Analisis Faktor Attrition**: Melakukan EDA mendalam mengenai hubungan antara variabel finansial, kepuasan kerja, dan pola karier terhadap kecenderungan karyawan untuk keluar.
- **Pembuatan Business Dashboard**: Menyajikan visualisasi interaktif untuk memonitor faktor risiko attrition secara berkala.
- **Rekomendasi Strategis**: Memberikan langkah konkret bagi manajemen untuk menekan angka attrition.

### Persiapan

Sumber data: [Dicoding Employee Dataset](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

Setup environment:
```bash
pip install -r Requirements.txt
```

Cara menjalankan Business Dashboard:
```bash
streamlit run app.py
```

## Business Dashboard

Proyek ini menyertakan **dua buah dashboard** untuk memberikan solusi yang komprehensif bagi departemen HR di perusahaan Jaya Jaya Maju:

### 1. Metabase Dashboard (Business Intelligence)
Dashboard ini difokuskan pada pemantauan metrik bisnis (*business metrics*) dan visualisasi data (*Exploratory Data Analysis*) untuk memahami faktor-faktor penyebab tingginya *attrition rate*.
**Akses Metabase:**
- **File Database:** `metabase.db.mv.db` (disertakan di dalam *repository*)
- **Email/Username:** `root@mail.com`
- **Password:** `root123`

### 2. Streamlit Dashboard (Machine Learning & Predictive Analytics)
Dashboard interaktif ini berfungsi sebagai *Early Warning System*. HR dapat memasukkan data profil karyawan (seperti usia, departemen, kepuasan kerja, dll.) melalui *form*, dan model **Machine Learning (Random Forest)** akan secara *real-time* memprediksi risiko karyawan tersebut untuk *resign*. Dashboard ini juga memuat grafik interaktif berbasis *Plotly*.

**Akses Langsung (Live Dashboard):**
🔗 **[Dashboard HR Attrition Prediction](https://dashboard-hrd-attrition.streamlit.app/)**

**Cara Menjalankan Secara Lokal (Localhost):**
```bash
streamlit run app.py
```

## Conclusion

- **Identifikasi Akar Masalah:** Analisis menunjukkan bahwa attrition bukan hanya disebabkan oleh masalah finansial, tetapi juga oleh beban kerja berlebih (OverTime) dan stagnasi karier (YearsInCurrentRole).
- **Performa Model:** Model Random Forest terbukti efektif sebagai *early warning system* untuk mendeteksi karyawan berisiko, membantu HR bertindak lebih cepat sebelum karyawan memutuskan untuk keluar.
- **Profil Karyawan Berisiko:** Data mengidentifikasi pola bahwa karyawan dengan masa kerja tertentu dan beban kerja yang tinggi adalah kelompok yang paling rentan terhadap attrition.

### Rekomendasi Action Items

1. **Pengelolaan Beban Kerja:** Melakukan peninjauan ulang terhadap kebijakan lembur (OverTime) dan mempertimbangkan penambahan staf di departemen yang memiliki attrition tinggi.
2. **Program Pengembangan Karier:** Menyusun jalur karier (*career path*) yang lebih transparan dan memberikan kesempatan rotasi internal bagi karyawan yang sudah berada di posisi yang sama selama 2-3 tahun untuk mencegah stagnasi.
3. **Peningkatan Peran Manajer:** Memberikan pelatihan *leadership* bagi manajer untuk meningkatkan hubungan dan komunikasi dengan tim mereka, karena durasi kerja dengan manajer terbukti berpengaruh terhadap retensi.
4. **Implementasi Sistem Prediksi:** Mengintegrasikan model prediksi ke dalam *business dashboard* agar HR bisa memantau risiko attrition secara *real-time* dan memberikan perhatian khusus pada karyawan yang masuk dalam kategori "risiko tinggi".
