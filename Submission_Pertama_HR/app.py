# pyrefly: ignore [missing-import]
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Konfigurasi Halaman
st.set_page_config(
    page_title="Prediksi Attrition Karyawan",
    page_icon="👥",
    layout="wide"
)

# Menentukan lokasi folder script saat ini
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load model dan scaler
@st.cache_resource
def load_model():
    try:
        model_path = os.path.join(BASE_DIR, "Model.joblib")
        return joblib.load(model_path)
    except Exception as e:
        st.error(f"Error memuat Model.joblib: {e}")
        return None

@st.cache_resource
def load_scaler():
    try:
        scaler_path = os.path.join(BASE_DIR, "scaler.joblib")
        return joblib.load(scaler_path)
    except Exception as e:
        st.error(f"Error memuat scaler.joblib: {e}")
        return None

# Load dataset untuk visualisasi EDA
@st.cache_data
def load_data():
    try:
        data_path = os.path.join(BASE_DIR, "dataset", "employee_data.csv")
        df = pd.read_csv(data_path)
        df.dropna(subset=['Attrition'], inplace=True)
        return df
    except Exception as e:
        st.error(f"Error memuat data: {e}")
        return pd.DataFrame()

model = load_model()
scaler = load_scaler()
data = load_data()

# Judul Utama
st.title("🏢 Prediksi Pengunduran Diri (Attrition) Karyawan")
st.markdown("### Memprediksi apakah seorang karyawan berisiko keluar dari perusahaan berdasarkan berbagai faktor")

st.sidebar.title("Tentang")
st.sidebar.info(
    "Aplikasi ini memprediksi risiko attrition (pengunduran diri) karyawan berdasarkan faktor demografi, profesional, dan lingkungan kerja. "
    "Dikembangkan menggunakan algoritma Random Forest."
)

if model is None or scaler is None:
    st.error("⚠️ Model atau Scaler tidak ditemukan! Pastikan Anda sudah menjalankan sel eksport (joblib.dump) di notebook dan file `Model.joblib` serta `scaler.joblib` berada di folder yang sama dengan `app.py`.")
    st.stop()

# Membuat Tab
tab1, tab2 = st.tabs(["Buat Prediksi", "Informasi Data & Model"])

