"""Educational ML demo for direct-driver classes using entirely synthetic features."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, ConfusionMatrixDisplay, accuracy_score

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "synthetic_deforestation_alerts.csv"
OUT = BASE_DIR / "outputs"
OUT.mkdir(exist_ok=True)
FEATURES = ["ndvi_change", "nbr_change", "distance_to_road_km", "distance_to_settlement_km", "fire_hotspot_count", "slope_degree", "dry_season_ratio", "regrowth_after_12m"]


def main():
    df = pd.read_csv(DATA_PATH)
    X_train, X_test, y_train, y_test = train_test_split(
        df[FEATURES], df["direct_driver"], test_size=.25, random_state=42, stratify=df["direct_driver"]
    )
    model = RandomForestClassifier(n_estimators=300, random_state=42, min_samples_leaf=2, class_weight="balanced")
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    report = classification_report(y_test, pred, zero_division=0)
    (OUT / "classification_report.txt").write_text(
        "CLASSIFICATION REPORT — DATA SINTETIS, BUKAN ATRIBUSI LAPANGAN\n\n" + report +
        f"\nAccuracy: {accuracy_score(y_test, pred):.3f}\n\n" +
        "Model ini hanya membuktikan alur kerja kode pada data buatan. Jangan gunakan untuk mengatribusikan kejadian nyata.\n", encoding="utf-8"
    )
    fig, ax = plt.subplots(figsize=(10, 8))
    ConfusionMatrixDisplay.from_predictions(y_test, pred, xticks_rotation=45, cmap="Greens", colorbar=False, ax=ax)
    ax.set_title("Confusion Matrix — Driver Kehilangan Pohon (Sintetis)")
    fig.tight_layout(); fig.savefig(OUT / "deforestation_confusion_matrix.png", dpi=160); plt.close(fig)
    importance = pd.Series(model.feature_importances_, index=FEATURES).sort_values()
    fig, ax = plt.subplots(figsize=(8, 5))
    importance.plot(kind="barh", ax=ax)
    ax.set_title("Feature Importance — Data Sintetis")
    ax.set_xlabel("Kepentingan relatif dalam model")
    fig.tight_layout(); fig.savefig(OUT / "feature_importance.png", dpi=160); plt.close(fig)
    print("=== DEFORESTATION DRIVER CLASSIFICATION: SIMULASI ===")
    print(report)
    print(f"Accuracy: {accuracy_score(y_test, pred):.3f}")
    print("Penting: semua fitur dan label untuk demonstrasi adalah sintetis; akurasi tidak berlaku untuk hutan nyata.")
    print(f"Keluaran tersimpan di: {OUT}")

if __name__ == "__main__":
    main()
