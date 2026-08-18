import pandas as pd


def baseline_prediction(file_path="data.csv"):
    data = pd.read_csv(file_path)

    # Baseline: predict the average GDP growth
    average_gdp = data["gdp_growth"].mean()

    return round(float(average_gdp), 2)


if __name__ == "__main__":
    prediction = baseline_prediction()

    print("Baseline GDP growth prediction:", prediction)