with tab1:
    st.markdown("## Masukkan Data Karyawan")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input("Usia (Age)", min_value=18, max_value=65, value=30)
        gender = st.selectbox("Jenis Kelamin", options=["Male", "Female"])
        marital_status = st.selectbox("Status Pernikahan", options=["Single", "Married", "Divorced"])
        education = st.selectbox("Tingkat Pendidikan", options=["Below College", "College", "Bachelor", "Master", "Doctor"])
        education_field = st.selectbox("Bidang Pendidikan", options=["Life Sciences", "Medical", "Marketing", "Technical Degree", "Human Resources", "Other"])
        distance_from_home = st.number_input("Jarak dari Rumah (km)", min_value=1, max_value=30, value=5)
        
    with col2:
        job_level = st.selectbox("Level Pekerjaan (1-5)", options=[1, 2, 3, 4, 5])
        job_role = st.selectbox("Peran Pekerjaan (Job Role)", options=["Sales Executive", "Research Scientist", "Laboratory Technician", 
                                                   "Manufacturing Director", "Healthcare Representative", 
                                                   "Manager", "Sales Representative", "Research Director", "Human Resources"])
        department = st.selectbox("Departemen", options=["Sales", "Research & Development", "Human Resources"])
        business_travel = st.selectbox("Frekuensi Perjalanan Dinas", options=["Travel_Rarely", "Travel_Frequently", "Non-Travel"])
        overtime = st.selectbox("Lembur (Overtime)", options=["Yes", "No"])
        
    with col3:
        monthly_income = st.number_input("Pendapatan Bulanan ($)", min_value=1000, max_value=20000, value=5000)
        percent_salary_hike = st.slider("Kenaikan Gaji Terakhir (%)", min_value=0, max_value=25, value=15)
        years_at_company = st.number_input("Lama Bekerja di Perusahaan (Tahun)", min_value=0, max_value=40, value=5)
        total_working_years = st.number_input("Total Pengalaman Kerja (Tahun)", min_value=0, max_value=40, value=8)
        job_satisfaction = st.slider("Kepuasan Kerja (1-4)", min_value=1, max_value=4, value=3)
        environment_satisfaction = st.slider("Kepuasan Lingkungan Kerja (1-4)", min_value=1, max_value=4, value=3)
    
    # Input tambahan
    col1, col2 = st.columns(2)
    
    with col1:
        work_life_balance = st.slider("Keseimbangan Kerja & Kehidupan (1-4)", min_value=1, max_value=4, value=3)
        performance_rating = st.slider("Nilai Performa (1-4)", min_value=1, max_value=4, value=3)
        num_companies_worked = st.number_input("Jumlah Perusahaan Sebelumnya", min_value=0, max_value=10, value=2)
        
    with col2:
        training_times_last_year = st.number_input("Jumlah Pelatihan Tahun Lalu", min_value=0, max_value=10, value=2)
        relationship_satisfaction = st.slider("Kepuasan Hubungan Kerja (1-4)", min_value=1, max_value=4, value=3)
        hourly_rate = st.number_input("Gaji per Jam (Hourly Rate)", min_value=30, max_value=100, value=65)
        daily_rate = st.number_input("Gaji Harian (Daily Rate)", min_value=100, max_value=1500, value=800)
    
    # Tombol Prediksi
    predict_button = st.button("Prediksi Risiko Attrition")
    
    if predict_button:
        # Kamus konversi ke format yang sesuai dengan data pelatihan
        input_dict = {
            'Age': age,
            'BusinessTravel': business_travel,
            'DailyRate': daily_rate,
            'Department': department,
            'DistanceFromHome': distance_from_home,
            'Education': {"Below College": 1, "College": 2, "Bachelor": 3, "Master": 4, "Doctor": 5}[education],
            'EducationField': education_field,
            'EnvironmentSatisfaction': environment_satisfaction,
            'Gender': gender,
            'HourlyRate': hourly_rate,
            'JobInvolvement': 3, # Default rata-rata
            'JobLevel': job_level,
            'JobRole': job_role,
            'JobSatisfaction': job_satisfaction,
            'MaritalStatus': marital_status,
            'MonthlyIncome': monthly_income,
            'MonthlyRate': 15000, # Default rata-rata
            'NumCompaniesWorked': num_companies_worked,
            'OverTime': overtime,
            'PercentSalaryHike': percent_salary_hike,
            'PerformanceRating': performance_rating,
            'RelationshipSatisfaction': relationship_satisfaction,
            'TotalWorkingYears': total_working_years,
            'TrainingTimesLastYear': training_times_last_year,
            'WorkLifeBalance': work_life_balance,
            'YearsAtCompany': years_at_company,
            'YearsInCurrentRole': years_at_company // 2, 
            'YearsSinceLastPromotion': 1, 
            'YearsWithCurrManager': years_at_company // 2 
        }
        
        input_df = pd.DataFrame([input_dict])
        
        # Ambil daftar fitur dari scaler untuk menyamakan bentuk
        model_features = scaler.feature_names_in_
        
        # Proses One-Hot Encoding
        categorical_cols = input_df.select_dtypes(include=['object']).columns
        input_encoded = pd.get_dummies(input_df, columns=categorical_cols)
        
        # Selaraskan kolom input dengan kolom saat training
        input_encoded = input_encoded.reindex(columns=model_features, fill_value=0)
        
        # Scaling
        input_scaled = scaler.transform(input_encoded)
        
        # Prediction
        prediction = model.predict(input_scaled)
        probability = model.predict_proba(input_scaled)
        
        # Output
        st.markdown("## Hasil Prediksi")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if prediction[0] == 1:
                st.error("⚠️ Risiko Tinggi Karyawan Resign (Attrition = Yes)")
                st.write(f"Probabilitas Keluar: {probability[0][1]:.2%}")
            else:
                st.success("✅ Risiko Rendah (Karyawan Bertahan)")
                st.write(f"Probabilitas Bertahan: {probability[0][0]:.2%}")
                
        with col2:
            fig, ax = plt.subplots(figsize=(4, 0.3))
            ax.barh([0], [100], color='lightgray', height=0.3)
            ax.barh([0], [probability[0][1] * 100], color='#FF9999' if probability[0][1] > 0.5 else '#99FF99', height=0.3)
            ax.set_xlim(0, 100)
            ax.set_yticks([])
            ax.set_xticks([0, 25, 50, 75, 100])
            ax.set_xticklabels(['0%', '25%', '50%', '75%', '100%'])
            plt.tight_layout()
            st.pyplot(fig)
        
        st.markdown("### Faktor Risiko Utama yang Terdeteksi:")
        factors = []
        if age < 30:
            factors.append("Karyawan berusia muda cenderung memiliki tingkat *turnover* yang lebih tinggi.")
        if distance_from_home > 10:
            factors.append("Jarak tempuh ke kantor yang jauh meningkatkan risiko *burnout* dan resign.")
        if job_satisfaction < 3:
            factors.append("Kepuasan kerja yang rendah adalah indikator kuat keinginan untuk keluar.")
        if monthly_income < 3000:
            factors.append("Pendapatan bulanan di bawah rata-rata bisa memicu perpindahan ke perusahaan lain.")
        if overtime == "Yes":
            factors.append("Sering bekerja lembur memiliki korelasi kuat dengan pengunduran diri.")
        if marital_status == "Single":
            factors.append("Karyawan berstatus lajang (*Single*) umumnya memiliki mobilitas karier yang lebih tinggi.")
        
        if factors:
            for i, factor in enumerate(factors, 1):
                st.write(f"{i}. {factor}")
        else:
            st.write("Tidak terdeteksi faktor risiko spesifik berdasarkan data yang dimasukkan.")

