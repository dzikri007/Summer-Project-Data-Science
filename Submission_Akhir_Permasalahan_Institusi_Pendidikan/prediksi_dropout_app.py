import streamlit as st
import pandas as pd
import numpy as np
import joblib

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="Prediksi Dropout Mahasiswa",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS ---
st.markdown("""
<style>
    .main-title {
        text-align: center;
        color: var(--primary-color);
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .sub-title {
        text-align: center;
        color: var(--text-color);
        opacity: 0.8;
        font-size: 1rem;
        margin-bottom: 2rem;
    }
    .result-box {
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        margin: 1rem 0;
    }
    .dropout-warning {
        background: linear-gradient(135deg, #FF6B6B, #EE5A24);
        color: white;
    }
    .safe-indicator {
        background: linear-gradient(135deg, #26de81, #20bf6b);
        color: white;
    }
    .info-card {
        background-color: var(--secondary-background-color);
        color: var(--text-color);
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid var(--primary-color);
        margin-bottom: 1rem;
    }
    .footer-text {
        text-align: center;
        color: var(--text-color);
        opacity: 0.6;
        font-size: 0.85rem;
        margin-top: 3rem;
        padding: 1rem 0;
        border-top: 1px solid var(--secondary-background-color);
    }
</style>
""", unsafe_allow_html=True)


# --- Load model ---
@st.cache_resource
def muat_model():
    """Memuat model machine learning yang sudah dilatih."""
    import os
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(BASE_DIR, 'model.pkl')
    return joblib.load(model_path)


# --- Opsi input kategorikal ---
OPSI_MODE_PENDAFTARAN = [
    "1st phase - general contingent",
    "2nd phase - general contingent",
    "3rd phase - general contingent",
    "Over 23 years old",
    "International student (bachelor)",
    "Transfer",
    "Change of course",
    "Change of institution/course",
    "Change of institution/course (International)",
    "Technological specialization diploma holders",
    "Holders of other higher courses",
    "Short cycle diploma holders",
    "1st phase - special contingent (Madeira Island)",
    "1st phase - special contingent (Azores Island)",
    "Ordinance No. 612/93",
    "Ordinance No. 854-B/99",
    "Ordinance No. 533-A/99, item b2 (Different Plan)",
    "Ordinance No. 533-A/99, item b3 (Other Institution)"
]

OPSI_PROGRAM_STUDI = [
    "Management", "Nursing", "Social Service",
    "Veterinary Nursing", "Journalism and Communication",
    "Advertising and Marketing Management",
    "Management (evening attendance)", "Tourism",
    "Communication Design", "Animation and Multimedia Design",
    "Social Service (evening attendance)", "Agronomy",
    "Basic Education", "Informatics Engineering",
    "Equinculture", "Oral Hygiene",
    "Biofuel Production Technologies"
]

OPSI_KUALIFIKASI = ["Basic Education", "Secondary Education", "Higher Education", "Other"]

OPSI_PEKERJAAN_IBU = [
    "Unskilled Workers", "Administrative Staff", "Service Workers",
    "Technicians", "Professionals", "Skilled Workers", "Student",
    "Managers", "Agricultural Workers", "Other", "Machine Operators"
]

OPSI_PEKERJAAN_AYAH = [
    "Unskilled Workers", "Skilled Workers", "Service Workers",
    "Administrative Staff", "Technicians", "Machine Operators",
    "Armed Forces", "Agricultural Workers", "Professionals",
    "Managers", "Student", "Other"
]


def ambil_input_sidebar():
    """Mengambil semua input data mahasiswa dari sidebar."""

    st.sidebar.header("📝 Input Data Mahasiswa")
    st.sidebar.markdown("---")

    # --- Data Demografi ---
    st.sidebar.markdown("### 👤 Data Demografi")
    jenis_kelamin = st.sidebar.selectbox("Jenis Kelamin", ["Male", "Female"])
    usia = st.sidebar.number_input("Usia Saat Mendaftar", min_value=16, max_value=70, value=19)
    is_displaced = st.sidebar.selectbox("Mahasiswa Terlantar?", ["Yes", "No"])

    # --- Data Pendaftaran ---
    st.sidebar.markdown("### 📋 Data Pendaftaran")
    mode_daftar = st.sidebar.selectbox("Mode Pendaftaran", OPSI_MODE_PENDAFTARAN)
    urutan_pilihan = st.sidebar.selectbox("Pilihan Kursus", ["First Choice", "Second Choice"])
    prodi = st.sidebar.selectbox("Program Studi", OPSI_PROGRAM_STUDI)
    nilai_kualifikasi = st.sidebar.slider("Nilai Kualifikasi Sebelumnya", 0, 200, 100)
    nilai_masuk = st.sidebar.slider("Nilai Penerimaan", 0, 200, 100)

    # --- Data Keluarga ---
    st.sidebar.markdown("### 👨‍👩‍👧 Data Keluarga")
    kualifikasi_ibu = st.sidebar.selectbox("Pendidikan Ibu", OPSI_KUALIFIKASI)
    kualifikasi_ayah = st.sidebar.selectbox("Pendidikan Ayah", OPSI_KUALIFIKASI)
    pekerjaan_ibu = st.sidebar.selectbox("Pekerjaan Ibu", OPSI_PEKERJAAN_IBU)
    pekerjaan_ayah = st.sidebar.selectbox("Pekerjaan Ayah", OPSI_PEKERJAAN_AYAH)

    # --- Data Akademik ---
    st.sidebar.markdown("### 📊 Performa Akademik")
    sem1_credited = st.sidebar.number_input("SKS Diakui (Sem 1)", min_value=0, value=0)
    sem1_evaluations = st.sidebar.number_input("Jumlah Evaluasi (Sem 1)", min_value=0, value=0)
    sem1_grade = st.sidebar.number_input("Rata-rata Nilai (Sem 1)", min_value=0.0, value=0.0, format="%.2f")
    sem1_no_eval = st.sidebar.number_input("SKS Tanpa Evaluasi (Sem 1)", min_value=0, value=0)
    sem2_no_eval = st.sidebar.number_input("SKS Tanpa Evaluasi (Sem 2)", min_value=0, value=0)

    # --- Indikator Ekonomi ---
    st.sidebar.markdown("### 🌐 Indikator Ekonomi")
    unemployment = st.sidebar.number_input("Tingkat Pengangguran (%)", value=10.0, format="%.2f")
    inflation = st.sidebar.number_input("Tingkat Inflasi (%)", value=1.0, format="%.2f")
    gdp = st.sidebar.number_input("GDP", value=1.0, format="%.2f")

    # Susun menjadi DataFrame sesuai format model
    data = pd.DataFrame({
        'Previous_qualification_grade': [nilai_kualifikasi],
        'Admission_grade': [nilai_masuk],
        'Age_at_enrollment': [usia],
        'Curricular_units_1st_sem_credited': [sem1_credited],
        'Curricular_units_1st_sem_evaluations': [sem1_evaluations],
        'Curricular_units_1st_sem_grade': [sem1_grade],
        'Curricular_units_1st_sem_without_evaluations': [sem1_no_eval],
        'Curricular_units_2nd_sem_without_evaluations': [sem2_no_eval],
        'Unemployment_rate': [unemployment],
        'Inflation_rate': [inflation],
        'GDP': [gdp],
        'Application_mode': [mode_daftar],
        'Application_order': [urutan_pilihan],
        'Course': [prodi],
        'Mothers_qualification': [kualifikasi_ibu],
        'Fathers_qualification': [kualifikasi_ayah],
        'Mothers_occupation': [pekerjaan_ibu],
        'Fathers_occupation': [pekerjaan_ayah],
        'Displaced': [is_displaced],
        'Gender': [jenis_kelamin]
    })

    return data


