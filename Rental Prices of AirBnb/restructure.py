import json

with open('AirBnB.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

replacements = {
    "# Mengimpor Pustaka (Library)": "# 1. Persiapan: Mengimpor Pustaka (Library)",
    "# Mengimpor Data": "# 2. Memuat Data (Load Data)",
    "# Prapemrosesan Data": "# 3. Prapemrosesan Data (Data Preprocessing)",
    "# Memeriksa Outlier (Pencilan)": "### 3.1 Memeriksa Outlier (Pencilan)",
    "# Hasil dari Outlier": "### 3.2 Hasil dari Outlier",
    "# Label Encoding untuk Mengubah Data Tekstual Menjadi Data Numerik": "### 3.3 Label Encoding (Mengubah Data Tekstual)",
    "# Membagi Data menjadi Data Uji (Test) dan Latih (Train)": "### 3.4 Membagi Data (Train-Test Split)",
    "# Menskalakan (Scaling) Data": "### 3.5 Menskalakan (Scaling) Data",
    "# Menerapkan Model pada Data": "# 4. Pemodelan (Modeling)",
    "# Prediksi pada Model yang Telah Dilatih": "### 4.1 Prediksi",
    "# Akurasi Model": "# 5. Evaluasi Model",
    "# Visualisasi": "# 6. Visualisasi (Visualization)",
    "# Ringkasan Statistik": "### 6.1 Ringkasan Statistik",
    "# Populasi target akan mendapatkan manfaat dari hasil analisis dengan memperoleh pemahaman yang lebih baik mengenai faktor-faktor yang memengaruhi harga sewa AirBnB.": "# 7. Kesimpulan dan Dampak Analisis\nPopulasi target akan mendapatkan manfaat dari hasil analisis dengan memperoleh pemahaman yang lebih baik mengenai faktor-faktor yang memengaruhi harga sewa AirBnB."
}

for cell in nb['cells']:
    if cell['cell_type'] == 'markdown':
        new_source = []
        for line in cell['source']:
            for k, v in replacements.items():
                if line.startswith(k):
                    line = line.replace(k, v)
            new_source.append(line)
        cell['source'] = new_source

with open('AirBnB.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Heading transformation complete.")
