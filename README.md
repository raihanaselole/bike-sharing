# Bike Sharing Data

Proyek ini disusun sebagai bagian dari submission akhir pada kelas DBS Foundation Dicoding dalam jalur pembelajaran (learning path) Data Science, khususnya untuk modul Belajar Fundamental Analisis Data.

Dalam proyek ini dilakukan serangkaian tahapan analisis data yang mencakup proses pengolahan data (data wrangling), eksplorasi data (exploratory data analysis/EDA), pembuatan visualisasi, hingga penerapan analisis tambahan seperti pengelompokan tingkat penyewaan (binning) dan analisis pola musiman, dengan memanfaatkan bahasa pemrograman Python.

### Setup Environment - Anaconda
```shell
conda create --name bike-ds python=3.12
conda activate bike-ds
pip install -r requirements.txt
```

### Setup Environment - Shell/Terminal
```shell
mkdir bike-sharing-analysis 
cd bike-sharing-analysis 
pipenv install 
pipenv shell 
pip install -r requirements.txt

### Run steamlit app
```shell
cd dashboard
streamlit run dashboard.py
```