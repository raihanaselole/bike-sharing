import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

BASE_DIR = os.path.dirname(__file__)

# data
day_df = pd.read_csv(os.path.join(BASE_DIR, 'main_data.csv'))
hour_df = pd.read_csv(os.path.join(BASE_DIR, 'hour_data.csv'))

day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

st.title("Bike Sharing Dashboard")
st.markdown("Analisis Pola Penyewaan Sepeda Berdasarkan Waktu, Cuaca, dan Faktor Lingkungan")

# sidebar
st.sidebar.header("Filter Data")

year_filter = st.sidebar.selectbox("Pilih Tahun", options=[2011, 2012])

day_clean = day_df[day_df['yr'] == (year_filter - 2011)]
hour_clean = hour_df[hour_df['yr'] == (year_filter - 2011)]

# metric
st.subheader("Summary Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Rentals", int(day_clean['total_rentals'].sum()))
col2.metric("Rata-rata Harian", int(day_clean['total_rentals'].mean()))
col3.metric("Max Rentals", int(day_clean['total_rentals'].max()))

# jam penyewaan
st.subheader("Pola Penyewaan Berdasarkan Jam")

hourly_usage = hour_clean.groupby('hr')['total_rentals'].mean().reset_index()

fig, ax = plt.subplots(figsize=(10,5))
sns.lineplot(data=hourly_usage, x='hr', y='total_rentals', ax=ax)
ax.set_title("Rata-rata Penyewaan per Jam")
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig)

# hari kerja dan hari libur
st.subheader("Hari Kerja vs Hari Libur")

workingday_usage = day_clean.groupby('workingday')['total_rentals'].mean().reset_index()

fig2, ax2 = plt.subplots()
sns.barplot(data=workingday_usage, x='workingday', y='total_rentals', ax=ax2)
ax2.set_title("Perbandingan Hari Kerja vs Libur")
ax2.set_xlabel("Working Day (1=Ya, 0=Tidak)")
ax2.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig2)

# cuaca
st.subheader("Pengaruh Cuaca")

weather_usage = day_clean.groupby('weather_label')['total_rentals'].mean().reset_index()

fig3, ax3 = plt.subplots()
sns.barplot(data=weather_usage, x='weather_label', y='total_rentals', ax=ax3)
ax3.set_title("Pengaruh Cuaca terhadap Penyewaan")
ax3.set_ylabel("Jumlah Penyewaan")
ax3.set_xlabel("Cuaca")
ax3.tick_params(axis='x', rotation=30)
st.pyplot(fig3)

# korelasi
st.subheader("Korelasi Faktor Lingkungan")

corr = day_clean[['temp','hum','windspeed','total_rentals']].corr()

fig4, ax4 = plt.subplots()
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax4)
ax4.set_title("Correlation Matrix")
st.pyplot(fig4)

# musim
st.subheader("Penyewaan Berdasarkan Musim")

season_usage = day_clean.groupby('season_label')['total_rentals'].mean().reset_index()

fig5, ax5 = plt.subplots()
sns.barplot(data=season_usage, x='season_label', y='total_rentals', ax=ax5)
ax5.set_title("Rata-rata Penyewaan per Musim")
ax5.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig5)

# bulan
st.subheader("Pola Penyewaan Bulanan")

monthly_usage = day_clean.groupby('mnth')['total_rentals'].mean().reset_index()

fig6, ax6 = plt.subplots()
sns.lineplot(data=monthly_usage, x='mnth', y='total_rentals', marker='o', ax=ax6)
ax6.set_title("Rata-rata Penyewaan per Bulan")
ax6.set_xlabel("Bulan")
ax6.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig6)

# distribusi
st.subheader("Distribusi Penyewaan")

fig7, ax7 = plt.subplots()
sns.histplot(day_clean['total_rentals'], kde=True, ax=ax7)
ax7.set_title("Distribusi Total Penyewaan")
st.pyplot(fig7)

fig8, ax8 = plt.subplots()
sns.boxplot(x=day_clean['total_rentals'], ax=ax8)
ax8.set_title("Boxplot Total Penyewaan")
st.pyplot(fig8)