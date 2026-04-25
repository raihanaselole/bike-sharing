import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# data
day_df = pd.read_csv('main_data.csv')
hour_df = pd.read_csv('hour_data.csv')

day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])


st.title("Bike Sharing Dashboard")
st.markdown("Analisis Pola Penyewaan Sepeda Berdasarkan Waktu dan Cuaca")

# sidebar
st.sidebar.header("Filter Data")

year_filter = st.sidebar.selectbox("Pilih Tahun", options=[2011, 2012])

filtered_day = day_df[day_df['yr'] == (year_filter - 2011)]
filtered_hour = hour_df[hour_df['yr'] == (year_filter - 2011)]

# metric
st.subheader("Summary Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Rentals", int(filtered_day['total_rentals'].sum()))
col2.metric("Rata-rata Harian", int(filtered_day['total_rentals'].mean()))
col3.metric("Max Rentals", int(filtered_day['total_rentals'].max()))

# Pola Jam
st.subheader("Pola Penyewaan Berdasarkan Jam")

hourly = filtered_hour.groupby('hr')['total_rentals'].mean()

fig, ax = plt.subplots()
ax.plot(hourly.index, hourly.values)
ax.set_title("Rata-rata Penyewaan per Jam")
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Penyewaan")

st.pyplot(fig)

# tingkat penyewaan sepeda hari kerja
st.subheader("Hari Kerja vs Libur")

working = filtered_day.groupby('workingday')['total_rentals'].mean()

fig2, ax2 = plt.subplots()
ax2.bar(working.index.astype(str), working.values)
ax2.set_title("Perbandingan Hari Kerja vs Libur")
ax2.set_xlabel("Working Day (1=Ya, 0=Tidak)")
ax2.set_ylabel("Jumlah Penyewaan")

st.pyplot(fig2)

# cuaca
st.subheader("Pengaruh Cuaca")

weather = filtered_day.groupby('weather_label')['total_rentals'].mean()

fig3, ax3 = plt.subplots()
ax3.bar(weather.index, weather.values)
ax3.set_title("Pengaruh Cuaca terhadap Penyewaan")
ax3.set_ylabel("Jumlah Penyewaan")

st.pyplot(fig3)

# korelasi lingkungan
st.subheader("Korelasi Faktor Lingkungan")

corr = filtered_day[['temp','hum','windspeed','total_rentals']].corr()

fig4, ax4 = plt.subplots()
sns.heatmap(corr, annot=True, ax=ax4)
ax4.set_title("Correlation Matrix")

st.pyplot(fig4)

st.subheader("Kategori Tingkat Penyewaan")

# buat kategori
filtered_day['usage_level'] = pd.qcut(
    filtered_day['total_rentals'],
    q=3,
    labels=['Low', 'Medium', 'High']
)

usage_dist = filtered_day['usage_level'].value_counts().sort_index()

fig5, ax5 = plt.subplots()
ax5.bar(usage_dist.index, usage_dist.values)
ax5.set_title("Distribusi Tingkat Penyewaan")
ax5.set_xlabel("Kategori")
ax5.set_ylabel("Jumlah Hari")

st.pyplot(fig5)

st.subheader("Analisis Penyewaan Berdasarkan Musim")

season_usage = filtered_day.groupby('season_label')['total_rentals'].mean()

fig6, ax6 = plt.subplots()
ax6.bar(season_usage.index, season_usage.values)
ax6.set_title("Rata-rata Penyewaan per Musim")
ax6.set_ylabel("Jumlah Penyewaan")

st.pyplot(fig6)

