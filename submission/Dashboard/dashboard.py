import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
import os

# Set Page Config for a premium feel
st.set_page_config(
    page_title="E-Commerce Analysis Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Premium styling
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    [data-testid="stSidebar"] {
        background-color: #161b22;
    }
    .stMetric {
        background-color: #1f2937;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        border: 1px solid #374151;
    }
    .stMetric label {
        color: #9ca3af !important;
        font-weight: 600;
    }
    .stMetric div[data-testid="stMetricValue"] {
        color: #60a5fa !important;
        font-weight: 800;
    }
    h1, h2, h3 {
        color: #f3f4f6 !important;
        font-family: 'Inter', sans-serif;
    }
    .reportview-container .main .block-container {
        padding-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Set global plotting style for Dark Mode
plt.style.use('dark_background')
sns.set_palette("bright")

# Load Data function with caching
@st.cache_data
def load_data():
    current_dir = os.path.dirname(os.path.realpath(__file__))
<<<<<<< HEAD
    file_path = os.path.join(current_dir, "main_data.csv")
=======
    # Try local main_data.csv first
    file_path = os.path.join(current_dir, "main_data.csv")
    
>>>>>>> c174b96 (Submission)
    df = pd.read_csv(file_path)
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
    return df

all_df = load_data()

# Helper functions for data preparation
def create_monthly_orders_df(df):
    monthly_orders_df = df.resample(rule='M', on='order_purchase_timestamp').agg({
        "order_id": "nunique",
        "price": "sum"
    }).reset_index()
    monthly_orders_df.rename(columns={"order_id": "order_count", "price": "revenue"}, inplace=True)
    monthly_orders_df['month_name'] = monthly_orders_df['order_purchase_timestamp'].dt.strftime('%B %Y')
    return monthly_orders_df

def create_sum_order_items_df(df):
    sum_order_items_df = df.groupby("product_category").order_item_id.count().sort_values(ascending=False).reset_index()
    sum_order_items_df.rename(columns={"order_item_id": "product_count"}, inplace=True)
    return sum_order_items_df

def create_bystate_df(df):
    bystate_df = df.groupby(by="customer_state").customer_id.nunique().reset_index()
    bystate_df.rename(columns={"customer_id": "customer_count"}, inplace=True)
    bystate_df = bystate_df.sort_values(by="customer_count", ascending=False)
    return bystate_df

# Sidebar
with st.sidebar:
    # Logo Placeholder
    st.markdown("<h1 style='text-align: center; color: #60a5fa;'>📦 E-Shop</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### Filters")
    
    min_date = all_df["order_purchase_timestamp"].min()
    max_date = all_df["order_purchase_timestamp"].max()
    
    try:
        start_date, end_date = st.date_input(
            label='Pilih Rentang Waktu',
            min_value=min_date,
            max_value=max_date,
            value=[min_date, max_date]
        )
    except ValueError:
        st.error("Mohon pilih rentang waktu yang valid.")
        st.stop()

# Filter Main Data
main_df = all_df[(all_df["order_purchase_timestamp"] >= pd.to_datetime(start_date)) & 
                (all_df["order_purchase_timestamp"] <= pd.to_datetime(end_date))]

# Build Dataframes
monthly_orders_df = create_monthly_orders_df(main_df)
sum_order_items_df = create_sum_order_items_df(main_df)
bystate_df = create_bystate_df(main_df)

# Header
st.title('🛍️ Public E-Commerce Analysis Dashboard')
st.markdown("Dashboard ini menyajikan analisis mendalam berdasarkan data operasional tahun 2016-2018.")

# Metrics Section
col1, col2, col3 = st.columns(3)
with col1:
    total_orders = main_df.order_id.nunique()
    st.metric("Total Pesanan", value=f"{total_orders:,}")
with col2:
    total_revenue = main_df.price.sum()
    st.metric("Total Pendapatan", value=format_currency(total_revenue, "BRL", locale='pt_BR'))
with col3:
    total_customers = main_df.customer_id.nunique()
    st.metric("Total Pelanggan", value=f"{total_customers:,}")

st.markdown("---")

# Row 1: Monthly Sales Trend (Question 2)
st.subheader("📈 Tren Penjualan Bulanan (Pertanyaan Bisnis 2)")
st.caption("Visualisasi ini menjawab pola tren dan musiman penjualan selama periode pengamatan.")

fig, ax = plt.subplots(figsize=(16, 6))
ax.plot(monthly_orders_df["order_purchase_timestamp"], monthly_orders_df["order_count"], marker='o', linewidth=3, color="#60a5fa")
ax.fill_between(monthly_orders_df["order_purchase_timestamp"], monthly_orders_df["order_count"], color="#60a5fa", alpha=0.1)

# Adding peaks highlights (optional but premium)
max_order = monthly_orders_df.order_count.max()
max_date_val = monthly_orders_df[monthly_orders_df.order_count == max_order].order_purchase_timestamp.iloc[0]
ax.annotate(f'Peak: {max_order}', xy=(max_date_val, max_order), xytext=(max_date_val, max_order+200),
            arrowprops=dict(facecolor='#f87171', shrink=0.05), fontsize=12, color="#f87171", fontweight='bold')

ax.set_title("Jumlah Pesanan per Bulan", fontsize=20, color="#ffffff", pad=20)
ax.set_xlabel(None)
ax.set_ylabel("Jumlah Pesanan", fontsize=12, color="#ffffff")
ax.grid(axis='y', linestyle='--', alpha=0.2)
st.pyplot(fig)

with st.expander("Lihat Detail Insight Tren Bulanan"):
    st.write("""
    - **Tren Pertumbuhan**: Terlihat pertumbuhan signifikan dari akhir tahun 2016 hingga puncak di tahun 2017.
    - **Pola Musiman**: Terdapat lonjakan tajam pada bulan **November**, yang bertepatan dengan periode Black Friday.
    - **Stabilisasi**: Penjualan cenderung stabil dan tinggi sepanjang semester pertama tahun 2018.
    """)

st.markdown("---")

# Row 2: Product Performance (Question 1)
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏆 Kategori Produk Terlaris (Pertanyaan Bisnis 1)")
    st.caption("Menjawab kategori produk mana yang memiliki volume penjualan tertinggi.")
    
    fig, ax = plt.subplots(figsize=(12, 8))
    top_items = sum_order_items_df.head(10)
    
    # Gradient colors
    colors = sns.color_palette("Blues_r", n_colors=10)
    sns.barplot(x="product_count", y="product_category", data=top_items, palette=colors, ax=ax)
    
    ax.set_title("10 Kategori Produk dengan Volume Penjualan Tertinggi", fontsize=18, color="#ffffff", pad=15)
    ax.set_xlabel("Jumlah Item Terjual", fontsize=12, color="#ffffff")
    ax.set_ylabel(None)
    st.pyplot(fig)

with col2:
    st.subheader("📍 Persebaran Pelanggan per Wilayah")
    st.caption("Informasi demografis pelanggan untuk mendukung strategi pemasaran.")
    
    fig, ax = plt.subplots(figsize=(12, 8))
    top_states = bystate_df.head(10)
    sns.barplot(x="customer_count", y="customer_state", data=top_states, palette="viridis", ax=ax)
    
    ax.set_title("10 Negara Bagian dengan Pelanggan Terbanyak", fontsize=18, color="#ffffff", pad=15)
    ax.set_xlabel("Jumlah Pelanggan", fontsize=12, color="#ffffff")
    ax.set_ylabel(None)
    st.pyplot(fig)

st.markdown("---")

# Conclusion Section (Mirroring Notebook)
st.subheader("🏁 Kesimpulan & Rekomendasi")
con_col1, con_col2 = st.columns(2)

with con_col1:
    st.info("#### Kesimpulan Analisis")
    st.markdown("""
    1. **Produk Dominan**: Kategori **Bed Bath Table** dan **Health Beauty** adalah penggerak volume penjualan utama. Hal ini menunjukkan fokus konsumen pada kebutuhan rumah tangga dan perawatan diri.
    2. **Momen Emas**: Bulan **November** adalah periode kritis bagi bisnis dengan volume pesanan tertinggi secara musiman, dipicu oleh Black Friday.
    3. **Konsentrasi Geografis**: Mayoritas pelanggan terpusat di negara bagian SP (Sao Paulo), yang menunjukkan pusat aktivitas ekonomi e-commerce.
    """)

with con_col2:
    st.success("#### Rekomendasi Strategis")
    st.markdown("""
    1. **Optimasi Stok**: Tingkatkan ketersediaan stok untuk kategori *top-performer* minimal 20% sebelum memasuki kuartal keempat (Q4).
    2. **Targeting Marketing**: Fokuskan kampanye iklan berbayar pada wilayah dengan kepadatan pelanggan tinggi (SP, RJ, MG) untuk efisiensi budget.
    3. **Persiapan Black Friday**: Siapkan kapasitas logistik dan server tambahan di bulan Oktober untuk mengantisipasi lonjakan ekstrim di bulan November.
    """)

# Footer
st.markdown("---")
st.caption(f'Terakhir diperbarui pada: {pd.Timestamp.now().strftime("%Y-%m-%d %H:%M")}')
st.caption('Dicoding Data Analysis Project | Aditya Maulana Pamungkas')