def tampilkan_hasil(probabilitas):
    """Menampilkan hasil prediksi dropout."""

    prob_dropout = probabilitas[0][1]
    prob_lulus = probabilitas[0][0]

    st.markdown("---")
    st.subheader("📈 Hasil Analisis Prediksi")

    kol1, kol2 = st.columns(2)
    with kol1:
        st.metric("Probabilitas Dropout", f"{prob_dropout:.1%}",
                   delta="Tinggi" if prob_dropout > 0.5 else "Rendah",
                   delta_color="inverse")
    with kol2:
        st.metric("Probabilitas Lulus", f"{prob_lulus:.1%}",
                   delta="Tinggi" if prob_lulus > 0.5 else "Rendah",
                   delta_color="normal")

    st.markdown("---")
    if prob_dropout > 0.5:
        st.markdown(f"""
        <div class="result-box dropout-warning">
            <h3>⚠️ PERINGATAN: Risiko Dropout Tinggi</h3>
            <p style="font-size: 1.2rem;">
                Mahasiswa ini memiliki kemungkinan <strong>{prob_dropout:.1%}</strong>
                untuk mengalami dropout.
            </p>
            <p>Disarankan untuk segera memberikan intervensi berupa
            bimbingan akademik dan/atau bantuan finansial.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="result-box safe-indicator">
            <h3>✅ Status Aman</h3>
            <p style="font-size: 1.2rem;">
                Mahasiswa ini diprediksi <strong>tidak berisiko dropout</strong>
                dengan probabilitas lulus sebesar <strong>{prob_lulus:.1%}</strong>.
            </p>
            <p>Tetap pantau perkembangan akademik mahasiswa secara berkala.</p>
        </div>
        """, unsafe_allow_html=True)

    # Progress bar
    st.markdown("#### Distribusi Probabilitas")
    c1, c2 = st.columns(2)
    with c1:
        st.caption("🟢 Probabilitas Lulus")
        st.progress(float(max(0.0, min(1.0, prob_lulus))))
    with c2:
        st.caption("🔴 Probabilitas Dropout")
        st.progress(float(max(0.0, min(1.0, prob_dropout))))


# ============================================================
#  MAIN
# ============================================================
def main():
    model = muat_model()

    st.markdown('<p class="main-title">🎓 Sistem Prediksi Dropout Mahasiswa</p>',
                unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Aplikasi berbasis Machine Learning untuk '
                'mengidentifikasi mahasiswa yang berisiko dropout secara dini</p>',
                unsafe_allow_html=True)

    st.markdown("""
    <div class="info-card">
        <strong>ℹ️ Petunjuk:</strong> Isi data mahasiswa di <em>sidebar</em> kiri,
        lalu klik <strong>"🔍 Analisis Sekarang"</strong>.
    </div>
    """, unsafe_allow_html=True)

    df_input = ambil_input_sidebar()

    st.sidebar.markdown("---")
    tombol = st.sidebar.button("🔍 Analisis Sekarang", use_container_width=True, type="primary")

    if tombol:
        if df_input.isnull().values.any():
            st.error("❌ Mohon lengkapi semua data terlebih dahulu!")
        else:
            with st.spinner("⏳ Memproses prediksi..."):
                hasil = model.predict_proba(df_input)
            tampilkan_hasil(hasil)

    st.markdown(
        "<div class='footer-text'>"
        "Dibuat oleh <strong>Mohammad Dzikri Raihan</strong> — "
        "dzikrijokowi@gmail.com &nbsp;|&nbsp; © 2026"
        "</div>", unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
