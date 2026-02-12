# Data Analysis Project: E-Commerce Public Dataset

## Ringkasan Proyek
Proyek ini merupakan analisis data end-to-end pada **Brazilian E-Commerce Public Dataset** oleh Olist. Tujuan utama proyek ini adalah untuk memberikan wawasan berbasis data (data-driven insights) mengenai performa penjualan, tren musiman, dan kategori produk unggulan guna mendukung pengambilan keputusan strategis bisnis.

## URL Project
https://d8wib5lqp8hteufjx9xrxp.streamlit.app/

## Rumusan Masalah (SMART Questions)
Analisis ini dirancang untuk menjawab pertanyaan bisnis yang spesifik, terukur, dan berbasis data:
1.  **Analisis Kategori Produk**: Kategori produk apa yang memiliki volume penjualan tertinggi berdasarkan jumlah item terjual selama periode pengamatan (2016-2018), dan bagaimana implikasinya terhadap strategi stok serta pemasaran?
2.  **Analisis Tren & Musiman**: Bagaimana tren penjualan bulanan berdasarkan jumlah order selama periode 2016-2018, dan apakah terdapat pola musiman yang dapat dimanfaatkan untuk perencanaan operasional?

## Analisis yang Dilakukan
Proyek ini mengimplementasikan siklus data analisis yang ketat:
- **Data Wrangling**: Pengumpulan data, pembersihan data secara komprehensif (handling missing values, konversi tipe data datetime, validasi kronologi), dan integrasi dataset.
- **Exploratory Data Analysis (EDA)**: Analisis statistik deskriptif mendalam (`describe`, `include='all'`), analisis distribusi (histogram), deteksi outlier (boxplots), serta analisis korelasi (`corr`) dan kovarians.
- **Visualization & Explanatory Analysis**: Visualisasi tren bulanan dan performa kategori produk menggunakan Matplotlib dan Seaborn.
- **Conclusion & Recommendations**: Memberikan temuan spesifik (seperti dominasi kategori *Bed Bath Table* dan lonjakan *Black Friday*) serta rekomendasi aksi nyata (aksi stok, strategi pemasaran, dan operasional).

## Struktur Repositori
```text
.
├── Dashboard/
│   ├── dashboard.py         # Script utama dashboard Streamlit
│   └── requirements.txt     # Dependensi khusus untuk dashboard
├── Data/                    # Folder berisi dataset mentah (CSV)
├── all_data.csv             # Dataset final hasil cleaning & integrasi
├── notebook_revisi.ipynb    # Notebook dokumentasi proses analisis lengkap
├── requirements.txt         # Seluruh dependensi python utama projek
└── README.md                # Dokumentasi proyek ini
```

## Persiapan Lingkungan (Setup Environment)
Gunakan instruksi berikut untuk menjalankan proyek di komputer Anda:

### 1. Persiapan Virtual Environment
```bash
# Membuat environment
python -m venv venv

# Aktivasi environment (Windows)
.\venv\Scripts\activate

# Aktivasi environment (macOS/Linux)
source venv/bin/activate

# Install Dependensi
pip install -r requirements.txt
```

## Cara Menjalankan Dashboard
Dashboard interaktif dapat dijalankan untuk mengeksplorasi temuan secara visual.

1.  Pastikan dependensi dashboard terinstall jika belum:
    ```bash
    pip install -r Dashboard/requirements.txt
    ```
2.  Masuk ke direktori dashboard:
    ```bash
    cd Dashboard
    ```
3.  Jalankan aplikasi streamlit:
    ```bash
    streamlit run dashboard.py
    ```

## Fitur Utama Dashboard
*   **Business Overview Metrics**: Pantau Total Pesanan, Total Pendapatan, dan Total Pelanggan secara real-time.
*   **Monthly Sales Trend**: Analisis pertumbuhan bulanan dengan highlight pada periode puncak (Black Friday).
*   **Top Product Categories**: Visualisasi kategori produk dengan volume penjualan tertinggi.
*   **Geographic Distribution**: Persebaran pelanggan berdasarkan negara bagian (states).
*   **Actionable Recommendations**: Strategi bisnis langsung berdasarkan hasil temuan data.

## Identitas Penulis
- **Nama:** Aditya Maulana Pamungkas
- **Email:** ampaditya55@gmail.com
- **ID Dicoding:** aditya082

---
© 2026 Aditya Maulana Pamungkas
