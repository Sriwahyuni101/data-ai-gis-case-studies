"""Run all six study-case scripts in sequence from the repository root."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
SCRIPTS = [
    "01-data-analytics/src/main.py",
    "02-hpc/src/benchmark_hpc.py",
    "03-gis/src/main.py",
    "04-machine-learning/src/main.py",
    "05-hci-data-visualization/src/main.py",
    "06-deforestation-ai/src/main.py",
]


def main():
    for relative_script in SCRIPTS:
        print(f"\n{'=' * 72}\nMenjalankan: {relative_script}\n{'=' * 72}", flush=True)
        completed = subprocess.run([sys.executable, str(ROOT / relative_script)], cwd=ROOT)
        if completed.returncode != 0:
            raise SystemExit(f"Gagal menjalankan {relative_script} (kode {completed.returncode}).")
    print("\nSemua studi kasus selesai dijalankan.")


if __name__ == "__main__":
    main()