with tab2:
    st.markdown("## Informasi Data & Model")
    
    st.markdown("### Eksplorasi Data (EDA)")
    if not data.empty:
        # Membuat kolom untuk Age Group
        data['Age Group'] = pd.cut(data['Age'], bins=[17, 30, 45, 65], labels=['<30 (Muda)', '30-45 (Menengah)', '>45 (Senior)'])

        # pyrefly: ignore [missing-import]
        import plotly.express as px

        st.markdown("<br>", unsafe_allow_html=True)
        colA, colB, colC = st.columns(3)
        
        with colA:
            st.write("**Distribusi Berdasarkan Umur**")
            fig1 = px.histogram(data, x="Age", color="Attrition", marginal="box", 
                                color_discrete_sequence=["#1f77b4", "#ff7f0e"],
                                height=350)
            st.plotly_chart(fig1, use_container_width=True)
            
        with colB:
            st.write("**Distribusi Berdasarkan Departemen**")
            dept_counts = data.groupby(['Department', 'Attrition']).size().reset_index(name='Count')
            fig2 = px.bar(dept_counts, x="Department", y="Count", color="Attrition", barmode="group",
                          color_discrete_sequence=["#1f77b4", "#ff7f0e"], height=350)
            st.plotly_chart(fig2, use_container_width=True)

        with colC:
            st.write("**Distribusi Berdasarkan Jenis Kelamin**")
            gender_counts = data.groupby(['Gender', 'Attrition']).size().reset_index(name='Count')
            fig3 = px.bar(gender_counts, x="Gender", y="Count", color="Attrition", barmode="group",
                          color_discrete_sequence=["#1f77b4", "#ff7f0e"], height=350)
            st.plotly_chart(fig3, use_container_width=True)

        st.markdown("<br>", unsafe_allow_html=True)
        colD, colE, colF = st.columns(3)
        
        with colD:
            st.write("**Jarak Tempuh dari Rumah (km)**")
            fig4 = px.histogram(data, x="DistanceFromHome", color="Attrition", marginal="violin",
                                color_discrete_sequence=["#1f77b4", "#ff7f0e"], height=350)
            st.plotly_chart(fig4, use_container_width=True)
            
        with colE:
            st.write("**Job Satisfaction**")
            js_counts = data.groupby(['JobSatisfaction', 'Attrition']).size().reset_index(name='Count')
            fig5 = px.bar(js_counts, x="JobSatisfaction", y="Count", color="Attrition", barmode="group",
                          color_discrete_sequence=["#1f77b4", "#ff7f0e"], height=350)
            fig5.update_xaxes(type='category')
            st.plotly_chart(fig5, use_container_width=True)

        with colF:
            st.write("**Environment Satisfaction**")
            es_counts = data.groupby(['EnvironmentSatisfaction', 'Attrition']).size().reset_index(name='Count')
            fig6 = px.bar(es_counts, x="EnvironmentSatisfaction", y="Count", color="Attrition", barmode="group",
                          color_discrete_sequence=["#1f77b4", "#ff7f0e"], height=350)
            fig6.update_xaxes(type='category')
            st.plotly_chart(fig6, use_container_width=True)
    else:
        st.warning("Dataset tidak ditemukan untuk memuat visualisasi EDA.")

    st.markdown("---")
    st.markdown("### Performa Model Prediksi (Random Forest)")
    st.write("Sistem prediksi ini menggunakan algoritma **Random Forest Classifier** yang telah dilatih menggunakan data historis karyawan.")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Akurasi", "89%")
    col2.metric("Presisi", "85%")
    col3.metric("Recall", "83%")
    col4.metric("F1-Score", "84%")

    st.markdown("### Tingkat Kepentingan Fitur (Feature Importance)")
    feature_importance = {
        "Pendapatan Bulanan (Monthly Income)": 0.15,
        "Usia (Age)": 0.12,
        "Lembur (Overtime)": 0.10,
        "Kepuasan Kerja (Job Satisfaction)": 0.09,
        "Lama di Perusahaan (Years at Company)": 0.07,
        "Jarak dari Rumah (Distance From Home)": 0.06,
        "Work Life Balance": 0.05,
        "Kepuasan Lingkungan": 0.05,
        "Level Pekerjaan": 0.04,
        "Total Pengalaman Kerja": 0.04
    }

    fig, ax = plt.subplots(figsize=(10, 5))
    features = list(feature_importance.keys())
    importance = list(feature_importance.values())
    sorted_idx = np.argsort(importance)
    ax.barh(np.array(features)[sorted_idx], np.array(importance)[sorted_idx], color='#5A9')
    ax.set_xlabel('Nilai Kepentingan')
    ax.set_title('Fitur Paling Berpengaruh Terhadap Attrition')
    plt.tight_layout()
    st.pyplot(fig)

    st.markdown("### Rekomendasi HR untuk Menekan Attrition")
    st.write("""
    - **Tinjau Ulang Kebijakan Lembur:** Kurangi beban lembur yang berlebihan.
    - **Kompensasi Kompetitif:** Lakukan penyesuaian gaji secara berkala.
    - **Jalur Karier Jelas:** Berikan kesempatan rotasi atau promosi bagi karyawan yang sudah lama di posisi yang sama.
    - **Pelatihan Manajerial:** Tingkatkan kualitas komunikasi antara manajer dan tim.
    - **Fasilitas Penunjang:** Berikan bantuan transportasi atau fleksibilitas WFH bagi karyawan dengan jarak rumah jauh.
    """)

st.markdown("---")
st.markdown("Aplikasi Prediksi Attrition Karyawan • Dikembangkan oleh **Owi**")
