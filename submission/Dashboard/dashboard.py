import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
import os

# Set Page Config for a premium feel
st.set_page_config(
    page_title="E-Commerce Analysis Dashboard",
    page_icon="�️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Dark Mode styling
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
    }
    .stMetric div[data-testid="stMetricValue"] {
        color: #60a5fa !important;
    }
    h1, h2, h3 {
        color: #f3f4f6 !important;
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
    file_path = os.path.join(current_dir, "main_data.csv")
    df = pd.read_csv(file_path)
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
    return df

all_df = load_data()

# Helper functions for data preparation
def create_daily_orders_df(df):
    daily_orders_df = df.resample(rule='D', on='order_purchase_timestamp').agg({
        "order_id": "nunique",
        "price": "sum"
    }).reset_index()
    daily_orders_df.rename(columns={"order_id": "order_count", "price": "revenue"}, inplace=True)
    return daily_orders_df

def create_sum_order_items_df(df):
    return df.groupby("product_category").order_item_id.count().sort_values(ascending=False).reset_index()

def create_bystate_df(df):
    bystate_df = df.groupby(by="customer_state").customer_id.nunique().reset_index()
    bystate_df.rename(columns={"customer_id": "customer_count"}, inplace=True)
    bystate_df = bystate_df.sort_values(by="customer_count", ascending=False)
    return bystate_df

def create_rfm_df(df):
    rfm_df = df.groupby(by="customer_unique_id", as_index=False).agg({
        "order_purchase_timestamp": "max",
        "order_id": "nunique",
        "price": "sum"
    })
    rfm_df.columns = ["customer_id", "max_order_timestamp", "frequency", "monetary"]
    recent_date = df["order_purchase_timestamp"].max()
    rfm_df["recency"] = rfm_df["max_order_timestamp"].apply(lambda x: (recent_date - x).days)
    rfm_df.drop("max_order_timestamp", axis=1, inplace=True)
    return rfm_df

# Sidebar
with st.sidebar:
    st.image("https://raw.githubusercontent.com/dicodingacademy/assets/main/logo.png", width=200)
    st.markdown("## Filters")
    
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
main_df = all_df[(all_df["order_purchase_timestamp"] >= str(start_date)) & 
                (all_df["order_purchase_timestamp"] <= str(end_date))]

# Build Dataframes
daily_orders_df = create_daily_orders_df(main_df)
sum_order_items_df = create_sum_order_items_df(main_df)
bystate_df = create_bystate_df(main_df)
rfm_df = create_rfm_df(main_df)

# Header
st.title('🛍️ Public E-Commerce Dashboard')
st.markdown("Wawasan mendalam mengenai performa penjualan, pelanggan, dan produk Anda.")

# Overview Metrics
st.subheader("Business Overview")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Pesanan", value=f"{daily_orders_df.order_count.sum():,}")
with col2:
    total_rev = daily_orders_df.revenue.sum()
    st.metric("Total Pendapatan", value=format_currency(total_rev, "BRL", locale='pt_BR'))
with col3:
    avg_order = main_df.groupby('order_id').price.sum().mean()
    st.metric("Rata-rata Nilai Pesanan", value=format_currency(avg_order, "BRL", locale='pt_BR'))

st.markdown("---")

# Row 1: Sales Trend
st.subheader("📈 Tren Penjualan Harian")
fig, ax = plt.subplots(figsize=(16, 6))
ax.plot(daily_orders_df["order_purchase_timestamp"], daily_orders_df["order_count"], marker='o', linewidth=3, color="#00d4ff")
ax.fill_between(daily_orders_df["order_purchase_timestamp"], daily_orders_df["order_count"], color="#00d4ff", alpha=0.15)
ax.set_title("Jumlah Pesanan per Hari", fontsize=20, color="#ffffff")
ax.set_xlabel(None)
ax.set_ylabel("Jumlah Pesanan", fontsize=12, color="#ffffff")
ax.grid(axis='y', linestyle='--', alpha=0.3)
st.pyplot(fig)

# Row 2: Products & Demographics
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏆 Produk Terlaris")
    fig, ax = plt.subplots(figsize=(12, 10))
    top_5 = sum_order_items_df.head(5)
    sns.barplot(x="order_item_id", y="product_category", data=top_5, palette="rocket", ax=ax)
    ax.set_title("5 Kategori Produk Teratas", fontsize=18, color="#ffffff")
    ax.set_xlabel("Jumlah Terjual", fontsize=12, color="#ffffff")
    ax.set_ylabel(None)
    st.pyplot(fig)

with col2:
    st.subheader("📍 Persebaran Pelanggan")
    fig, ax = plt.subplots(figsize=(12, 10))
    top_states = bystate_df.sort_values(by="customer_count", ascending=False).head(10)
    sns.barplot(x="customer_count", y="customer_state", data=top_states, palette="mako", ax=ax)
    ax.set_title("10 Negara Bagian dengan Pelanggan Terbanyak", fontsize=18, color="#ffffff")
    ax.set_xlabel("Jumlah Pelanggan", fontsize=12, color="#ffffff")
    ax.set_ylabel(None)
    st.pyplot(fig)

st.markdown("---")

# Row 3: RFM Analysis
st.subheader("💎 Segmentasi Pelanggan (Analisis RFM)")
rfm_col1, rfm_col2, rfm_col3 = st.columns(3)

# Function to plot RFM
def plot_rfm(data, col, title, ylabel, is_monetary=False):
    data['customer_id_short'] = data['customer_id'].str[:8] + "..."
    # High contrast colors for bars
    bar_colors = ["#00d4ff" if i == 0 else "#2d3748" for i in range(len(data))]
    sns.barplot(y=col, x="customer_id_short", data=data, palette=bar_colors, ax=ax)
    ax.set_title(title, fontsize=20, color="#ffffff")
    ax.set_ylabel(ylabel, fontsize=15, color="#ffffff")
    ax.set_xlabel(None)
    ax.tick_params(axis='x', rotation=45, colors="#ffffff")
    ax.tick_params(axis='y', colors="#ffffff")
    for b in ax.spines.values():
        b.set_edgecolor('#4a5568')
    
    for i, v in enumerate(data[col]):
        label = f"R$ {v:,.0f}" if is_monetary else str(v)
        ax.text(i, v, label, ha='center', va='bottom', fontsize=12, fontweight='bold', color="#00d4ff")

# Recency
with rfm_col1:
    fig, ax = plt.subplots(figsize=(10, 8))
    plot_rfm(rfm_df.sort_values(by="recency", ascending=True).head(5), "recency", "Top Customers by Recency", "Days since last purchase")
    st.pyplot(fig)

# Frequency
with rfm_col2:
    fig, ax = plt.subplots(figsize=(10, 8))
    plot_rfm(rfm_df.sort_values(by="frequency", ascending=False).head(5), "frequency", "Top Customers by Frequency", "Number of Purchases")
    st.pyplot(fig)

# Monetary
with rfm_col3:
    fig, ax = plt.subplots(figsize=(10, 8))
    plot_rfm(rfm_df.sort_values(by="monetary", ascending=False).head(5), "monetary", "Top Customers by Monetary", "Total Spend", True)
    st.pyplot(fig)

st.caption(f'Terakhir diperbarui pada: {pd.Timestamp.now().strftime("%Y-%m-%d %H:%M")}')
st.caption('Copyright © Aditya Maulana Pamungkas 2026')
