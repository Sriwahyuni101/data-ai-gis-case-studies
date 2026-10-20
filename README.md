# Paket 6 Studi Kasus Resume Webinar: Data, AI, HPC, GIS, dan HCI

Repositori ini berisi enam studi kasus praktis yang dikembangkan berdasarkan **judul enam resume materi** yang diberikan. Karena transkrip/slides lengkap para pemateri tidak disertakan, contoh kasus, dataset, dan analisis dalam paket ini adalah **rancangan pembelajaran mandiri**, bukan kutipan atau klaim hasil eksperimen para pemateri.

## Daftar studi kasus

| No. | Materi resume | Studi kasus | Implementasi |
|---|---|---|---|
| 1 | Make Sense of Data with Analytics and AI | Analisis dan prediksi pendapatan toko berdasarkan transaksi simulasi | Pandas, feature engineering, Random Forest Regressor |
| 2 | Bridging Global Infrastructure to Address Local Challenges in HPC | Menghitung indeks simulasi pada grid lingkungan secara serial dan paralel | NumPy, `ProcessPoolExecutor`, benchmark |
| 3 | Career and Competition in Industrial Era with GIS | Menentukan kandidat lokasi pusat layanan UMKM dari titik permintaan dan fasilitas pesaing | Analisis jarak haversine, skoring lokasi, peta titik |
| 4 | Introduction to Machine Learning | Mengidentifikasi mahasiswa yang mungkin membutuhkan dukungan akademik | Random Forest Classifier, classification report, confusion matrix |
| 5 | Human-Computer Interaction & Data Visualization | Evaluasi usability sistem informasi kampus menggunakan task testing dan SUS | Perhitungan SUS, metrik tugas, visualisasi Matplotlib |
| 6 | Attributing Direct Drivers to Deforestation Alerts with Satellite Imagery and AI | Demonstrasi klasifikasi penyebab kehilangan tutupan pohon dari fitur satelit simulasi | Random Forest Classifier; contoh tambahan Google Earth Engine |

## Struktur repositori

Setiap folder studi kasus memiliki `README.md`, data CSV di `data/`, kode yang dapat dijalankan di `src/`, dan folder `outputs/` untuk hasil. Semua CSV simulasi sudah disertakan agar kode Python utama bisa dicoba tanpa mengunduh data eksternal.

```text
studi-kasus-resume/
├── README.md
├── requirements.txt
├── run_all.py
├── DATA_NOTES.md
├── LICENSE
├── 01-data-analytics/
├── 02-hpc/
├── 03-gis/
├── 04-machine-learning/
├── 05-hci-data-visualization/
└── 06-deforestation-ai/
```

## Cara menjalankan

Gunakan Python 3.10 atau yang lebih baru.

1. Ekstrak ZIP lalu buka folder `studi-kasus-resume` di VS Code atau terminal.
2. Buat dan aktifkan virtual environment:

   **Windows**
   ```bash
   py -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS/Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install library:
   ```bash
   pip install -r requirements.txt
   ```
4. Jalankan studi kasus. Contoh:
   ```bash
   python 01-data-analytics/src/main.py
   python 02-hpc/src/benchmark_hpc.py
   python 03-gis/src/main.py
   python 04-machine-learning/src/main.py
   python 05-hci-data-visualization/src/main.py
   python 06-deforestation-ai/src/main.py
   ```

Hasil metrik, CSV keluaran, dan gambar akan disimpan di folder `outputs/` masing-masing. Untuk menjalankan seluruh studi kasus secara berurutan, gunakan `python run_all.py`. Benchmark HPC dapat memiliki hasil kecepatan berbeda tergantung spesifikasi perangkat, jumlah core, dan beban sistem.

## Mengunggah ke GitHub

1. Buat repository baru di GitHub.
2. Ekstrak ZIP; buka terminal di folder utama proyek.
3. Jalankan:
   ```bash
   git init
   git add .
   git commit -m "Add six practical case studies from webinar summaries"
   git branch -M main
   git remote add origin https://github.com/USERNAME/NAMA-REPO.git
   git push -u origin main
   ```
4. Ganti `USERNAME/NAMA-REPO` dengan alamat repository milik sendiri. Jangan unggah data pribadi atau kredensial.

## Catatan integritas data

- Dataset yang bernama `synthetic`, serta dataset di folder data yang dijelaskan sebagai simulasi, dibuat secara programatik untuk latihan. Nilainya **bukan data resmi** tentang mahasiswa, penjualan toko, lokasi fasilitas, banjir, atau deforestasi.
- Studi GIS menggunakan koordinat ilustratif. Jangan menganggap kandidat lokasi sebagai alamat/fasilitas nyata.
- Studi dukungan akademik hanya untuk contoh teknis. Prediksi tidak boleh dipakai sebagai dasar tunggal untuk memberi label, menghukum, atau mengambil keputusan tentang mahasiswa nyata.
- Studi deforestasi menggunakan data sintetis untuk melatih model offline. Folder itu juga menyediakan contoh opsional untuk melihat peta penyebab kehilangan tutupan pohon dari dataset publik Google Earth Engine. Klasifikasi pada data simulasi tidak membuktikan penyebab deforestasi di wilayah nyata.
- Semua kasus perlu dievaluasi, disesuaikan, dan diuji ulang apabila dikembangkan dengan data nyata.

## Referensi utama

- pandas, *Getting started*: https://pandas.pydata.org/docs/getting_started/
- scikit-learn, *Metrics and scoring*: https://scikit-learn.org/stable/modules/model_evaluation.html
- Python, *multiprocessing*: https://docs.python.org/3/library/multiprocessing.html
- GeoPandas, *Getting started*: https://geopandas.org/en/stable/getting_started.html
- Google Earth Engine, *WRI/Google DeepMind Global Drivers of Forest Loss 2001–2023 v1.1*: https://developers.google.com/earth-engine/datasets/catalog/projects_landandcarbon_assets_wri_gdm_drivers_forest_loss_1km_v1_1_2001_2023
- Brooke, J. (1996). *SUS: A quick and dirty usability scale*. Dalam P. W. Jordan, B. Thomas, B. A. Weerdmeester, & I. L. McClelland (Eds.), *Usability Evaluation in Industry*. Taylor & Francis.

## Lisensi

Kode contoh memakai lisensi MIT. Dataset buatan untuk latihan dan dokumentasi ada di dalam repository untuk keperluan pendidikan.
