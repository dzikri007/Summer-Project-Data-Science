# 🚢 Titanic Survival Prediction: Logistic Regression & SVM Baseline

Repositoti ini berisi proyek baseline **Titanic Survival Prediction** menggunakan **Logistic Regression** dan **Support Vector Machine (SVM)** dengan fokus pada kemudahan pemahaman bagi pemula (*beginner-friendly*). Proyek ini berfokus pada Analisis Data Eksploratif (EDA), manipulasi fitur sederhana (*Feature Engineering*), dan pembuatan alur preprocessing data terstandarisasi menggunakan Pipeline Scikit-Learn.

Proyek ini dikembangkan menggunakan dataset resmi dari kompetisi legendaris [Kaggle Titanic: Machine Learning from Disaster](https://www.kaggle.com/competitions/titanic).

---
## Alur Proyek

### 1. Eksplorasi Data & Pembersihan awal (EDA)
- Menganalisis ukuran data (891 baris, 12 fitur pada dataset latih) serta tipe data masing-masing kolom.
- Mengidentifikasi nilai yang hilang (*missing values*) pada fitur `Cabin`, `Age`, dan `Embarked`.
- Visualisasi hubungan antara fitur kategori (seperti jenis kelamin `Sex`, kelas penumpang `Pclass`) dengan peluang bertahan hidup (`Survived`).

> [!NOTE]
> Dari analisis awal, ditemukan bahwa **Jenis Kelamin (Sex)** dan **Kelas Penumpang (Pclass)** merupakan faktor prediktor terkuat. Wanita dan penumpang kelas satu memiliki tingkat keselamatan jauh lebih tinggi.

### 2. Rekayasa Fitur (Feature Engineering)
Untuk meningkatkan akurasi baseline, preprocessing tambahan dilakukan:
- **Imputasi Nilai Hilang**: Mengisi nilai kosong pada `Age` dan `Fare` menggunakan median kelompok, serta `Embarked` dengan nilai modus.
- **FamilySize**: Menggabungkan `SibSp` (saudara/pasangan) dan `Parch` (orang tua/anak) ditambah 1 untuk melihat total anggota keluarga di kapal.
- **Title Extraction**: Mengekstrak gelar panggilan dari nama (seperti Mr, Miss, Mrs) dan mengelompokkan gelar langka (seperti Dr, Rev, Col) ke dalam kategori `Rare`.
- **Age Binning**: Membagi usia menjadi beberapa kelompok (`Child`, `Teen`, `YoungAdult`, `Adult`, `Senior`) untuk menangkap pengaruh kategori umur secara non-linear.

### 3. Pipeline Preprocessing & Model Baseline
Menggunakan Scikit-Learn `ColumnTransformer` dan `Pipeline` agar pemrosesan data latih dan data uji konsisten, serta mencegah kebocoran data (*data leakage*):
- **Fitur Numerik** (`Age`, `Fare`, `FamilySize`): Dinormalisasi menggunakan `StandardScaler`.
- **Fitur Kategorikal** (`Pclass`, `Sex`, `Embarked`): Dikodekan secara biner menggunakan `OneHotEncoder(handle_unknown='ignore')`.

Dua algoritma machine learning dilatih dan divalidasi:
1. **Logistic Regression (Baseline)**: Sebagai model klasifikasi linear awal.
2. **Support Vector Machine (SVM)**: Dengan kernel Radial Basis Function (RBF) dan penalaan parameter menggunakan `GridSearchCV`.

---

## Hasil Evaluasi & Performa Model

Berikut adalah ringkasan hasil akurasi model pada data validasi (split 20%) dan rata-rata 5-Fold Cross Validation:

| Model | Parameter Terbaik | Akurasi Validasi (Val Accuracy) | Akurasi Cross-Validation (CV) |
| :--- | :--- | :---: | :---: |
| **Logistic Regression** | Default (`max_iter=1000`) | ~81.0% | ~75.0% |
| **SVM (RBF Kernel)** | `C=10`, `gamma=0.01` | ~81.0% | ~78.0% |

> [!IMPORTANT]
> Selisih akurasi antara validasi tunggal (~81%) dan cross-validation (~75-78%) menunjukkan bahwa model masih cukup sensitif terhadap pembagian data (split). SVM dengan RBF Kernel memberikan performa yang sedikit lebih stabil di berbagai lipatan data (fold) dibanding Logistic Regression.

---

## Rencana Pengembangan Selanjutnya
Untuk meningkatkan akurasi model agar menembus batas >80% pada submission Kaggle, langkah-langkah berikut direkomendasikan:
1. **Fitur Tambahan**: Membuat fitur `IsAlone` (apakah bepergian sendiri) dan mendeteksi kelompok keluarga berdasarkan kesamaan nama belakang.
2. **Algoritma Ensemble**: Menggunakan model berbasis pohon keputusan (*decision trees*) seperti **Random Forest**, **XGBoost**, atau **LightGBM** yang lebih andal dalam menangani hubungan non-linear pada dataset Titanic.
3. **Imputasi Usia Tingkat Lanjut**: Mengisi nilai kosong usia berdasarkan median gelar panggilan (`Title`) alih-alih median keseluruhan.
