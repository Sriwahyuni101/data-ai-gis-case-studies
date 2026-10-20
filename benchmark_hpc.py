"""Benchmark serial vs process-parallel numeric grid simulation (synthetic only)."""
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
import os, time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "synthetic_grid.csv"
OUT = BASE_DIR / "outputs"
OUT.mkdir(exist_ok=True)
PASSES = 160


def calculate_chunk(payload):
    elevation, rainfall, saturation = payload
    elevation = np.asarray(elevation, dtype=np.float64)
    rainfall = np.asarray(rainfall, dtype=np.float64)
    saturation = np.asarray(saturation, dtype=np.float64)
    state = rainfall / 350.0 + saturation * 0.45 - elevation / 500.0
    for _ in range(PASSES):
        state = np.tanh(0.73 * state + 0.12 * np.sin(2.0 * state) + rainfall / 900.0 - elevation / 950.0)
    return np.clip((state + 1.0) / 2.0, 0.0, 1.0)


def main():
    df = pd.read_csv(DATA_PATH)
    elevation = df["elevation_m"].to_numpy()
    rainfall = df["rainfall_mm"].to_numpy()
    saturation = df["soil_saturation"].to_numpy()
    t0 = time.perf_counter()
    serial = calculate_chunk((elevation, rainfall, saturation))
    serial_time = time.perf_counter() - t0

    workers = min(4, os.cpu_count() or 1)
    indices = np.array_split(np.arange(len(df)), workers)
    payloads = [(elevation[idx], rainfall[idx], saturation[idx]) for idx in indices if len(idx)]
    t0 = time.perf_counter()
    with ProcessPoolExecutor(max_workers=workers) as pool:
        chunk_results = list(pool.map(calculate_chunk, payloads))
    parallel = np.concatenate(chunk_results)
    parallel_time = time.perf_counter() - t0
    # map() preserves the input order of chunks; chunks were created in index order.
    checksum_equal = bool(np.allclose(serial, parallel, atol=1e-12))
    speedup = serial_time / parallel_time if parallel_time > 0 else float("nan")
    efficiency = speedup / workers
    result = pd.DataFrame([
        {"mode":"serial", "workers":1, "seconds":serial_time, "speedup":1.0, "parallel_efficiency":1.0},
        {"mode":"parallel", "workers":workers, "seconds":parallel_time, "speedup":speedup, "parallel_efficiency":efficiency},
    ])
    result.to_csv(OUT / "hpc_benchmark.csv", index=False)
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.bar(result["mode"], result["seconds"])
    ax.set_title("Benchmark Komputasi Grid Simulasi")
    ax.set_ylabel("Waktu (detik)"); ax.set_xlabel("Mode pemrosesan")
    ax.grid(axis="y", alpha=.25)
    fig.tight_layout(); fig.savefig(OUT / "hpc_benchmark.png", dpi=160); plt.close(fig)
    print("=== HPC BENCHMARK: SIMULASI GRID ===")
    print(f"Jumlah sel: {len(df):,} | iterasi per sel: {PASSES} | worker: {workers}")
    print(f"Serial:   {serial_time:.4f} detik")
    print(f"Parallel: {parallel_time:.4f} detik")
    print(f"Speedup: {speedup:.3f}x | efisiensi paralel: {efficiency:.3f}")
    print(f"Hasil serial dan paralel konsisten: {checksum_equal}")
    print("Catatan: jika parallel lebih lambat, overhead multiprocessing dapat menjadi penyebabnya.")
    print(f"Keluaran tersimpan di: {OUT}")

if __name__ == "__main__":
    main()
