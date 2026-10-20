# Studi Kasus 6 — Attributing Direct Drivers to Deforestation Alerts with Satellite Imagery and AI

## 1. Latar belakang
Citra satelit dapat digunakan untuk mendeteksi perubahan tutupan pohon. Namun, mendeteksi perubahan tidak sama dengan mengetahui penyebab langsungnya. Atribusi penyebab membutuhkan fitur penginderaan jauh, informasi kontekstual, label referensi, dan validasi yang cermat.

## 2. Kasus dan rumusan masalah
Sebagai demonstrasi ML, dapatkah fitur perubahan indeks vegetasi (misalnya NDVI/NBR), jarak ke jalan/permukiman, hotspot api, kemiringan lereng, kondisi musim kering, dan pertumbuhan kembali membantu membedakan beberapa kelas penyebab kehilangan tutupan pohon?

## 3. Dua jalur dalam paket
**Jalur A — Python offline:** `data/synthetic_deforestation_alerts.csv` berisi 1.260 sampel sintetis. `src/main.py` melatih Random Forest untuk mengklasifikasikan tujuh kelas ilustratif, mengevaluasi hasil uji, dan menyimpan confusion matrix serta feature importance. Data ini dibuat untuk latihan; hasil modelnya tidak dapat digunakan untuk menyimpulkan penyebab kejadian nyata.

**Jalur B — melihat dataset global publik:** file `src/earth_engine_viewer.js` adalah contoh opsional Google Earth Engine untuk menampilkan dataset *WRI/Google DeepMind Global Drivers of Forest Loss 2001–2023 v1.1*. Jalur ini membutuhkan akun/akses Earth Engine dan dijalankan di Code Editor Earth Engine, bukan dengan Python lokal. Dataset tersebut memetakan penggerak dominan pada resolusi sekitar 1 km dengan tujuh kelas dan mempunyai keterbatasan interpretasi.

## 4. Menjalankan Python offline

```bash
python 06-deforestation-ai/src/main.py
```

## 5. Keluaran Python
- `outputs/classification_report.txt`
- `outputs/deforestation_confusion_matrix.png`
- `outputs/feature_importance.png`

## 6. Menampilkan layer Earth Engine (opsional)
1. Buka https://code.earthengine.google.com/ dan pastikan akses Earth Engine tersedia.
2. Salin isi `src/earth_engine_viewer.js` ke Code Editor.
3. Tekan **Run** dan aktifkan/nonaktifkan layer pada panel peta.
4. Script hanya memvisualisasikan layer kelas dominan dan probabilitas kelas pertanian permanen; ia tidak menghitung sendiri semua alert di suatu lokasi.

## 7. Batasan penting
Peta penggerak dominan tidak selalu menunjukkan seluruh penyebab yang terjadi pada sel yang sama atau urutan waktunya. Produk global yang dirujuk juga tidak membedakan semua kehilangan pohon alami dengan pohon perkebunan. Sebelum membuat kesimpulan atau rekomendasi kebijakan, periksa definisi kelas, skala spasial, periode waktu, data label, ketidakpastian, dan validasi lapangan/interpretasi citra resolusi tinggi.

## Referensi
- WRI/Google DeepMind Global Drivers of Forest Loss 2001–2023 v1.1, Google Earth Engine Data Catalog: https://developers.google.com/earth-engine/datasets/catalog/projects_landandcarbon_assets_wri_gdm_drivers_forest_loss_1km_v1_1_2001_2023
- Hansen et al., Global Forest Change dataset: https://developers.google.com/earth-engine/datasets/catalog/UMD_hansen_global_forest_change_2025_v1_13
- scikit-learn model evaluation: https://scikit-learn.org/stable/modules/model_evaluation.html
