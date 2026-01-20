# Data Analysis Project: E-Commerce Public Dataset

## Ringkasan Proyek
Proyek ini bertujuan untuk melakukan analisis mendalam terhadap **Brazilian E-Commerce Public Dataset** yang disediakan oleh Olist. Fokus utama adalah mengekstraksi wawasan berharga (actionable insights) mengenai performa bisnis, tren pertumbuhan, perilaku pelanggan, dan efektivitas kategori produk untuk mendukung pengambilan keputusan strategis.

## Analisis yang Dilakukan
Dalam proyek ini, langkah-langkah analisis data yang komprehensif telah diimplementasikan:
1.  **Data Wrangling**: Mengumpulkan data dari berbagai tabel, membersihkan data yang hilang (missing values), duplikasi, serta memastikan tipe data sudah sesuai (terutama kolom tanggal).
2.  **Exploratory Data Analysis (EDA)**: Mengeksplorasi keterkaitan antar variabel, menghitung statistik deskriptif, dan mengidentifikasi pola penjualan serta distribusi pelanggan.
3.  **Visualization & Explanatory Analysis**: Menjawab pertanyaan bisnis seperti:
    *   Bagaimana tren jumlah pesanan bulanan selama periode tertentu?
    *   Kategori produk apa yang paling banyak diminati oleh pelanggan?
    *   Bagaimana persebaran geografis pelanggan di berbagai negara bagian?
4.  **RFM Analysis**: Mengelompokkan pelanggan berdasarkan tingkat kebaruan transaksi (Recency), frekuensi pembelian (Frequency), dan total nilai ekonomi pelanggan (Monetary).

## Struktur Repositori
```text
.
├── dashboard/
│   ├── dashboard.py         # Script utama dashboard Streamlit
│   ├── all_data.csv        # Dataset yang telah dibersihkan & digabung
│   └── requirements.txt     # Dependensi khusus untuk dashboard
├── data/                    # Folder berisi dataset mentah (CSV)
├── Proyek_Analisis_Data.ipynb # Dokumentasi lengkap proses analisis
├── requirements.txt         # Seluruh dependensi python projek
├── README.md                # Panduan dokumentasi ini
└── ...
```

## Persiapan Lingkungan (Setup Environment)
Untuk menjalankan proyek ini secara lokal, ikuti langkah-langkah berikut:

### 1. Menggunakan Anaconda/Conda (Opsional tapi Direkomendasikan)
```bash
conda create --name ecommerce-ds python=3.13
conda activate ecommerce-ds
pip install -r requirements.txt
```

### 2. Menggunakan Virtual Environment (Python venv)
```bash
# Untuk Windows:
python -m venv venv
.\venv\Scripts\activate

# Untuk macOS/Linux:
python -m venv venv
source venv/bin/activate

# Install Dependensi:
pip install -r requirements.txt
```

## Cara Menjalankan Dashboard
Dashboard dibangun menggunakan **Streamlit** untuk menyajikan data secara interaktif.

1.  Buka terminal/command prompt.
2.  Pastikan Anda berada di direktori proyek.
3.  Arahkan ke folder dashboard: `cd dashboard`
4.  Jalankan dashboard dengan perintah:
    ```bash
    streamlit run dashboard.py
    ```
5.  Link lokal dashboard akan muncul (biasanya `http://localhost:8501`).

## Fitur Utama Dashboard
*   **Overview Performa**: Menampilkan metrik utama seperti Total Transaksi dan Total Revenue.
*   **Seasonal Trends**: Visualisasi pertumbuhan pesanan dari waktu ke waktu.
*   **Best & Worst Products**: Analisis kategori produk berdasarkan jumlah penjualan.
*   **Customer Demographics**: Melihat wilayah mana yang menjadi pasar utama.
*   **RFM Insights**: Segmentasi pelanggan untuk strategi pemasaran berbasis data.

## Identitas Penulis
- **Nama:** Aditya Maulana Pamungkas
- **Email:** ampaditya55@gmail.com
- **ID Dicoding:** aditya082

---
© 2026 Aditya Maulana Pamungkas