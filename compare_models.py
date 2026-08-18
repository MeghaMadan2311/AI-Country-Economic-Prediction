import pandas as pd
import matplotlib.pyplot as plt

from model import train_model, predict_gdp
from baseline import baseline_prediction


def compare_models(file_path="data.csv"):
    data = pd.read_csv(file_path)

    model = train_model(file_path)

    # ML model predictions
    model_predictions = []

    for _, row in data.iterrows():
        prediction = predict_gdp(
            model,
            row["inflation"],
            row["unemployment"]
        )
        model_predictions.append(prediction)

    # Baseline prediction
    baseline = baseline_prediction(file_path)

    # Visualization
    plt.figure(figsize=(10, 6))

    plt.plot(
        data["country"],
        model_predictions,
        marker="o",
        label="ML Model"
    )

    plt.axhline(
        y=baseline,
        linestyle="--",
        label="Baseline Model"
    )

    plt.xticks(rotation=45)
    plt.xlabel("Country")
    plt.ylabel("Predicted GDP Growth (%)")
    plt.title("ML Model vs Baseline Model")
    plt.legend()
    plt.tight_layout()

    plt.savefig("model_vs_baseline.png")
    plt.close()

    print("Comparison visualization saved as model_vs_baseline.png")


if __name__ == "__main__":
    compare_models()
